"""
Score each Canadian occupation group's AI exposure using an LLM via OpenRouter.

Reads Markdown summaries from pages/, sends each to an LLM with a scoring
rubric, and collects structured scores. Results are cached incrementally to
scores.json so the script can be resumed if interrupted.

Usage:
    uv run python score.py
    uv run python score.py --model google/gemini-3-flash-preview
    uv run python score.py --start 0 --end 10
"""

import argparse
import json
import os
import time

import httpx
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = "google/gemini-3-flash-preview"
OUTPUT_FILE = "scores.json"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
FATAL_STATUS_CODES = {401, 402, 403}

SYSTEM_PROMPT = """\
You are an expert analyst evaluating how exposed Canadian occupation groups are
 to AI. You will be given a compact labour-market summary for one occupation
 group from Statistics Canada, including the official occupation title and a few
 recent indicators such as employment and wages.

Rate the occupation group's overall AI Exposure on a scale from 0 to 10.

AI Exposure measures: how much will AI reshape this occupation group? Consider
 both direct effects (AI automating tasks currently done by humans) and
 indirect effects (AI making each worker so productive that fewer are needed).

A key signal is whether the job's work product is fundamentally digital. If the
 work can largely be done from a computer through writing, coding, analysis,
 design, documentation, or routine communication, AI exposure is inherently
 high. Conversely, jobs requiring physical presence, manual skill, mobility, or
 embodied human care have a stronger barrier.

Use these anchors to calibrate your score:
- 0-1: Minimal exposure. Mostly physical, hands-on, or field work.
- 2-3: Low exposure. AI helps with admin edges, not the core work.
- 4-5: Moderate exposure. Mixed digital and physical/interpersonal work.
- 6-7: High exposure. Knowledge work where AI already boosts productivity.
- 8-9: Very high exposure. Core work is largely computer-based.
- 10: Maximum exposure. Routine digital processing where AI can do most tasks.

Respond with ONLY a JSON object in this exact format:
{
  "exposure": <0-10 integer>,
  "rationale": "<2-3 sentences explaining the key factors>"
}
"""


def score_occupation(client, text, model):
    response = client.post(
        API_URL,
        headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"},
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
            "temperature": 0.2,
        },
        timeout=60,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if content.startswith("```"):
        content = content.split("\n", 1)[1]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()

    return json.loads(content)


def save_scores(scores):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        json.dump(list(scores.values()), handle, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int, default=None)
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--force", action="store_true", help="Re-score even if already cached")
    args = parser.parse_args()

    with open("occupations.json", encoding="utf-8") as handle:
        occupations = json.load(handle)

    subset = occupations[args.start:args.end]

    scores = {}
    if os.path.exists(OUTPUT_FILE) and not args.force:
        with open(OUTPUT_FILE, encoding="utf-8") as handle:
            for entry in json.load(handle):
                scores[entry["slug"]] = entry

    print(f"Scoring {len(subset)} occupation groups with {args.model}")
    print(f"Already cached: {len(scores)}")

    if not os.getenv("OPENROUTER_API_KEY"):
        raise SystemExit("OPENROUTER_API_KEY is not set. Add it to .env before running score.py.")

    errors = []
    client = httpx.Client()

    try:
        for index, occupation in enumerate(subset, start=1):
            slug = occupation["slug"]
            if slug in scores:
                continue

            md_path = f"pages/{slug}.md"
            if not os.path.exists(md_path):
                print(f"  [{index}] SKIP {slug} (no markdown summary)")
                continue

            with open(md_path, encoding="utf-8") as handle:
                text = handle.read()

            print(f"  [{index}/{len(subset)}] {occupation['title']}...", end=" ", flush=True)

            try:
                result = score_occupation(client, text, args.model)
                scores[slug] = {
                    "slug": slug,
                    "title": occupation["title"],
                    "noc_code": occupation.get("noc_code", ""),
                    **result,
                }
                save_scores(scores)
                print(f"exposure={result['exposure']}")
            except httpx.HTTPStatusError as exc:
                print(f"ERROR: {exc}")
                errors.append(slug)
                if exc.response.status_code in FATAL_STATUS_CODES:
                    raise SystemExit(
                        f"OpenRouter returned HTTP {exc.response.status_code}. Check your API key, credits, and model access before retrying."
                    )
            except Exception as exc:
                print(f"ERROR: {exc}")
                errors.append(slug)

            if index < len(subset):
                time.sleep(args.delay)
    finally:
        client.close()

    print(f"\nDone. Scored {len(scores)} occupation groups, {len(errors)} errors.")
    if errors:
        print(f"Errors: {errors}")

    values = [entry for entry in scores.values() if "exposure" in entry]
    if values:
        avg = sum(entry["exposure"] for entry in values) / len(values)
        by_score = {}
        for entry in values:
            bucket = entry["exposure"]
            by_score[bucket] = by_score.get(bucket, 0) + 1
        print(f"\nAverage exposure across {len(values)} occupation groups: {avg:.1f}")
        print("Distribution:")
        for score in sorted(by_score):
            print(f"  {score}: {'#' * by_score[score]} ({by_score[score]})")


if __name__ == "__main__":
    main()
