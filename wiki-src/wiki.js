/* Neutron wiki: sidebar search, group toggles, mobile drawer, starfield.
   Copied to wiki/wiki.js by build.py, which fills in the search index below.
   Every page is complete static HTML; this file only adds the interactive parts. */
(function(){
var INDEX = /*@INDEX@*/[];
var $ = function(s){ return document.querySelector(s); };

/* sidebar groups: click a heading to fold it (the group you are in stays open) */
var KEY = 'neutron-wiki-groups', saved = {};
try { saved = JSON.parse(sessionStorage.getItem(KEY)) || {}; } catch(e) {}
Array.prototype.forEach.call(document.querySelectorAll('.grp.toggle'), function(h){
  var body = h.nextElementSibling, label = h.getAttribute('data-group'), pinned = h.hasAttribute('data-active');
  function set(open){
    body.hidden = !open;
    h.querySelector('.chev').textContent = open ? '▾' : '▸';
    h.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (!pinned && Object.prototype.hasOwnProperty.call(saved, label)) set(!!saved[label]);
  function toggle(){
    if (pinned) return;
    var open = body.hidden; set(open); saved[label] = open;
    try { sessionStorage.setItem(KEY, JSON.stringify(saved)); } catch(e) {}
  }
  h.addEventListener('click', toggle);
  h.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
});

/* sidebar search: replaces the tree with matching articles while there is a query */
var q = $('#q'), tree = $('#tree');
if (q && tree) {
  var hits = document.createElement('div'); hits.hidden = true; tree.parentNode.appendChild(hits);
  var el = function(tag, cls, text){ var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  var search = function(){
    var v = q.value.trim().toLowerCase();
    if (!v) { hits.hidden = true; tree.hidden = false; return; }
    hits.innerHTML = '';
    var found = INDEX.filter(function(a){ return (a.t + ' ' + a.s + ' ' + a.S + ' ' + a.C).toLowerCase().indexOf(v) >= 0; });
    if (!found.length) hits.appendChild(el('div', 'noresult', 'No matches.'));
    found.slice(0, 40).forEach(function(a){
      var lbl = el('div', 'grp', a.S + ' · ' + a.C); lbl.style.margin = '10px 8px 2px';
      var w = el('div', 'arts'); w.style.margin = '0 0 4px 0';
      var link = el('a'); link.href = a.h;
      link.appendChild(el('span', 'dot ' + a.st)); link.appendChild(document.createTextNode(a.t));
      w.appendChild(link); hits.appendChild(lbl); hits.appendChild(w);
    });
    tree.hidden = true; hits.hidden = false;
  };
  q.addEventListener('input', search);
  if (q.value) search();
}

/* mobile drawer */
var sb = $('#sidebar'), scrim = $('#scrim'), btn = $('#menuBtn');
function closeDrawer(){ sb.classList.remove('open'); scrim.classList.remove('show'); }
if (btn) btn.addEventListener('click', function(){ sb.classList.toggle('open'); scrim.classList.toggle('show'); });
if (scrim) scrim.addEventListener('click', closeDrawer);
})();

/* starfield (shared, subtle) */
(function(){var c=document.querySelector('#starfield');if(!c)return;var x=c.getContext('2d');var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;var W,H,dpr,parts=[],t=0,raf=null;
function seed(){parts=[];var n=Math.min(500,Math.round(W*H/4200));for(var i=0;i<n;i++)parts.push({x:Math.random()*W,y:Math.random()*H,r:.4+Math.pow(Math.random(),1.7)*1.5,vx:(Math.random()-.5)*.05,vy:(Math.random()-.5)*.05,ph:Math.random()*6.28,tw:.3+Math.random()*1.5,red:Math.random()<.02});}
function resize(){dpr=Math.min(devicePixelRatio||1,2);W=innerWidth;H=innerHeight;c.width=W*dpr;c.height=H*dpr;x.setTransform(dpr,0,0,dpr,0,0);seed();if(reduce)draw();}
function draw(){x.clearRect(0,0,W,H);t+=.016;for(var i=0;i<parts.length;i++){var p=parts[i];p.x+=p.vx;p.y+=p.vy;if(p.x<-5)p.x=W+5;if(p.x>W+5)p.x=-5;if(p.y<-5)p.y=H+5;if(p.y>H+5)p.y=-5;var b=.06+.24*(p.r/1.9);var a=reduce?b:b*(.34+.66*Math.sin(t*p.tw+p.ph));x.globalAlpha=Math.max(a,.03);x.fillStyle=p.red?'#FC3D21':'#D9E4F4';x.beginPath();x.arc(p.x,p.y,p.r,0,6.28);x.fill();}x.globalAlpha=1;}
function loop(){draw();raf=requestAnimationFrame(loop);}
document.addEventListener('visibilitychange',function(){if(reduce)return;if(document.hidden)cancelAnimationFrame(raf);else loop();});
addEventListener('resize',resize);resize();if(!reduce)loop();})();
