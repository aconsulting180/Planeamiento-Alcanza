"""
Apply all modifications to Planeamiento_2026.html to add Inmobiliaria and Constructora areas.
"""

with open('Planeamiento_2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('seeds_output_v2.js', 'r', encoding='utf-8') as f:
    seeds_js = f.read().strip()

# ═══════════════════════════════════════════════════════════════
# 1. CSS: Add .area-tag.inmob and .area-tag.const + dash-card styles
# ═══════════════════════════════════════════════════════════════
old_css = '.area-tag.gis{background:var(--med-blue);color:white;}.area-tag.metro{background:var(--green);color:white;}'
new_css = '.area-tag.gis{background:var(--med-blue);color:white;}.area-tag.metro{background:var(--green);color:white;}.area-tag.inmob{background:var(--orange);color:white;}.area-tag.const{background:#7B2D8E;color:white;}'
html = html.replace(old_css, new_css)

old_dash_css = '.dash-card.gis{border-left-color:var(--med-blue);}.dash-card.gis .dash-icon{background:var(--pale-blue);color:var(--med-blue);}\n.dash-card.metro{border-left-color:var(--green);}.dash-card.metro .dash-icon{background:var(--light-green);color:var(--green);}'
new_dash_css = """.dash-card.gis{border-left-color:var(--med-blue);}.dash-card.gis .dash-icon{background:var(--pale-blue);color:var(--med-blue);}
.dash-card.metro{border-left-color:var(--green);}.dash-card.metro .dash-icon{background:var(--light-green);color:var(--green);}
.dash-card.inmob{border-left-color:var(--orange);}.dash-card.inmob .dash-icon{background:#FFF3E0;color:var(--orange);}
.dash-card.const{border-left-color:#7B2D8E;}.dash-card.const .dash-icon{background:#F3E5F5;color:#7B2D8E;}"""
html = html.replace(old_dash_css, new_dash_css)

# ═══════════════════════════════════════════════════════════════
# 2. SIDEBAR: Add Inmobiliaria and Constructora nav sections
# ═══════════════════════════════════════════════════════════════
old_sidebar_end = """  <div class="nav-item" onclick="showPage('ar-metro')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="save-status">"""
new_sidebar_end = """  <div class="nav-item" onclick="showPage('ar-metro')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="area-label">Inmobiliaria</div>
  <div class="nav-item" onclick="showPage('la-inmob')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-inmob')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-inmob')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-inmob')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="area-label">Constructora</div>
  <div class="nav-item" onclick="showPage('la-const')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-const')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-const')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-const')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="save-status">"""
html = html.replace(old_sidebar_end, new_sidebar_end)

# ═══════════════════════════════════════════════════════════════
# 3. DASHBOARD: Add new area cards + charts
# ═══════════════════════════════════════════════════════════════
old_charts = """    <div class="charts-grid" style="margin-top:20px">
      <div class="chart-card"><h4>PPC Mensual — GIS</h4><canvas id="dash-chart-ppc-gis"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Metropolitano</h4><canvas id="dash-chart-ppc-metro"></canvas></div>
    </div>
  </div>"""
new_charts = """    <h3 style="margin:16px 0 10px;color:var(--orange)"><i class="ri-home-office-line"></i> Inmobiliaria</h3>
    <div class="dash-grid">
      <div class="dash-card inmob" onclick="showPage('la-inmob')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card inmob" onclick="showPage('pm-inmob')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card inmob" onclick="showPage('ppc-inmob')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card inmob" onclick="showPage('ar-inmob')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>
    <h3 style="margin:16px 0 10px;color:#7B2D8E"><i class="ri-building-2-line"></i> Constructora</h3>
    <div class="dash-grid">
      <div class="dash-card const" onclick="showPage('la-const')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card const" onclick="showPage('pm-const')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card const" onclick="showPage('ppc-const')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card const" onclick="showPage('ar-const')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>
    <div class="charts-grid" style="margin-top:20px">
      <div class="chart-card"><h4>PPC Mensual — GIS</h4><canvas id="dash-chart-ppc-gis"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Metropolitano</h4><canvas id="dash-chart-ppc-metro"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Inmobiliaria</h4><canvas id="dash-chart-ppc-inmob"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Constructora</h4><canvas id="dash-chart-ppc-const"></canvas></div>
    </div>
  </div>"""
html = html.replace(old_charts, new_charts)

# ═══════════════════════════════════════════════════════════════
# 4. PAGE DIVS: Add 8 new page divs
# ═══════════════════════════════════════════════════════════════
old_pages = """  <div class="page" id="page-ar-metro"></div>
</div>"""
new_pages = """  <div class="page" id="page-ar-metro"></div>
  <div class="page" id="page-la-inmob"></div>
  <div class="page" id="page-pm-inmob"></div>
  <div class="page" id="page-ppc-inmob"></div>
  <div class="page" id="page-ar-inmob"></div>
  <div class="page" id="page-la-const"></div>
  <div class="page" id="page-pm-const"></div>
  <div class="page" id="page-ppc-const"></div>
  <div class="page" id="page-ar-const"></div>
</div>"""
html = html.replace(old_pages, new_pages)

# ═══════════════════════════════════════════════════════════════
# 5. SEEDS: Insert INMOB_SEED and CONST_SEED after METRO_SEED
# ═══════════════════════════════════════════════════════════════
# Find the position right after METRO_SEED's closing ];
metro_end_marker = """// ══════════════════════════════════════════════════════════════════
// STATE
// ══════════════════════════════════════════════════════════════════"""
# Insert seeds before STATE section
html = html.replace(metro_end_marker, seeds_js + "\n\n" + metro_end_marker)

# ═══════════════════════════════════════════════════════════════
# 6. STATE: Update defaultState + localStorage key
# ═══════════════════════════════════════════════════════════════
html = html.replace("const SK='lps2026v3';", "const SK='lps2026v4';")

old_state = """  return {
    la:{gis:buildArea(GIS_SEED),metro:buildArea(METRO_SEED)},
    pm:{gis:{},metro:{}}, // pm[key][ogIdx-oeIdx-actIdx][month] = {status,avance}
    ppc:{gis:{},metro:{}}, // ppc[key][id][month] = {compr,ejec}
    ar:{gis:[],metro:[]},
  };"""
new_state = """  return {
    la:{gis:buildArea(GIS_SEED),metro:buildArea(METRO_SEED),inmob:buildArea(INMOB_SEED),const:buildArea(CONST_SEED)},
    pm:{gis:{},metro:{},inmob:{},const:{}},
    ppc:{gis:{},metro:{},inmob:{},const:{}},
    ar:{gis:[],metro:[],inmob:[],const:[]},
  };"""
html = html.replace(old_state, new_state)

# ═══════════════════════════════════════════════════════════════
# 7. showPage: Update map
# ═══════════════════════════════════════════════════════════════
old_showpage = "  const map=['dashboard','la-gis','pm-gis','ppc-gis','ar-gis','la-metro','pm-metro','ppc-metro','ar-metro'];"
new_showpage = "  const map=['dashboard','la-gis','pm-gis','ppc-gis','ar-gis','la-metro','pm-metro','ppc-metro','ar-metro','la-inmob','pm-inmob','ppc-inmob','ar-inmob','la-const','pm-const','ppc-const','ar-const'];"
html = html.replace(old_showpage, new_showpage)

# ═══════════════════════════════════════════════════════════════
# 8. Render functions: Update area tag/class mapping in LA, PM, PPC, AR
# ═══════════════════════════════════════════════════════════════
# renderLA
old_la_tag = """  const areaTag=key==='gis'?'GIS (POSTVENTA)':'METROPOLITANO (DISEÑO)';
  const ac=key==='gis'?'gis':'metro';
  const el=document.getElementById('page-la-'+key);"""
new_la_tag = """  const areaNames={gis:'GIS (POSTVENTA)',metro:'METROPOLITANO (DISEÑO)',inmob:'INMOBILIARIA',const:'CONSTRUCTORA'};
  const areaTag=areaNames[key]||key.toUpperCase();
  const ac=key;
  const el=document.getElementById('page-la-'+key);"""
html = html.replace(old_la_tag, new_la_tag)

# renderPM
old_pm_tag = """  const ac=key==='gis'?'gis':'metro';
  const areaTag=key==='gis'?'GIS (POSTVENTA)':'METROPOLITANO (DISEÑO)';
  const el=document.getElementById('page-pm-'+key);"""
new_pm_tag = """  const areaNames={gis:'GIS (POSTVENTA)',metro:'METROPOLITANO (DISEÑO)',inmob:'INMOBILIARIA',const:'CONSTRUCTORA'};
  const ac=key;
  const areaTag=areaNames[key]||key.toUpperCase();
  const el=document.getElementById('page-pm-'+key);"""
html = html.replace(old_pm_tag, new_pm_tag)

# renderPPC
old_ppc_tag = """  const ac=key==='gis'?'gis':'metro';
  const areaTag=key==='gis'?'GIS (POSTVENTA)':'METROPOLITANO (DISEÑO)';
  const el=document.getElementById('page-ppc-'+key);"""
new_ppc_tag = """  const areaNames={gis:'GIS (POSTVENTA)',metro:'METROPOLITANO (DISEÑO)',inmob:'INMOBILIARIA',const:'CONSTRUCTORA'};
  const ac=key;
  const areaTag=areaNames[key]||key.toUpperCase();
  const el=document.getElementById('page-ppc-'+key);"""
html = html.replace(old_ppc_tag, new_ppc_tag)

# renderAR
old_ar_tag = """  const ac=key==='gis'?'gis':'metro';
  const areaTag=key==='gis'?'GIS (POSTVENTA)':'METROPOLITANO (DISEÑO)';
  const el=document.getElementById('page-ar-'+key);"""
new_ar_tag = """  const areaNames={gis:'GIS (POSTVENTA)',metro:'METROPOLITANO (DISEÑO)',inmob:'INMOBILIARIA',const:'CONSTRUCTORA'};
  const ac=key;
  const areaTag=areaNames[key]||key.toUpperCase();
  const el=document.getElementById('page-ar-'+key);"""
html = html.replace(old_ar_tag, new_ar_tag)

# ═══════════════════════════════════════════════════════════════
# 9. DASHBOARD: Update updateDash() for 4 areas
# ═══════════════════════════════════════════════════════════════
old_dash = """let _dC={};
function updateDash(){
  const g=calcPPCData('gis'),m=calcPPCData('metro');
  const arG=(S.ar.gis||[]).filter(r=>r.estado!=='Levantada').length;
  const arM=(S.ar.metro||[]).filter(r=>r.estado!=='Levantada').length;
  const el=document.getElementById('dash-stats');
  if(el)el.innerHTML=`
    <div class="stat-card" style="border-left:4px solid var(--med-blue)"><div class="stat-value" style="color:${g.global>=80?'var(--green)':'var(--red)'}">${g.global}%</div><div class="stat-label">PPC GIS</div></div>
    <div class="stat-card" style="border-left:4px solid var(--green)"><div class="stat-value" style="color:${m.global>=80?'var(--green)':'var(--red)'}">${m.global}%</div><div class="stat-label">PPC Metropolitano</div></div>
    <div class="stat-card" style="border-left:4px solid var(--orange)"><div class="stat-value" style="color:var(--orange)">${arG}</div><div class="stat-label">Restricciones GIS</div></div>
    <div class="stat-card" style="border-left:4px solid var(--red)"><div class="stat-value" style="color:var(--red)">${arM}</div><div class="stat-label">Restricciones Metro</div></div>`;
  ['gis','metro'].forEach(k=>{
    const {monthly}=calcPPCData(k);
    if(_dC[k])_dC[k].destroy();
    const c=document.getElementById(`dash-chart-ppc-${k}`);
    if(c)_dC[k]=new Chart(c,{type:'line',data:{labels:MONTHS.slice(1),datasets:[
      {label:'PPC %',data:monthly.map(x=>x.ppc),borderColor:'#1B2A4A',backgroundColor:'rgba(68,114,196,0.1)',borderWidth:3,fill:true,tension:0.3,pointRadius:5,pointBackgroundColor:'#4472C4'},
      {label:'Meta 80%',data:Array(12).fill(80),borderColor:'#C00000',borderWidth:2,borderDash:[6,3],pointRadius:0,fill:false},
    ]},options:{responsive:true,scales:{y:{min:0,max:100,ticks:{callback:v=>v+'%'}}},plugins:{legend:{position:'bottom'}}}});
  });
}"""

new_dash = """let _dC={};
function updateDash(){
  const areas=[
    {key:'gis',label:'PPC GIS',color:'var(--med-blue)'},
    {key:'metro',label:'PPC Metropolitano',color:'var(--green)'},
    {key:'inmob',label:'PPC Inmobiliaria',color:'var(--orange)'},
    {key:'const',label:'PPC Constructora',color:'#7B2D8E'},
  ];
  const el=document.getElementById('dash-stats');
  if(el){
    let sh='';
    areas.forEach(a=>{
      const d=calcPPCData(a.key);
      const ar=(S.ar[a.key]||[]).filter(r=>r.estado!=='Levantada').length;
      sh+=`<div class="stat-card" style="border-left:4px solid ${a.color}"><div class="stat-value" style="color:${d.global>=80?'var(--green)':'var(--red)'}">${d.global}%</div><div class="stat-label">${a.label}</div></div>`;
    });
    // Restricciones summary
    areas.forEach(a=>{
      const ar=(S.ar[a.key]||[]).filter(r=>r.estado!=='Levantada').length;
      sh+=`<div class="stat-card" style="border-left:4px solid ${a.color}"><div class="stat-value" style="color:${a.color}">${ar}</div><div class="stat-label">Restr. ${a.key.toUpperCase()}</div></div>`;
    });
    el.innerHTML=sh;
  }
  ['gis','metro','inmob','const'].forEach(k=>{
    const {monthly}=calcPPCData(k);
    if(_dC[k])_dC[k].destroy();
    const c=document.getElementById(`dash-chart-ppc-${k}`);
    if(c)_dC[k]=new Chart(c,{type:'line',data:{labels:MONTHS.slice(1),datasets:[
      {label:'PPC %',data:monthly.map(x=>x.ppc),borderColor:'#1B2A4A',backgroundColor:'rgba(68,114,196,0.1)',borderWidth:3,fill:true,tension:0.3,pointRadius:5,pointBackgroundColor:'#4472C4'},
      {label:'Meta 80%',data:Array(12).fill(80),borderColor:'#C00000',borderWidth:2,borderDash:[6,3],pointRadius:0,fill:false},
    ]},options:{responsive:true,scales:{y:{min:0,max:100,ticks:{callback:v=>v+'%'}}},plugins:{legend:{position:'bottom'}}}});
  });
}"""
html = html.replace(old_dash, new_dash)

# ═══════════════════════════════════════════════════════════════
# 10. EXPORT: Update exportAll() for 4 areas
# ═══════════════════════════════════════════════════════════════
old_export = "  ['gis','metro'].forEach(key=>{\n    const label=key==='gis'?'GIS':'METRO';"
new_export = "  ['gis','metro','inmob','const'].forEach(key=>{\n    const label={gis:'GIS',metro:'METRO',inmob:'INMOB',const:'CONST'}[key]||key.toUpperCase();"
html = html.replace(old_export, new_export)

# ═══════════════════════════════════════════════════════════════
# Write result
# ═══════════════════════════════════════════════════════════════
with open('Planeamiento_2026.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ All modifications applied successfully!")
print(f"  File size: {len(html)} chars")

# Verify all changes took effect
checks = [
    ('.area-tag.inmob{', 'CSS inmob class'),
    ('.area-tag.const{', 'CSS const class'),
    ('.dash-card.inmob{', 'CSS dash-card inmob'),
    ('.dash-card.const{', 'CSS dash-card const'),
    ("showPage('la-inmob')", 'Sidebar inmob'),
    ("showPage('la-const')", 'Sidebar const'),
    ('page-la-inmob', 'Page div inmob'),
    ('page-la-const', 'Page div const'),
    ('INMOB_SEED', 'Inmob seed'),
    ('CONST_SEED', 'Const seed'),
    ('lps2026v4', 'localStorage key v4'),
    ('inmob:buildArea(INMOB_SEED)', 'State inmob'),
    ('const:buildArea(CONST_SEED)', 'State const'),
    ("'la-inmob','pm-inmob'", 'showPage map inmob'),
    ("'la-const','pm-const'", 'showPage map const'),
    ("inmob:'INMOBILIARIA'", 'renderLA area name'),
    ("const:'CONSTRUCTORA'", 'renderLA area name'),
    ("'gis','metro','inmob','const'", 'exportAll 4 areas'),
    ('dash-chart-ppc-inmob', 'Dashboard chart inmob'),
    ('dash-chart-ppc-const', 'Dashboard chart const'),
]

all_ok = True
for needle, desc in checks:
    if needle in html:
        print(f"  ✓ {desc}")
    else:
        print(f"  ✗ MISSING: {desc}")
        all_ok = False

if all_ok:
    print("\n✅ ALL checks passed!")
else:
    print("\n⚠️ Some checks failed!")
