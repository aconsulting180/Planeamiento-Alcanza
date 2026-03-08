
// === INMOBILIARIAS ===
const INMOB_SEED = [
 {og:"OG-01",og_desc:"Garantizar la liquidez del grupo (Holding y Sucursales)",oes:[
  {oe:"OE-01.1",oe_desc:"Implementar el Plan de trabajo financiero por Hitos de proyectos",kpi:"Resultado positivo en Flujo de Caja",acts:[
   {cod:"A01",act:"Asegurar la proyección de resultados del FC sostenible en el tiempo",ent:"Flujo de Caja",resp:"CFO",weeks:WEEKS.filter(w=>[1,2].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer un plan de trabajo por áreas (& gestión de riesgos).",ent:"Plan de trabajo",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Difundir a los involucrados",ent:"Acta de entrega",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Seguimiento Ingresos",ent:"Reporte de seguimiento semanal",resp:"Finanzas",weeks:WEEKS.filter(w=>[3,4,5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Seguimiento Egresos",ent:"Reporte de seguimiento semanal",resp:"Finanzas",weeks:WEEKS.filter(w=>[3,4,5,6].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-01.2",oe_desc:"Asegurar la precisión del flujo de caja con horizonte 3 meses: Precisión >= 90%",kpi:"Precisión de FC >= 90%",acts:[
   {cod:"A01",act:"Medir el porcentaje de precisión actual",ent:"Mov. Real vs  Mov. Proyectado x 100",resp:"Finanzas",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Buscar e implementar mecanismos para incrementar la precisión en las proyecciones de ingresos y egresos.",ent:"Mejoras varias en el flujo.",resp:"Finanzas",weeks:WEEKS.filter(w=>[3,4,5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Migrar el reporte de Flujo de Caja a un Software versatil (no Excel)",ent:"Software",resp:"Finanzas",weeks:WEEKS.filter(w=>[6,7,8,9,10].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Medir el porcentaje de precisión optimizado",ent:"Mov. Real vs  Mov. Proyectado x 100",resp:"Finanzas",weeks:WEEKS.filter(w=>[6,7,8,9,10,11].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-02",og_desc:"Estrategia de crecimiento 2027 - 2028 (backlog)",oes:[
  {oe:"OE-02.1",oe_desc:"Asegurar la liquidez del grupo + nuevos proyectos",kpi:"Liquidez positiva",acts:[
   {cod:"A01",act:"Realizar análisis de flujos de caja típicos de proyectos de acuerdo con su tamaño.",ent:"Informe de Análisis Financiero",resp:"CFO",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer Nro. De proyectos \"pequeños\" vs cada proyecto grande.",ent:"Informe de Análisis Financiero & recomendación",resp:"CFO",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Difusión a los involucrados (brokers, gerencias, etc).",ent:"Actas de reuniones",resp:"Directorio",weeks:WEEKS.filter(w=>[8].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-02.2",oe_desc:"Mínimo un (01) proyecto fuera de Santa Catalina",kpi:"01 proyecto importante fuera de Sta Catalina",acts:[
   {cod:"A01",act:"Enfocar búsqueda de terrenos/casas fuera de Santa Catalina",ent:"Coordinación con brokers",resp:"Directorio",weeks:WEEKS.filter(w=>[4,5,6,7,8,9].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-02.3",oe_desc:"Establecer alianzas estratégicas con brokers busca-terrenos",kpi:"5 brokers busca-terrenos asociados",acts:[
   {cod:"A01",act:"Diseñar sistema de trabajo",ent:"Procedimiento de trabajo.",resp:"Directorio",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Difundir a nivel interno",ent:"Acta de capacitación al personal",resp:"Directorio",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Difundir a nivel externo (Jorge & En Marcha)",ent:"Actas de reunión",resp:"Directorio",weeks:WEEKS.filter(w=>[5].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Buscar + brokers",ent:"+ 3 brokers asociados",resp:"Directorio",weeks:WEEKS.filter(w=>[5,6,7,8].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-03",og_desc:"Mejorar la rentabilidad de los proyectos actuales",oes:[
  {oe:"OE-03.1",oe_desc:"Medir la rentabilidad de proyectos entregados",kpi:"Informes de Costos",acts:[
   {cod:"A01",act:"Recabar la información histórica de costos e ingresos de los proyectos SCAT IX, Zentric y Midori.",ent:"Base de datos",resp:"Contabilidad",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Clasificar información histórica de costos e ingresos.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[11].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Realizar análisis de ratios de costos, ingresos y plazos (INDICADORES)",ent:"Informe financiero",resp:"CFO",weeks:WEEKS.filter(w=>[11].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-03.2",oe_desc:"Sincerar presupuesto meta de proyectos actuales",kpi:"Presupuesto Meta por Proyecto",acts:[
   {cod:"A01",act:"Actualizar y difundir la estructura de costos de los proyectos.",ent:"Base de datos",resp:"Contabilidad",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Recabar información histórica de costos e ingresos de los proyectos en ejecución.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Recabar información histórica de costos e ingresos de la Oficina Principal.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Clasificar información histórica de costos e ingresos de acuerdo a la nueva estructura.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[10,11].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Realizar análisis de ratios de costos, ingresos y plazos (INDICADORES).",ent:"Informe financiero",resp:"CFO",weeks:WEEKS.filter(w=>[12].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-03.3",oe_desc:"Implementar estrategias de reducción de costos y gastos",kpi:"Costo real menor al Presupuesto Meta",acts:[
   {cod:"A01",act:"Analizar partidas de mayor incidencia en costo y plazo.",ent:"Análisis de Informe",resp:"Contabilidad",weeks:WEEKS.filter(w=>[3,4].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Buscar e implementar estrategias de reducción de costos.",ent:"Resultado del Proyecto",resp:"Finanzas & Directorio",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Buscar e implementar estrategias de reducción de gastos.",ent:"Resultado del Proyecto",resp:"Finanzas & Directorio",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Implementar política de Pagos y Caja Chica.",ent:"Política difundida.",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Buscar e implementar estrategias de ampliación de plazos en egresos.",ent:"Resultado del Proyecto",resp:"Finanzas & Directorio",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-03.4",oe_desc:"Implementar estrategias de incremento de ingresos",kpi:"Ingreso real mayor al Presupuesto de Ingresos",acts:[
   {cod:"A01",act:"Analizar flujo de ingresos (cuentas corrientes y de garantía) y precios por m2.",ent:"Base de datos",resp:"Contabilidad",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Buscar e implementar estrategias de incremento de ingresos.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Buscar e implementar estrategias de reducción de plazos en ingresos.",ent:"Menor gasto financiero",resp:"Finanzas",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-03.5",oe_desc:"Sincerar ratios de costos y plazos óptimos para proyectos futuros",kpi:"Base de datos de Indicadores financieros clave con sustento técnico.",acts:[
   {cod:"A01",act:"Elaborar Excel \"presupuestador\" de proyectos con ratios sincerados.",ent:"Base de datos",resp:"Contabilidad",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Actualizar la política de Cobranzas.",ent:"Política difundida.",resp:"CFO",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Actualizar la política de Pagos y Caja Chica.",ent:"Política difundida.",resp:"CFO",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-04",og_desc:"Obtener una (1) fuente de financiamiento NO tradicional",oes:[
  {oe:"OE-04.1",oe_desc:"Ordenar la Contabilidad",kpi:"Estados Financieros Consolidados y Auditados (Holding + SPV)",acts:[
   {cod:"A01",act:"Homologar estructura de costos de las SPV.",ent:"Registro de costos con nueva estructura en Contabilidad",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Implementar la estructura de costos de la Holding.",ent:"Registro de costos con nueva estructura en Contabilidad",resp:"Contabilidad",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar la contabilidad de costos y Estados Financieros Consolidados.",ent:"Primer reporte de Estados Financieros Consolidado",resp:"Contabilidad",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Implementar procedimientos de gestión administrativo-contable.",ent:"Procedimiento difundido",resp:"Procesos",weeks:WEEKS.filter(w=>[5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Contratar el servicio de auditoría externa de los procesos contables.",ent:"Informe de Auditoría Externa",resp:"CFO",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A06",act:"Contratar el servicio de auditoría externa de los Estados Financieros.",ent:"Informe de Auditoría Externa",resp:"CFO",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A07",act:"Levantar observaciones de la auditoría externa.",ent:"Informe de Levantamiento de Observaciones de Auditoría",resp:"Contabilidad",weeks:WEEKS.filter(w=>[11].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.2",oe_desc:"Ordenar las Ventas",kpi:"Sistema de Trabajo",acts:[
   {cod:"A01",act:"Implementar política de ventas y cobranzas.",ent:"Política Corporativa",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Implementar procedimiento de cobranzas de ventas al contado y desembolsos de créditos hipotecarios.",ent:"Procedimiento difundido",resp:"Finanzas",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Consultoría externa comercial.",ent:"Informe de consultoría.",resp:"Directorio",weeks:WEEKS.filter(w=>[3,4].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Evaluar la implementación del área de Administración de Ventas.",ent:"Informe de recomendación",resp:"Finanzas",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.3",oe_desc:"Ordenar la Gestión de Proyectos",kpi:"Sistema de Trabajo Auditable (ISO 9001, 31000, 22301)",acts:[
   {cod:"A01",act:"Actualizar los procedimientos de gestión de Proyectos/Operaciones.",ent:"Procedimiento difundido",resp:"Procesos",weeks:WEEKS.filter(w=>[2,3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Difundir e implementar los procedimientos.",ent:"Informe de consultoría",resp:"CFO",weeks:WEEKS.filter(w=>[4,5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Actualizar procedimientos + Gestión de Riesgos + Costumer Experience + Compliance",ent:"Informe de levantamiento de observaciones",resp:"CFO",weeks:WEEKS.filter(w=>[7,8,9,10].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.4",oe_desc:"Ordenar el área Legal",kpi:"Propuesta Formal de Financiamiento",acts:[
   {cod:"A01",act:"Establecer estándar de minutas de compra-venta:  cláusulas Negociables y No negociables",ent:"Modelo estándar de minuta de compra-venta",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer flujo de aprobaciones de contratos.",ent:"Procedimiento y Política de Gestión Contractual",resp:"Procesos",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar procesos de compliance.",ent:"Procedimiento difundido.",resp:"Procesos",weeks:WEEKS.filter(w=>[6,7,8].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.5",oe_desc:"Ordenar las Finanzas",kpi:"Propuesta Formal de Financiamiento",acts:[
   {cod:"A01",act:"Obtener checklist de requerimiento de 3 fondos de inversión reconocidos en el mercado.",ent:"Checklist consolidado de Fondos de Inversión",resp:"CFO",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Revisar y evaluar checklist de requerimiento.",ent:"Informe de evaluación de checklist",resp:"Finanzas",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Consultoría con asesor financiero.",ent:"Informe de consultoría.",resp:"CFO",weeks:WEEKS.filter(w=>[8,9].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Consultoría con asesor legal.",ent:"Informe de consultoría.",resp:"CFO",weeks:WEEKS.filter(w=>[8,9].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Consultoría con asesor contable.",ent:"Informe de consultoría.",resp:"CFO",weeks:WEEKS.filter(w=>[8,9].includes(w.month)).map(w=>w.wk)},
   {cod:"A06",act:"Implementar procedimientos y políticas de gestión de proyectos con financiamiento externo.",ent:"Procedimientos y lineamientos",resp:"CFO",weeks:WEEKS.filter(w=>[10,11].includes(w.month)).map(w=>w.wk)},
   {cod:"A07",act:"Recopilar información requerida y pasar evaluación",ent:"Expediente de financiamiento",resp:"Finanzas",weeks:WEEKS.filter(w=>[11].includes(w.month)).map(w=>w.wk)},
   {cod:"A08",act:"Seguimiento a la propuesta formal.",ent:"Propuesta Formal de Financiamiento o Carta de Intención",resp:"Finanzas",weeks:WEEKS.filter(w=>[12].includes(w.month)).map(w=>w.wk)},
   {cod:"A09",act:"Obtener checklist de requerimiento de 5 bancos (actuales + BBVA + IBK).",ent:"Checklist consolidado de Bancos",resp:"CFO",weeks:WEEKS.filter(w=>[5].includes(w.month)).map(w=>w.wk)},
   {cod:"A10",act:"Revisar y evaluar checklist de requerimiento.",ent:"Informe de evaluación de checklist",resp:"Finanzas",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A11",act:"Actualizar procedimientos de gestión de financiamiento con bancos",ent:"Procedimientos y lineamientos",resp:"Finanzas",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A12",act:"Recopilar información requerida y pasar evaluación con BANCO NUEVO.",ent:"Expediente de financiamiento",resp:"Finanzas",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A13",act:"Seguimiento a la propuesta formal.",ent:"Propuesta Formal de Financiamiento o Carta de Intención",resp:"Finanzas",weeks:WEEKS.filter(w=>[8].includes(w.month)).map(w=>w.wk)},
   {cod:"A14",act:"Realizar estructuración de proyecto con socio inversionista por casuísticas principales: Aporte de terreno; Aporte de fondos.",ent:"Análisis de rentabilidad por escenarios.",resp:"CFO",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A15",act:"Consultoría con asesor financiero.",ent:"Informe de consultoría.",resp:"CFO",weeks:WEEKS.filter(w=>[7,8].includes(w.month)).map(w=>w.wk)},
   {cod:"A16",act:"Consultoría con asesor legal.",ent:"Informe de consultoría.",resp:"CFO",weeks:WEEKS.filter(w=>[7,8].includes(w.month)).map(w=>w.wk)},
   {cod:"A17",act:"Consultoría con asesor contable.",ent:"Informe de consultoría.",resp:"CFO",weeks:WEEKS.filter(w=>[7,8].includes(w.month)).map(w=>w.wk)},
   {cod:"A18",act:"Implementar procedimientos y políticas de gestión de proyectos con financiamiento externo.",ent:"Procedimientos y lineamientos",resp:"CFO",weeks:WEEKS.filter(w=>[9,10].includes(w.month)).map(w=>w.wk)},
   {cod:"A19",act:"Explorar opciones de financiamiento con FFF",ent:"Búsqueda activa",resp:"CFO",weeks:WEEKS.filter(w=>[10,11,12].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
];

// Total activities for Inmobiliarias: 72

// === CONSTRUCTORAS ===
const CONST_SEED = [
 {og:"OG-01",og_desc:"Garantizar la cadena de suministros",oes:[
  {oe:"OE-01.1",oe_desc:"Establecer el sistema de gestión de la cadena de suministros",kpi:"Sistema de trabajo implementado.",acts:[
   {cod:"A01",act:"Implementar procesos de gestión de adquisiciones (materiales y servicios)",ent:"Procedimientos difundidos",resp:"Procesos",weeks:WEEKS.filter(w=>[1,2].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Contratar personal con know how para asimilar",ent:"2 contrataciones (mínimo)",resp:"Directorio",weeks:WEEKS.filter(w=>[2,3,7,8].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Desarrollar el plan de carrera para el personal de confianza asignado",ent:"Plan de trabajo",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Implementar la política de adquisiciones.",ent:"Política difundida",resp:"CFO",weeks:WEEKS.filter(w=>[2,3].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Implementar modelos estándar de contratos.",ent:"Modelo corporativo implementado",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-02",og_desc:"Lograr rentabilidad en los proyectos",oes:[
  {oe:"OE-02.1",oe_desc:"Establecer un precio por m2 de construcción con un margen de utilidad de 10%",kpi:"Rentabilidad 10% en EEFF",acts:[
   {cod:"A01",act:"Emitir presupuesto de costos y gastos 2026",ent:"Presupuesto aprobado",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Emitir EEFF proyectados 2026.",ent:"EEFF 2026 proyectados.",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Contratar un estudio de precios de transferencia para sincerar la utilidad de cada proyecto.",ent:"Informe de Estudio de precios",resp:"CFO",weeks:WEEKS.filter(w=>[6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Realizar seguimiento al presupuesto 2026",ent:"EEFF mensuales con análisis de desviaciones",resp:"Finanzas",weeks:WEEKS.filter(w=>[4,5,6,7,8,9,10,11,12].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-03",og_desc:"Incrementar la rentabilidad de los proyectos",oes:[
  {oe:"OE-03.1",oe_desc:"Reducir el costo por m2 de construcción en un 3%",kpi:"Rentabilidad + 3%",acts:[
   {cod:"A01",act:"Analizar el costo por m2 según el presupuesto meta de los proyectos.",ent:"Informe de análisis de costos",resp:"CFO",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Revisar la estrategia de adquisiciones actual.",ent:"Análisis interno.",resp:"Directorio",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Revisar la estrategia de operaciones actual",ent:"Análisis interno.",resp:"Directorio",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Revisar la proyección de uso de equipos en obras.",ent:"Análisis interno.",resp:"Directorio",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Re-plantear las estrategias de adquisiciones y operaciones.",ent:"Informe de análisis técnico",resp:"Directorio",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A06",act:"Implementar las mejoras identificadas",ent:"Plan de trabajo.",resp:"GG Constructoras",weeks:WEEKS.filter(w=>[8,9,10,11,12].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-04",og_desc:"Culminar con la implementación de los procedimientos de gestión",oes:[
  {oe:"OE-04.1",oe_desc:"Reducir el costo por m2 de construcción en un 3%",kpi:"Procedimientos implementados",acts:[
   {cod:"A01",act:"Actualizar el plan de trabajo de procesos",ent:"Plan de trabajo actualizado.",resp:"Procesos",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer reuniones periódicas para reporte de avances.",ent:"Cronograma de reuniones",resp:"Directorio",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar procesos de gestión de cadena de suministros (compras - almacén - costos).",ent:"Procedimientos aprobados.",resp:"Procesos / GG Constructoras",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Implementar procesos de gestión de tesorería.",ent:"Procedimientos aprobados.",resp:"Procesos / GG Constructoras",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Implementar procesos de gestión de operaciones (producción).",ent:"Procedimientos aprobados.",resp:"Procesos / GG Constructoras",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A06",act:"Implementar MOF de cada puesto clave (GG Constructoras, Operaciones, Logística, Almacén, Residente de Obra, Administración).",ent:"MOF aprobado.",resp:"Procesos / Directorio",weeks:WEEKS.filter(w=>[8].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.2",oe_desc:"Implementar el Sistema de Gestión de Calidad de Inmobiliaria en Constructora",kpi:"SGC implementado.",acts:[
   {cod:"A01",act:"Establecer el plan de trabajo de procesos.",ent:"Plan de trabajo.",resp:"Calidad",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer reuniones periódicas para reporte de avances.",ent:"Cronograma de reuniones.",resp:"Directorio",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar manual de gestión.",ent:"Manual de procesos constructivos aprobado.",resp:"Procesos / G. Construcción",weeks:WEEKS.filter(w=>[4,5,6,7,8,9].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
];

// Total activities for Constructoras: 24
