#!/usr/bin/env python3
"""
Generador de Excel de Planeamiento 2026
- Lookahead Anual (Gantt semanal)
- Plan Mensual
- PPC (Porcentaje de Plan Cumplido)
- AR (Análisis de Restricciones)
Para: GIS (Postventa) y METROPOLITANO (Diseño)
"""
import xlsxwriter
from datetime import date, timedelta
import math

# ══════════════════════════════════════════════════════════════════════════════
# DATA - GIS (POSTVENTA)
# ══════════════════════════════════════════════════════════════════════════════

GIS_DATA = {
    "area": "GIS (Postventa)",
    "short": "GIS",
    "objetivos": [
        {
            "og": "OG-01",
            "og_desc": "Mejorar la eficiencia operativa enfocada en la satisfacción del cliente (BPTL)",
            "oes": [
                {
                    "oe": "OE-01.1",
                    "oe_desc": "Reducir el LT de atención de postventa",
                    "kpi": "% de incidencias atendidas dentro de 48 horas hábiles ≥ 90%",
                    "actividades": [
                        {"cod": "A01", "act": "Diagnóstico del proceso actual de atención Postventa", "entregable": "Mapa del proceso actual + diagnóstico de tiempos", "resp": "GIS", "meses": [1,2,3]},
                        {"cod": "A02", "act": "Definición de estándares de atención y tiempos límite", "entregable": "Matriz de tiempos de atención y prioridades", "resp": "Directorio/GIS", "meses": [2,3]},
                        {"cod": "A03", "act": "Optimización del flujo de atención Postventa", "entregable": "Proceso optimizado de atención Postventa", "resp": "Directorio/GIS", "meses": [2,3]},
                        {"cod": "A04", "act": "Implementación de herramientas de control y seguimiento", "entregable": "Herramienta de control de solicitudes Postventa", "resp": "GIS", "meses": [3,4,5,6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-01.2",
                    "oe_desc": "Implementar Sperant en los proyectos que se entregarán este año",
                    "kpi": "% de proyectos entregados con Sperant implementado y operativo 100%",
                    "actividades": [
                        {"cod": "A01", "act": "Definir qué procesos se migran a Sperant y cuáles se mantienen fuera", "entregable": "Documento de alcance de implementación de Sperant", "resp": "Directorio/GIS", "meses": [2,3]},
                        {"cod": "A02", "act": "Planificación de la implementación por proyecto y cronograma", "entregable": "Cronograma de implementación de Sperant por proyecto", "resp": "Directorio/GIS", "meses": [2,3]},
                        {"cod": "A03", "act": "Configuración y parametrización de Sperant", "entregable": "Sperant configurado y listo por proyecto", "resp": "GIS", "meses": [2,3,4]},
                        {"cod": "A04", "act": "Implementación piloto y ajustes iniciales - Midori", "entregable": "Informe de piloto", "resp": "GIS", "meses": [1,2,3,4,5,6]},
                        {"cod": "A05", "act": "Implementación progresiva en los demás proyectos", "entregable": "Reportes de desempeño", "resp": "GIS", "meses": [6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-01.3",
                    "oe_desc": "Implementar nuevos Canales de atención: Chatbot + Servicio al cliente",
                    "kpi": "% de incidencias registradas a través de los nuevos canales ≥ 60%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición de alcance y rol de los nuevos canales", "entregable": "Documento de alcance y funcionamiento de los nuevos canales", "resp": "Directorio/GIS", "meses": [2,3]},
                        {"cod": "A02", "act": "Diseño del flujo de atención multicanal", "entregable": "Flujo de atención multicanal documentado", "resp": "Directorio/GIS/Procesos", "meses": [2,3]},
                        {"cod": "A03", "act": "Implementación del Chatbot piloto (Piloto: Midori)", "entregable": "Política difundida", "resp": "GIS", "meses": [3,4,5]},
                        {"cod": "A04", "act": "Implementación del Servicio de Atención telefónica (Piloto: Midori)", "entregable": "Política difundida", "resp": "GIS", "meses": [3,4,5]},
                        {"cod": "A05", "act": "Comunicación a clientes y puesta en marcha", "entregable": "Reporte de desempeño de los nuevos canales", "resp": "GIS", "meses": [4,5,6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-01.4",
                    "oe_desc": "Implementar herramientas operativas, tecnológicas y de transporte",
                    "kpi": "% de atenciones de Post Venta realizadas con herramientas implementadas ≥ 80%",
                    "actividades": [
                        {"cod": "A01", "act": "Diagnóstico de necesidades operativas en campo", "entregable": "Diagnóstico de necesidades tecnológicas y movilidad", "resp": "GIS", "meses": [3,4]},
                        {"cod": "A02", "act": "Definición de herramientas operativas, tecnológicas y medios de transporte", "entregable": "Listado y especificación de herramientas", "resp": "Directorio/GIS", "meses": [4]},
                        {"cod": "A03", "act": "Evaluación de costos y aprobación", "entregable": "Presupuesto aprobado para implementación", "resp": "Directorio", "meses": [4,5]},
                        {"cod": "A04", "act": "Implementación en campo y seguimiento continuo", "entregable": "Reporte de desempeño y mejoras implementadas", "resp": "GIS", "meses": [4,5,6,7,8,9,10,11,12]},
                    ]
                },
            ]
        },
        {
            "og": "OG-02",
            "og_desc": "Asegurar la Calidad de los proyectos a entregar",
            "oes": [
                {
                    "oe": "OE-02.1",
                    "oe_desc": "Elaborar nueva versión de Manual de Propietarios para cada proyecto",
                    "kpi": "% de proyectos entregados con Manual de Propietario actualizado 100%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición de alcance y estructura del Manual de Propietarios", "entregable": "Estructura y alcance del Manual", "resp": "Directorio/GIS/Inmobiliaria", "meses": [3]},
                        {"cod": "A02", "act": "Solicitud de información de áreas involucradas", "entregable": "Información recopilada y validada por área", "resp": "GIS/Calidad/Inmobiliaria/Metropolitano", "meses": [3,4]},
                        {"cod": "A03", "act": "Desarrollo del contenido del Manual por proyecto", "entregable": "Borrador del Manual de Propietarios por proyecto", "resp": "GIS", "meses": [4,5,6,7,8,9,10,11,12]},
                        {"cod": "A04", "act": "Revisión y validación multidisciplinaria", "entregable": "Manual validado", "resp": "GIS/Calidad/Inmobiliaria/Metropolitano/Legal", "meses": [6,9,12]},
                        {"cod": "A05", "act": "Implementación y entrega al cliente", "entregable": "Manual entregado al cliente", "resp": "GIS", "meses": [6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-02.2",
                    "oe_desc": "Elaborar e implementar Procedimiento de Recepción de UI y AC",
                    "kpi": "% de proyectos que aplican el procedimiento de recepción ≥ 95%",
                    "actividades": [
                        {"cod": "A01", "act": "Definir Alcance del procedimiento de Recepción y Entrega", "entregable": "Alcance y estructura del Procedimiento", "resp": "Directorio/GIS/Inmobiliaria/Procesos", "meses": [2,3]},
                        {"cod": "A02", "act": "Estandarización del proceso de inspecciones y control de calidad", "entregable": "Procedimiento de inspecciones y checklist estandarizado", "resp": "GIS/CALIDAD/Procesos", "meses": [3,4]},
                        {"cod": "A03", "act": "Formalización de la recepción de Obra hacia Calidad y Postventa", "entregable": "Procedimiento de recepción formal Obra → Calidad/Postventa", "resp": "GIS/CALIDAD/Procesos", "meses": [4,5]},
                        {"cod": "A04", "act": "Definición del procedimiento de entrega a clientes finales y AC", "entregable": "Procedimiento documentado de entrega", "resp": "Directorio/GIS/Inmobiliaria/Procesos", "meses": [5,6]},
                        {"cod": "A05", "act": "Estandarización de documentación técnica a entregar", "entregable": "Matriz de documentación técnica por tipo de entrega", "resp": "GIS/CALIDAD/Inmobiliaria", "meses": [5,6]},
                        {"cod": "A06", "act": "Implementación y capacitación", "entregable": "Reporte de seguimiento", "resp": "GIS", "meses": [6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-02.3",
                    "oe_desc": "Implementar Manual de tolerancias brindado por el Área de Calidad",
                    "kpi": "% de proyectos entregados aplicando el Manual de Tolerancias ≥ 95%",
                    "actividades": [
                        {"cod": "A01", "act": "Revisión y definición del alcance del Manual de Tolerancias", "entregable": "Alcance definido del Manual y su aplicación", "resp": "Directorio/GIS/CALIDAD/Inmobiliaria/Legal", "meses": [2,3,4]},
                        {"cod": "A02", "act": "Integración del Manual de Tolerancias al proceso de Recepción", "entregable": "Manual integrado al proceso operativo", "resp": "GIS", "meses": [5,6]},
                        {"cod": "A03", "act": "Implementación del Manual de Tolerancias", "entregable": "Actas de recepción de clientes", "resp": "GIS", "meses": [6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-02.4",
                    "oe_desc": "Documentar Lecciones Aprendidas - Matriz General",
                    "kpi": "Número de lecciones aprendidas documentadas por proyecto - 100%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición del alcance y estructura de la matriz de Lecciones Aprendidas", "entregable": "Formato de matriz general de Lecciones Aprendidas", "resp": "GIS", "meses": [2,3]},
                        {"cod": "A02", "act": "Identificación y levantamiento de lecciones aprendidas por proyecto", "entregable": "Listado consolidado de lecciones aprendidas", "resp": "GIS", "meses": [3,4,6,7,9,10,12]},
                        {"cod": "A03", "act": "Implementación y uso en proyectos siguientes", "entregable": "Matriz aplicada en proyectos activos", "resp": "Directorio/GIS/Inmobiliaria", "meses": [5,8,11]},
                    ]
                },
                {
                    "oe": "OE-02.5",
                    "oe_desc": "Medir la Satisfacción de los clientes (Encuestas)",
                    "kpi": "Índice de satisfacción del cliente Post Venta (%) ≥ 85%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición del enfoque y alcance de la medición", "entregable": "Alcance y enfoque de la medición de satisfacción", "resp": "CX/GIS/Inmobiliaria", "meses": [3]},
                        {"cod": "A02", "act": "Diseño de la encuesta de satisfacción / Alineado con CX", "entregable": "Encuesta de satisfacción diseñada", "resp": "CX/GIS/Inmobiliaria", "meses": [3,4]},
                        {"cod": "A03", "act": "Definición de herramientas y canales de aplicación", "entregable": "Plan de aplicación de encuestas", "resp": "CX/GIS/Inmobiliaria", "meses": [4]},
                        {"cod": "A04", "act": "Implementación de la encuesta (Midori, Zentric, Parque Emilio)", "entregable": "Encuestas aplicadas y base de datos de resultados", "resp": "GIS", "meses": [5,6]},
                        {"cod": "A05", "act": "Implementación en proyectos restantes (hasta Infinity)", "entregable": "Encuestas aplicadas y base de datos de resultados", "resp": "GIS", "meses": [7,8,9,10,11,12]},
                        {"cod": "A06", "act": "Análisis de resultados y medición de indicadores", "entregable": "Reporte de satisfacción del cliente", "resp": "GIS", "meses": [7,8,9,10,11,12]},
                    ]
                },
            ]
        },
        {
            "og": "OG-03",
            "og_desc": "Evaluar elemento diferenciador en el Servicio Post Venta",
            "oes": [
                {
                    "oe": "OE-03.1",
                    "oe_desc": "Analizar alternativas innovadoras para el servicio Postventa",
                    "kpi": "Nº de iniciativas innovadoras evaluadas e implementadas ≥ 1/año",
                    "actividades": [
                        {"cod": "A01", "act": "Definición del marco de análisis y criterios de diferenciación", "entregable": "Marco de análisis y criterios de evaluación", "resp": "Directorio/CX", "meses": [7,8]},
                        {"cod": "A02", "act": "Investigación de buenas prácticas y referentes del mercado", "entregable": "Informe de benchmarking y buenas prácticas", "resp": "Directorio/CX", "meses": [7,8]},
                        {"cod": "A03", "act": "Identificación y evaluación de alternativas innovadoras", "entregable": "Matriz de evaluación y priorización", "resp": "Directorio/CX", "meses": [9,10]},
                        {"cod": "A04", "act": "Selección de alternativas a implementar", "entregable": "Alternativas seleccionadas para implementación", "resp": "Directorio/CX", "meses": [11,12]},
                    ]
                },
            ]
        },
        {
            "og": "OG-04",
            "og_desc": "Ordenar la gestión de pagos a proveedores",
            "oes": [
                {
                    "oe": "OE-04.1",
                    "oe_desc": "Estandarizar el proceso de solicitud, validación y aprobación de pagos",
                    "kpi": "% de pagos a proveedores realizados dentro del plazo ≥ 95%",
                    "actividades": [
                        {"cod": "A01", "act": "Levantamiento del proceso actual de pagos a proveedores", "entregable": "Mapa del proceso actual de pagos", "resp": "GIS/Procesos", "meses": [1,2]},
                        {"cod": "A02", "act": "Definición del proceso estándar de gestión de pagos", "entregable": "Proceso de trabajo", "resp": "Directorio/GIS/Procesos", "meses": [3,4,5]},
                        {"cod": "A03", "act": "Estandarización de formatos y documentación", "entregable": "Formatos y checklist de pagos a proveedores", "resp": "GIS", "meses": [3,4,5]},
                        {"cod": "A04", "act": "Definición de tiempos y SLA del proceso", "entregable": "Matriz de tiempos y SLA del proceso de pagos", "resp": "Directorio/GIS/Procesos", "meses": [5]},
                        {"cod": "A05", "act": "Implementación y seguimiento", "entregable": "Proceso implementado y reporte de seguimiento", "resp": "GIS/Procesos", "meses": [5,6,7,8,9,10,11,12]},
                    ]
                },
            ]
        },
        {
            "og": "OG-05",
            "og_desc": "Asegurar la gestión de cobranza del FG de proveedores",
            "oes": [
                {
                    "oe": "OE-05.1",
                    "oe_desc": "Implementar sistema de control y seguimiento del Fondo de Garantía",
                    "kpi": "% de FG registrados y conciliados en matriz de control ≥ 90%",
                    "actividades": [
                        {"cod": "A01", "act": "Diseño de matriz de control", "entregable": "Matriz oficial de control del FG", "resp": "Finanzas", "meses": [3]},
                        {"cod": "A02", "act": "Levantamiento de información (Revisión de contrato y fondos)", "entregable": "Base consolidada de fondos retenidos", "resp": "GIS/Finanzas", "meses": [3,4]},
                        {"cod": "A03", "act": "Integración con Finanzas (conciliación mensual)", "entregable": "Reporte mensual de conciliación del FG", "resp": "GIS/Finanzas", "meses": [4,5,6,7,8,9,10,11,12]},
                        {"cod": "A04", "act": "Implementación y seguimiento", "entregable": "Reporte de seguimiento mensual actualizado", "resp": "GIS/Finanzas", "meses": [5,6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-05.2",
                    "oe_desc": "Asegurar la recuperación o ejecución del FG ante incumplimientos",
                    "kpi": "% de FG ejecutados ante incumplimiento ≥ 90%",
                    "actividades": [
                        {"cod": "A01", "act": "Definir criterios de ejecución", "entregable": "Matriz de causales de ejecución", "resp": "GIS/Constructora", "meses": [3]},
                        {"cod": "A02", "act": "Procedimiento de notificación al proveedor", "entregable": "Formato estándar de notificación", "resp": "GIS/Constructora/Procesos", "meses": [3,4]},
                        {"cod": "A03", "act": "Aplicación del fondo", "entregable": "Registro formal de fondos ejecutados", "resp": "GIS/Finanzas", "meses": [4,5,6,7,8,9,10,11,12]},
                        {"cod": "A04", "act": "Cierre y reporte", "entregable": "Informe trimestral de ejecución del Fondo", "resp": "GIS", "meses": [5,6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-05.3",
                    "oe_desc": "Reducir riesgos financieros asociados a devoluciones indebidas",
                    "kpi": "% de devoluciones realizadas conforme a procedimiento ≥ 90%",
                    "actividades": [
                        {"cod": "A01", "act": "Definir Checklist previo a devolución", "entregable": "Checklist obligatorio previo a devolución", "resp": "GIS/Constructora", "meses": [3]},
                        {"cod": "A02", "act": "Validación interáreas antes de devolución", "entregable": "Acta de autorización de devolución", "resp": "GIS/Constructora/Finanzas", "meses": [3,4,5,6,7,8,9,10,11,12]},
                    ]
                },
            ]
        },
        {
            "og": "OG-06",
            "og_desc": "Brindar servicios de implementación y mantenimiento de Oficinas y Casetas",
            "oes": [
                {
                    "oe": "OE-06.1",
                    "oe_desc": "Garantizar la ejecución del servicio",
                    "kpi": "% Inmuebles implementados dentro del plazo ≥ 95%",
                    "actividades": [
                        {"cod": "A01", "act": "Definir alcance estándar del servicio", "entregable": "Checklist de Alcance", "resp": "GIS/Inmobiliaria", "meses": [2,4]},
                        {"cod": "A02", "act": "Elaborar cronograma (plantilla)", "entregable": "Cronograma", "resp": "GIS", "meses": [2,4]},
                        {"cod": "A03", "act": "Elaborar presupuesto", "entregable": "Presupuesto", "resp": "GIS", "meses": [2,4]},
                        {"cod": "A04", "act": "Validación y Ejecución del servicio", "entregable": "Acta de entrega firmada por el cliente", "resp": "GIS/Inmobiliaria", "meses": [2,3,4,5]},
                    ]
                },
            ]
        },
        {
            "og": "OG-07",
            "og_desc": "Elaborar procesos",
            "oes": [
                {
                    "oe": "OE-07.1",
                    "oe_desc": "Revisión de procesos actuales y optimizarlos",
                    "kpi": "% de procesos críticos optimizados e implementados ≥ 80%",
                    "actividades": [
                        {"cod": "A01", "act": "Identificación y levantamiento de procesos actuales + comparativo", "entregable": "Mapa de procesos actuales", "resp": "GIS/Administración", "meses": [3,4]},
                        {"cod": "A02", "act": "Rev 0 Procesos Postventa", "entregable": "Flujos de procesos postventa", "resp": "Directorio/GIS/Administración", "meses": [4,5]},
                        {"cod": "A03", "act": "Propuesta de optimización de procesos", "entregable": "Procesos optimizados propuestos", "resp": "GIS/Procesos", "meses": [8,9]},
                        {"cod": "A04", "act": "Implementación y seguimiento", "entregable": "Procesos optimizados implementados", "resp": "GIS/Procesos", "meses": [9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-07.2",
                    "oe_desc": "Establecer Manual de funciones de los integrantes del Organigrama",
                    "kpi": "% de puestos con funciones formalizadas y difundidas 100%",
                    "actividades": [
                        {"cod": "A01", "act": "Revisión del organigrama actual", "entregable": "Organigrama validado", "resp": "Directorio", "meses": [8,9]},
                        {"cod": "A02", "act": "Definición de funciones y responsabilidades por puesto", "entregable": "Funciones y responsabilidades por puesto", "resp": "GIS/Procesos", "meses": [9,10]},
                        {"cod": "A03", "act": "Elaboración del manual de funciones", "entregable": "Manual de funciones elaborado", "resp": "GIS/Procesos", "meses": [9,10]},
                        {"cod": "A04", "act": "Validación, aprobación y difusión", "entregable": "Manual de funciones aprobado y difundido", "resp": "Directorio/GIS", "meses": [10,11]},
                    ]
                },
                {
                    "oe": "OE-07.3",
                    "oe_desc": "Elaborar Informes Mensuales y Trimestrales",
                    "kpi": "% de informes entregados en el plazo 100%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición del alcance de los informes", "entregable": "Alcance y estructura de informes", "resp": "Directorio/GIS", "meses": [2]},
                        {"cod": "A02", "act": "Definición de indicadores y fuentes de información", "entregable": "Matriz de indicadores y fuentes", "resp": "Directorio/GIS", "meses": [2]},
                        {"cod": "A03", "act": "Diseño de formatos de informe", "entregable": "Formato estándar de informes", "resp": "GIS", "meses": [2]},
                        {"cod": "A04", "act": "Elaboración y presentación de informes", "entregable": "Informes mensuales y trimestrales elaborados", "resp": "GIS", "meses": [2,3,4,5,6,7,8,9,10,11,12]},
                        {"cod": "A05", "act": "Seguimiento y mejora de los informes", "entregable": "Reportes de informes", "resp": "GIS", "meses": [3,4,5,6,7,8,9,10,11,12]},
                    ]
                },
            ]
        },
    ]
}

# ══════════════════════════════════════════════════════════════════════════════
# DATA - METROPOLITANO (DISEÑO)
# ══════════════════════════════════════════════════════════════════════════════

METRO_DATA = {
    "area": "METROPOLITANO (Diseño)",
    "short": "METRO",
    "objetivos": [
        {
            "og": "OG-01",
            "og_desc": "Asegurar la innovación constante en diseño",
            "oes": [
                {
                    "oe": "OE-01.1",
                    "oe_desc": "Desarrollar propuestas arquitectónicas diferenciadas con cumplimiento normativo",
                    "kpi": "Nº de criterios innovadores incorporados ≥ 2/año",
                    "actividades": [
                        {"cod": "A01", "act": "Monitoreo continuo de tendencias e innovación arquitectónica / Capacitaciones", "entregable": "Registro de tendencias y referentes aplicables", "resp": "CP", "meses": [3,4,7,8,11,12]},
                        {"cod": "A02", "act": "Actualización periódica de normativa aplicable / Capacitaciones", "entregable": "Matriz normativa actualizada (municipal, RNE)", "resp": "CP", "meses": [3,4,7,8,11,12]},
                        {"cod": "A03", "act": "Checklist normativo y de innovación por proyecto", "entregable": "Checklist", "resp": "CP", "meses": [3,4,7,8,11,12]},
                        {"cod": "A04", "act": "Estandarización de criterios innovadores exitosos", "entregable": "Actualización de lineamientos y estándares", "resp": "CP", "meses": [3,4,7,8,11,12]},
                        {"cod": "A05", "act": "Presentación Mensual", "entregable": "Acta de las reuniones", "resp": "CP", "meses": [4,8,12]},
                    ]
                },
                {
                    "oe": "OE-01.2",
                    "oe_desc": "Implementar Proyecto Verde: Edge, Bono verde o LEED",
                    "kpi": "% de proyectos que incorporan certificación verde ≥ 50%",
                    "actividades": [
                        {"cod": "A01", "act": "Evaluación de viabilidad", "entregable": "Informe de viabilidad", "resp": "Directorio/CP", "meses": [3,4]},
                        {"cod": "A02", "act": "Definición de estrategias sostenibles", "entregable": "Matriz de estrategias sostenibles", "resp": "CP", "meses": [3,4]},
                        {"cod": "A03", "act": "Incorporación en el diseño", "entregable": "Expediente con criterios verdes incorporados", "resp": "CP", "meses": [4]},
                        {"cod": "A04", "act": "Validación técnica", "entregable": "Check de cumplimiento empresa certificadora", "resp": "CP", "meses": [4,5,6]},
                    ]
                },
                {
                    "oe": "OE-01.3",
                    "oe_desc": "Uso de IA / VR en diseños",
                    "kpi": "% de proyectos que utilizan IA/VR en al menos una etapa ≥ 50%",
                    "actividades": [
                        {"cod": "A01", "act": "Identificación de herramientas IA/VR", "entregable": "Informe comparativo de herramientas IA/VR", "resp": "CP", "meses": [3,4,10,11]},
                        {"cod": "A02", "act": "Capacitación del equipo", "entregable": "Registro de capacitaciones", "resp": "CP", "meses": [3,4,10,11]},
                        {"cod": "A03", "act": "Aplicación piloto - Expediente comercial", "entregable": "Proyecto piloto con IA/VR aplicada", "resp": "CP", "meses": [3,4,10,11]},
                        {"cod": "A04", "act": "Evaluación y estandarización", "entregable": "Lineamientos de uso de IA/VR en diseño", "resp": "CP", "meses": [4,5,11,12]},
                    ]
                },
            ]
        },
        {
            "og": "OG-02",
            "og_desc": "Mejorar el sistema de trabajo para optimización en tiempo y costos",
            "oes": [
                {
                    "oe": "OE-02.1",
                    "oe_desc": "Establecer indicadores de gestión / Reducir tiempos de entrega ≥ 10%",
                    "kpi": "% de reducción del tiempo de entrega de expedientes ≥ 10%",
                    "actividades": [
                        {"cod": "A01", "act": "Línea base de tiempos por cada actividad", "entregable": "Matriz de tiempos actuales", "resp": "Directorio/CP", "meses": [1,2,3]},
                        {"cod": "A02", "act": "Definición de flujos BIM", "entregable": "Flujo BIM estandarizado", "resp": "CP/Coordinador BIM", "meses": [2,3,4]},
                        {"cod": "A03", "act": "Implementación piloto Armoni 1 / Catalina Living", "entregable": "Expediente técnico bajo flujo BIM", "resp": "CP/Coordinador BIM", "meses": [3,4,5,6,7,8,9]},
                        {"cod": "A04", "act": "Medición de mejora de tiempos", "entregable": "Informe comparativo pre/post BIM", "resp": "CP/Coordinador BIM", "meses": [4,5,6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-02.2",
                    "oe_desc": "Reducir los errores de diseño mediante revisiones colaborativas",
                    "kpi": "% de reducción de observaciones de diseño en obra ≥ 20%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición del proceso de revisión colaborativa", "entregable": "Procedimiento de revisiones colaborativas", "resp": "CP/Procesos", "meses": [1,2,3,4]},
                        {"cod": "A02", "act": "Programación de reuniones semanales interdisciplinarias", "entregable": "Actas de reuniones interdisciplinarias", "resp": "CP", "meses": [1,2,3,4]},
                        {"cod": "A03", "act": "Registro y seguimiento de observaciones", "entregable": "Matriz de observaciones", "resp": "CP", "meses": [3,4,5,6,7,8,9,10,11,12]},
                        {"cod": "A04", "act": "Cierre de observaciones antes de entrega a obra", "entregable": "Expediente compatibilizado", "resp": "CP", "meses": [5,6,9,10]},
                    ]
                },
                {
                    "oe": "OE-02.3",
                    "oe_desc": "Implementar BIM en el 100% de los proyectos el 2026",
                    "kpi": "% de proyectos desarrollados bajo metodología BIM 100%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición del Plan de Implementación BIM", "entregable": "Plan de implementación BIM", "resp": "CP/Coordinador BIM", "meses": [3,4]},
                        {"cod": "A02", "act": "Capacitación del equipo y especialistas", "entregable": "Acta de capacitación al personal", "resp": "CP", "meses": [3,4]},
                        {"cod": "A03", "act": "Ejecución del proyecto piloto (Armoni 1)", "entregable": "Modelo BIM integral", "resp": "CP/Coordinador BIM", "meses": [4,5,6]},
                        {"cod": "A04", "act": "Escalamiento BIM al total de proyectos", "entregable": "Proyectos BIM en ejecución", "resp": "CP/Coordinador BIM", "meses": [5,6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-02.4",
                    "oe_desc": "Uso de gadgets para mejorar procesos de Supervisión y Compatibilización",
                    "kpi": "% de revisiones en campo con soporte digital ≥ 80%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición de requerimientos tecnológicos (tablets, software)", "entregable": "Especificación de equipos", "resp": "CP", "meses": [3,4]},
                        {"cod": "A02", "act": "Adquisición y configuración de equipos", "entregable": "Equipos configurados", "resp": "CP", "meses": [3,4]},
                        {"cod": "A03", "act": "Capacitación del equipo en uso en campo", "entregable": "Registros de capacitación", "resp": "CP", "meses": [4,5]},
                        {"cod": "A04", "act": "Implementación en supervisiones y compatibilización", "entregable": "Reportes de supervisión digital", "resp": "CP", "meses": [5,6,7,8,9,10,11,12]},
                    ]
                },
                {
                    "oe": "OE-02.5",
                    "oe_desc": "Implementar Metrados en el Área",
                    "kpi": "% de proyectos que entregan metrados desde el Área ≥ 80%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición del alcance de metrados", "entregable": "Alcance de metrados", "resp": "CP", "meses": [1,2,3]},
                        {"cod": "A02", "act": "Integración de metrados desde modelos BIM", "entregable": "Metrados desde modelo BIM", "resp": "CP", "meses": [1,2,3,4,5,6,7,8,9,10]},
                        {"cod": "A03", "act": "Entrega estandarizada de metrados por proyecto", "entregable": "Metrados validados por proyecto", "resp": "CP", "meses": [1,2,3,4,5,6,7,8,9,10]},
                    ]
                },
            ]
        },
        {
            "og": "OG-03",
            "og_desc": "Mejorar la Calidad en los proyectos",
            "oes": [
                {
                    "oe": "OE-03.1",
                    "oe_desc": "Asegurar que los proyectos cumplan con Estándares de Calidad",
                    "kpi": "% de proyectos aprobados sin observaciones críticas ≥ 95%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición de estándares de calidad aplicables / Manual de tolerancias", "entregable": "Checklist de calidad", "resp": "CP/Calidad", "meses": [3,4]},
                        {"cod": "A02", "act": "Implementación de revisiones técnicas internas", "entregable": "Actas de reunión", "resp": "CP/Calidad", "meses": [3,4,8,9]},
                        {"cod": "A03", "act": "Validación cruzada Diseño-Calidad-Obra", "entregable": "Actas de validación", "resp": "CP/Calidad/Constructora", "meses": [5,6,10,11]},
                    ]
                },
                {
                    "oe": "OE-03.2",
                    "oe_desc": "Iniciar la elaboración de Manual de Diseño y Especificaciones Técnicas",
                    "kpi": "% de avance del Manual de Diseño 100% elaborado y aprobado",
                    "actividades": [
                        {"cod": "A01", "act": "Recopilación de criterios y especificaciones existentes", "entregable": "Índice de Manual", "resp": "CP", "meses": [8]},
                        {"cod": "A02", "act": "Redacción del Manual de diseño", "entregable": "Borrador de Manual", "resp": "CP", "meses": [8,9,10]},
                        {"cod": "A03", "act": "Revisión y validación interáreas", "entregable": "Actas de reunión", "resp": "CP/Calidad/Inmobiliaria", "meses": [10,11]},
                        {"cod": "A04", "act": "Aprobación y difusión del manual (1era versión)", "entregable": "Manual validado", "resp": "CP/Calidad/Inmobiliaria", "meses": [11,12]},
                    ]
                },
                {
                    "oe": "OE-03.3",
                    "oe_desc": "Medir la satisfacción del cliente (Inmobiliarias)",
                    "kpi": "Índice de satisfacción de las inmobiliarias ≥ 85%",
                    "actividades": [
                        {"cod": "A01", "act": "Definición de criterios de evaluación y encuesta", "entregable": "Modelo de encuesta", "resp": "Directorio/CP", "meses": [8]},
                        {"cod": "A02", "act": "Aplicación de encuestas a inmobiliarias", "entregable": "Resultados de encuesta", "resp": "Directorio/CP", "meses": [8,9,10]},
                        {"cod": "A03", "act": "Análisis de resultados y brechas", "entregable": "Informe de resultados", "resp": "Directorio/CP", "meses": [10,11]},
                        {"cod": "A04", "act": "Implementación de mejoras en diseño", "entregable": "Plan de acción de mejoras", "resp": "CP", "meses": [11,12]},
                    ]
                },
            ]
        },
        {
            "og": "OG-04",
            "og_desc": "Elaborar procesos",
            "oes": [
                {
                    "oe": "OE-04.1",
                    "oe_desc": "Revisión de procesos actuales y optimizarlos con BIM",
                    "kpi": "% de procesos optimizados e implementados con BIM ≥ 80%",
                    "actividades": [
                        {"cod": "A01", "act": "Levantamiento de procesos actuales de Metropolitano", "entregable": "Mapa de procesos", "resp": "CP", "meses": [4,5,6]},
                        {"cod": "A02", "act": "Identificación de oportunidades de mejora con BIM", "entregable": "Procesos BIM", "resp": "CP", "meses": [4,5,6]},
                        {"cod": "A03", "act": "Rediseño y estandarización de procesos", "entregable": "Procesos operativos", "resp": "CP", "meses": [9,10]},
                        {"cod": "A04", "act": "Implementación y seguimiento", "entregable": "Reportes de Informes", "resp": "CP", "meses": [10,11,12]},
                    ]
                },
                {
                    "oe": "OE-04.2",
                    "oe_desc": "Establecer Manual de funciones de los integrantes del Organigrama",
                    "kpi": "% de puestos con funciones formalizadas 100%",
                    "actividades": [
                        {"cod": "A01", "act": "Revisión del organigrama de Metropolitano", "entregable": "Organigrama", "resp": "Directorio/CP", "meses": [7,8]},
                        {"cod": "A02", "act": "Definición de funciones y responsabilidades por puesto", "entregable": "Fichas de puesto", "resp": "Procesos/CP", "meses": [8,9]},
                        {"cod": "A03", "act": "Elaboración del Manual de funciones", "entregable": "Borrador del Manual", "resp": "Procesos/CP", "meses": [9,10]},
                        {"cod": "A04", "act": "Aprobación y difusión del manual", "entregable": "Manual de funciones validado", "resp": "Procesos/CP", "meses": [10,11,12]},
                    ]
                },
            ]
        },
    ]
}

# ══════════════════════════════════════════════════════════════════════════════
# WEEK MAPPING
# ══════════════════════════════════════════════════════════════════════════════
MONTH_NAMES = ["", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
MONTH_FULL = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def get_weeks_2026():
    """Return list of (week_num, start_date, end_date, month) for 2026"""
    weeks = []
    # Start from Jan 5, 2026 (Monday of first full week)
    d = date(2026, 1, 5)
    wk = 1
    while d.year == 2026 or (d.year == 2027 and d.month == 1 and wk <= 52):
        end = d + timedelta(days=4)  # Friday
        month = d.month if d.year == 2026 else 12
        weeks.append((wk, d, end, month))
        d += timedelta(days=7)
        wk += 1
        if wk > 52:
            break
    return weeks

WEEKS = get_weeks_2026()

def month_to_weeks(month_num):
    """Get week indices for a given month"""
    return [i for i, (wk, sd, ed, m) in enumerate(WEEKS) if m == month_num]

def months_to_week_ranges(meses):
    """Get all week indices covered by the given months"""
    wks = []
    for m in meses:
        wks.extend(month_to_weeks(m))
    return sorted(set(wks))

# ══════════════════════════════════════════════════════════════════════════════
# FLATTEN ACTIVITIES
# ══════════════════════════════════════════════════════════════════════════════
def flatten_data(area_data):
    """Flatten the hierarchical data into rows for Lookahead"""
    rows = []
    for og in area_data["objetivos"]:
        rows.append({"type": "og", "code": og["og"], "desc": og["og_desc"], "kpi": "", "resp": "", "meses": [], "entregable": ""})
        for oe in og["oes"]:
            rows.append({"type": "oe", "code": oe["oe"], "desc": oe["oe_desc"], "kpi": oe["kpi"], "resp": "", "meses": [], "entregable": ""})
            for act in oe["actividades"]:
                rows.append({
                    "type": "act",
                    "code": act["cod"],
                    "desc": act["act"],
                    "kpi": "",
                    "resp": act["resp"],
                    "meses": act["meses"],
                    "entregable": act["entregable"],
                    "oe_code": oe["oe"],
                    "og_code": og["og"],
                })
    return rows

def flatten_activities_only(area_data):
    """Flatten to only activities with full context"""
    acts = []
    for og in area_data["objetivos"]:
        for oe in og["oes"]:
            for act in oe["actividades"]:
                acts.append({
                    "og": og["og"],
                    "og_desc": og["og_desc"],
                    "oe": oe["oe"],
                    "oe_desc": oe["oe_desc"],
                    "kpi": oe["kpi"],
                    "cod": act["cod"],
                    "act": act["act"],
                    "entregable": act["entregable"],
                    "resp": act["resp"],
                    "meses": act["meses"],
                })
    return acts


# ══════════════════════════════════════════════════════════════════════════════
# EXCEL GENERATION
# ══════════════════════════════════════════════════════════════════════════════
OUTPUT_FILE = r"c:\Users\Yrving\PLANEAMIENTO_3ERO\Planeamiento_2026_LPS.xlsx"

wb = xlsxwriter.Workbook(OUTPUT_FILE)

# ─── COLORS ──────────────────────────────────────────────────────────────────
C_DARK_BLUE = "#1B2A4A"
C_MED_BLUE = "#2E5090"
C_LIGHT_BLUE = "#4472C4"
C_PALE_BLUE = "#D6E4F0"
C_VERY_PALE = "#EDF2F9"
C_GREEN = "#548235"
C_LIGHT_GREEN = "#C6EFCE"
C_DARK_GREEN = "#006100"
C_RED = "#C00000"
C_LIGHT_RED = "#FFC7CE"
C_DARK_RED = "#9C0006"
C_YELLOW = "#FFD966"
C_LIGHT_YELLOW = "#FFEB9C"
C_ORANGE = "#ED7D31"
C_WHITE = "#FFFFFF"
C_GRAY = "#D9D9D9"
C_DARK_GRAY = "#595959"

# ─── FORMATS ─────────────────────────────────────────────────────────────────
fmt_title = wb.add_format({
    'bold': True, 'font_size': 16, 'font_color': C_WHITE, 'bg_color': C_DARK_BLUE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
})
fmt_subtitle = wb.add_format({
    'bold': True, 'font_size': 11, 'font_color': C_WHITE, 'bg_color': C_MED_BLUE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
})
fmt_header = wb.add_format({
    'bold': True, 'font_size': 10, 'font_color': C_WHITE, 'bg_color': C_LIGHT_BLUE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_header_month = wb.add_format({
    'bold': True, 'font_size': 10, 'font_color': C_WHITE, 'bg_color': C_MED_BLUE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
})
fmt_og = wb.add_format({
    'bold': True, 'font_size': 11, 'font_color': C_WHITE, 'bg_color': C_DARK_BLUE,
    'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_oe = wb.add_format({
    'bold': True, 'font_size': 10, 'font_color': C_WHITE, 'bg_color': C_MED_BLUE,
    'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_oe_kpi = wb.add_format({
    'bold': False, 'font_size': 9, 'font_color': C_WHITE, 'bg_color': C_MED_BLUE,
    'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'italic': True, 'font_name': 'Calibri'
})
fmt_act = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_VERY_PALE,
    'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_act_alt = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_WHITE,
    'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_act_center = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_VERY_PALE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_act_center_alt = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_WHITE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_gantt_planned = wb.add_format({
    'bg_color': C_LIGHT_BLUE, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'font_name': 'Calibri'
})
fmt_gantt_empty = wb.add_format({
    'bg_color': C_WHITE, 'border': 1, 'font_name': 'Calibri'
})
fmt_gantt_empty_alt = wb.add_format({
    'bg_color': C_VERY_PALE, 'border': 1, 'font_name': 'Calibri'
})
fmt_week_header = wb.add_format({
    'bold': True, 'font_size': 8, 'font_color': C_WHITE, 'bg_color': C_LIGHT_BLUE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'rotation': 90, 'font_name': 'Calibri'
})
fmt_pct = wb.add_format({
    'font_size': 11, 'font_color': C_DARK_BLUE, 'bg_color': C_VERY_PALE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': '0%', 'bold': True, 'font_name': 'Calibri'
})
fmt_pct_header = wb.add_format({
    'bold': True, 'font_size': 12, 'font_color': C_WHITE, 'bg_color': C_GREEN,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
})
fmt_pct_good = wb.add_format({
    'font_size': 14, 'font_color': C_DARK_GREEN, 'bg_color': C_LIGHT_GREEN,
    'align': 'center', 'valign': 'vcenter', 'border': 2, 'num_format': '0.0%', 'bold': True, 'font_name': 'Calibri'
})
fmt_pct_bad = wb.add_format({
    'font_size': 14, 'font_color': C_DARK_RED, 'bg_color': C_LIGHT_RED,
    'align': 'center', 'valign': 'vcenter', 'border': 2, 'num_format': '0.0%', 'bold': True, 'font_name': 'Calibri'
})
fmt_cell_normal = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_WHITE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
})
fmt_cell_wrap = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_WHITE,
    'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_cell_wrap_pale = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_VERY_PALE,
    'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_number = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_WHITE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': '0', 'font_name': 'Calibri'
})
fmt_date = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_WHITE,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': 'dd/mm/yyyy', 'font_name': 'Calibri'
})
fmt_ar_header = wb.add_format({
    'bold': True, 'font_size': 10, 'font_color': C_WHITE, 'bg_color': C_RED,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
})
fmt_ar_title = wb.add_format({
    'bold': True, 'font_size': 16, 'font_color': C_WHITE, 'bg_color': C_RED,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
})
fmt_status_complete = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_GREEN, 'bg_color': C_LIGHT_GREEN,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
})
fmt_status_pending = wb.add_format({
    'font_size': 10, 'font_color': '#9C6500', 'bg_color': C_LIGHT_YELLOW,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
})
fmt_border_thin = wb.add_format({'border': 1})
fmt_plan_si = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_GREEN, 'bg_color': C_LIGHT_GREEN,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
})
fmt_plan_no = wb.add_format({
    'font_size': 10, 'font_color': C_DARK_RED, 'bg_color': C_LIGHT_RED,
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
})


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 1: LOOKAHEAD
# ══════════════════════════════════════════════════════════════════════════════

def create_lookahead(area_data, sheet_name):
    ws = wb.add_worksheet(sheet_name)
    ws.hide_gridlines(2)
    ws.set_landscape()
    ws.set_paper(9)  # A4
    ws.set_zoom(70)
    
    # Freeze panes
    ws.freeze_panes(4, 5)
    
    rows_data = flatten_data(area_data)
    
    # Column widths
    ws.set_column(0, 0, 5)    # #
    ws.set_column(1, 1, 8)    # Código
    ws.set_column(2, 2, 45)   # Actividad
    ws.set_column(3, 3, 35)   # Entregable
    ws.set_column(4, 4, 18)   # Responsable
    
    # Week columns
    for i in range(52):
        ws.set_column(5 + i, 5 + i, 3.5)
    
    # TITLE ROW
    ws.merge_range(0, 0, 0, 56, f"LOOKAHEAD ANUAL 2026 - {area_data['area']}", fmt_title)
    ws.set_row(0, 35)
    
    # SUB-TITLE ROW: Area info
    ws.merge_range(1, 0, 1, 4, "PLAN DE TRABAJO 2026 - CRONOGRAMA SEMANAL", fmt_subtitle)
    
    # Month headers
    current_col = 5
    for m in range(1, 13):
        m_weeks = month_to_weeks(m)
        if m_weeks:
            start_col = 5 + m_weeks[0]
            end_col = 5 + m_weeks[-1]
            if start_col == end_col:
                ws.write(1, start_col, MONTH_NAMES[m], fmt_header_month)
            else:
                ws.merge_range(1, start_col, 1, end_col, MONTH_NAMES[m], fmt_header_month)
    ws.set_row(1, 22)
    
    # Week number headers
    ws.write(2, 0, "#", fmt_header)
    ws.write(2, 1, "Código", fmt_header)
    ws.write(2, 2, "Actividad", fmt_header)
    ws.write(2, 3, "Entregable", fmt_header)
    ws.write(2, 4, "Responsable", fmt_header)
    
    for i, (wk, sd, ed, m) in enumerate(WEEKS):
        ws.write(2, 5 + i, f"S{wk}", fmt_week_header)
    
    # Date sub-headers
    ws.write(3, 0, "", fmt_header)
    ws.write(3, 1, "", fmt_header)
    ws.write(3, 2, "", fmt_header)
    ws.write(3, 3, "", fmt_header)
    ws.write(3, 4, "", fmt_header)
    
    for i, (wk, sd, ed, m) in enumerate(WEEKS):
        ws.write(3, 5 + i, sd.strftime("%d/%m"), fmt_week_header)
    ws.set_row(2, 30)
    ws.set_row(3, 35)
    
    # DATA ROWS
    row = 4
    act_counter = 0
    for item in rows_data:
        if item["type"] == "og":
            ws.merge_range(row, 0, row, 4, f'{item["code"]} | {item["desc"]}', fmt_og)
            for c in range(5, 57):
                ws.write(row, c, "", fmt_og)
            ws.set_row(row, 28)
            row += 1
        elif item["type"] == "oe":
            ws.merge_range(row, 0, row, 2, f'{item["code"]} | {item["desc"]}', fmt_oe)
            ws.merge_range(row, 3, row, 4, f'KPI: {item["kpi"]}', fmt_oe_kpi)
            for c in range(5, 57):
                ws.write(row, c, "", fmt_oe)
            ws.set_row(row, 25)
            row += 1
        else:
            act_counter += 1
            alt = act_counter % 2 == 0
            f_text = fmt_act_alt if alt else fmt_act
            f_center = fmt_act_center_alt if alt else fmt_act_center
            f_empty = fmt_gantt_empty_alt if alt else fmt_gantt_empty
            
            ws.write(row, 0, act_counter, f_center)
            ws.write(row, 1, item["code"], f_center)
            ws.write(row, 2, item["desc"], f_text)
            ws.write(row, 3, item["entregable"], f_text)
            ws.write(row, 4, item["resp"], f_center)
            
            # Gantt bars
            planned_weeks = months_to_week_ranges(item["meses"])
            for i in range(52):
                if i in planned_weeks:
                    ws.write(row, 5 + i, "■", fmt_gantt_planned)
                else:
                    ws.write(row, 5 + i, "", f_empty)
            ws.set_row(row, 22)
            row += 1
    
    # Legend
    row += 1
    ws.write(row, 1, "Leyenda:", fmt_og)
    ws.write(row, 2, "", fmt_og)
    row += 1
    ws.write(row, 1, "■", fmt_gantt_planned)
    ws.write(row, 2, "Actividad Planificada", fmt_act)
    
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 2: PLAN MENSUAL
# ══════════════════════════════════════════════════════════════════════════════

def create_plan_mensual(area_data, sheet_name):
    ws = wb.add_worksheet(sheet_name)
    ws.hide_gridlines(2)
    ws.set_landscape()
    ws.set_zoom(80)
    ws.freeze_panes(4, 6)
    
    acts = flatten_activities_only(area_data)
    
    # Column widths
    ws.set_column(0, 0, 4)    # #
    ws.set_column(1, 1, 10)   # OE
    ws.set_column(2, 2, 8)    # Código
    ws.set_column(3, 3, 42)   # Actividad
    ws.set_column(4, 4, 30)   # Entregable
    ws.set_column(5, 5, 15)   # Responsable
    
    # Month columns (each month: Planificado, Estado, % Avance)
    col = 6
    for m in range(1, 13):
        ws.set_column(col, col, 11)      # Planificado
        ws.set_column(col + 1, col + 1, 12)  # Estado
        ws.set_column(col + 2, col + 2, 10)  # % Avance
        col += 3
    
    # TITLE
    ws.merge_range(0, 0, 0, 5 + 36, f"PLAN MENSUAL 2026 - {area_data['area']}", fmt_title)
    ws.set_row(0, 35)
    
    # Month group headers
    col = 6
    for m in range(1, 13):
        ws.merge_range(1, col, 1, col + 2, MONTH_FULL[m], fmt_header_month)
        col += 3
    ws.set_row(1, 22)
    
    # Sub-headers
    ws.write(2, 0, "#", fmt_header)
    ws.write(2, 1, "OE", fmt_header)
    ws.write(2, 2, "Código", fmt_header)
    ws.write(2, 3, "Actividad", fmt_header)
    ws.write(2, 4, "Entregable", fmt_header)
    ws.write(2, 5, "Responsable", fmt_header)
    
    col = 6
    for m in range(1, 13):
        ws.write(2, col, "Planif.", fmt_header)
        ws.write(2, col + 1, "Estado", fmt_header)
        ws.write(2, col + 2, "% Avance", fmt_header)
        col += 3
    ws.set_row(2, 20)
    
    # Sub-sub-headers (instructions)
    ws.write(3, 0, "", fmt_header)
    ws.write(3, 1, "", fmt_header)
    ws.write(3, 2, "", fmt_header)
    ws.write(3, 3, "", fmt_header)
    ws.write(3, 4, "", fmt_header)
    ws.write(3, 5, "", fmt_header)
    col = 6
    for m in range(1, 13):
        ws.write(3, col, "Auto", fmt_header)
        ws.write(3, col + 1, "Seleccionar", fmt_header)
        ws.write(3, col + 2, "Ingresar", fmt_header)
        col += 3
    ws.set_row(3, 16)
    
    # DATA ROWS
    row = 4
    for idx, act in enumerate(acts):
        alt = idx % 2 == 0
        f_text = fmt_cell_wrap_pale if alt else fmt_cell_wrap
        f_center = fmt_act_center if alt else fmt_act_center_alt
        
        ws.write(row, 0, idx + 1, f_center)
        ws.write(row, 1, act["oe"], f_center)
        ws.write(row, 2, act["cod"], f_center)
        ws.write(row, 3, act["act"], f_text)
        ws.write(row, 4, act["entregable"], f_text)
        ws.write(row, 5, act["resp"], f_center)
        
        col = 6
        for m in range(1, 13):
            if m in act["meses"]:
                ws.write(row, col, "✓", fmt_plan_si)
            else:
                ws.write(row, col, "-", fmt_gantt_empty if not alt else fmt_gantt_empty_alt)
            
            # Estado dropdown
            ws.data_validation(row, col + 1, row, col + 1, {
                'validate': 'list',
                'source': ['No Iniciado', 'En Proceso', 'Completado', 'Retrasado', 'N/A'],
                'error_message': 'Seleccione un estado válido',
            })
            if m in act["meses"]:
                ws.write(row, col + 1, "No Iniciado", fmt_cell_normal)
            else:
                ws.write(row, col + 1, "N/A", fmt_cell_normal)
            
            # % Avance
            if m in act["meses"]:
                ws.write(row, col + 2, 0, wb.add_format({
                    'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_WHITE if not alt else C_VERY_PALE,
                    'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': '0%', 'font_name': 'Calibri'
                }))
            else:
                ws.write(row, col + 2, "", fmt_gantt_empty if not alt else fmt_gantt_empty_alt)
            col += 3
        
        ws.set_row(row, 28)
        row += 1
    
    # Conditional formatting for Estado columns
    for m in range(1, 13):
        state_col = 6 + (m - 1) * 3 + 1
        ws.conditional_format(4, state_col, 4 + len(acts) - 1, state_col, {
            'type': 'text', 'criteria': 'containing', 'value': 'Completado',
            'format': fmt_status_complete
        })
        ws.conditional_format(4, state_col, 4 + len(acts) - 1, state_col, {
            'type': 'text', 'criteria': 'containing', 'value': 'Retrasado',
            'format': wb.add_format({
                'font_size': 10, 'font_color': C_DARK_RED, 'bg_color': C_LIGHT_RED,
                'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
            })
        })
        ws.conditional_format(4, state_col, 4 + len(acts) - 1, state_col, {
            'type': 'text', 'criteria': 'containing', 'value': 'En Proceso',
            'format': wb.add_format({
                'font_size': 10, 'font_color': '#9C6500', 'bg_color': C_LIGHT_YELLOW,
                'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
            })
        })
    
    # SUMMARY section at bottom
    summ_row = row + 2
    ws.merge_range(summ_row, 0, summ_row, 5, "RESUMEN MENSUAL - % AVANCE PROMEDIO", fmt_pct_header)
    col = 6
    for m in range(1, 13):
        ws.merge_range(summ_row, col, summ_row, col + 2, MONTH_NAMES[m], fmt_header_month)
        col += 3
    
    summ_row += 1
    ws.merge_range(summ_row, 0, summ_row, 5, "% Avance Promedio (actividades del mes)", wb.add_format({
        'bold': True, 'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_PALE_BLUE,
        'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
    }))
    
    col = 6
    for m in range(1, 13):
        # Count activities for this month
        month_acts = [i for i, a in enumerate(acts) if m in a["meses"]]
        if month_acts:
            # AVERAGEIF based on avance column
            avance_col_letter = xlsxwriter.utility.xl_col_to_name(col + 2)
            plan_col_letter = xlsxwriter.utility.xl_col_to_name(col)
            first_data_row = 5  # row 4 + 1 (1-indexed)
            last_data_row = 4 + len(acts)
            formula = f'=AVERAGEIF({plan_col_letter}{first_data_row}:{plan_col_letter}{last_data_row},"✓",{avance_col_letter}{first_data_row}:{avance_col_letter}{last_data_row})'
            ws.merge_range(summ_row, col, summ_row, col + 2, "", fmt_pct)
            ws.write_formula(summ_row, col, formula, fmt_pct)
        else:
            ws.merge_range(summ_row, col, summ_row, col + 2, "N/A", fmt_cell_normal)
        col += 3
    ws.set_row(summ_row, 30)
    
    # Chart: Monthly progress
    chart_row = summ_row + 3
    chart = wb.add_chart({'type': 'column'})
    chart.set_title({'name': f'Avance Mensual - {area_data["area"]}'})
    chart.set_style(10)
    chart.set_size({'width': 900, 'height': 400})
    
    # We'll reference the summary row for chart data
    # Categories: month names
    # Values: the averaged percentages
    chart.add_series({
        'name': '% Avance',
        'categories': [sheet_name, summ_row - 1, 6, summ_row - 1, 6 + 33],  # month headers
        'values': [sheet_name, summ_row, 6, summ_row, 6 + 33],
        'fill': {'color': C_LIGHT_BLUE},
        'gap': 80,
    })
    chart.set_y_axis({'name': '% Avance', 'min': 0, 'max': 1, 'num_format': '0%'})
    chart.set_x_axis({'name': 'Mes'})
    chart.set_legend({'position': 'bottom'})
    
    ws.insert_chart(chart_row, 1, chart)
    
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 3: PPC (Porcentaje de Plan Cumplido)
# ══════════════════════════════════════════════════════════════════════════════

def create_ppc(area_data, sheet_name):
    ws = wb.add_worksheet(sheet_name)
    ws.hide_gridlines(2)
    ws.set_landscape()
    ws.set_zoom(75)
    ws.freeze_panes(5, 5)
    
    acts = flatten_activities_only(area_data)
    
    # Column widths
    ws.set_column(0, 0, 4)    # #
    ws.set_column(1, 1, 10)   # OE
    ws.set_column(2, 2, 8)    # Código
    ws.set_column(3, 3, 40)   # Actividad
    ws.set_column(4, 4, 15)   # Responsable
    
    # For each month: 4 week columns with "Planif" + "Ejec" (8 cols per month)
    # But let's simplify: for each month just 4 weeks, each week has Plan/Real
    # That's too many columns. Let's do month-based instead.
    
    # Simplified approach: Track by month
    # Columns per month: Planificado(auto) | Comprometido(user) | Ejecutado(user)
    col_start = 5
    for m in range(1, 13):
        ws.set_column(col_start, col_start, 8)      # Plan
        ws.set_column(col_start + 1, col_start + 1, 10)  # Comprometido
        ws.set_column(col_start + 2, col_start + 2, 10)  # Ejecutado
        col_start += 3
    
    # TITLE
    total_cols = 5 + 36
    ws.merge_range(0, 0, 0, total_cols - 1, f"PPC - PORCENTAJE DE PLAN CUMPLIDO 2026 - {area_data['area']}", wb.add_format({
        'bold': True, 'font_size': 16, 'font_color': C_WHITE, 'bg_color': C_GREEN,
        'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
    }))
    ws.set_row(0, 35)
    
    # Subtitle
    ws.merge_range(1, 0, 1, 4, "Seguimiento de compromisos planificados vs ejecutados", wb.add_format({
        'bold': True, 'font_size': 11, 'font_color': C_WHITE, 'bg_color': C_GREEN,
        'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
    }))
    
    # Month group headers
    col = 5
    for m in range(1, 13):
        ws.merge_range(1, col, 1, col + 2, MONTH_FULL[m], fmt_header_month)
        col += 3
    ws.set_row(1, 22)
    
    # Headers row 2
    ws.write(2, 0, "#", fmt_header)
    ws.write(2, 1, "OE", fmt_header)
    ws.write(2, 2, "Código", fmt_header)
    ws.write(2, 3, "Actividad", fmt_header)
    ws.write(2, 4, "Responsable", fmt_header)
    
    col = 5
    for m in range(1, 13):
        ws.write(2, col, "Plan", fmt_header)
        ws.write(2, col + 1, "Compr.", wb.add_format({
            'bold': True, 'font_size': 10, 'font_color': C_WHITE, 'bg_color': C_ORANGE,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
        }))
        ws.write(2, col + 2, "Ejec.", wb.add_format({
            'bold': True, 'font_size': 10, 'font_color': C_WHITE, 'bg_color': C_GREEN,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
        }))
        col += 3
    ws.set_row(2, 20)
    
    # Row 3: instructions
    ws.write(3, 0, "", fmt_header)
    ws.write(3, 1, "", fmt_header)
    ws.write(3, 2, "", fmt_header)
    ws.write(3, 3, "", fmt_header)
    ws.write(3, 4, "", fmt_header)
    col = 5
    for m in range(1, 13):
        ws.write(3, col, "Auto", wb.add_format({
            'bold': True, 'font_size': 8, 'font_color': C_DARK_GRAY, 'bg_color': C_GRAY,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'italic': True, 'font_name': 'Calibri'
        }))
        ws.write(3, col + 1, "Sí / No", wb.add_format({
            'bold': True, 'font_size': 8, 'font_color': C_DARK_GRAY, 'bg_color': C_GRAY,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'italic': True, 'font_name': 'Calibri'
        }))
        ws.write(3, col + 2, "Sí / No", wb.add_format({
            'bold': True, 'font_size': 8, 'font_color': C_DARK_GRAY, 'bg_color': C_GRAY,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'italic': True, 'font_name': 'Calibri'
        }))
        col += 3
    ws.set_row(3, 15)
    
    # Instruction row
    ws.merge_range(4, 0, 4, 4, "→ Marcar 'Sí' en Comprometido si se compromete a ejecutar. Marcar 'Sí' en Ejecutado si se completó.", wb.add_format({
        'font_size': 9, 'font_color': C_DARK_GRAY, 'bg_color': C_LIGHT_YELLOW,
        'align': 'left', 'valign': 'vcenter', 'border': 1, 'italic': True, 'text_wrap': True, 'font_name': 'Calibri'
    }))
    col = 5
    for m in range(1, 13):
        ws.write(4, col, "", wb.add_format({'bg_color': C_LIGHT_YELLOW, 'border': 1}))
        ws.write(4, col + 1, "", wb.add_format({'bg_color': C_LIGHT_YELLOW, 'border': 1}))
        ws.write(4, col + 2, "", wb.add_format({'bg_color': C_LIGHT_YELLOW, 'border': 1}))
        col += 3
    ws.set_row(4, 20)
    
    # DATA ROWS
    data_start_row = 5
    row = data_start_row
    for idx, act in enumerate(acts):
        alt = idx % 2 == 0
        f_text = fmt_cell_wrap_pale if alt else fmt_cell_wrap
        f_center = fmt_act_center if alt else fmt_act_center_alt
        f_empty = fmt_gantt_empty_alt if alt else fmt_gantt_empty
        
        ws.write(row, 0, idx + 1, f_center)
        ws.write(row, 1, act["oe"], f_center)
        ws.write(row, 2, act["cod"], f_center)
        ws.write(row, 3, act["act"], f_text)
        ws.write(row, 4, act["resp"], f_center)
        
        col = 5
        for m in range(1, 13):
            if m in act["meses"]:
                ws.write(row, col, "✓", fmt_plan_si)
                # Comprometido dropdown
                ws.data_validation(row, col + 1, row, col + 1, {
                    'validate': 'list',
                    'source': ['Sí', 'No'],
                })
                ws.write(row, col + 1, "", fmt_cell_normal)
                # Ejecutado dropdown
                ws.data_validation(row, col + 2, row, col + 2, {
                    'validate': 'list',
                    'source': ['Sí', 'No'],
                })
                ws.write(row, col + 2, "", fmt_cell_normal)
            else:
                ws.write(row, col, "-", f_empty)
                ws.write(row, col + 1, "", f_empty)
                ws.write(row, col + 2, "", f_empty)
            col += 3
        
        ws.set_row(row, 25)
        row += 1
    
    # Conditional formatting for Comprometido and Ejecutado
    for m in range(1, 13):
        compr_col = 5 + (m - 1) * 3 + 1
        ejec_col = 5 + (m - 1) * 3 + 2
        for c in [compr_col, ejec_col]:
            ws.conditional_format(data_start_row, c, data_start_row + len(acts) - 1, c, {
                'type': 'text', 'criteria': 'containing', 'value': 'Sí',
                'format': fmt_plan_si
            })
            ws.conditional_format(data_start_row, c, data_start_row + len(acts) - 1, c, {
                'type': 'text', 'criteria': 'containing', 'value': 'No',
                'format': fmt_plan_no
            })
    
    # ── PPC SUMMARY ──────────────────────────────────────────────────────
    summ_row = row + 2
    ws.merge_range(summ_row, 0, summ_row, 4, "PPC - RESUMEN MENSUAL", wb.add_format({
        'bold': True, 'font_size': 14, 'font_color': C_WHITE, 'bg_color': C_GREEN,
        'align': 'center', 'valign': 'vcenter', 'border': 2, 'font_name': 'Calibri'
    }))
    col = 5
    for m in range(1, 13):
        ws.merge_range(summ_row, col, summ_row, col + 2, MONTH_NAMES[m], fmt_header_month)
        col += 3
    ws.set_row(summ_row, 30)
    
    # Row: Total Comprometidas
    summ_row += 1
    ws.merge_range(summ_row, 0, summ_row, 4, "Total Actividades Comprometidas", wb.add_format({
        'bold': True, 'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': C_PALE_BLUE,
        'align': 'right', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
    }))
    col = 5
    for m in range(1, 13):
        compr_col_letter = xlsxwriter.utility.xl_col_to_name(col + 1)
        r1 = data_start_row + 1
        r2 = data_start_row + len(acts)
        formula = f'=COUNTIF({compr_col_letter}{r1}:{compr_col_letter}{r2},"Sí")'
        ws.merge_range(summ_row, col, summ_row, col + 2, "", fmt_number)
        ws.write_formula(summ_row, col, formula, fmt_number)
        col += 3
    
    # Row: Total Ejecutadas
    summ_row += 1
    ws.merge_range(summ_row, 0, summ_row, 4, "Total Actividades Ejecutadas", wb.add_format({
        'bold': True, 'font_size': 10, 'font_color': C_DARK_GREEN, 'bg_color': C_LIGHT_GREEN,
        'align': 'right', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
    }))
    col = 5
    for m in range(1, 13):
        ejec_col_letter = xlsxwriter.utility.xl_col_to_name(col + 2)
        r1 = data_start_row + 1
        r2 = data_start_row + len(acts)
        formula = f'=COUNTIF({ejec_col_letter}{r1}:{ejec_col_letter}{r2},"Sí")'
        ws.merge_range(summ_row, col, summ_row, col + 2, "", fmt_number)
        ws.write_formula(summ_row, col, formula, fmt_number)
        col += 3
    
    # Row: PPC %
    summ_row += 1
    ws.merge_range(summ_row, 0, summ_row, 4, "PPC (% Plan Cumplido) = Ejecutadas / Comprometidas", wb.add_format({
        'bold': True, 'font_size': 12, 'font_color': C_WHITE, 'bg_color': C_DARK_BLUE,
        'align': 'center', 'valign': 'vcenter', 'border': 2, 'font_name': 'Calibri'
    }))
    col = 5
    compr_summ_row = summ_row - 2  # 1-indexed: summ_row - 1
    ejec_summ_row = summ_row - 1
    for m in range(1, 13):
        # Use column letter of merged cell (col)
        col_letter = xlsxwriter.utility.xl_col_to_name(col)
        cr = compr_summ_row + 1  # 1-based
        er = ejec_summ_row + 1
        formula = f'=IFERROR({col_letter}{er}/{col_letter}{cr},0)'
        ws.merge_range(summ_row, col, summ_row, col + 2, "", fmt_pct)
        ws.write_formula(summ_row, col, formula, fmt_pct)
        col += 3
    ws.set_row(summ_row, 35)
    
    # Conditional formatting for PPC row
    col = 5
    for m in range(1, 13):
        ws.conditional_format(summ_row, col, summ_row, col, {
            'type': 'cell', 'criteria': '>=', 'value': 0.8,
            'format': fmt_pct_good
        })
        ws.conditional_format(summ_row, col, summ_row, col, {
            'type': 'cell', 'criteria': '<', 'value': 0.8,
            'format': fmt_pct_bad
        })
        col += 3
    
    # ── PPC CHART ────────────────────────────────────────────────────────
    chart_row = summ_row + 3
    
    chart = wb.add_chart({'type': 'column'})
    chart.set_title({'name': f'PPC Mensual - {area_data["area"]}'})
    chart.set_style(10)
    chart.set_size({'width': 900, 'height': 420})
    
    # Comprometidas series
    chart.add_series({
        'name': 'Comprometidas',
        'categories': [sheet_name, summ_row - 3, 5, summ_row - 3, 5 + 33],
        'values': [sheet_name, summ_row - 2, 5, summ_row - 2, 5 + 33],
        'fill': {'color': C_ORANGE},
        'gap': 60,
    })
    
    # Ejecutadas series
    chart.add_series({
        'name': 'Ejecutadas',
        'values': [sheet_name, summ_row - 1, 5, summ_row - 1, 5 + 33],
        'fill': {'color': C_GREEN},
    })
    
    chart.set_y_axis({'name': 'Cantidad de Actividades'})
    chart.set_x_axis({'name': 'Mes'})
    chart.set_legend({'position': 'bottom'})
    
    ws.insert_chart(chart_row, 1, chart)
    
    # PPC Line Chart
    chart2 = wb.add_chart({'type': 'line'})
    chart2.set_title({'name': f'Tendencia PPC - {area_data["area"]}'})
    chart2.set_style(10)
    chart2.set_size({'width': 900, 'height': 400})
    
    chart2.add_series({
        'name': 'PPC %',
        'categories': [sheet_name, summ_row - 3, 5, summ_row - 3, 5 + 33],
        'values': [sheet_name, summ_row, 5, summ_row, 5 + 33],
        'line': {'color': C_DARK_BLUE, 'width': 3},
        'marker': {'type': 'circle', 'size': 8, 'fill': {'color': C_LIGHT_BLUE}, 'border': {'color': C_DARK_BLUE}},
    })
    
    # Add target line at 80%
    chart2.add_series({
        'name': 'Meta (80%)',
        'categories': [sheet_name, summ_row - 3, 5, summ_row - 3, 5 + 33],
        'values': [sheet_name, summ_row, 5, summ_row, 5 + 33],  # placeholder
        'line': {'color': C_RED, 'width': 2, 'dash_type': 'dash'},
    })
    
    chart2.set_y_axis({'name': 'PPC %', 'min': 0, 'max': 1, 'num_format': '0%'})
    chart2.set_x_axis({'name': 'Mes'})
    chart2.set_legend({'position': 'bottom'})
    
    ws.insert_chart(chart_row + 22, 1, chart2)
    
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 4: AR (Análisis de Restricciones)
# ══════════════════════════════════════════════════════════════════════════════

def create_ar(area_data, sheet_name):
    ws = wb.add_worksheet(sheet_name)
    ws.hide_gridlines(2)
    ws.set_landscape()
    ws.set_zoom(85)
    ws.freeze_panes(4, 0)
    
    # Column widths
    ws.set_column(0, 0, 5)    # #
    ws.set_column(1, 1, 10)   # OE
    ws.set_column(2, 2, 8)    # Código Act.
    ws.set_column(3, 3, 35)   # Actividad
    ws.set_column(4, 4, 35)   # Descripción de Restricción
    ws.set_column(5, 5, 14)   # Tipo de Restricción
    ws.set_column(6, 6, 14)   # Responsable
    ws.set_column(7, 7, 13)   # Fecha Identificación
    ws.set_column(8, 8, 13)   # Fecha Requerida
    ws.set_column(9, 9, 13)   # Fecha Levantamiento
    ws.set_column(10, 10, 12) # Estado
    ws.set_column(11, 11, 12) # Impacto
    ws.set_column(12, 12, 30) # Acción de Mitigación
    ws.set_column(13, 13, 25) # Observaciones
    
    # TITLE
    ws.merge_range(0, 0, 0, 13, f"ANÁLISIS DE RESTRICCIONES 2026 - {area_data['area']}", fmt_ar_title)
    ws.set_row(0, 38)
    
    # Subtitle / description
    ws.merge_range(1, 0, 1, 13, 
        "Registre las restricciones que impiden o podrían impedir el cumplimiento del plan. Actualice el estado periódicamente.",
        wb.add_format({
            'font_size': 10, 'font_color': C_DARK_GRAY, 'bg_color': C_LIGHT_YELLOW,
            'align': 'left', 'valign': 'vcenter', 'border': 1, 'italic': True, 'text_wrap': True, 'font_name': 'Calibri'
        })
    )
    ws.set_row(1, 28)
    
    # Instructions row
    ws.merge_range(2, 0, 2, 13,
        "Tipos: Información | Recurso | Equipos | Diseño | Materiales | Aprobación | Legal | Financiero | Otro  |  Estados: Pendiente | En Gestión | Levantada | Vencida  |  Impacto: Bajo | Medio | Alto | Crítico",
        wb.add_format({
            'font_size': 9, 'font_color': C_DARK_BLUE, 'bg_color': C_PALE_BLUE,
            'align': 'left', 'valign': 'vcenter', 'border': 1, 'italic': True, 'text_wrap': True, 'font_name': 'Calibri'
        })
    )
    ws.set_row(2, 22)
    
    # HEADERS
    headers_ar = [
        "#", "OE", "Cód. Act.", "Actividad Asociada", "Descripción de la Restricción",
        "Tipo", "Responsable", "Fecha Identif.", "Fecha Requerida", "Fecha Levant.",
        "Estado", "Impacto", "Acción de Mitigación", "Observaciones"
    ]
    for c, h in enumerate(headers_ar):
        ws.write(3, c, h, fmt_ar_header)
    ws.set_row(3, 35)
    
    # Pre-fill rows with data validation (50 rows for user to fill)
    acts = flatten_activities_only(area_data)
    
    # Create a list of activity references for dropdown
    act_list = [f"{a['oe']}-{a['cod']}: {a['act'][:50]}" for a in acts]
    oe_list = list(set([a['oe'] for a in acts]))
    oe_list.sort()
    
    NUM_AR_ROWS = 60  # Pre-format 60 empty rows
    
    for r in range(NUM_AR_ROWS):
        row = 4 + r
        alt = r % 2 == 0
        bg = C_WHITE if alt else C_VERY_PALE
        
        f_normal = wb.add_format({
            'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': bg,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
        })
        f_wrap = wb.add_format({
            'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': bg,
            'align': 'left', 'valign': 'vcenter', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
        })
        f_date_r = wb.add_format({
            'font_size': 10, 'font_color': C_DARK_BLUE, 'bg_color': bg,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': 'dd/mm/yyyy', 'font_name': 'Calibri'
        })
        
        ws.write(row, 0, r + 1, f_normal)       # #
        
        # OE dropdown
        ws.data_validation(row, 1, row, 1, {
            'validate': 'list', 'source': oe_list,
        })
        ws.write(row, 1, "", f_normal)
        
        ws.write(row, 2, "", f_normal)           # Código Act.
        ws.write(row, 3, "", f_wrap)             # Actividad
        ws.write(row, 4, "", f_wrap)             # Descripción Restricción
        
        # Tipo dropdown
        ws.data_validation(row, 5, row, 5, {
            'validate': 'list',
            'source': ['Información', 'Recurso', 'Equipos', 'Diseño', 'Materiales', 'Aprobación', 'Legal', 'Financiero', 'Otro'],
        })
        ws.write(row, 5, "", f_normal)
        
        ws.write(row, 6, "", f_normal)           # Responsable
        ws.write(row, 7, "", f_date_r)          # Fecha Identificación
        ws.write(row, 8, "", f_date_r)          # Fecha Requerida
        ws.write(row, 9, "", f_date_r)          # Fecha Levantamiento
        
        # Estado dropdown
        ws.data_validation(row, 10, row, 10, {
            'validate': 'list',
            'source': ['Pendiente', 'En Gestión', 'Levantada', 'Vencida'],
        })
        ws.write(row, 10, "", f_normal)
        
        # Impacto dropdown
        ws.data_validation(row, 11, row, 11, {
            'validate': 'list',
            'source': ['Bajo', 'Medio', 'Alto', 'Crítico'],
        })
        ws.write(row, 11, "", f_normal)
        
        ws.write(row, 12, "", f_wrap)            # Acción
        ws.write(row, 13, "", f_wrap)            # Observaciones
        
        ws.set_row(row, 25)
    
    # Conditional formatting for Estado
    ws.conditional_format(4, 10, 4 + NUM_AR_ROWS - 1, 10, {
        'type': 'text', 'criteria': 'containing', 'value': 'Levantada',
        'format': fmt_status_complete
    })
    ws.conditional_format(4, 10, 4 + NUM_AR_ROWS - 1, 10, {
        'type': 'text', 'criteria': 'containing', 'value': 'Pendiente',
        'format': wb.add_format({
            'font_size': 10, 'font_color': '#9C6500', 'bg_color': C_LIGHT_YELLOW,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
        })
    })
    ws.conditional_format(4, 10, 4 + NUM_AR_ROWS - 1, 10, {
        'type': 'text', 'criteria': 'containing', 'value': 'Vencida',
        'format': wb.add_format({
            'font_size': 10, 'font_color': C_DARK_RED, 'bg_color': C_LIGHT_RED,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
        })
    })
    ws.conditional_format(4, 10, 4 + NUM_AR_ROWS - 1, 10, {
        'type': 'text', 'criteria': 'containing', 'value': 'En Gestión',
        'format': wb.add_format({
            'font_size': 10, 'font_color': C_WHITE, 'bg_color': C_ORANGE,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
        })
    })
    
    # Conditional formatting for Impacto
    ws.conditional_format(4, 11, 4 + NUM_AR_ROWS - 1, 11, {
        'type': 'text', 'criteria': 'containing', 'value': 'Crítico',
        'format': wb.add_format({
            'font_size': 10, 'font_color': C_WHITE, 'bg_color': C_RED,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
        })
    })
    ws.conditional_format(4, 11, 4 + NUM_AR_ROWS - 1, 11, {
        'type': 'text', 'criteria': 'containing', 'value': 'Alto',
        'format': wb.add_format({
            'font_size': 10, 'font_color': C_DARK_RED, 'bg_color': C_LIGHT_RED,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
        })
    })
    ws.conditional_format(4, 11, 4 + NUM_AR_ROWS - 1, 11, {
        'type': 'text', 'criteria': 'containing', 'value': 'Medio',
        'format': wb.add_format({
            'font_size': 10, 'font_color': '#9C6500', 'bg_color': C_LIGHT_YELLOW,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
        })
    })
    ws.conditional_format(4, 11, 4 + NUM_AR_ROWS - 1, 11, {
        'type': 'text', 'criteria': 'containing', 'value': 'Bajo',
        'format': wb.add_format({
            'font_size': 10, 'font_color': C_DARK_GREEN, 'bg_color': C_LIGHT_GREEN,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'bold': True, 'font_name': 'Calibri'
        })
    })
    
    # ── AR SUMMARY SECTION ───────────────────────────────────────────────
    summ_start = 4 + NUM_AR_ROWS + 2
    
    ws.merge_range(summ_start, 0, summ_start, 5, "RESUMEN DE RESTRICCIONES", wb.add_format({
        'bold': True, 'font_size': 14, 'font_color': C_WHITE, 'bg_color': C_RED,
        'align': 'center', 'valign': 'vcenter', 'border': 2, 'font_name': 'Calibri'
    }))
    ws.set_row(summ_start, 30)
    
    labels = ["Pendientes", "En Gestión", "Levantadas", "Vencidas", "TOTAL"]
    values_formulas = [
        f'=COUNTIF(K5:K{4+NUM_AR_ROWS},"Pendiente")',
        f'=COUNTIF(K5:K{4+NUM_AR_ROWS},"En Gestión")',
        f'=COUNTIF(K5:K{4+NUM_AR_ROWS},"Levantada")',
        f'=COUNTIF(K5:K{4+NUM_AR_ROWS},"Vencida")',
        f'=COUNTA(K5:K{4+NUM_AR_ROWS})-COUNTBLANK(K5:K{4+NUM_AR_ROWS})',
    ]
    colors = [C_YELLOW, C_ORANGE, C_GREEN, C_RED, C_DARK_BLUE]
    font_colors = [C_DARK_BLUE, C_WHITE, C_WHITE, C_WHITE, C_WHITE]
    
    for i, (lbl, fml, bg, fc) in enumerate(zip(labels, values_formulas, colors, font_colors)):
        r = summ_start + 1 + i
        ws.merge_range(r, 0, r, 2, lbl, wb.add_format({
            'bold': True, 'font_size': 11, 'font_color': fc, 'bg_color': bg,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
        }))
        ws.merge_range(r, 3, r, 5, "", wb.add_format({
            'bold': True, 'font_size': 14, 'font_color': fc, 'bg_color': bg,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': '0', 'font_name': 'Calibri'
        }))
        ws.write_formula(r, 3, fml, wb.add_format({
            'bold': True, 'font_size': 14, 'font_color': fc, 'bg_color': bg,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': '0', 'font_name': 'Calibri'
        }))
        ws.set_row(r, 28)
    
    # Donut chart for restrictions by state
    chart = wb.add_chart({'type': 'doughnut'})
    chart.set_title({'name': 'Estado de Restricciones'})
    chart.set_style(10)
    chart.set_size({'width': 450, 'height': 350})
    
    chart.add_series({
        'name': 'Restricciones',
        'categories': [sheet_name, summ_start + 1, 0, summ_start + 4, 0],
        'values': [sheet_name, summ_start + 1, 3, summ_start + 4, 3],
        'points': [
            {'fill': {'color': C_YELLOW}},
            {'fill': {'color': C_ORANGE}},
            {'fill': {'color': C_GREEN}},
            {'fill': {'color': C_RED}},
        ],
        'data_labels': {'percentage': True, 'category': True, 'separator': '\n', 'font': {'size': 9}},
    })
    chart.set_legend({'position': 'bottom'})
    
    ws.insert_chart(summ_start, 7, chart)
    
    # Pie chart by impact
    summ2_start = summ_start + 7
    ws.merge_range(summ2_start, 0, summ2_start, 5, "RESUMEN POR IMPACTO", wb.add_format({
        'bold': True, 'font_size': 12, 'font_color': C_WHITE, 'bg_color': C_DARK_BLUE,
        'align': 'center', 'valign': 'vcenter', 'border': 2, 'font_name': 'Calibri'
    }))
    
    imp_labels = ["Bajo", "Medio", "Alto", "Crítico"]
    imp_formulas = [
        f'=COUNTIF(L5:L{4+NUM_AR_ROWS},"Bajo")',
        f'=COUNTIF(L5:L{4+NUM_AR_ROWS},"Medio")',
        f'=COUNTIF(L5:L{4+NUM_AR_ROWS},"Alto")',
        f'=COUNTIF(L5:L{4+NUM_AR_ROWS},"Crítico")',
    ]
    imp_bg = [C_LIGHT_GREEN, C_LIGHT_YELLOW, C_LIGHT_RED, C_RED]
    imp_fc = [C_DARK_GREEN, '#9C6500', C_DARK_RED, C_WHITE]
    
    for i, (lbl, fml, bg, fc) in enumerate(zip(imp_labels, imp_formulas, imp_bg, imp_fc)):
        r = summ2_start + 1 + i
        ws.merge_range(r, 0, r, 2, lbl, wb.add_format({
            'bold': True, 'font_size': 11, 'font_color': fc, 'bg_color': bg,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
        }))
        ws.merge_range(r, 3, r, 5, "", wb.add_format({
            'bold': True, 'font_size': 14, 'font_color': fc, 'bg_color': bg,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': '0', 'font_name': 'Calibri'
        }))
        ws.write_formula(r, 3, fml, wb.add_format({
            'bold': True, 'font_size': 14, 'font_color': fc, 'bg_color': bg,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'num_format': '0', 'font_name': 'Calibri'
        }))
    
    chart2 = wb.add_chart({'type': 'doughnut'})
    chart2.set_title({'name': 'Restricciones por Nivel de Impacto'})
    chart2.set_style(10)
    chart2.set_size({'width': 450, 'height': 350})
    
    chart2.add_series({
        'name': 'Impacto',
        'categories': [sheet_name, summ2_start + 1, 0, summ2_start + 4, 0],
        'values': [sheet_name, summ2_start + 1, 3, summ2_start + 4, 3],
        'points': [
            {'fill': {'color': C_GREEN}},
            {'fill': {'color': C_YELLOW}},
            {'fill': {'color': C_ORANGE}},
            {'fill': {'color': C_RED}},
        ],
        'data_labels': {'percentage': True, 'category': True, 'separator': '\n', 'font': {'size': 9}},
    })
    chart2.set_legend({'position': 'bottom'})
    
    ws.insert_chart(summ2_start, 7, chart2)
    
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# CREATE DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════

def create_dashboard():
    ws = wb.add_worksheet("DASHBOARD")
    ws.hide_gridlines(2)
    ws.set_zoom(85)
    ws.set_tab_color(C_DARK_BLUE)
    
    ws.set_column(0, 0, 3)
    ws.set_column(1, 15, 15)
    
    # Title
    ws.merge_range(0, 0, 2, 15, "PLANEAMIENTO 2026\nTABLERO DE CONTROL", wb.add_format({
        'bold': True, 'font_size': 22, 'font_color': C_WHITE, 'bg_color': C_DARK_BLUE,
        'align': 'center', 'valign': 'vcenter', 'border': 2, 'font_name': 'Calibri', 'text_wrap': True
    }))
    ws.set_row(0, 30)
    ws.set_row(1, 30)
    ws.set_row(2, 30)
    
    # Section: GIS
    ws.merge_range(4, 1, 4, 7, "GIS (POSTVENTA)", wb.add_format({
        'bold': True, 'font_size': 14, 'font_color': C_WHITE, 'bg_color': C_MED_BLUE,
        'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
    }))
    
    ws.merge_range(4, 8, 4, 15, "METROPOLITANO (DISEÑO)", wb.add_format({
        'bold': True, 'font_size': 14, 'font_color': C_WHITE, 'bg_color': C_GREEN,
        'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
    }))
    ws.set_row(4, 30)
    
    # Navigation links
    sections = [
        ("Lookahead Anual", "LA - GIS", "LA - METRO"),
        ("Plan Mensual", "PM - GIS", "PM - METRO"),
        ("PPC", "PPC - GIS", "PPC - METRO"),
        ("Análisis de Restricciones", "AR - GIS", "AR - METRO"),
    ]
    
    r = 6
    for label, gis_sheet, metro_sheet in sections:
        ws.merge_range(r, 1, r, 3, label, wb.add_format({
            'bold': True, 'font_size': 12, 'font_color': C_DARK_BLUE, 'bg_color': C_PALE_BLUE,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
        }))
        ws.merge_range(r, 4, r, 7, "", wb.add_format({
            'bold': True, 'font_size': 11, 'font_color': C_MED_BLUE, 'bg_color': C_WHITE,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'underline': True, 'font_name': 'Calibri'
        }))
        ws.write_url(r, 4, f"internal:'{gis_sheet}'!A1", wb.add_format({
            'bold': True, 'font_size': 11, 'font_color': C_MED_BLUE, 'bg_color': C_WHITE,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'underline': True, 'font_name': 'Calibri'
        }), f"→ Ir a {gis_sheet}")
        
        ws.merge_range(r, 8, r, 11, label, wb.add_format({
            'bold': True, 'font_size': 12, 'font_color': C_DARK_BLUE, 'bg_color': C_PALE_BLUE,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Calibri'
        }))
        ws.merge_range(r, 12, r, 15, "", wb.add_format({
            'bold': True, 'font_size': 11, 'font_color': C_GREEN, 'bg_color': C_WHITE,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'underline': True, 'font_name': 'Calibri'
        }))
        ws.write_url(r, 12, f"internal:'{metro_sheet}'!A1", wb.add_format({
            'bold': True, 'font_size': 11, 'font_color': C_GREEN, 'bg_color': C_WHITE,
            'align': 'center', 'valign': 'vcenter', 'border': 1, 'underline': True, 'font_name': 'Calibri'
        }), f"→ Ir a {metro_sheet}")
        
        ws.set_row(r, 35)
        r += 1
    
    # Instructions
    r += 2
    ws.merge_range(r, 1, r + 6, 15, 
        "INSTRUCCIONES DE USO:\n\n"
        "1. LOOKAHEAD ANUAL: Vista general de todas las actividades del año divididas por semanas. "
        "Las barras azules muestran las actividades planificadas.\n\n"
        "2. PLAN MENSUAL: Para cada mes, seleccione el Estado de cada actividad (No Iniciado / En Proceso / "
        "Completado / Retrasado) e ingrese el % de Avance. Los gráficos se actualizan automáticamente.\n\n"
        "3. PPC (% Plan Cumplido): Marque 'Sí' en las actividades Comprometidas y después marque 'Sí' en las "
        "Ejecutadas. El PPC se calcula automáticamente: PPC = Ejecutadas / Comprometidas. Meta ≥ 80%.\n\n"
        "4. AR (Análisis de Restricciones): Registre cada restricción identificada, su tipo, impacto, responsable "
        "y acción de mitigación. Los gráficos de resumen se actualizan automáticamente.",
        wb.add_format({
            'font_size': 11, 'font_color': C_DARK_BLUE, 'bg_color': C_WHITE,
            'align': 'left', 'valign': 'top', 'border': 1, 'text_wrap': True, 'font_name': 'Calibri'
        })
    )
    
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# GENERATE ALL SHEETS
# ══════════════════════════════════════════════════════════════════════════════

print("Generando Dashboard...")
create_dashboard()

# GIS Sheets
print("Generando Lookahead GIS...")
ws_la_gis = create_lookahead(GIS_DATA, "LA - GIS")
ws_la_gis.set_tab_color(C_LIGHT_BLUE)

print("Generando Plan Mensual GIS...")
ws_pm_gis = create_plan_mensual(GIS_DATA, "PM - GIS")
ws_pm_gis.set_tab_color(C_MED_BLUE)

print("Generando PPC GIS...")
ws_ppc_gis = create_ppc(GIS_DATA, "PPC - GIS")
ws_ppc_gis.set_tab_color(C_GREEN)

print("Generando AR GIS...")
ws_ar_gis = create_ar(GIS_DATA, "AR - GIS")
ws_ar_gis.set_tab_color(C_RED)

# METROPOLITANO Sheets
print("Generando Lookahead METROPOLITANO...")
ws_la_metro = create_lookahead(METRO_DATA, "LA - METRO")
ws_la_metro.set_tab_color(C_LIGHT_BLUE)

print("Generando Plan Mensual METROPOLITANO...")
ws_pm_metro = create_plan_mensual(METRO_DATA, "PM - METRO")
ws_pm_metro.set_tab_color(C_MED_BLUE)

print("Generando PPC METROPOLITANO...")
ws_ppc_metro = create_ppc(METRO_DATA, "PPC - METRO")
ws_ppc_metro.set_tab_color(C_GREEN)

print("Generando AR METROPOLITANO...")
ws_ar_metro = create_ar(METRO_DATA, "AR - METRO")
ws_ar_metro.set_tab_color(C_RED)

# Close workbook
print(f"\nGuardando archivo: {OUTPUT_FILE}")
wb.close()
print("✓ Archivo generado exitosamente!")
print(f"  → {OUTPUT_FILE}")
