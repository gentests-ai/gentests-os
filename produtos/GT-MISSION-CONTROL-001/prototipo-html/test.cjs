// Zero-dependency functional logic/render checks. Not a browser or accessibility test.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const elements = new Map();
const el = selector => {
  if (!elements.has(selector)) elements.set(selector, {innerHTML:'',textContent:'',value:'',dataset:{},addEventListener(){},setAttribute(){},focus(){},reset(){},querySelector(){return null;}});
  return elements.get(selector);
};
const context = vm.createContext({document:{querySelector:el,querySelectorAll:()=>[]},location:{hash:'#dashboard'},window:{addEventListener(){},scrollTo(){},scrollY:0},FormData:class{}});
vm.runInContext(fs.readFileSync(__dirname+'/app.js','utf8'),context);
let checks=0;
function check(name,code){assert.equal(vm.runInContext(code,context),true,name);checks++;console.log('PASS '+name);}
check('F-12 unique IDs and partition 10+2=12',"missions.length===12 && new Set(missions.map(m=>m.id)).size===12 && missions.filter(m=>m.state).length===10 && missions.filter(m=>!m.state).length===2");
check('Exact operational counts',"JSON.stringify(states.map(s=>missions.filter(m=>m.state===s).length))==='[0,1,1,2,1,2,1,2]'");
check('GT-DEMO-001 consistently awaiting review',"missions[0].state==='Aguardando revisão' && detail(missions[0]).includes('Aguardando revisão')");
check('ID/title search case insensitive',"filters.search='gt-demo-002';selected().length===1 && selected()[0].id==='GT-DEMO-002'");
check('Unknown quality filter excludes operational states',"filters.search='';filters.state='Estado não verificado';selected().length===2 && selected().every(m=>m.state===null)");
check('Verified KPI filter has 10 missions',"filters.state='Estado comprovado (fixture)';selected().length===10");
check('Combined area priority owner filters',"filters={search:'',state:'Em execução',area:'Engenharia',priority:'Alta',owner:'Agente de Engenharia'};selected().length===1 && selected()[0].id==='GT-DEMO-003'");
check('No results preserves collection',"filters.search='missing';selected().length===0 && missions.length===12");
check('Six independent milestones with absent acceptance/start',"filters={};let d=detail(missions[1]);milestones.every(t=>d.includes(t)) && !missions[1].events.some(e=>e.type===milestones[4]||e.type===milestones[5])");
check('Merged does not imply mission closed',"missions[10].merged && missions[10].state===null && !missions[10].closed && detail(missions[10]).includes('encerramento NÃO VERIFICADO')");
check('Event provenance individual and unique',"missions.every(m=>new Set(m.events.map(e=>e.id)).size===m.events.length && m.events.every(e=>e.actor&&e.occurred&&e.observed&&e.source&&e.parser))");
check('Missing metric is not zero',"dashboard(missions).includes('Lead time: Não apurado')");
check('Error preserves data, last success and attempt',"scenario='error';render();selected().length===12 && document.querySelector('#sync').innerHTML.includes('14:00') && document.querySelector('#sync').innerHTML.includes('14:15') && document.querySelector('#sync').innerHTML.includes('429')");
check('Stale warning retained',"scenario='stale';render();document.querySelector('#sync').innerHTML.includes('desatualizados')");
check('Verified empty is distinct from partial no results',"scenario='empty';render();selected().length===0 && emptyMessage().includes('vazio verificado') && document.querySelector('#sync').innerHTML.includes('0/0')");
check('Mission, evidence and missing source routes render',"scenario='normal';location.hash='#mission/GT-DEMO-002';render();document.querySelector('#main').innerHTML.includes('Marcos independentes');location.hash='#evidence/GT-DEMO-002/2';render();document.querySelector('#main').innerHTML.includes('Evidência FICTÍCIA');location.hash='#evidence/GT-DEMO-002/99';render();document.querySelector('#main').innerHTML.includes('Fonte indisponível')");
check('All primary routes render',"['#dashboard','#missions','#agents','#alerts','#trace'].every(h=>{location.hash=h;render();return document.querySelector('#main').innerHTML.length>100;})");
check('Safe text escaping',"esc('<img onerror=alert(1)>').includes('&lt;') && !esc('<img onerror=alert(1)>').includes('<img')");
const html=fs.readFileSync(__dirname+'/index.html','utf8');
assert(html.includes("connect-src 'none'") && !/https?:\/\//.test(html));checks++;console.log('PASS offline CSP / no remote assets');
assert(!/\b(fetch|XMLHttpRequest|WebSocket|localStorage|sessionStorage)\b/.test(fs.readFileSync(__dirname+'/app.js','utf8')));checks++;console.log('PASS no network/storage APIs');
console.log(`${checks} checks passed. DOM stub: browser layout, keyboard and screen reader pending.`);
