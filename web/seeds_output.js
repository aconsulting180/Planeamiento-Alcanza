
// === INMOBILIARIAS ===
const INMOB_SEED = [
 {og:"OG-01",og_desc:"Garantizar la liquidez del grupo (Holding y Sucursales)",oes:[
  {oe:"OE-01.1",oe_desc:"Implementar el Plan de trabajo financiero por Hitos de proyectos",kpi:"Resultado positivo en Flujo de Caja",acts:[
   {cod:"A01",act:"Asegurar la proyecci¾n de resultados del FC sostenible en el tiempo",ent:"Flujo de Caja",resp:"CFO",weeks:WEEKS.filter(w=>[1,2].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer un plan de trabajo por ßreas (& gesti¾n de riesgos).",ent:"Plan de trabajo",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Difundir a los involucrados",ent:"Acta de entrega",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Seguimiento Ingresos",ent:"Reporte de seguimiento semanal",resp:"Finanzas",weeks:WEEKS.filter(w=>[3,4,5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Seguimiento Egresos",ent:"Reporte de seguimiento semanal",resp:"Finanzas",weeks:WEEKS.filter(w=>[3,4,5,6].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-01.2",oe_desc:"Asegurar la precisi¾n del flujo de caja con horizonte 3 meses: Precisi¾n >= 90%",kpi:"Precisi¾n de FC >= 90%",acts:[
   {cod:"A01",act:"Medir el porcentaje de precisi¾n actual",ent:"Mov. Real vs  Mov. Proyectado x 100",resp:"Finanzas",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Buscar e implementar mecanismos para incrementar la precisi¾n en las proyecciones de ingresos y egresos.",ent:"Mejoras varias en el flujo.",resp:"Finanzas",weeks:WEEKS.filter(w=>[3,4,5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Migrar el reporte de Flujo de Caja a un Software versatil (no Excel)",ent:"Software",resp:"Finanzas",weeks:WEEKS.filter(w=>[6,7,8,9,10].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Medir el porcentaje de precisi¾n optimizado",ent:"Mov. Real vs  Mov. Proyectado x 100",resp:"Finanzas",weeks:WEEKS.filter(w=>[6,7,8,9,10,11].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-02",og_desc:"Estrategia de crecimiento 2027 - 2028 (backlog)",oes:[
  {oe:"OE-02.1",oe_desc:"Asegurar la liquidez del grupo + nuevos proyectos",kpi:"Liquidez positiva",acts:[
   {cod:"A01",act:"Realizar anßlisis de flujos de caja tÝpicos de proyectos de acuerdo con su tama±o.",ent:"Informe de Anßlisis Financiero",resp:"CFO",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer Nro. De proyectos \"peque±os\" vs cada proyecto grande.",ent:"Informe de Anßlisis Financiero & recomendaci¾n",resp:"CFO",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Difusi¾n a los involucrados (brokers, gerencias, etc).",ent:"Actas de reuniones",resp:"Directorio",weeks:WEEKS.filter(w=>[8].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-02.2",oe_desc:"MÝnimo un (01) proyecto fuera de Santa Catalina",kpi:"01 proyecto importante fuera de Sta Catalina",acts:[
   {cod:"A01",act:"Enfocar b·squeda de terrenos/casas fuera de Santa Catalina",ent:"Coordinaci¾n con brokers",resp:"Directorio",weeks:WEEKS.filter(w=>[4,5,6,7,8,9].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-02.3",oe_desc:"Establecer alianzas estratÚgicas con brokers busca-terrenos",kpi:"5 brokers busca-terrenos asociados",acts:[
   {cod:"A01",act:"Dise±ar sistema de trabajo",ent:"Procedimiento de trabajo.",resp:"Directorio",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Difundir a nivel interno",ent:"Acta de capacitaci¾n al personal",resp:"Directorio",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Difundir a nivel externo (Jorge & En Marcha)",ent:"Actas de reuni¾n",resp:"Directorio",weeks:WEEKS.filter(w=>[5].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Buscar + brokers",ent:"+ 3 brokers asociados",resp:"Directorio",weeks:WEEKS.filter(w=>[5,6,7,8].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-03",og_desc:"Mejorar la rentabilidad de los proyectos actuales",oes:[
  {oe:"OE-03.1",oe_desc:"Medir la rentabilidad de proyectos entregados",kpi:"Informes de Costos",acts:[
   {cod:"A01",act:"Recabar la informaci¾n hist¾rica de costos e ingresos de los proyectos SCAT IX, Zentric y Midori.",ent:"Base de datos",resp:"Contabilidad",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Clasificar informaci¾n hist¾rica de costos e ingresos.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[11].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Realizar anßlisis de ratios de costos, ingresos y plazos (INDICADORES)",ent:"Informe financiero",resp:"CFO",weeks:WEEKS.filter(w=>[11].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-03.2",oe_desc:"Sincerar presupuesto meta de proyectos actuales",kpi:"Presupuesto Meta por Proyecto",acts:[
   {cod:"A01",act:"Actualizar y difundir la estructura de costos de los proyectos.",ent:"Base de datos",resp:"Contabilidad",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Recabar informaci¾n hist¾rica de costos e ingresos de los proyectos en ejecuci¾n.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Recabar informaci¾n hist¾rica de costos e ingresos de la Oficina Principal.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Clasificar informaci¾n hist¾rica de costos e ingresos de acuerdo a la nueva estructura.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[10,11].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Realizar anßlisis de ratios de costos, ingresos y plazos (INDICADORES).",ent:"Informe financiero",resp:"CFO",weeks:WEEKS.filter(w=>[12].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-03.3",oe_desc:"Implementar estrategias de reducci¾n de costos y gastos",kpi:"Costo real menor al Presupuesto Meta",acts:[
   {cod:"A01",act:"Analizar partidas de mayor incidencia en costo y plazo.",ent:"Anßlisis de Informe",resp:"Contabilidad",weeks:WEEKS.filter(w=>[3,4].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Buscar e implementar estrategias de reducci¾n de costos.",ent:"Resultado del Proyecto",resp:"Finanzas & Directorio",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Buscar e implementar estrategias de reducci¾n de gastos.",ent:"Resultado del Proyecto",resp:"Finanzas & Directorio",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Implementar polÝtica de Pagos y Caja Chica.",ent:"PolÝtica difundida.",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Buscar e implementar estrategias de ampliaci¾n de plazos en egresos.",ent:"Resultado del Proyecto",resp:"Finanzas & Directorio",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-03.4",oe_desc:"Implementar estrategias de incremento de ingresos",kpi:"Ingreso real mayor al Presupuesto de Ingresos",acts:[
   {cod:"A01",act:"Analizar flujo de ingresos (cuentas corrientes y de garantÝa) y precios por m2.",ent:"Base de datos",resp:"Contabilidad",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Buscar e implementar estrategias de incremento de ingresos.",ent:"Base de datos",resp:"Finanzas",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Buscar e implementar estrategias de reducci¾n de plazos en ingresos.",ent:"Menor gasto financiero",resp:"Finanzas",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-03.5",oe_desc:"Sincerar ratios de costos y plazos ¾ptimos para proyectos futuros",kpi:"Base de datos de Indicadores financieros clave con sustento tÚcnico.",acts:[
   {cod:"A01",act:"Elaborar Excel \"presupuestador\" de proyectos con ratios sincerados.",ent:"Base de datos",resp:"Contabilidad",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Actualizar la polÝtica de Cobranzas.",ent:"PolÝtica difundida.",resp:"CFO",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Actualizar la polÝtica de Pagos y Caja Chica.",ent:"PolÝtica difundida.",resp:"CFO",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-04",og_desc:"Obtener una (1) fuente de financiamiento NO tradicional",oes:[
  {oe:"OE-04.1",oe_desc:"Ordenar la Contabilidad",kpi:"Estados Financieros Consolidados y Auditados (Holding + SPV)",acts:[
   {cod:"A01",act:"Homologar estructura de costos de las SPV.",ent:"Registro de costos con nueva estructura en Contabilidad",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Implementar la estructura de costos de la Holding.",ent:"Registro de costos con nueva estructura en Contabilidad",resp:"Contabilidad",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar la contabilidad de costos y Estados Financieros Consolidados.",ent:"Primer reporte de Estados Financieros Consolidado",resp:"Contabilidad",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Implementar procedimientos de gesti¾n administrativo-contable.",ent:"Procedimiento difundido",resp:"Procesos",weeks:WEEKS.filter(w=>[5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Contratar el servicio de auditorÝa externa de los procesos contables.",ent:"Informe de AuditorÝa Externa",resp:"CFO",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A06",act:"Contratar el servicio de auditorÝa externa de los Estados Financieros.",ent:"Informe de AuditorÝa Externa",resp:"CFO",weeks:WEEKS.filter(w=>[10].includes(w.month)).map(w=>w.wk)},
   {cod:"A07",act:"Levantar observaciones de la auditorÝa externa.",ent:"Informe de Levantamiento de Observaciones de AuditorÝa",resp:"Contabilidad",weeks:WEEKS.filter(w=>[11].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.2",oe_desc:"Ordenar las Ventas",kpi:"Sistema de Trabajo",acts:[
   {cod:"A01",act:"Implementar polÝtica de ventas y cobranzas.",ent:"PolÝtica Corporativa",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Implementar procedimiento de cobranzas de ventas al contado y desembolsos de crÚditos hipotecarios.",ent:"Procedimiento difundido",resp:"Finanzas",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"ConsultorÝa externa comercial.",ent:"Informe de consultorÝa.",resp:"Directorio",weeks:WEEKS.filter(w=>[3,4].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Evaluar la implementaci¾n del ßrea de Administraci¾n de Ventas.",ent:"Informe de recomendaci¾n",resp:"Finanzas",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.3",oe_desc:"Ordenar la Gesti¾n de Proyectos",kpi:"Sistema de Trabajo Auditable (ISO 9001, 31000, 22301)",acts:[
   {cod:"A01",act:"Actualizar los procedimientos de gesti¾n de Proyectos/Operaciones.",ent:"Procedimiento difundido",resp:"Procesos",weeks:WEEKS.filter(w=>[2,3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Difundir e implementar los procedimientos.",ent:"Informe de consultorÝa",resp:"CFO",weeks:WEEKS.filter(w=>[4,5,6].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Actualizar procedimientos + Gesti¾n de Riesgos + Costumer Experience + Compliance",ent:"Informe de levantamiento de observaciones",resp:"CFO",weeks:WEEKS.filter(w=>[7,8,9,10].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.4",oe_desc:"Ordenar el ßrea Legal",kpi:"Propuesta Formal de Financiamiento",acts:[
   {cod:"A01",act:"Establecer estßndar de minutas de compra-venta: 
clßusulas Negociables y No negociables",ent:"Modelo estßndar de minuta de compra-venta",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer flujo de aprobaciones de contratos.",ent:"Procedimiento y PolÝtica de Gesti¾n Contractual",resp:"Procesos",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar procesos de compliance.",ent:"Procedimiento difundido.",resp:"Procesos",weeks:WEEKS.filter(w=>[6,7,8].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.5",oe_desc:"Ordenar las Finanzas",kpi:"Propuesta Formal de Financiamiento",acts:[
   {cod:"A01",act:"Obtener checklist de requerimiento de 3 fondos de inversi¾n reconocidos en el mercado.",ent:"Checklist consolidado de Fondos de Inversi¾n",resp:"CFO",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Revisar y evaluar checklist de requerimiento.",ent:"Informe de evaluaci¾n de checklist",resp:"Finanzas",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"ConsultorÝa con asesor financiero.",ent:"Informe de consultorÝa.",resp:"CFO",weeks:WEEKS.filter(w=>[8,9].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"ConsultorÝa con asesor legal.",ent:"Informe de consultorÝa.",resp:"CFO",weeks:WEEKS.filter(w=>[8,9].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"ConsultorÝa con asesor contable.",ent:"Informe de consultorÝa.",resp:"CFO",weeks:WEEKS.filter(w=>[8,9].includes(w.month)).map(w=>w.wk)},
   {cod:"A06",act:"Implementar procedimientos y polÝticas de gesti¾n de proyectos con financiamiento externo.",ent:"Procedimientos y lineamientos",resp:"CFO",weeks:WEEKS.filter(w=>[10,11].includes(w.month)).map(w=>w.wk)},
   {cod:"A07",act:"Recopilar informaci¾n requerida y pasar evaluaci¾n",ent:"Expediente de financiamiento",resp:"Finanzas",weeks:WEEKS.filter(w=>[11].includes(w.month)).map(w=>w.wk)},
   {cod:"A08",act:"Seguimiento a la propuesta formal.",ent:"Propuesta Formal de Financiamiento o Carta de Intenci¾n",resp:"Finanzas",weeks:WEEKS.filter(w=>[12].includes(w.month)).map(w=>w.wk)},
   {cod:"A09",act:"Obtener checklist de requerimiento de 5 bancos (actuales + BBVA + IBK).",ent:"Checklist consolidado de Bancos",resp:"CFO",weeks:WEEKS.filter(w=>[5].includes(w.month)).map(w=>w.wk)},
   {cod:"A10",act:"Revisar y evaluar checklist de requerimiento.",ent:"Informe de evaluaci¾n de checklist",resp:"Finanzas",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A11",act:"Actualizar procedimientos de gesti¾n de financiamiento con bancos",ent:"Procedimientos y lineamientos",resp:"Finanzas",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A12",act:"Recopilar informaci¾n requerida y pasar evaluaci¾n con BANCO NUEVO.",ent:"Expediente de financiamiento",resp:"Finanzas",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A13",act:"Seguimiento a la propuesta formal.",ent:"Propuesta Formal de Financiamiento o Carta de Intenci¾n",resp:"Finanzas",weeks:WEEKS.filter(w=>[8].includes(w.month)).map(w=>w.wk)},
   {cod:"A14",act:"Realizar estructuraci¾n de proyecto con socio inversionista por casuÝsticas principales: Aporte de terreno; Aporte de fondos.",ent:"Anßlisis de rentabilidad por escenarios.",resp:"CFO",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A15",act:"ConsultorÝa con asesor financiero.",ent:"Informe de consultorÝa.",resp:"CFO",weeks:WEEKS.filter(w=>[7,8].includes(w.month)).map(w=>w.wk)},
   {cod:"A16",act:"ConsultorÝa con asesor legal.",ent:"Informe de consultorÝa.",resp:"CFO",weeks:WEEKS.filter(w=>[7,8].includes(w.month)).map(w=>w.wk)},
   {cod:"A17",act:"ConsultorÝa con asesor contable.",ent:"Informe de consultorÝa.",resp:"CFO",weeks:WEEKS.filter(w=>[7,8].includes(w.month)).map(w=>w.wk)},
   {cod:"A18",act:"Implementar procedimientos y polÝticas de gesti¾n de proyectos con financiamiento externo.",ent:"Procedimientos y lineamientos",resp:"CFO",weeks:WEEKS.filter(w=>[9,10].includes(w.month)).map(w=>w.wk)},
   {cod:"A19",act:"Explorar opciones de financiamiento con FFF",ent:"B·squeda activa",resp:"CFO",weeks:WEEKS.filter(w=>[10,11,12].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
];

// Total activities for Inmobiliarias: 72

// === CONSTRUCTORAS ===
const CONST_SEED = [
 {og:"OG-01",og_desc:"Garantizar la cadena de suministros",oes:[
  {oe:"OE-01.1",oe_desc:"Establecer el sistema de gesti¾n de la cadena de suministros",kpi:"Sistema de trabajo implementado.",acts:[
   {cod:"A01",act:"Implementar procesos de gesti¾n de adquisiciones (materiales y servicios)",ent:"Procedimientos difundidos",resp:"Procesos",weeks:WEEKS.filter(w=>[1,2].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Contratar personal con know how para asimilar",ent:"2 contrataciones (mÝnimo)",resp:"Directorio",weeks:WEEKS.filter(w=>[2,3,7,8].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Desarrollar el plan de carrera para el personal de confianza asignado",ent:"Plan de trabajo",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Implementar la polÝtica de adquisiciones.",ent:"PolÝtica difundida",resp:"CFO",weeks:WEEKS.filter(w=>[2,3].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Implementar modelos estßndar de contratos.",ent:"Modelo corporativo implementado",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-02",og_desc:"Lograr rentabilidad en los proyectos",oes:[
  {oe:"OE-02.1",oe_desc:"Establecer un precio por m2 de construcci¾n con un margen de utilidad de 10%",kpi:"Rentabilidad 10% en EEFF",acts:[
   {cod:"A01",act:"Emitir presupuesto de costos y gastos 2026",ent:"Presupuesto aprobado",resp:"CFO",weeks:WEEKS.filter(w=>[2].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Emitir EEFF proyectados 2026.",ent:"EEFF 2026 proyectados.",resp:"CFO",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Contratar un estudio de precios de transferencia para sincerar la utilidad de cada proyecto.",ent:"Informe de Estudio de precios",resp:"CFO",weeks:WEEKS.filter(w=>[6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Realizar seguimiento al presupuesto 2026",ent:"EEFF mensuales con anßlisis de desviaciones",resp:"Finanzas",weeks:WEEKS.filter(w=>[4,5,6,7,8,9,10,11,12].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-03",og_desc:"Incrementar la rentabilidad de los proyectos",oes:[
  {oe:"OE-03.1",oe_desc:"Reducir el costo por m2 de construcci¾n en un 3%",kpi:"Rentabilidad + 3%",acts:[
   {cod:"A01",act:"Analizar el costo por m2 seg·n el presupuesto meta de los proyectos.",ent:"Informe de anßlisis de costos",resp:"CFO",weeks:WEEKS.filter(w=>[4].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Revisar la estrategia de adquisiciones actual.",ent:"Anßlisis interno.",resp:"Directorio",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Revisar la estrategia de operaciones actual",ent:"Anßlisis interno.",resp:"Directorio",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Revisar la proyecci¾n de uso de equipos en obras.",ent:"Anßlisis interno.",resp:"Directorio",weeks:WEEKS.filter(w=>[6].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Re-plantear las estrategias de adquisiciones y operaciones.",ent:"Informe de anßlisis tÚcnico",resp:"Directorio",weeks:WEEKS.filter(w=>[7].includes(w.month)).map(w=>w.wk)},
   {cod:"A06",act:"Implementar las mejoras identificadas",ent:"Plan de trabajo.",resp:"GG Constructoras",weeks:WEEKS.filter(w=>[8,9,10,11,12].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
 {og:"OG-04",og_desc:"Culminar con la implementaci¾n de los procedimientos de gesti¾n",oes:[
  {oe:"OE-04.1",oe_desc:"Reducir el costo por m2 de construcci¾n en un 3%",kpi:"Procedimientos implementados",acts:[
   {cod:"A01",act:"Actualizar el plan de trabajo de procesos",ent:"Plan de trabajo actualizado.",resp:"Procesos",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer reuniones peri¾dicas para reporte de avances.",ent:"Cronograma de reuniones",resp:"Directorio",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar procesos de gesti¾n de cadena de suministros (compras - almacÚn - costos).",ent:"Procedimientos aprobados.",resp:"Procesos / GG Constructoras",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A04",act:"Implementar procesos de gesti¾n de tesorerÝa.",ent:"Procedimientos aprobados.",resp:"Procesos / GG Constructoras",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A05",act:"Implementar procesos de gesti¾n de operaciones (producci¾n).",ent:"Procedimientos aprobados.",resp:"Procesos / GG Constructoras",weeks:WEEKS.filter(w=>[4,5,6,7].includes(w.month)).map(w=>w.wk)},
   {cod:"A06",act:"Implementar MOF de cada puesto clave (GG Constructoras, Operaciones, LogÝstica, AlmacÚn, Residente de Obra, Administraci¾n).",ent:"MOF aprobado.",resp:"Procesos / Directorio",weeks:WEEKS.filter(w=>[8].includes(w.month)).map(w=>w.wk)},
  ]},
  {oe:"OE-04.2",oe_desc:"Implementar el Sistema de Gesti¾n de Calidad de Inmobiliaria en Constructora",kpi:"SGC implementado.",acts:[
   {cod:"A01",act:"Establecer el plan de trabajo de procesos.",ent:"Plan de trabajo.",resp:"Calidad",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A02",act:"Establecer reuniones peri¾dicas para reporte de avances.",ent:"Cronograma de reuniones.",resp:"Directorio",weeks:WEEKS.filter(w=>[3].includes(w.month)).map(w=>w.wk)},
   {cod:"A03",act:"Implementar manual de gesti¾n.",ent:"Manual de procesos constructivos aprobado.",resp:"Procesos / G. Construcci¾n",weeks:WEEKS.filter(w=>[4,5,6,7,8,9].includes(w.month)).map(w=>w.wk)},
  ]},
 ]},
];

// Total activities for Constructoras: 24
