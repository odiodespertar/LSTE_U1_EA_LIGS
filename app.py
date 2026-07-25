import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos de Transporte - Teoría de Sistemas",
    page_icon="🚍",
    layout="wide",
)

# Título principal
st.title("📦 Aplicación de la Teoría de Sistemas en el Transporte")
st.markdown(
    "**Estudiante:** Liliana García Solís | **Matrícula:** ES251101336 | **Semestre:** 3°"
)
st.markdown("---")

# Pestañas para separar los dos sistemas de estudio
tab1, tab2 = st.tabs(
    [
        "🚍 1. Sistema Multimodal: CETRAM El Rosario (Pasajeros)",
        "💧 2. Sistema de Carga: Distribución de Agua en Garrafón",
    ]
)

# ==========================================
# PESTAÑA 1: CETRAM EL ROSARIO
# ==========================================
with tab1:
  st.header("Modelo Sistémico: Transporte Multimodal de Pasajeros")
  st.markdown(
      "Nodo estratégico urbano que articula infraestructura masiva, concesionada"
      " y no motorizada."
  )

  # Columnas para estructurar el enfoque sistémico
  col1, col2 = st.columns(2)

  with col1:
    st.subheader("📥 1. Entradas (Inputs)")
    st.markdown("""
        * **Infraestructura:** Andenes, pasillos de correspondencia, carriles confinados, ciclovías.
        * **Flota:** Trenes (Líneas 6 y 7), trolebuses, unidades de Metrobús, combis, microbuses y bicicletas.
        * **Demanda / Humano:** Flujos masivos de usuarios pendulares y tarifas de acceso.
        """)

    st.subheader("⚙️ 2. Proceso de Conversión")
    st.markdown("""
        * Regulación de flujos peatonales y vehiculares.
        * Programación de correspondencias e intervalos de despacho.
        * Operación de la intermodalidad y control de andenes en el CETRAM.
        """)

  with col2:
    st.subheader("📤 3. Salidas (Outputs)")
    st.markdown("""
        * Pasajeros transferidos eficientemente a sus destinos urbanos.
        * Reducción de tiempos de espera y ordenamiento del espacio público.
        * Emisiones optimizadas por consolidación del transporte masivo.
        """)

    st.subheader("🔄 4. Retroalimentación (Feedback)")
    st.markdown("""
        * Saturación e índices de congestión en horas pico.
        * Demoras reportadas en transbordos específicos.
        * Quejas o sugerencias de los usuarios sobre fluidez operativa.
        """)

  st.markdown("---")
  st.subheader(
      "🔗 Dinámica Operativa bajo las Variables de Manheim (1979)"
  )

  selected_rel_1 = st.selectbox(
      "Selecciona la relación analítica a consultar (CETRAM El Rosario):",
      [
          "Relación 1: Interacción de T y A sobre el Patrón de Flujos (F)",
          "Relación 2: Transformación del Sistema de Actividades (A) con el"
          " tiempo",
          "Relación 3: Modificación adaptativa del Sistema de Transporte (T)",
      ],
      key="manheim_pax",
  )

  if "Relación 1" in selected_rel_1:
    st.info(
        "**Análisis F = f(T, A):** El patrón de flujos de usuarios que"
        " convergen al CETRAM El Rosario está determinado por la oferta de"
        " transporte ($T$: Líneas 6 y 7 del Metro, Metrobús, trolebús, combis,"
        " microbuses y ciclovías) y la localización de zonas residenciales,"
        " escolares y de trabajo ($A$). Si se reconfiguran las plataformas o se"
        " integran nuevas rutas alimentadoras, los flujos peatonales se"
        " reorganizan de inmediato."
    )
  elif "Relación 2" in selected_rel_1:
    st.info(
        "**Impacto en Actividades:** La alta eficiencia o saturación del flujo"
        " de pasajeros en el nodo genera transformaciones en el sistema de"
        " actividades ($A$), estimulando el comercio formal e informal en el"
        " perímetro del CETRAM y alterando la dinámica de asentamientos"
        " urbanos periféricos."
    )
  else:
    st.info(
        "**Adaptación del Transporte:** A largo plazo, el incremento"
        " sostenido en el volumen de usuarios obliga a realizar modificaciones"
        " estructurales en el propio sistema de transporte ($T$), como la"
        " ampliación de estaciones, modernización de andenes o reordenamiento de"
        " carriles confinados."
    )

# ==========================================
# PESTAÑA 2: DISTRIBUCIÓN DE GARRAFONES
# ==========================================
with tab2:
  st.header("Modelo Sistémico: Distribución Local de Agua en Garrafón")
  st.markdown(
      "Modelo logístico de alta capilaridad, baja capacidad unitaria y alta"
      " frecuencia de reposición."
  )

  col3, col4 = st.columns(2)

  with col3:
    st.subheader("📥 1. Entradas (Inputs)")
    st.markdown("""
        * **Materiales:** Agua purificada procesada, envases de policarbonato (garrafones vacíos).
        * **Recursos:** Vehículos utilitarios de redilas de reparto local, personal operativo (chofer y ayudante/machetero).
        * **Demanda:** Pedidos programados y de última milla de hogares y comercios.
        """)

    st.subheader("⚙️ 2. Proceso de Conversión")
    st.markdown("""
        * Envasado y control de calidad en planta.
        * Ruteo operativo diario y asignación de zonas de entrega.
        * Ejecución de distribución bajo ventana horaria establecida (Lunes a Viernes 9:00 a 17:00 h, Sábados 9:00 a 14:00 h).
        """)

  with col4:
    st.subheader("📤 3. Salidas (Outputs)")
    st.markdown("""
        * Garrafones llenos entregados satisfactoriamente en puntos de consumo.
        * Recolección y retorno de envases vacíos para el ciclo de lavado.
        * Registro de notas de venta y control de inventarios ruteros.
        """)

    st.subheader("🔄 4. Retroalimentación (Feedback)")
    st.markdown("""
        * Devoluciones de producto por problemas de calidad o envase dañado.
        * Tiempos muertos en ruta por congestión vehicular urbana.
        * Variaciones estacionales en la demanda de agua (incremento en temporadas de calor).
        """)

  st.markdown("---")
  st.subheader(
      "🔗 Dinámica Operativa bajo las Variables de Manheim (1979)"
  )

  selected_rel_2 = st.selectbox(
      "Selecciona la relación analítica a consultar (Garrafones):",
      [
          "Relación 1: Interacción de T y A sobre el Patrón de Flujos (F)",
          "Relación 2: Transformación del Sistema de Actividades (A) con el"
          " tiempo",
          "Relación 3: Modificación adaptativa del Sistema de Transporte (T)",
      ],
      key="manheim_carga",
  )

  if "Relación 1" in selected_rel_2:
    st.info(
        "**Análisis F = f(T, A):** El flujo de distribución diaria ($F$) depende"
        " directamente de la capacidad de la flota de vehículos de redilas ($T$)"
        " y de la ubicación geográfica de los clientes minoristas y hogares"
        " ($A$). Al optimizar una ruta de entrega matutina, los tiempos y flujos"
        " de abastecimiento cambian al instante."
    )
  elif "Relación 2" in selected_rel_2:
    st.info(
        "**Impacto en Actividades:** El flujo constante de suministro de agua"
        " genera hábitos de consumo estables y fomenta la operación continua de"
        " pequeños negocios locales (tienditas de la esquina) que dependen de"
        " este insumo comercial."
    )
  else:
    st.info(
        "**Adaptación del Transporte:** Ante el crecimiento de la mancha"
        " urbana y la dispersión de la demanda, las empresas adaptan su sistema"
        " de transporte ($T$) incorporando unidades con mejor rendimiento,"
        " rediseñando esquemas de mantenimiento o integrando herramientas de"
        " geolocalización."
    )
