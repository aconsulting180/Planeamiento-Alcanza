"""
Reorder areas in Planeamiento_2026.html
FROM:  GIS → Metro → Inmob → Const → Rental
TO:    Inmob → Const → GIS → Metro → Rental
"""
import re

FILE = 'Planeamiento_2026.html'

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

original = html  # backup for comparison

# ============================================================
# 1) SIDEBAR: reorder area blocks (area-label + 4 nav-items)
# ============================================================
sidebar_old = """\
  <div class="area-label">GIS — Postventa</div>
  <div class="nav-item" onclick="showPage('la-gis')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-gis')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-gis')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-gis')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="area-label">Metropolitano — Diseño</div>
  <div class="nav-item" onclick="showPage('la-metro')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-metro')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-metro')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-metro')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
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
  <div class="area-label">CEQ Rental</div>
  <div class="nav-item" onclick="showPage('la-rental')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-rental')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-rental')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-rental')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>"""

sidebar_new = """\
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
  <div class="area-label">GIS — Postventa</div>
  <div class="nav-item" onclick="showPage('la-gis')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-gis')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-gis')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-gis')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="area-label">Metropolitano — Diseño</div>
  <div class="nav-item" onclick="showPage('la-metro')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-metro')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-metro')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-metro')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>
  <div class="area-label">CEQ Rental</div>
  <div class="nav-item" onclick="showPage('la-rental')"><span class="icon"><i class="ri-calendar-schedule-line"></i></span><span>Lookahead</span></div>
  <div class="nav-item" onclick="showPage('pm-rental')"><span class="icon"><i class="ri-task-line"></i></span><span>Plan Mensual</span></div>
  <div class="nav-item" onclick="showPage('ppc-rental')"><span class="icon"><i class="ri-line-chart-line"></i></span><span>PPC</span></div>
  <div class="nav-item" onclick="showPage('ar-rental')"><span class="icon"><i class="ri-alarm-warning-line"></i></span><span>Restricciones</span></div>"""

assert sidebar_old in html, "ERROR: sidebar old block not found"
html = html.replace(sidebar_old, sidebar_new)
print("[1/7] Sidebar reordered ✓")

# ============================================================
# 2) DASHBOARD CARDS: reorder h3 + dash-grid blocks
# ============================================================
dash_old = """\
    <h3 style="margin:16px 0 10px;color:var(--med-blue)"><i class="ri-building-4-line"></i> GIS — Postventa</h3>
    <div class="dash-grid">
      <div class="dash-card gis" onclick="showPage('la-gis')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card gis" onclick="showPage('pm-gis')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card gis" onclick="showPage('ppc-gis')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card gis" onclick="showPage('ar-gis')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>
    <h3 style="margin:16px 0 10px;color:var(--green)"><i class="ri-train-line"></i> Metropolitano — Diseño</h3>
    <div class="dash-grid">
      <div class="dash-card metro" onclick="showPage('la-metro')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card metro" onclick="showPage('pm-metro')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card metro" onclick="showPage('ppc-metro')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card metro" onclick="showPage('ar-metro')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>
    <h3 style="margin:16px 0 10px;color:var(--orange)"><i class="ri-home-office-line"></i> Inmobiliaria</h3>
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
    <h3 style="margin:16px 0 10px;color:#00897B"><i class="ri-tools-line"></i> CEQ Rental</h3>
    <div class="dash-grid">
      <div class="dash-card rental" onclick="showPage('la-rental')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card rental" onclick="showPage('pm-rental')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card rental" onclick="showPage('ppc-rental')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card rental" onclick="showPage('ar-rental')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>"""

dash_new = """\
    <h3 style="margin:16px 0 10px;color:var(--orange)"><i class="ri-home-office-line"></i> Inmobiliaria</h3>
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
    <h3 style="margin:16px 0 10px;color:var(--med-blue)"><i class="ri-building-4-line"></i> GIS — Postventa</h3>
    <div class="dash-grid">
      <div class="dash-card gis" onclick="showPage('la-gis')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card gis" onclick="showPage('pm-gis')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card gis" onclick="showPage('ppc-gis')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card gis" onclick="showPage('ar-gis')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>
    <h3 style="margin:16px 0 10px;color:var(--green)"><i class="ri-train-line"></i> Metropolitano — Diseño</h3>
    <div class="dash-grid">
      <div class="dash-card metro" onclick="showPage('la-metro')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card metro" onclick="showPage('pm-metro')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card metro" onclick="showPage('ppc-metro')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card metro" onclick="showPage('ar-metro')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>
    <h3 style="margin:16px 0 10px;color:#00897B"><i class="ri-tools-line"></i> CEQ Rental</h3>
    <div class="dash-grid">
      <div class="dash-card rental" onclick="showPage('la-rental')"><div class="dash-icon"><i class="ri-calendar-schedule-line"></i></div><h3>Lookahead Anual</h3><p>Cronograma semanal editable</p></div>
      <div class="dash-card rental" onclick="showPage('pm-rental')"><div class="dash-icon"><i class="ri-task-line"></i></div><h3>Plan Mensual</h3><p>Estado y avance por actividad</p></div>
      <div class="dash-card rental" onclick="showPage('ppc-rental')"><div class="dash-icon"><i class="ri-line-chart-line"></i></div><h3>PPC</h3><p>Porcentaje de Plan Cumplido</p></div>
      <div class="dash-card rental" onclick="showPage('ar-rental')"><div class="dash-icon"><i class="ri-alarm-warning-line"></i></div><h3>Restricciones</h3><p>Registro de restricciones</p></div>
    </div>"""

assert dash_old in html, "ERROR: dashboard cards old block not found"
html = html.replace(dash_old, dash_new)
print("[2/7] Dashboard cards reordered ✓")

# ============================================================
# 3) DASHBOARD CHARTS: reorder chart-card blocks
# ============================================================
charts_old = """\
      <div class="chart-card"><h4>PPC Mensual — GIS</h4><canvas id="dash-chart-ppc-gis"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Metropolitano</h4><canvas id="dash-chart-ppc-metro"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Inmobiliaria</h4><canvas id="dash-chart-ppc-inmob"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Constructora</h4><canvas id="dash-chart-ppc-const"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — CEQ Rental</h4><canvas id="dash-chart-ppc-rental"></canvas></div>"""

charts_new = """\
      <div class="chart-card"><h4>PPC Mensual — Inmobiliaria</h4><canvas id="dash-chart-ppc-inmob"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Constructora</h4><canvas id="dash-chart-ppc-const"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — GIS</h4><canvas id="dash-chart-ppc-gis"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — Metropolitano</h4><canvas id="dash-chart-ppc-metro"></canvas></div>
      <div class="chart-card"><h4>PPC Mensual — CEQ Rental</h4><canvas id="dash-chart-ppc-rental"></canvas></div>"""

assert charts_old in html, "ERROR: charts old block not found"
html = html.replace(charts_old, charts_new)
print("[3/7] Dashboard charts reordered ✓")

# ============================================================
# 4) showPage map array
# ============================================================
map_old = "const map=['dashboard','la-gis','pm-gis','ppc-gis','ar-gis','la-metro','pm-metro','ppc-metro','ar-metro','la-inmob','pm-inmob','ppc-inmob','ar-inmob','la-const','pm-const','ppc-const','ar-const','la-rental','pm-rental','ppc-rental','ar-rental'];"
map_new = "const map=['dashboard','la-inmob','pm-inmob','ppc-inmob','ar-inmob','la-const','pm-const','ppc-const','ar-const','la-gis','pm-gis','ppc-gis','ar-gis','la-metro','pm-metro','ppc-metro','ar-metro','la-rental','pm-rental','ppc-rental','ar-rental'];"

assert map_old in html, "ERROR: showPage map old not found"
html = html.replace(map_old, map_new)
print("[4/7] showPage map reordered ✓")

# ============================================================
# 5) updateDash areas array
# ============================================================
udash_old = """\
    {key:'gis',label:'PPC GIS',color:'var(--med-blue)'},
    {key:'metro',label:'PPC Metropolitano',color:'var(--green)'},
    {key:'inmob',label:'PPC Inmobiliaria',color:'var(--orange)'},
    {key:'const',label:'PPC Constructora',color:'#7B2D8E'},
    {key:'rental',label:'PPC CEQ Rental',color:'#00897B'},"""

udash_new = """\
    {key:'inmob',label:'PPC Inmobiliaria',color:'var(--orange)'},
    {key:'const',label:'PPC Constructora',color:'#7B2D8E'},
    {key:'gis',label:'PPC GIS',color:'var(--med-blue)'},
    {key:'metro',label:'PPC Metropolitano',color:'var(--green)'},
    {key:'rental',label:'PPC CEQ Rental',color:'#00897B'},"""

assert udash_old in html, "ERROR: updateDash areas old not found"
html = html.replace(udash_old, udash_new)
print("[5/7] updateDash areas reordered ✓")

# ============================================================
# 6) Dashboard chart forEach loop
# ============================================================
dchart_old = "  ['gis','metro','inmob','const','rental'].forEach(k=>{"
dchart_new = "  ['inmob','const','gis','metro','rental'].forEach(k=>{"

assert html.count(dchart_old) == 1, f"ERROR: dashboard chart forEach found {html.count(dchart_old)} times, expected 1"
html = html.replace(dchart_old, dchart_new)
print("[6/7] Dashboard chart forEach reordered ✓")

# ============================================================
# 7) exportAll forEach loop
# ============================================================
exp_old = "  ['gis','metro','inmob','const','rental'].forEach(key=>{"
exp_new = "  ['inmob','const','gis','metro','rental'].forEach(key=>{"

assert html.count(exp_old) == 1, f"ERROR: exportAll forEach found {html.count(exp_old)} times, expected 1"
html = html.replace(exp_old, exp_new)
print("[7/7] exportAll forEach reordered ✓")

# ============================================================
# WRITE
# ============================================================
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ All 7 reorder operations completed successfully!")
print(f"   File size: {len(html):,} chars")

# ============================================================
# VERIFICATION
# ============================================================
print("\n=== VERIFICATION ===")
checks = 0

# V1: Sidebar order
idx_inmob_sb = html.index('area-label">Inmobiliaria')
idx_const_sb = html.index('area-label">Constructora')
idx_gis_sb = html.index('area-label">GIS')
idx_metro_sb = html.index('area-label">Metropolitano')
idx_rental_sb = html.index('area-label">CEQ Rental')
assert idx_inmob_sb < idx_const_sb < idx_gis_sb < idx_metro_sb < idx_rental_sb, "Sidebar order wrong!"
checks += 1
print(f"  V{checks}: Sidebar order Inmob < Const < GIS < Metro < Rental ✓")

# V2: Dashboard cards order
idx_inmob_dc = html.index('dash-card inmob')
idx_const_dc = html.index('dash-card const')
idx_gis_dc = html.index('dash-card gis')
idx_metro_dc = html.index('dash-card metro')
idx_rental_dc = html.index('dash-card rental')
assert idx_inmob_dc < idx_const_dc < idx_gis_dc < idx_metro_dc < idx_rental_dc, "Dashboard cards order wrong!"
checks += 1
print(f"  V{checks}: Dashboard cards order ✓")

# V3: Dashboard charts order
idx_inmob_ch = html.index('dash-chart-ppc-inmob')
idx_const_ch = html.index('dash-chart-ppc-const')
idx_gis_ch = html.index('dash-chart-ppc-gis')
idx_metro_ch = html.index('dash-chart-ppc-metro')
idx_rental_ch = html.index('dash-chart-ppc-rental')
assert idx_inmob_ch < idx_const_ch < idx_gis_ch < idx_metro_ch < idx_rental_ch, "Dashboard charts order wrong!"
checks += 1
print(f"  V{checks}: Dashboard charts order ✓")

# V4: showPage map
assert "['dashboard','la-inmob','pm-inmob','ppc-inmob','ar-inmob','la-const','pm-const','ppc-const','ar-const','la-gis','pm-gis','ppc-gis','ar-gis','la-metro','pm-metro','ppc-metro','ar-metro','la-rental'" in html
checks += 1
print(f"  V{checks}: showPage map correct ✓")

# V5: updateDash
assert "key:'inmob'" in html and html.index("key:'inmob'") < html.index("key:'const'") < html.index("key:'gis'")
checks += 1
print(f"  V{checks}: updateDash areas order ✓")

# V6: dashboard chart forEach
assert "['inmob','const','gis','metro','rental'].forEach(k=>" in html
checks += 1
print(f"  V{checks}: Dashboard chart forEach order ✓")

# V7: exportAll forEach
assert "['inmob','const','gis','metro','rental'].forEach(key=>" in html
checks += 1
print(f"  V{checks}: exportAll forEach order ✓")

# V8: No old order remnants in key arrays
old_order = "['gis','metro','inmob','const','rental']"
assert old_order not in html, "Old order array still present!"
checks += 1
print(f"  V{checks}: No old-order arrays remaining ✓")

# V9: File not corrupted - still has all 5 seeds
for seed in ['GIS_SEED','METRO_SEED','INMOB_SEED','CONST_SEED','RENTAL_SEED']:
    assert seed in html, f"{seed} missing!"
checks += 1
print(f"  V{checks}: All 5 SEED constants present ✓")

# V10: All 20 page divs still present
for area in ['gis','metro','inmob','const','rental']:
    for prefix in ['la','pm','ppc','ar']:
        pid = f'page-{prefix}-{area}'
        assert pid in html, f"Page div {pid} missing!"
checks += 1
print(f"  V{checks}: All 20 page divs present ✓")

print(f"\n✅ All {checks} verification checks passed!")
