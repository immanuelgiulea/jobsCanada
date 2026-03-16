(function(){
  const KIND_ORDER={major:0,unit:1,profile:2}
  const KIND_LABELS={major:"Major groups",unit:"Unit groups",profile:"OaSIS profiles"}
  const RESULT_LIMITS={major:4,unit:6,profile:6}
  const DEFAULT_PLACEHOLDER="Search major-group codes, unit-group codes, OaSIS profile codes, titles, or aliases"
  let instanceCounter=0
  let cachedIndexPromise=null

  function escapeHTML(value){
    return String(value).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;").replaceAll("'","&#39;")
  }

  function normalizeText(value){
    return String(value||"").toLowerCase().replace(/[^a-z0-9]+/g," ").trim().replace(/\s+/g," ")
  }

  function normalizeCode(value){
    return String(value||"").replace(/\D+/g,"")
  }

  function looksLikeCode(raw,codeNorm){
    return /^[\d.\s-]+$/.test(String(raw||"").trim())&&[2,5,7].includes(codeNorm.length)
  }

  function matchTextScore(query,target){
    if(!query||!target)return 0
    if(target===query)return 460
    if(target.startsWith(query))return 390
    if(target.split(" ").some(word=>word.startsWith(query)))return 340
    const queryParts=query.split(" ").filter(Boolean)
    if(queryParts.length>1&&queryParts.every(part=>target.includes(part)))return 300
    if(query.length>=3&&target.includes(query))return 240
    return 0
  }

  function prepareIndex(payload){
    const entries=(payload&&Array.isArray(payload.entries)?payload.entries:[]).map((entry,index)=>{
      const aliases=Array.isArray(entry.a)?entry.a.filter(Boolean):[]
      return{
        ...entry,
        _index:index,
        _codeNorm:normalizeCode(entry.c),
        _titleNorm:normalizeText(entry.t),
        _aliasNorms:aliases.map(normalizeText).filter(Boolean),
      }
    })
    const exactCodeLookup=new Map()
    for(const entry of entries){
      if(entry._codeNorm&&!exactCodeLookup.has(entry._codeNorm))exactCodeLookup.set(entry._codeNorm,entry)
    }
    return{meta:payload&&payload.meta?payload.meta:{},entries,exactCodeLookup}
  }

  function loadSearchIndex(searchIndexUrl){
    if(!cachedIndexPromise){
      cachedIndexPromise=fetch(searchIndexUrl||"search-index.json").then(response=>{
        if(!response.ok)throw new Error(`HTTP ${response.status}`)
        return response.json()
      }).then(prepareIndex)
    }
    return cachedIndexPromise
  }

  function scoreEntry(entry,textNorm,codeNorm){
    let score=0
    let matchKind=""
    let matchValue=""
    if(codeNorm){
      if(entry._codeNorm===codeNorm){
        score=1200
        matchKind="code"
        matchValue=entry.c
      }else if(entry._codeNorm.startsWith(codeNorm)){
        score=880-Math.min(120,entry._codeNorm.length-codeNorm.length)
        matchKind="code"
        matchValue=entry.c
      }
    }
    const titleScore=matchTextScore(textNorm,entry._titleNorm)
    if(titleScore>score){
      score=titleScore
      matchKind="title"
      matchValue=entry.t
    }
    const aliases=Array.isArray(entry.a)?entry.a:[]
    for(let index=0;index<entry._aliasNorms.length;index++){
      const aliasScore=matchTextScore(textNorm,entry._aliasNorms[index])
      if(aliasScore>score){
        score=aliasScore
        matchKind="alias"
        matchValue=aliases[index]||""
      }
    }
    return score?{score,matchKind,matchValue}:null
  }

  function searchEntries(index,query){
    const raw=String(query||"").trim()
    const textNorm=normalizeText(raw)
    const codeNorm=normalizeCode(raw)
    if(!raw||(!textNorm&&!codeNorm))return{directHit:null,groups:{major:[],unit:[],profile:[]},items:[]}
    const directHit=looksLikeCode(raw,codeNorm)?index.exactCodeLookup.get(codeNorm)||null:null
    const matches=[]
    for(const entry of index.entries){
      const result=scoreEntry(entry,textNorm,codeNorm)
      if(!result)continue
      matches.push({...entry,_score:result.score,_matchKind:result.matchKind,_matchValue:result.matchValue})
    }
    matches.sort((left,right)=>{
      if(right._score!==left._score)return right._score-left._score
      if(KIND_ORDER[left.k]!==KIND_ORDER[right.k])return KIND_ORDER[left.k]-KIND_ORDER[right.k]
      return String(left.c).localeCompare(String(right.c))
    })
    const groups={major:[],unit:[],profile:[]}
    for(const match of matches){
      const bucket=groups[match.k]
      if(!bucket||bucket.length>=(RESULT_LIMITS[match.k]||5))continue
      bucket.push(match)
    }
    const items=[...groups.major,...groups.unit,...groups.profile]
    return{directHit,groups,items}
  }

  function resultSubtitle(entry){
    const parts=[]
    if(entry.k==="major")parts.push("NOC major group")
    else if(entry.k==="unit")parts.push(`Unit group in major ${entry.m}`)
    else parts.push(`OaSIS profile for unit ${entry.u||String(entry.c).slice(0,5)}`)
    if(entry._matchKind==="alias"&&entry._matchValue)parts.push(`Alias: ${entry._matchValue}`)
    return parts.join(" | ")
  }

  function focusHashForEntry(entry){
    if(entry.k==="unit"&&entry.f)return`#unit-${entry.f}`
    if(entry.k==="profile"&&entry.f)return`#profile-${String(entry.f).replace(".","-")}`
    return""
  }

  function buildEntryUrl(entry,state){
    const params=new URLSearchParams()
    const context=state&&typeof state==="object"?state:{}
    for(const [key,value] of Object.entries(context)){
      if(value==null||value==="")continue
      params.set(key,String(value))
    }
    if(entry.f)params.set("focus",String(entry.f))
    const search=params.toString()
    return`${entry.r}${search?`?${search}`:""}${focusHashForEntry(entry)}`
  }

  function renderGroups(query,results,activeIndex){
    const sections=[]
    if(results.directHit){
      sections.push(`<div class="global-search__hint">Press Enter to open exact code hit: <strong>${escapeHTML(results.directHit.c)}</strong></div>`)
    }
    for(const kind of["major","unit","profile"]){
      const items=results.groups[kind]||[]
      if(!items.length)continue
      sections.push(
        `<section class="global-search__group"><div class="global-search__group-title">${escapeHTML(KIND_LABELS[kind])}</div><div class="global-search__results">${items.map((item,index)=>{
          const itemIndex=[...results.groups.major,...results.groups.unit,...results.groups.profile].indexOf(item)
          return`<button type="button" class="global-search__result${itemIndex===activeIndex?" is-active":""}" data-index="${itemIndex}" role="option" aria-selected="${itemIndex===activeIndex?"true":"false"}"><span class="global-search__result-code">${escapeHTML(item.c)}</span><span class="global-search__result-copy"><span class="global-search__result-title">${escapeHTML(item.t)}</span><span class="global-search__result-sub">${escapeHTML(resultSubtitle(item))}</span></span></button>`
        }).join("")}</div></section>`
      )
    }
    if(!sections.length){
      return`<div class="global-search__empty">No matches for "${escapeHTML(query)}".</div>`
    }
    return sections.join("")
  }

  window.initGlobalNocSearch=function initGlobalNocSearch(options){
    const mount=options&&options.mount&&options.mount.nodeType===1?options.mount:document.getElementById(options&&options.mountId?options.mountId:"globalSearchMount")
    if(!mount)return null
    instanceCounter+=1
    const inputId=`global-search-input-${instanceCounter}`
    const panelId=`global-search-panel-${instanceCounter}`
    const label=options&&Object.prototype.hasOwnProperty.call(options,"label")?options.label:"Global NOC search"
    const helperText=options&&Object.prototype.hasOwnProperty.call(options,"helperText")?options.helperText:"Matches major-group codes, unit-group codes, OaSIS profile codes, titles, and aliases."
    const placeholder=options&&Object.prototype.hasOwnProperty.call(options,"placeholder")?options.placeholder:DEFAULT_PLACEHOLDER
    const variant=options&&Object.prototype.hasOwnProperty.call(options,"variant")?options.variant:"default"
    mount.innerHTML=`<div class="global-search global-search--${escapeHTML(variant)}"><div class="global-search__shell"><label class="global-search__label" for="${inputId}">${escapeHTML(label)}</label><div class="global-search__input-wrap"><input id="${inputId}" class="global-search__input" type="search" placeholder="${escapeHTML(placeholder)}" autocomplete="off" spellcheck="false" aria-autocomplete="list" aria-controls="${panelId}" aria-expanded="false"><button type="button" class="global-search__clear" aria-label="Clear search" hidden>&times;</button></div>${helperText?`<div class="global-search__helper">${escapeHTML(helperText)}</div>`:""}<div id="${panelId}" class="global-search__panel" role="listbox" hidden></div></div></div>`
    const root=mount.querySelector(".global-search")
    const input=mount.querySelector(".global-search__input")
    const clearButton=mount.querySelector(".global-search__clear")
    const panel=mount.querySelector(".global-search__panel")
    const searchIndexUrl=options&&options.searchIndexUrl?options.searchIndexUrl:"search-index.json"
    const getNavigationState=options&&typeof options.getNavigationState==="function"?options.getNavigationState:()=>({})
    const navigateHandler=options&&typeof options.navigate==="function"?options.navigate:null
    let index=null
    let latestResults={directHit:null,groups:{major:[],unit:[],profile:[]},items:[]}
    let activeIndex=-1

    loadSearchIndex(searchIndexUrl).then(value=>{
      index=value
    }).catch(error=>{
      console.error(error)
      input.disabled=true
      input.placeholder="Search index unavailable"
    })

    function closePanel(){
      activeIndex=-1
      panel.hidden=true
      root.classList.remove("is-open")
      input.setAttribute("aria-expanded","false")
      input.removeAttribute("aria-activedescendant")
    }

    function syncClearButton(){
      clearButton.hidden=!input.value
    }

    function navigateToEntry(entry){
      if(!entry)return
      const url=buildEntryUrl(entry,getNavigationState())
      closePanel()
      if(navigateHandler&&navigateHandler({entry,url})===true)return
      window.location.assign(url)
    }

    function setActiveIndex(nextIndex){
      if(!latestResults.items.length){
        activeIndex=-1
        input.removeAttribute("aria-activedescendant")
        return
      }
      activeIndex=(nextIndex+latestResults.items.length)%latestResults.items.length
      panel.innerHTML=renderGroups(input.value.trim(),latestResults,activeIndex)
      panel.querySelectorAll(".global-search__result").forEach(button=>{
        button.addEventListener("click",()=>navigateToEntry(latestResults.items[Number(button.dataset.index)]))
      })
      const activeButton=panel.querySelector(`.global-search__result[data-index="${activeIndex}"]`)
      if(activeButton){
        activeButton.id=`${panelId}-option-${activeIndex}`
        input.setAttribute("aria-activedescendant",activeButton.id)
        activeButton.scrollIntoView({block:"nearest"})
      }
    }

    async function refreshResults(){
      const query=input.value.trim()
      syncClearButton()
      if(!query){
        latestResults={directHit:null,groups:{major:[],unit:[],profile:[]},items:[]}
        closePanel()
        return
      }
      if(!index){
        try{
          index=await loadSearchIndex(searchIndexUrl)
        }catch(error){
          console.error(error)
          return
        }
      }
      latestResults=searchEntries(index,query)
      activeIndex=-1
      panel.innerHTML=renderGroups(query,latestResults,activeIndex)
      panel.querySelectorAll(".global-search__result").forEach(button=>{
        button.addEventListener("click",()=>navigateToEntry(latestResults.items[Number(button.dataset.index)]))
      })
      panel.hidden=false
      root.classList.add("is-open")
      input.setAttribute("aria-expanded","true")
      input.removeAttribute("aria-activedescendant")
    }

    input.addEventListener("input",()=>{void refreshResults()})
    input.addEventListener("focus",()=>{if(input.value.trim())void refreshResults()})
    input.addEventListener("search",()=>{void refreshResults()})
    input.addEventListener("keydown",event=>{
      if(event.key==="ArrowDown"){
        if(!panel.hidden&&latestResults.items.length){
          event.preventDefault()
          setActiveIndex(activeIndex+1)
        }
        return
      }
      if(event.key==="ArrowUp"){
        if(!panel.hidden&&latestResults.items.length){
          event.preventDefault()
          setActiveIndex(activeIndex-1)
        }
        return
      }
      if(event.key==="Escape"){
        closePanel()
        return
      }
      if(event.key!=="Enter")return
      if(activeIndex>=0&&latestResults.items[activeIndex]){
        event.preventDefault()
        navigateToEntry(latestResults.items[activeIndex])
        return
      }
      const raw=input.value.trim()
      const codeNorm=normalizeCode(raw)
      if(index&&looksLikeCode(raw,codeNorm)){
        const exact=index.exactCodeLookup.get(codeNorm)
        if(exact){
          event.preventDefault()
          navigateToEntry(exact)
          return
        }
      }
      if(raw){
        event.preventDefault()
        void refreshResults()
      }
    })

    clearButton.addEventListener("click",()=>{
      input.value=""
      syncClearButton()
      closePanel()
      input.focus()
    })

    document.addEventListener("click",event=>{
      if(!mount.contains(event.target))closePanel()
    })

    return{
      close:closePanel,
      focus(){input.focus()}
    }
  }
})()
