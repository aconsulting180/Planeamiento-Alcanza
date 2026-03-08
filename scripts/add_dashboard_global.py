"""
Add Dashboard Global page to Planeamiento_2026.html
Shows:
  - Global PPC chart with 3 lines: PPC LB (75%), PPC Mensual, PPC Acumulado
  - Per-area PPC comparison chart
  - Per-area restriction summary
  - Summary stats
"""

FILE = 'Planeamiento_2026.html'

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1) SIDEBAR: Add "Dashboard Global" nav-item after Dashboard
# ============================================================
sidebar_anchor = '  <div class="nav-item active" onclick="showPage(\'dashboard\')"><span class="icon"><i class="ri-dashboard-3-line"></i></span><span>Dashboard</span></div>'
sidebar_insert = sidebar_anchor + '\n  <div class="nav-item" onclick="showPage(\'dashboard-global\')"><span class="icon"><i class="ri-pie-chart-2-line"></i></span><span>Dashboard Global</span></div>'

assert sidebar_anchor in html, "ERROR: sidebar anchor not found"
html = html.replace(sidebar_anchor, sidebar_insert)
print("[1/5] Sidebar nav-item added ✓")

# ============================================================
# 2) PAGE DIV: Add page-dashboard-global after page-dashboard close
# ============================================================
# The dashboard page ends right before the first area page div
page_anchor = '  <div class="page" id="page-la-gis"></div>'
# Actually I need to find where dashboard closes. Let me find better anchor.
# The dashboard page closes with </div> before the area page divs.
# Let me insert the new page div before the first area page.
# But actually, the area pages are in order: inmob first now... Let me check:
# page-la-inmob comes first since we reordered
page_anchor = '  <div class="page" id="page-la-inmob"></div>'
page_insert = """  <!-- DASHBOARD GLOBAL -->
  <div class="page" id="page-dashboard-global"></div>

  """ + page_anchor

assert page_anchor in html, "ERROR: page anchor not found"
html = html.replace(page_anchor, page_insert, 1)
print("[2/5] Page div added ✓")

# ============================================================
# 3) showPage MAP: Add 'dashboard-global' after 'dashboard'
# ============================================================
map_old = "const map=['dashboard','la-inmob'"
map_new = "const map=['dashboard','dashboard-global','la-inmob'"

assert map_old in html, "ERROR: showPage map anchor not found"
html = html.replace(map_old, map_new)
print("[3/5] showPage map updated ✓")

# ============================================================
# 4) showPage FUNCTION: Add render call for dashboard-global
# ============================================================
render_anchor = "  if(id==='dashboard')updateDash();"
render_insert = render_anchor + "\n  if(id==='dashboard-global')renderDashGlobal();"

assert render_anchor in html, "ERROR: showPage render anchor not found"
html = html.replace(render_anchor, render_insert)
print("[4/5] showPage render call added ✓")

# ============================================================
# 5) JS FUNCTION: Add renderDashGlobal() before EXPORT PDF section
# ============================================================
js_anchor = """// ══════════════════════════════════════════════════════════════════
// EXPORT PDF — coordenadas absolutas + onclone + html2pdf 0.9.3
// ══════════════════════════════════════════════════════════════════"""

js_new_func = r"""// ══════════════════════════════════════════════════════════════════
// DASHBOARD GLOBAL
// ══════════════════════════════════════════════════════════════════
let _dgC={};
function renderDashGlobal(){
  const el=document.getElementById('page-dashboard-global');
  if(!el)return;
  const areas=[
    {key:'inmob',label:'Inmobiliaria',color:'var(--orange)',hex:'#ED7D31'},
    {key:'const',label:'Constructora',color:'#7B2D8E',hex:'#7B2D8E'},
    {key:'gis',label:'GIS',color:'var(--med-blue)',hex:'#4472C4'},
    {key:'metro',label:'Metropolitano',color:'var(--green)',hex:'#548235'},
    {key:'rental',label:'CEQ Rental',color:'#00897B',hex:'#00897B'},
  ];

  // Calculate global monthly PPC
  const globalMonthly=[];
  let gTC=0,gTE=0;
  for(let m=1;m<=12;m++){
    let mc=0,me=0;
    areas.forEach(a=>{
      const acts=flatActs(a.key);
      acts.forEach(act=>{
        const pk=getPMKey(act._oi,act._ei,act._ai);
        const pmS=S.pm[a.key]?.[pk]?.[m];
        if(pmS&&pmS.plan){
          const p=S.ppc[a.key]?.[pk]?.[m];
          if(p?.compr){mc++;gTC++;}
          if(p?.ejec){me++;gTE++;}
        }
      });
    });
    globalMonthly.push({m,compr:mc,ejec:me,ppc:mc>0?Math.round(me/mc*100):0});
  }
  const globalPPC=gTC>0?Math.round(gTE/gTC*100):0;

  // PPC Acumulado (cumulative)
  let cumC=0,cumE=0;
  const ppcAcum=globalMonthly.map(gm=>{
    cumC+=gm.compr;cumE+=gm.ejec;
    return cumC>0?Math.round(cumE/cumC*100):0;
  });
  const ppcMensual=globalMonthly.map(gm=>gm.ppc);
  const ppcLB=Array(12).fill(75);

  // Per-area monthly PPC
  const perArea=areas.map(a=>{
    const d=calcPPCData(a.key);
    const restr=(S.ar[a.key]||[]).filter(r=>r.estado!=='Levantada').length;
    return {...a,data:d,restr};
  });

  // Total restrictions
  const totalRestr=perArea.reduce((s,a)=>s+a.restr,0);

  let h=`<div class="page-header">
    <h2><i class="ri-pie-chart-2-line" style="color:var(--light-blue)"></i> Dashboard Global — Planeamiento 2026</h2>
    <div style="display:flex;gap:8px;flex-wrap:wrap">
      <button class="btn btn-pdf btn-sm" onclick="exportPagePDF('page-dashboard-global','landscape','a4')"><i class="ri-file-pdf-2-line"></i> PDF</button>
      <button class="btn btn-outline btn-sm" onclick="showPage('dashboard')"><i class="ri-arrow-left-s-line"></i> Dashboard</button>
    </div>
  </div>`;

  // Summary stats row
  const gCls=globalPPC>=80?'var(--green)':'var(--red)';
  h+=`<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px">
    <div class="stat-card" style="border-left:4px solid var(--dark-blue)"><div class="stat-value" style="color:${gCls}">${globalPPC}%</div><div class="stat-label">PPC Global</div></div>
    <div class="stat-card" style="border-left:4px solid var(--orange)"><div class="stat-value" style="color:var(--orange)">${gTC}</div><div class="stat-label">Total Comprometidas</div></div>
    <div class="stat-card" style="border-left:4px solid var(--green)"><div class="stat-value" style="color:var(--green)">${gTE}</div><div class="stat-label">Total Ejecutadas</div></div>
    <div class="stat-card" style="border-left:4px solid var(--red)"><div class="stat-value" style="color:var(--red)">${totalRestr}</div><div class="stat-label">Restricciones Activas</div></div>
  </div>`;

  // Per-area PPC row
  h+=`<div class="stats-row" style="margin-bottom:24px">`;
  perArea.forEach(a=>{
    const cls=a.data.global>=80?'var(--green)':'var(--red)';
    h+=`<div class="stat-card" style="border-left:4px solid ${a.color}"><div class="stat-value" style="color:${cls}">${a.data.global}%</div><div class="stat-label">PPC ${a.label}</div></div>`;
  });
  h+=`</div>`;

  // MAIN CHART: PPC Global (like the image)
  h+=`<div class="card" style="padding:24px;margin-bottom:20px">
    <h3 style="text-align:center;font-size:18px;font-weight:800;margin-bottom:18px;color:var(--dark-blue)">PORCENTAJE DE PLAN COMPLETADO [PPC]</h3>
    <div style="max-width:900px;margin:0 auto"><canvas id="dg-chart-global"></canvas></div>
  </div>`;

  // PER-AREA CHARTS ROW
  h+=`<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:20px">`;
  h+=`<div class="card" style="padding:18px"><h4 style="margin-bottom:10px;color:var(--dark-blue)">PPC Mensual por Área</h4><canvas id="dg-chart-areas"></canvas></div>`;
  h+=`<div class="card" style="padding:18px"><h4 style="margin-bottom:10px;color:var(--dark-blue)">Comprometidas vs Ejecutadas por Área</h4><canvas id="dg-chart-bars"></canvas></div>`;
  h+=`</div>`;

  // Per-area restriction chart
  h+=`<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:20px">`;
  h+=`<div class="card" style="padding:18px"><h4 style="margin-bottom:10px;color:var(--dark-blue)">Restricciones Activas por Área</h4><canvas id="dg-chart-restr"></canvas></div>`;
  h+=`<div class="card" style="padding:18px"><h4 style="margin-bottom:10px;color:var(--dark-blue)">PPC Acumulado por Área</h4><canvas id="dg-chart-acum-area"></canvas></div>`;
  h+=`</div>`;

  el.innerHTML=h;

  // Destroy old charts
  Object.keys(_dgC).forEach(k=>{if(_dgC[k])_dgC[k].destroy();});
  _dgC={};

  // CHART 1: Global PPC (3 lines like the image)
  const c1=document.getElementById('dg-chart-global');
  if(c1)_dgC.global=new Chart(c1,{type:'line',data:{labels:MONTHS.slice(1),datasets:[
    {label:'PPC LB',data:ppcLB,borderColor:'#1B2A4A',backgroundColor:'transparent',borderWidth:3,pointRadius:4,pointBackgroundColor:'#1B2A4A',tension:0,fill:false},
    {label:'PPC Mensual',data:ppcMensual,borderColor:'#C00000',backgroundColor:'transparent',borderWidth:3,pointRadius:5,pointBackgroundColor:'#C00000',tension:0.3,fill:false},
    {label:'PPC Acum',data:ppcAcum,borderColor:'#ED7D31',backgroundColor:'transparent',borderWidth:3,pointRadius:5,pointBackgroundColor:'#ED7D31',tension:0.3,fill:false},
  ]},options:{responsive:true,scales:{y:{min:0,max:100,ticks:{callback:v=>v+'%',stepSize:20}},x:{grid:{display:false}}},plugins:{legend:{position:'top',labels:{usePointStyle:true,pointStyle:'rect',padding:20,font:{size:13,weight:'bold'}}}}}});

  // CHART 2: Per-area PPC line chart
  const c2=document.getElementById('dg-chart-areas');
  if(c2){
    const datasets=perArea.map(a=>({
      label:a.label,data:a.data.monthly.map(m=>m.ppc),borderColor:a.hex,backgroundColor:'transparent',borderWidth:2.5,pointRadius:4,pointBackgroundColor:a.hex,tension:0.3,fill:false
    }));
    datasets.push({label:'Meta 75%',data:Array(12).fill(75),borderColor:'#999',borderWidth:1.5,borderDash:[6,3],pointRadius:0,fill:false});
    _dgC.areas=new Chart(c2,{type:'line',data:{labels:MONTHS.slice(1),datasets},options:{responsive:true,scales:{y:{min:0,max:100,ticks:{callback:v=>v+'%'}}},plugins:{legend:{position:'bottom',labels:{usePointStyle:true}}}}});
  }

  // CHART 3: Per-area bar chart (committed vs executed)
  const c3=document.getElementById('dg-chart-bars');
  if(c3)_dgC.bars=new Chart(c3,{type:'bar',data:{labels:perArea.map(a=>a.label),datasets:[
    {label:'Comprometidas',data:perArea.map(a=>a.data.tc),backgroundColor:perArea.map(a=>a.hex+'99'),borderColor:perArea.map(a=>a.hex),borderWidth:1,borderRadius:4},
    {label:'Ejecutadas',data:perArea.map(a=>a.data.te),backgroundColor:perArea.map(a=>a.hex),borderRadius:4},
  ]},options:{responsive:true,plugins:{legend:{position:'bottom'}}}});

  // CHART 4: Restrictions bar chart
  const c4=document.getElementById('dg-chart-restr');
  if(c4)_dgC.restr=new Chart(c4,{type:'bar',data:{labels:perArea.map(a=>a.label),datasets:[
    {label:'Restricciones Activas',data:perArea.map(a=>a.restr),backgroundColor:perArea.map(a=>a.hex),borderRadius:4},
  ]},options:{responsive:true,indexAxis:'y',plugins:{legend:{display:false}}}});

  // CHART 5: Per-area cumulative PPC
  const c5=document.getElementById('dg-chart-acum-area');
  if(c5){
    const dsAcum=perArea.map(a=>{
      let cc=0,ce=0;
      const acumData=a.data.monthly.map(m=>{cc+=m.compr;ce+=m.ejec;return cc>0?Math.round(ce/cc*100):0;});
      return {label:a.label,data:acumData,borderColor:a.hex,backgroundColor:'transparent',borderWidth:2.5,pointRadius:3,pointBackgroundColor:a.hex,tension:0.3,fill:false};
    });
    dsAcum.push({label:'Meta 75%',data:Array(12).fill(75),borderColor:'#999',borderWidth:1.5,borderDash:[6,3],pointRadius:0,fill:false});
    _dgC.acumArea=new Chart(c5,{type:'line',data:{labels:MONTHS.slice(1),datasets:dsAcum},options:{responsive:true,scales:{y:{min:0,max:100,ticks:{callback:v=>v+'%'}}},plugins:{legend:{position:'bottom',labels:{usePointStyle:true}}}}});
  }
}

""" + js_anchor

assert js_anchor in html, "ERROR: JS anchor not found"
html = html.replace(js_anchor, js_new_func)
print("[5/5] renderDashGlobal() function added ✓")

# ============================================================
# WRITE
# ============================================================
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Dashboard Global page added!")
print(f"   File size: {len(html):,} chars")

# ============================================================
# VERIFICATION
# ============================================================
print("\n=== VERIFICATION ===")
checks = 0

# V1: Sidebar has Dashboard Global nav-item
assert "showPage('dashboard-global')" in html
checks += 1
print(f"  V{checks}: Sidebar nav-item present ✓")

# V2: Page div exists
assert 'id="page-dashboard-global"' in html
checks += 1
print(f"  V{checks}: Page div present ✓")

# V3: showPage map includes dashboard-global
assert "'dashboard','dashboard-global','la-inmob'" in html
checks += 1
print(f"  V{checks}: showPage map updated ✓")

# V4: showPage render call
assert "if(id==='dashboard-global')renderDashGlobal()" in html
checks += 1
print(f"  V{checks}: showPage render call present ✓")

# V5: renderDashGlobal function exists
assert "function renderDashGlobal()" in html
checks += 1
print(f"  V{checks}: renderDashGlobal function present ✓")

# V6: Global PPC chart canvas
assert 'id="dg-chart-global"' in html
checks += 1
print(f"  V{checks}: Global PPC chart canvas in function ✓")

# V7: PPC LB, PPC Mensual, PPC Acum labels
assert "'PPC LB'" in html and "'PPC Mensual'" in html and "'PPC Acum'" in html
checks += 1
print(f"  V{checks}: 3 chart lines (LB/Mensual/Acum) present ✓")

# V8: Per-area charts
for cid in ['dg-chart-areas','dg-chart-bars','dg-chart-restr','dg-chart-acum-area']:
    assert cid in html, f"{cid} missing!"
checks += 1
print(f"  V{checks}: All 5 chart canvases present ✓")

# V9: All original seeds intact
for seed in ['GIS_SEED','METRO_SEED','INMOB_SEED','CONST_SEED','RENTAL_SEED']:
    assert seed in html, f"{seed} missing!"
checks += 1
print(f"  V{checks}: All 5 SEED constants intact ✓")

# V10: All 20 area page divs intact
for area in ['gis','metro','inmob','const','rental']:
    for prefix in ['la','pm','ppc','ar']:
        pid = f'page-{prefix}-{area}'
        assert pid in html, f"Page div {pid} missing!"
checks += 1
print(f"  V{checks}: All 20+1 area page divs intact ✓")

print(f"\n✅ All {checks} verification checks passed!")
