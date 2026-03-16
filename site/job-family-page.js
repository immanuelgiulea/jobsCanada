const EMBEDDED_FAMILY_SLUG = typeof window.__FAMILY_SLUG__ === "string" ? window.__FAMILY_SLUG__ : "";
const DASHBOARD_VIEWS = new Set(["treemap","trend","outlook"]);

let meta = {};
let family = null;
let geoLookup = {};
let selectedGeo = "CA";
let openUnits = new Set();
let openProfiles = new Set();
let searchController = null;

function formatCompact(value){
  if(value==null)return"-";
  if(value>=1e6)return(value/1e6).toFixed(1)+"M";
  if(value>=1e3)return Math.round(value/1e3)+"K";
  return Number(value).toLocaleString();
}

function formatMoney(value){return value==null?"-":"$"+Number(value).toFixed(2)}
function formatPercent(value){return value==null?"-":Number(value).toFixed(1)+"%"}
function formatSignedPercent(value){return value==null?"-":(value>0?"+":"")+Number(value).toFixed(1)+"%"}
function formatDecimal(value){return value==null?"-":Number(value).toFixed(2)}
function escapeHTML(value){return String(value).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;").replaceAll("'","&#39;")}

function normalizeMajorSlug(value){
  const text=String(value||"").trim();
  if(/^major-\d{2}$/.test(text))return text;
  if(/^\d{2}$/.test(text))return`major-${text}`;
  return"";
}

function resolveFamilySlug(){
  const query=new URLSearchParams(window.location.search);
  return normalizeMajorSlug(EMBEDDED_FAMILY_SLUG||query.get("slug")||query.get("code"));
}

function getGeoList(){
  return Array.isArray(meta.geographies)&&meta.geographies.length
    ?meta.geographies
    :[{code:"CA",label_en:"Canada",label_fr:"Canada",type:"country"}];
}

function getGeoMeta(code){
  return geoLookup[code]||geoLookup[meta.default_geography]||{code:"CA",label_en:"Canada",label_fr:"Canada",type:"country"};
}

function resolveSelectedGeo(){
  const requested=(new URLSearchParams(window.location.search).get("geo")||meta.default_geography||"CA").toUpperCase();
  return geoLookup[requested]?requested:(meta.default_geography||"CA");
}

function resolveDashboardView(){
  const requested=String(new URLSearchParams(window.location.search).get("view")||"").trim();
  return DASHBOARD_VIEWS.has(requested)?requested:"";
}

function resolveStats(item){
  return item&&item.stats_by_geo&&item.stats_by_geo[selectedGeo]?item.stats_by_geo[selectedGeo]:{};
}

function getFocusTarget(){
  const params=new URLSearchParams(window.location.search);
  return String(params.get("focus")||window.location.hash.replace(/^#/,"")||"").trim();
}

function isFocusedUnit(unitCode){
  const focus=getFocusTarget();
  return /^\d{5}$/.test(focus)?focus===unitCode:/^\d{5}\.\d{2}$/.test(focus)?focus.slice(0,5)===unitCode:false;
}

function isFocusedProfile(profileCode){
  return getFocusTarget()===profileCode;
}

function captureOpenState(){
  openUnits=new Set(Array.from(document.querySelectorAll(".unit-details[open]")).map(node=>node.dataset.unitCode||"").filter(Boolean));
  openProfiles=new Set(Array.from(document.querySelectorAll(".profile-card[open]")).map(node=>node.dataset.profileCode||"").filter(Boolean));
}

function updateBackLink(){
  const backLink=document.querySelector(".back-link");
  if(!backLink)return;
  const params=new URLSearchParams();
  if(selectedGeo!==(meta.default_geography||"CA"))params.set("geo",selectedGeo);
  const dashboardView=resolveDashboardView();
  if(dashboardView&&dashboardView!=="treemap")params.set("view",dashboardView);
  backLink.href=`./${params.toString()?`?${params.toString()}`:""}`;
}

function updateUrlState(){
  const params=new URLSearchParams(window.location.search);
  if(EMBEDDED_FAMILY_SLUG){
    params.delete("slug");
    params.delete("code");
  }else{
    params.set("slug",family.slug);
    params.delete("code");
  }
  if(selectedGeo===(meta.default_geography||"CA"))params.delete("geo");else params.set("geo",selectedGeo);
  const nextUrl=`${window.location.pathname}${params.toString()?`?${params.toString()}`:""}${window.location.hash}`;
  window.history.replaceState(null,"",nextUrl);
}

function pageSummaryCopy(){
  const stats=resolveStats(family);
  const geo=getGeoMeta(selectedGeo);
  if(selectedGeo===(meta.default_geography||"CA")){
    return`Canada-wide labour metrics for this official major group. OaSIS profiles remain the same national release regardless of geography.`;
  }
  if(stats.jobs!=null){
    return`${geo.label_en} switches the labour-market metrics for this major group. OaSIS profiles stay fixed because the current official release is not geography-specific.`;
  }
  if(stats.outlook_label||stats.outlook_score!=null){
    return`${geo.label_en} has outlook coverage for this family, but current StatCan labour counts are unavailable for this selector. OaSIS profiles remain available.`;
  }
  return`Current source tables do not provide labour-market coverage for ${geo.label_en}. OaSIS profiles remain available from the current official release.`;
}

function sourceLink(url,label){
  if(!url)return"";
  return`<a class="source-link" href="${escapeHTML(url)}" target="_blank" rel="noopener">${escapeHTML(label)}</a>`;
}

function renderNoteParagraphs(parts){
  const lines=parts.filter(Boolean);
  if(!lines.length)return"";
  return`<div class="stack">${lines.map(line=>`<div class="note"><p>${escapeHTML(line)}</p></div>`).join("")}</div>`;
}

function limitedItems(items,limit){
  const values=Array.isArray(items)?items.filter(Boolean):[];
  return{visible:values.slice(0,limit),remaining:Math.max(0,values.length-limit)};
}

function renderListPanel(title,items,emptyMessage,limit){
  const {visible,remaining}=limitedItems(items,limit);
  if(!visible.length){
    return`<section class="list-panel"><h4>${escapeHTML(title)}</h4><div class="empty-note">${escapeHTML(emptyMessage)}</div></section>`;
  }
  return`<section class="list-panel"><h4>${escapeHTML(title)}</h4><ul>${visible.map(item=>`<li>${escapeHTML(item)}</li>`).join("")}</ul>${remaining?`<div class="overflow-note">Plus ${remaining.toLocaleString()} more.</div>`:""}</section>`;
}

function formatExampleTitle(item){
  if(!item||!item.job_title_text)return"";
  return item.job_title_type?`${item.job_title_text} (${item.job_title_type})`:item.job_title_text;
}

function formatExclusion(item){
  if(!item)return"";
  if(item.job_title&&item.excluded_profile_code)return`${item.job_title} (${item.excluded_profile_code})`;
  return item.job_title||item.excluded_profile_code||"";
}

function formatCompetency(item){
  if(!item)return"";
  if(item.competency&&item.statement)return`${item.competency}: ${item.statement}`;
  return item.competency||item.statement||"";
}

function renderMetricCard(label,value,sub,isText){
  return`<div class="metric-card"><div class="metric-label">${escapeHTML(label)}</div><div class="metric-value${isText?" text":""}">${escapeHTML(value)}</div><div class="metric-sub">${escapeHTML(sub)}</div></div>`;
}

function renderProfileCard(profile){
  const profileCode=profile.oasis_profile_code;
  const profileId=`profile-${profileCode.replace(".","-")}`;
  const isOpen=openProfiles.has(profileCode)||isFocusedProfile(profileCode);
  const profileKind=profile.is_unit_group_profile?"Unit-group profile":"Split profile";
  const exampleTitles=(profile.example_titles||[]).map(formatExampleTitle).filter(Boolean);
  const exclusions=(profile.exclusions||[]).map(formatExclusion).filter(Boolean);
  const competencies=(profile.core_competencies||[]).map(formatCompetency).filter(Boolean);
  return`
    <details class="profile-card${isFocusedProfile(profileCode)?" focused":""}" id="${profileId}" data-profile-code="${escapeHTML(profileCode)}"${isOpen?" open":""}>
      <summary>
        <div class="profile-summary">
          <div class="profile-title-block">
            <div class="eyebrow">OaSIS ${escapeHTML(profileCode)}</div>
            <h4 class="profile-title">${escapeHTML(profile.profile_title||profileCode)}</h4>
            <div class="profile-meta">${escapeHTML(profile.mapping_method||"Official OaSIS mapping")}</div>
          </div>
          <span class="profile-kind">${escapeHTML(profileKind)}</span>
        </div>
      </summary>
      <div class="profile-body">
        <div class="note"><p>${escapeHTML(profile.lead_statement||"Lead statement unavailable in the current OaSIS release.")}</p></div>
        <div class="list-grid">
          ${renderListPanel("Main duties",profile.main_duties||[],"No main duties listed in the current release.",8)}
          ${renderListPanel("Employment requirements",profile.employment_requirements||[],"No employment requirements listed in the current release.",8)}
          ${renderListPanel("Example titles",exampleTitles,"No example titles listed in the current release.",12)}
          ${renderListPanel("Workplaces and employers",profile.workplaces_employers||[],"No workplaces or employers listed in the current release.",10)}
          ${renderListPanel("Core competencies",competencies,"No core competencies listed in the current release.",6)}
          ${renderListPanel("Exclusions",exclusions,"No explicit exclusions listed in the current release.",8)}
        </div>
        ${renderListPanel("Additional information",profile.additional_information||[],"No additional information listed in the current release.",8)}
      </div>
    </details>`;
}

function renderUnitCard(unit,index){
  const stats=resolveStats(unit);
  const jobsYear=stats.jobs_year||meta.jobs_year||family.jobs_year||"-";
  const trendWindow=stats.trend_from_year!=null&&jobsYear!=="-"?`${stats.trend_from_year}-${jobsYear}`:"recent";
  const outlookWindow=stats.outlook_window_start&&stats.outlook_window_end?`${stats.outlook_window_start}-${stats.outlook_window_end}`:`${meta.outlook_window_start||2025}-${meta.outlook_window_end||2027}`;
  const focusedUnit=isFocusedUnit(unit.noc_code);
  const isOpen=openUnits.has(unit.noc_code)||focusedUnit||(!openUnits.size&&!getFocusTarget()&&index===0);
  const unitId=`unit-${unit.noc_code}`;
  const profileCount=(unit.oasis_profiles||[]).length;
  return`
    <article class="unit-card${focusedUnit?" focused":""}" id="${unitId}">
      <details class="unit-details" data-unit-code="${escapeHTML(unit.noc_code)}"${isOpen?" open":""}>
        <summary>
          <div class="unit-summary">
            <div class="unit-title-block">
              <div class="eyebrow">NOC ${escapeHTML(unit.noc_code)}</div>
              <h3 class="unit-title">${escapeHTML(unit.title)}</h3>
              <div class="unit-meta">${escapeHTML(`${unit.sub_major_group_code||"-"} ${unit.sub_major_group_title||""}`.trim())} | ${escapeHTML(`${unit.minor_group_code||"-"} ${unit.minor_group_title||""}`.trim())}</div>
            </div>
            <div class="unit-pills">
              <span class="mini-pill">${escapeHTML(getGeoMeta(selectedGeo).label_en)} jobs ${escapeHTML(formatCompact(stats.jobs))}</span>
              <span class="mini-pill">Outlook ${escapeHTML(stats.outlook_label||"Undetermined")}</span>
              <span class="mini-pill">High exp. ${escapeHTML(formatPercent(unit.epiac_high_exposure_pct))}</span>
              <span class="mini-pill">${escapeHTML(formatCompact(profileCount))} OaSIS profiles</span>
            </div>
          </div>
        </summary>
        <div class="unit-body">
          <div class="metric-grid">
            ${renderMetricCard("Workers",formatCompact(stats.jobs),jobsYear!=="-"?`${jobsYear} estimate`:"Current estimate",false)}
            ${renderMetricCard("Employment change",formatSignedPercent(stats.trend_pct),`Trend window ${trendWindow}`,false)}
            ${renderMetricCard("Median hourly wage",formatMoney(stats.pay_hourly),jobsYear!=="-"?`${jobsYear} published value`:"Published value",false)}
            ${renderMetricCard("Outlook",stats.outlook_label||"Undetermined",`${outlookWindow} ESDC outlook`,true)}
            ${renderMetricCard("Employment share",formatPercent(stats.employment_share_pct),`${getGeoMeta(selectedGeo).label_en} labour market`,false)}
            ${renderMetricCard("Men / women",`${formatPercent(stats.men_share_pct)} / ${formatPercent(stats.women_share_pct)}`,"Published source shares",true)}
            ${renderMetricCard("Unemployment",formatPercent(stats.unemployment_rate),jobsYear!=="-"?`${jobsYear} published value`:"Published value",false)}
            ${renderMetricCard("OaSIS mapping",unit.oasis_mapping_kind?unit.oasis_mapping_kind.replaceAll("_"," "):"missing",`${profileCount.toLocaleString()} attached profile(s)`,true)}
          </div>
          ${unit.definition?`<div class="note"><p>${escapeHTML(unit.definition)}</p></div>`:""}
          <div class="meta-row">
            <a class="inline-link" href="${escapeHTML(unit.detail_route)}">Open legacy unit detail page</a>
            <span class="tag">${escapeHTML(unit.epiac_group_label||"EPIAC group unavailable")}</span>
            <span class="tag">AIOE ${escapeHTML(formatDecimal(unit.epiac_aioe))}</span>
            <span class="tag">Complementarity ${escapeHTML(formatDecimal(unit.epiac_complementarity))}</span>
          </div>
          <div class="divider"></div>
          <div class="stack">
            <div class="section-head">
              <div>
                <h2>Nested OaSIS Profiles</h2>
                <div class="section-copy">${profileCount?`${formatCompact(profileCount)} official occupational profile(s) attached to this unit group in the current release.`:"No official OaSIS profiles were attached to this unit group in the current release."}</div>
              </div>
            </div>
            <div class="stack">${profileCount?(unit.oasis_profiles||[]).map(renderProfileCard).join(""):'<div class="note"><p>No official OaSIS profiles were attached to this unit group in the current release.</p></div>'}</div>
          </div>
        </div>
      </details>
    </article>`;
}

function renderSourceSection(){
  const links=[
    {url:family.url,label:"Official NOC classification source"},
    {url:family.employment_url,label:"StatCan annual employment table"},
    {url:family.wages_url,label:"StatCan annual wages table"},
    {url:family.epiac_source_url,label:family.epiac_source_title||"StatCan EPIAC study"},
    {url:family.outlook_url,label:"ESDC outlook dataset"},
    {url:meta.oasis&&meta.oasis.package_url?meta.oasis.package_url:"",label:meta.oasis&&meta.oasis.title?meta.oasis.title:"Occupational and Skills Information System (OaSIS)"},
  ];
  const research=(meta.research_sources||[]).map(item=>({url:item.url,label:item.name}));
  const seen=new Set();
  const deduped=links.concat(research).filter(item=>{
    if(!item.url)return false;
    if(seen.has(item.url))return false;
    seen.add(item.url);
    return true;
  });
  return`
    <section class="panel">
      <div class="section-head">
        <div>
          <h2>References And Notes</h2>
          <div class="section-copy">Labour metrics switch by geography. OaSIS profile content remains tied to the current official release.</div>
        </div>
      </div>
      ${renderNoteParagraphs([family.metric_rationale,meta.metric_model_note,family.exposure_rationale,meta.profile_layer_note])}
      <div class="sources-grid">${deduped.map(item=>sourceLink(item.url,item.label)).join("")}</div>
    </section>`;
}

function renderApp(){
  const app=document.getElementById("app");
  if(!app||!family)return;
  const stats=resolveStats(family);
  const jobsYear=stats.jobs_year||family.jobs_year||meta.jobs_year||"-";
  const trendWindow=stats.trend_from_year!=null&&jobsYear!=="-"?`${stats.trend_from_year}-${jobsYear}`:"recent";
  const outlookWindow=stats.outlook_window_start&&stats.outlook_window_end?`${stats.outlook_window_start}-${stats.outlook_window_end}`:`${meta.outlook_window_start||2025}-${meta.outlook_window_end||2027}`;
  const geoLabel=getGeoMeta(selectedGeo).label_en;
  document.title=`${family.title} | AI Exposure of the Canadian Job Market`;
  app.className="";
  app.innerHTML=`
    <div class="layout">
      <section class="hero">
        <div class="hero-main">
          <div class="eyebrow">Official major-group family page / ${escapeHTML(geoLabel)}</div>
          <h1>${escapeHTML(family.title)}</h1>
          <div class="summary">${escapeHTML(`${family.category}. This official major group contains ${family.official_unit_group_count} canonical unit groups and ${family.oasis_profile_count} attached OaSIS occupational profiles. Labour metrics update for the selected geography while OaSIS profile content stays fixed to the current official release.`)}</div>
          ${family.definition?`<div class="definition">${escapeHTML(family.definition)}</div>`:""}
          <div class="pill-row">
            <span class="pill accent-pill">NOC ${escapeHTML(family.noc_code)}</span>
            <span class="pill">${escapeHTML(geoLabel)}</span>
            <span class="pill">${escapeHTML(formatCompact(family.official_unit_group_count))} unit groups</span>
            <span class="pill">${escapeHTML(formatCompact(family.oasis_profile_count))} OaSIS profiles</span>
            <span class="pill">${escapeHTML(formatCompact(family.oasis_multi_profile_unit_group_count))} split-profile unit groups</span>
          </div>
        </div>
        <div class="hero-side">
          <div class="control-card stack">
            <div class="control-label">Geography</div>
            <label class="select-wrap">
              <select id="geographySelect" aria-label="Select geography">${getGeoList().map(geo=>`<option value="${escapeHTML(geo.code)}"${geo.code===selectedGeo?" selected":""}>${escapeHTML(geo.label_en)}</option>`).join("")}</select>
            </label>
            <div class="control-copy">${escapeHTML(pageSummaryCopy())}</div>
          </div>
          <div class="control-card stack">
            <div class="control-label">Family scope</div>
            <div class="panel-copy">${escapeHTML(`Broad category ${family.broad_category_code||"-"} ${family.broad_category_title||""}`.trim())}</div>
            <div class="panel-copy">${escapeHTML(`Sub-major groups: ${family.official_sub_major_group_count} | Minor groups: ${family.official_minor_group_count}`)}</div>
          </div>
        </div>
      </section>
      <section class="panel">
        <div class="section-head">
          <div>
            <h2>${escapeHTML(geoLabel)} Summary</h2>
            <div class="section-copy">${escapeHTML(`Selected geography metrics for the ${family.noc_code} family. EPIAC values remain mapped at the official Canadian source grain and do not change by geography.`)}</div>
          </div>
        </div>
        <div class="stat-grid">
          <div class="stat-card"><div class="stat-label">Workers</div><div class="stat-value">${escapeHTML(formatCompact(stats.jobs))}</div><div class="stat-sub">${escapeHTML(jobsYear!=="-"?`${jobsYear} estimate`:"Current estimate")}</div></div>
          <div class="stat-card"><div class="stat-label">Employment Share</div><div class="stat-value">${escapeHTML(formatPercent(stats.employment_share_pct))}</div><div class="stat-sub">${escapeHTML(`${geoLabel} labour market`)}</div></div>
          <div class="stat-card"><div class="stat-label">Employment Change</div><div class="stat-value">${escapeHTML(formatSignedPercent(stats.trend_pct))}</div><div class="stat-sub">${escapeHTML(`Trend window ${trendWindow}`)}</div></div>
          <div class="stat-card"><div class="stat-label">Median Hourly Wage</div><div class="stat-value">${escapeHTML(formatMoney(stats.pay_hourly))}</div><div class="stat-sub">${escapeHTML(jobsYear!=="-"?`${jobsYear} published value`:"Published value")}</div></div>
          <div class="stat-card"><div class="stat-label">Outlook</div><div class="stat-value text">${escapeHTML(stats.outlook_label||"Undetermined")}</div><div class="stat-sub">${escapeHTML(`${outlookWindow} ESDC outlook`)}</div></div>
          <div class="stat-card"><div class="stat-label">High-Exposure Share</div><div class="stat-value">${escapeHTML(formatPercent(family.epiac_high_exposure_pct))}</div><div class="stat-sub">${escapeHTML(`Mapped EPIAC ${family.epiac_reference_year||meta.exposure_reference_year||2021}`)}</div></div>
        </div>
      </section>
      <section class="panel">
        <div class="section-head">
          <div>
            <h2>Underlying Unit Groups</h2>
            <div class="section-copy">${escapeHTML(`${family.official_unit_group_count} official unit groups nested under major group ${family.noc_code}. Each card keeps the selected geography's labour metrics beside the attached OaSIS profiles.`)}</div>
          </div>
        </div>
        <div class="unit-list">${(family.units||[]).map(renderUnitCard).join("")}</div>
      </section>
      ${renderSourceSection()}
    </div>`;
  const geographySelect=document.getElementById("geographySelect");
  if(geographySelect){
    geographySelect.addEventListener("change",event=>{
      captureOpenState();
      selectedGeo=event.target.value;
      updateUrlState();
      updateBackLink();
      renderApp();
    });
  }
  updateBackLink();
  applyFocus();
}

function applyFocus(){
  document.querySelectorAll(".focused").forEach(node=>node.classList.remove("focused"));
  const focus=getFocusTarget();
  if(!focus)return;
  let target=null;
  if(/^\d{5}$/.test(focus)){
    const details=document.querySelector(`.unit-details[data-unit-code="${focus}"]`);
    if(details)details.open=true;
    target=document.getElementById(`unit-${focus}`);
  }else if(/^\d{5}\.\d{2}$/.test(focus)){
    const unitCode=focus.slice(0,5);
    const unitDetails=document.querySelector(`.unit-details[data-unit-code="${unitCode}"]`);
    if(unitDetails)unitDetails.open=true;
    const profileDetails=document.querySelector(`.profile-card[data-profile-code="${focus}"]`);
    if(profileDetails)profileDetails.open=true;
    target=document.getElementById(`profile-${focus.replace(".","-")}`);
  }else{
    target=document.getElementById(focus);
  }
  if(target){
    target.classList.add("focused");
    requestAnimationFrame(()=>target.scrollIntoView({behavior:"smooth",block:"start"}));
  }
}

function renderEmpty(message){
  const app=document.getElementById("app");
  if(!app)return;
  document.title="Family page not found";
  app.className="empty";
  app.innerHTML=escapeHTML(message);
}

function loadFamilyPage(){
  const slug=resolveFamilySlug();
  if(!slug){
    renderEmpty("No major-group family matched that route. Return to the dashboard and try again.");
    return;
  }
  fetch(`family-data/${slug}.json`).then(response=>{
    if(!response.ok)throw new Error(`HTTP ${response.status}`);
    return response.json();
  }).then(payload=>{
    meta=payload.meta||{};
    family=payload.family||null;
    if(!family){
      renderEmpty("No family payload matched that route.");
      return;
    }
    family.units=Array.isArray(family.units)?family.units:[];
    geoLookup=Object.fromEntries(getGeoList().map(geo=>[geo.code,geo]));
    selectedGeo=resolveSelectedGeo();
    if(!searchController&&window.initGlobalNocSearch){
      searchController=window.initGlobalNocSearch({
        mount: document.getElementById("globalSearchMount"),
        variant: "nav",
        searchIndexUrl: meta.search_index_route||"search-index.json",
        placeholder: "Search codes, titles, or aliases",
        helperText: "",
        getNavigationState: ()=>({
          geo: selectedGeo!==(meta.default_geography||"CA")?selectedGeo:"",
          view: resolveDashboardView()&&resolveDashboardView()!=="treemap"?resolveDashboardView():"",
        }),
      });
    }
    renderApp();
  }).catch(error=>{
    console.error(error);
    renderEmpty("Failed to load the family page.");
  });
}

window.addEventListener("hashchange",applyFocus);
loadFamilyPage();
