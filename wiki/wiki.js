/* Neutron wiki: sidebar search, group toggles, mobile drawer, starfield.
   Copied to wiki/wiki.js by build.py, which fills in the search index below.
   Every page is complete static HTML; this file only adds the interactive parts. */
(function(){
var INDEX = [{"t":"What is Neutron?","s":"The three pieces, in one minute.","S":"Getting Started","C":"Basics","h":"/wiki/start/basics/what-is-neutron/","st":"guide"},{"t":"Installing Collider","s":"From a clean Linux machine to your first Adobe launch — the whole stack, end to end.","S":"Getting Started","C":"Basics","h":"/wiki/start/basics/install-collider/","st":"guide"},{"t":"Running your first app","s":"You clicked Launch — here’s what to expect, and how to get to real work.","S":"Getting Started","C":"Basics","h":"/wiki/start/basics/first-app/","st":"guide"},{"t":"What Neutron does","s":"The engine, and the one rule that holds it together.","S":"Neutron","C":"Overview","h":"/wiki/neutron/overview/what-it-is/","st":"guide"},{"t":"Where the fixes live","s":"Neither Wine nor Adobe is broken — the defect is in the seam.","S":"Neutron","C":"Architecture","h":"/wiki/neutron/architecture/where-fixes-live/","st":"guide"},{"t":"Native GPU canvas & present path","s":"Drawing straight to the GPU under Wayland.","S":"Neutron","C":"Features","h":"/wiki/neutron/features/native-canvas/","st":"stub"},{"t":"AI/ML features running natively","s":"Camera Raw Denoise and AI masking on Linux.","S":"Neutron","C":"Features","h":"/wiki/neutron/features/ai-features/","st":"stub"},{"t":"The ten-second menu","s":"Why Lightroom’s “Edit in Photoshop” hung — and how a quarter-second file read explains it.","S":"Neutron","C":"Fixes","h":"/wiki/neutron/fixes/edit-in-lag/","st":"fix"},{"t":"Owned/modal dialogs not shown (Wayland)","s":"Some modal dialogs render but never display.","S":"Neutron","C":"Known Issues","h":"/wiki/neutron/issues/owned-popups/","st":"issue"},{"t":"How runtimes are versioned","s":"Proton-style: the repo is the recipe, releases are prebuilt trees.","S":"Neutron","C":"Runtimes & Builds","h":"/wiki/neutron/runtimes/versioned-runtimes/","st":"guide"},{"t":"What Collider is","s":"The launcher, and why it deliberately knows nothing about fixes.","S":"Collider","C":"Overview","h":"/wiki/collider/overview/what-it-is/","st":"guide"},{"t":"Appearance & theming","s":"Color themes and custom app icons.","S":"Collider","C":"Features","h":"/wiki/collider/features/appearance/","st":"stub"},{"t":"Per-app widgets","s":"A tinted tile for each installed app.","S":"Collider","C":"Features","h":"/wiki/collider/features/app-widgets/","st":"stub"},{"t":"Installing Collider","s":"","S":"Collider","C":"Setup","h":"/wiki/collider/setup/install/","st":"stub"},{"t":"Known issues","s":"","S":"Collider","C":"Known Issues","h":"/wiki/collider/issues/placeholder/","st":"stub"},{"t":"What Mud Hut is","s":"One-click Adobe install, no manual prefix.","S":"Mud Hut","C":"Overview","h":"/wiki/mudhut/overview/what-it-is/","st":"guide"},{"t":"Capabilities","s":"","S":"Mud Hut","C":"Features","h":"/wiki/mudhut/features/placeholder/","st":"stub"},{"t":"Common install problems","s":"When an install doesn’t go cleanly.","S":"Mud Hut","C":"Troubleshooting","h":"/wiki/mudhut/troubleshooting/placeholder/","st":"stub"},{"t":"What works","s":"","S":"Photoshop","C":"Status","h":"/wiki/photoshop/status/overview/","st":"stub"},{"t":"Notable fixes","s":"","S":"Photoshop","C":"Fixes","h":"/wiki/photoshop/fixes/placeholder/","st":"stub"},{"t":"Known issues","s":"","S":"Photoshop","C":"Known Issues","h":"/wiki/photoshop/issues/placeholder/","st":"stub"},{"t":"What works","s":"Where Lightroom Classic stands today.","S":"Lightroom Classic","C":"Status","h":"/wiki/lightroom/status/overview/","st":"feature"},{"t":"The ten-second Edit-In menu","s":"Filed in full under Neutron → Fixes.","S":"Lightroom Classic","C":"Fixes","h":"/wiki/lightroom/fixes/edit-in-lag/","st":"fix"},{"t":"Known issues","s":"The cosmetic rough edges, detailed.","S":"Lightroom Classic","C":"Known Issues","h":"/wiki/lightroom/issues/placeholder/","st":"stub"},{"t":"What works","s":"","S":"Premiere Pro","C":"Status","h":"/wiki/premiere/status/overview/","st":"stub"},{"t":"Known issues","s":"","S":"Premiere Pro","C":"Known Issues","h":"/wiki/premiere/issues/placeholder/","st":"stub"},{"t":"What works","s":"","S":"After Effects","C":"Status","h":"/wiki/aftereffects/status/overview/","st":"stub"},{"t":"Known issues","s":"","S":"After Effects","C":"Known Issues","h":"/wiki/aftereffects/issues/placeholder/","st":"stub"}];
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
