import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Simulador Logístico - Teoría de Sistemas",
    page_icon="🎮",
    layout="wide",
)

# Estilo visual moderno con tarjetas
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("🎮 Simulador Interactivo de Modelos de Transporte")
st.markdown("**Estudiante:** Liliana García Solís | **Matrícula:** ES251101336 | **Asignatura:** Fundamentos del Sistema de Transporte")
st.markdown("---")

# Menú principal de navegación en pestañas
tab1, tab2 = st.tabs([
    "🚍 Simulación 1: CETRAM El Rosario (Pasajeros)",
    "💧 Simulación 2: Distribución de Agua en Garrafón (Carga)"
])

# ==========================================
# PESTAÑA 1: CETRAM EL ROSARIO (INTERACTIVO)
# ==========================================
with tab1:
    st.header("CETRAM El Rosario: Nodo Multimodal Interactivo")
    st.markdown("Modifica los parámetros operativos de la estación para evaluar el comportamiento del sistema bajo la teoría de sistemas.")

    col_control1, col_viz1 = st.columns([1, 2])

    with col_control1:
        st.subheader("🎛️ Panel de Control (Inputs)")
        num_trenes = st.slider("Trenes activos (Metro L6 y L7)", 10, 50, 25)
        num_buses = st.slider("Unidades de Metrobús / Trolebús", 5, 30, 15)
        demanda_usuarios = st.selectbox("Nivel de Demanda Actual", ["Hora Valle", "Hora Pico Matutina", "Hora Pico Vespertina"])
        
        # Cálculo simulado basado en los inputs
        if demanda_usuarios == "Hora Pico Matutina":
            eficiencia = "Baja (Saturación)"
            tiempo_espera = f"{num_trenes * 1.5:.1f} min"
        elif demanda_usuarios == "Hora Pico Vespertina":
            eficiencia = "Media-Baja"
            tiempo_espera = f"{num_trenes * 1.2:.1f} min"
        else:
            eficiencia = "Óptima / Fluida"
            tiempo_espera = "3.5 min"

    with col_viz1:
        st.subheader("📊 Panel de Resultados y Conversión")
        m1, m2, m3 = st.columns(3)
        m1.metric("Capacidad Operativa", f"{ (num_trenes + num_buses) * 120 } pas/h")
        m2.metric("Tiempo Estimado de Transbordo", tiempo_espera)
        m3.metric("Estado del Sistema", eficiencia)

        st.markdown("### 🔄 Análisis Dinámico bajo las Variables de Manheim (1979)")
        
        # Selección interactiva de Manheim
        caso_manheim_pax = st.radio(
            "Selecciona la dimensión analítica a evaluar en el CETRAM:",
            ["Relación 1 (Flujos F en función de T y A)", "Relación 2 (Impacto en Actividades A)", "Relación 3 (Adaptación del Transporte T)"],
            key="m_pax"
        )

        if "Relación 1" in caso_manheim_pax:
            st.success(f"**Simulación activa:** Con {num_trenes} trenes y {num_buses} unidades de apoyo operando en {demanda_usuarios}, el Patrón de Flujos ($F$) reorganiza los andenes del CETRAM de forma inmediata para evitar congestionamientos masivos.")
        elif "Relación 2" in caso_manheim_pax:
            st.info("**Evolución del entorno:** El flujo constante de pasajeros en este nodo multimodal impulsa el comercio local y la adaptabilidad urbana de los asentamientos alrededor de El Rosario.")
        else:
            st.warning("**Respuesta a largo plazo:** Si la demanda en hora pico continúa saturando el sistema, la infraestructura ($T$) requerirá una ampliación de andenes o reordenamiento de carriles confinados.")

# ==========================================
# PESTAÑA 2: DISTRIBUCIÓN DE GARRAFONES (INTERACTIVO)
# ==========================================
with tab2:
    st.header("Distribución de Agua en Garrafón: Simulador de Ruta")
    st.markdown("Configura los recursos logísticos de la flota de reparto para medir el rendimiento de entrega en la localidad.")

    col_control2, col_viz2 = st.columns([1, 2])

    with col_control2:
        st.subheader("🎛️ Panel de Control (Inputs)")
        camiones_redilas = st.slider("Vehículos de redilas activos", 1, 10, 3)
        garrafones_por_unidad = st.slider("Garrafones por viaje unitario", 20, 100, 50)
        clima_estacion = st.selectbox("Condición Climática / Estacional", ["Templado (Normal)", "Calor Extremo (Alta Demanda)"])

        # Cálculo logístico simulado
        total_entregas = camiones_redilas * garrafones_por_unidad
        if clima_estacion == "Calor Extremo (Alta Demanda)":
            total_entregas = int(total_entregas * 1.3)
            rendimiento_flota = "Máxima exigencia"
        else:
            rendimiento_flota = "Estable"

    with col_viz2:
        st.subheader("📊 Panel de Resultados y Conversión")
        c1, c2, c3 = st.columns(3)
        c1.metric("Unidades en Ruta", f"{camiones_redilas} camiones")
        c2.metric("Volumen Diario Suministrado", f"{total_entregas} garrafones")
        c3.metric("Estado de la Flota", rendimiento_flota)

        st.markdown("### 🔄 Análisis Dinámico bajo las Variables de Manheim (1979)")
        
        caso_manheim_carga = st.radio(
            "Selecciona la dimensión analítica a evaluar en la distribución:",
            ["Relación 1 (Flujos F en función de T y A)", "Relación 2 (Impacto en Actividades A)", "Relación 3 (Adaptación del Transporte T)"],
            key="m_carga"
        )

        if "Relación 1" in caso_manheim_carga:
            st.success(f"**Simulación activa:** Con una flota de {camiones_redilas} vehículos de redilas, el flujo de distribución ($F$) cubre dinámicamente los pedidos de los hogares y tienditas de la zona bajo la ventana horaria establecida.")
        elif "Relación 2" in caso_manheim_carga:
            st.info("**Evolución del entorno:** El suministro constante de agua potable asegura la continuidad operativa de los pequeños comercios locales que dependen directamente de este insumo.")
        else:
            st.warning("**Respuesta a largo plazo:** Ante el crecimiento de la mancha urbana y el aumento de pedidos por clima cálido, el sistema de transporte ($T$) se adaptará incorporando ruteo satelital y unidades de mayor capacidad.")

# Pie de página
st.markdown("---")
st.markdown("📌 *Aplicación desarrollada en Streamlit para la visualización de sistemas de transporte.*")
