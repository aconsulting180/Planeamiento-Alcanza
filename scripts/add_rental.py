"""
Add CEQ Rental area to Planeamiento_2026.html
Data: 1 OG, 2 OEs, 8 activities from rental Excel
"""

with open('Planeamiento_2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ═══════════════════════════════════════════════════════════════
# RENTAL_SEED JavaScript
# ═══════════════════════════════════════════════════════════════
RENTAL_SEED_JS = """
// === CEQ RENTAL ===
const RENTAL_SEED = [
 {og:"OG-01",og_desc:"Implementar el sistema de gestión de activos",oes:[
  {oe:"OE-01.1",oe_desc:"Sistema de trabajo",kpi:"Sistema de gestión implementado",acts:[
   {cod:"A01",act:"Implementar procesos de evaluación de compra/alquiler de activos",ent:"Procedimiento de trabajo.",resp:"Procesos",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Implementar procesos de gestión de activos.",ent:"Procedimiento de trabajo.",resp:"Procesos",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar control de activos.",ent:"Inventario de activos.",resp:"GG Shark Tank",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Consolidar activos de empresas del grupo en CEQ Rental",ent:"Compra-venta de activos.",resp:"GG Shark Tank",weeks:WEEKS.filter(w=>[3,4].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-01.2",oe_desc:"Invertir en activos",kpi:"Inversión en nuevos activos 500K",acts:[
   {cod:"A01",act:"Comprar andamios colgantes eléctricos",ent:"Activo comprado y alquilado",resp:"GG Shark Tank",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Explorar oportunidades de inversión (demanda interna)",ent:"Informes de evaluación",resp:"CFO",weeks:WEEKS.filter(w=>[4,5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Explorar oportunidades de inversión (demanda externa)",ent:"Informes de evaluación",resp:"CFO",weeks:WEEKS.filter(w=>[5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Ejecutar compras de activos x oportunidades identificadas",ent:"Activo comprado y alquilado",resp:"GG Shark Tank",weeks:WEEKS.filter(w=>[5,6,7,8,9,10].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
];

// Total activities for CEQ Rental: 8
"""

# ═══════════════════════════════════════════════════════════════
# 1. CSS: Add .area-tag.rental and .dash-card.rental
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    ".area-tag.const{background:#7B2D8E;color:white;}",
    ".area-tag.const{background:#7B2D8E;color:white;}.area-tag.rental{background:#00897B;color:white;}"
)

html = html.replace(
    ".dash-card.const{border-left-color:#7B2D8E;}.dash-card.const .dash-icon{background:#F3E5F5;color:#7B2D8E;}",
    ".dash-card.const{border-left-color:#7B2D8E;}.dash-card.const .dash-icon{background:#F3E5F5;color:#7B2D8E;}\n.dash-card.rental{border-left-color:#00897B;}.dash-card.rental .dash-icon{background:#E0F2F1;color:#00897B;}"
)

# ═══════════════════════════════════════════════════════════════
# 2. SIDEBAR: Add CEQ Rental nav section after Constructora
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    """  <div class="nav-item" onclick="showPage('ar-const')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="save-status">""",
    """  <div class="nav-item" onclick="showPage('ar-const')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="area-label">CEQ Rental</div>
  <div class="nav-item" onclick="showPage('la-rental')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-rental')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-rental')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-rental')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="save-status">"""
)

# ═══════════════════════════════════════════════════════════════
# 3. DASHBOARD: Add CEQ Rental cards before charts grid
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    """    <div class="charts-grid" style="margin-top:20px">
      <div class="chart-card"><h4>PPC Mensual — GIS</h4><canvas id="dash-chart-ppc-gis"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Metropolitano</h4><canvas id="dash-chart-ppc-metro"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Inmobiliaria</h4><canvas id="dash-chart-ppc-inmob"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Constructora</h4><canvas id="dash-chart-ppc-const"></canvas></div>
    </div>""",
    """    <h3 style="margin:16px 0 10px;color:#00897B"><i class="ri-tools-line"></i> CEQ Rental</h3>
    <div class="dash-grid">
      <div class="dash-card rental" onclick="showPage('la-rental')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card rental" onclick="showPage('pm-rental')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card rental" onclick="showPage('ppc-rental')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card rental" onclick="showPage('ar-rental')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>
    <div class="charts-grid" style="margin-top:20px">
      <div class="chart-card"><h4>PPC Mensual — GIS</h4><canvas id="dash-chart-ppc-gis"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Metropolitano</h4><canvas id="dash-chart-ppc-metro"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Inmobiliaria</h4><canvas id="dash-chart-ppc-inmob"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Constructora</h4><canvas id="dash-chart-ppc-const"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — CEQ Rental</h4><canvas id="dash-chart-ppc-rental"></canvas></div>
    </div>"""
)

# ═══════════════════════════════════════════════════════════════
# 4. PAGE DIVS: Add 4 new page divs for rental
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    '  <div class="page" id="page-ar-const"></div>\n</div>',
    '  <div class="page" id="page-ar-const"></div>\n  <div class="page" id="page-la-rental"></div>\n  <div class="page" id="page-pm-rental"></div>\n  <div class="page" id="page-ppc-rental"></div>\n  <div class="page" id="page-ar-rental"></div>\n</div>'
)

# ═══════════════════════════════════════════════════════════════
# 5. SEED: Insert RENTAL_SEED after CONST_SEED
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    "// Total activities for Constructoras: 24\n\n// ══",
    "// Total activities for Constructoras: 24\n" + RENTAL_SEED_JS + "\n// ══"
)

# ═══════════════════════════════════════════════════════════════
# 6. STATE: Add rental to defaultState + bump storage key
# ═══════════════════════════════════════════════════════════════
html = html.replace("const SK='lps2026v4';", "const SK='lps2026v5';")

html = html.replace(
    "la:{gis:buildArea(GIS_SEED),metro:buildArea(METRO_SEED),inmob:buildArea(INMOB_SEED),const:buildArea(CONST_SEED)},",
    "la:{gis:buildArea(GIS_SEED),metro:buildArea(METRO_SEED),inmob:buildArea(INMOB_SEED),const:buildArea(CONST_SEED),rental:buildArea(RENTAL_SEED)},"
)
html = html.replace(
    "pm:{gis:{},metro:{},inmob:{},const:{}},",
    "pm:{gis:{},metro:{},inmob:{},const:{},rental:{}},"
)
html = html.replace(
    "ppc:{gis:{},metro:{},inmob:{},const:{}},",
    "ppc:{gis:{},metro:{},inmob:{},const:{},rental:{}},"
)
html = html.replace(
    "ar:{gis:[],metro:[],inmob:[],const:[]},",
    "ar:{gis:[],metro:[],inmob:[],const:[],rental:[]},"
)

# ═══════════════════════════════════════════════════════════════
# 7. showPage: Add rental to map
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    "'la-const','pm-const','ppc-const','ar-const']",
    "'la-const','pm-const','ppc-const','ar-const','la-rental','pm-rental','ppc-rental','ar-rental']"
)

# ═══════════════════════════════════════════════════════════════
# 8. Render functions: Add rental to areaNames dict (all 4 renderers)
# ═══════════════════════════════════════════════════════════════
# We need to add rental to all areaNames dicts
old_area_names = "const areaNames={gis:'GIS (POSTVENTA)',metro:'METROPOLITANO (DISEÑO)',inmob:'INMOBILIARIA',const:'CONSTRUCTORA'};"
new_area_names = "const areaNames={gis:'GIS (POSTVENTA)',metro:'METROPOLITANO (DISEÑO)',inmob:'INMOBILIARIA',const:'CONSTRUCTORA',rental:'CEQ RENTAL'};"
# This appears 4 times (renderLA, renderPM, renderPPC, renderAR)
html = html.replace(old_area_names, new_area_names)

# ═══════════════════════════════════════════════════════════════
# 9. Dashboard: Add rental to updateDash areas array
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    """{key:'const',label:'PPC Constructora',color:'#7B2D8E'},
  ];""",
    """{key:'const',label:'PPC Constructora',color:'#7B2D8E'},
    {key:'rental',label:'PPC CEQ Rental',color:'#00897B'},
  ];"""
)

html = html.replace(
    "['gis','metro','inmob','const'].forEach(k=>{\n    const {monthly}=calcPPCData(k);",
    "['gis','metro','inmob','const','rental'].forEach(k=>{\n    const {monthly}=calcPPCData(k);"
)

# ═══════════════════════════════════════════════════════════════
# 10. EXPORT: Add rental to exportAll
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    "['gis','metro','inmob','const'].forEach(key=>{\n    const label={gis:'GIS',metro:'METRO',inmob:'INMOB',const:'CONST'}[key]||key.toUpperCase();",
    "['gis','metro','inmob','const','rental'].forEach(key=>{\n    const label={gis:'GIS',metro:'METRO',inmob:'INMOB',const:'CONST',rental:'RENTAL'}[key]||key.toUpperCase();"
)

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
with open('Planeamiento_2026.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ CEQ Rental area added! File size: {len(html)} chars")

# Verify
checks = [
    ('.area-tag.rental{', 'CSS rental tag'),
    ('.dash-card.rental{', 'CSS dash-card rental'),
    ("showPage('la-rental')", 'Sidebar rental'),
    ('page-la-rental', 'Page div rental'),
    ('RENTAL_SEED', 'Rental seed'),
    ('lps2026v5', 'Storage key v5'),
    ('rental:buildArea(RENTAL_SEED)', 'State la rental'),
    ("'la-rental','pm-rental'", 'showPage map rental'),
    ("rental:'CEQ RENTAL'", 'areaNames rental'),
    ("key:'rental'", 'Dashboard rental stat'),
    ('dash-chart-ppc-rental', 'Dashboard chart rental'),
    ("'rental'].forEach(key=>", 'exportAll rental'),
]

all_ok = True
for needle, desc in checks:
    if needle in html:
        print(f"  ✓ {desc}")
    else:
        print(f"  ✗ MISSING: {desc}")
        all_ok = False

print("\n✅ ALL checks passed!" if all_ok else "\n⚠️ Some checks failed!")
