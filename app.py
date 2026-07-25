import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Simulador de Teoría de Sistemas - Transporte",
    page_icon="🔄",
    layout="wide",
)

# Título principal
st.title("🔄 Simulador Sistémico Interactivo de Transporte")
st.markdown("**Estudiante:** Liliana García Solís | **Matrícula:** ES251101336 | **Asignatura:** Fundamentos del Sistema de Transporte")
st.markdown("---")

# Menú principal de pestañas
tab1, tab2 = st.tabs([
    "🚍 CETRAM El Rosario (Sistema de Pasajeros)",
    "💧 Distribución de Agua en Garrafón (Sistema de Carga)"
])

# ==========================================
# PESTAÑA 1: CETRAM EL ROSARIO
# ==========================================
with tab1:
    st.header("Modelo Sistémico: CETRAM El Rosario")
    st.markdown("Modifica los parámetros para ver cómo se transforman las fases del sistema en tiempo real.")

    col_ctrl_1, col_view_1 = st.columns([1, 2])

    with col_ctrl_1:
        st.subheader("🎛️ Controles del Sistema")
        num_trenes = st.slider("Trenes activos (Líneas 6 y 7)", 10, 50, 25, key="t_pax")
        num_buses = st.slider("Unidades de Metrobús y Trolebús", 5, 30, 15, key="b_pax")
        demanda_pax = st.selectbox("Fluctuación de Demanda", ["Hora Valle (Baja)", "Hora Pico Matutina (Alta)", "Hora Pico Vespertina (Alta)"], key="d_pax")

        # Variables dinámicas para el proceso
        if "Alta" in demanda_pax:
            estado_sistema = "Saturación Operativa"
            tiempo_transbordo = f"{num_trenes * 1.4:.1f} min"
        else:
            estado_sistema = "Fluido / Eficiente"
            tiempo_transbordo = "3.0 min"

    with col_view_1:
        st.subheader("📊 Métricas Operativas en Vivo")
        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Capacidad de Oferta", f"{(num_trenes + num_buses) * 110} pas/h")
        metric2.metric("Tiempo de Transbordo", tiempo_transbordo)
        metric3.metric("Estado del Sistema", estado_sistema)

        st.markdown("### 🧩 Fases del Sistema de Transporte Interactivas")
        
        # Desplegables interactivos de las fases
        with st.expander("📥 1. Entradas (Inputs) - Ver estado actual", expanded=True):
            st.write(f"- **Infraestructura:** Andenes del CETRAM, carriles confinados y ciclovías.")
            st.write(f"- **Flota activa:** {num_trenes} trenes y {num_buses} unidades de superficie (Trolebús/Metrobús).")
            st.write(f"- **Demanda ingresada:** Condición actual en nivel **{demanda_pax}**.")

        with st.expander("⚙️ 2. Proceso de Conversión - Ver operación"):
            st.write(f"- Regulación de flujos peatonales masivos en pasillos de correspondencia.")
            st.write(f"- Sincronización de intervalos de despacho ajustados a {tiempo_transbordo} promedio de espera.")
            st.write(f"- Operación intermodal coordinada entre transporte masivo, concesionado y no motorizado.")

        with st.expander("📤 3. Salidas (Outputs) - Ver resultados"):
            st.write(f"- Personas transferidas eficientemente hacia sus destinos urbanos.")
            st.write(f"- Condición general de operación resultante: **{estado_sistema}**.")
            st.write("- Mitigación acumulada de emisiones por uso de transporte masivo.")

        with st.expander("🔄 4. Retroalimentación (Feedback) - Ver avisos"):
            if "Alta" in demanda_pax:
                st.warning("⚠️ **Alerta de Retroalimentación:** Se detectan filas prolongadas en andenes. El sistema requiere reordenamiento inmediato de frecuencias o apoyo operativo.")
            else:
                st.success("✅ **Retroalimentación favorable:** Los tiempos de espera se encuentran dentro de los rangos óptimos de satisfacción del usuario.")

# ==========================================
# PESTAÑA 2: DISTRIBUCIÓN DE GARRAFONES
# ==========================================
with tab2:
    st.Modelo = "Modelo Sistémico: Distribución de Carga"
    st.header("Modelo Sistémico: Distribución Local de Agua en Garrafón")
    st.markdown("Configura los recursos logísticos para visualizar el comportamiento de las fases del sistema.")

    col_ctrl_2, col_view_2 = st.columns([1, 2])

    with col_ctrl_2:
        st.subheader("🎛️ Controles del Sistema")
        camiones = st.slider("Vehículos de redilas activos", 1, 10, 3, key="c_carga")
        capacidad_unitaria = st.slider("Garrafones por unidad", 20, 100, 50, key="cap_carga")
        clima = st.selectbox("Condición Climática", ["Templado (Demanda Normal)", "Calor Extremo (Alta Demanda)"], key="clim_carga")

        # Cálculos dinámicos
        total_garrafones = camiones * capacidad_unitaria
        if "Calor" in clima:
            total_garrafones = int(total_garrafones * 1.25)
            estatus_flota = "Alta Exigencia / Sobrecarga"
        else:
            estatus_flota = "Operación Estable"

    with col_view_2:
        st.subheader("📊 Métricas Logísticas en Vivo")
        c_m1, c_m2, c_m3 = st.columns(3)
        c_m1.metric("Flota en Ruta", f"{camiones} camiones")
        c_m2.metric("Volumen Suministrado", f"{total_garrafones} garrafones")
        c_m3.metric("Estatus de Flota", estatus_flota)

        st.markdown("### 🧩 Fases del Sistema de Logística Interactivas")

        with st.expander("📥 1. Entradas (Inputs) - Ver estado actual", expanded=True):
            st.write(f"- **Insumos:** Agua purificada procesada y envases de policarbonato.")
            st.write(f"- **Recursos físicos:** {camiones} vehículos de redilas operativos.")
            st.write(f"- **Contexto ambiental:** Condición climática registrada como **{clima}**.")

        with st.expander("⚙️ 2. Proceso de Conversión - Ver operación"):
            st.write(f"- Envasado en planta bajo controles estrictos de calidad.")
            st.write(f"- Ruteo diario de distribución cubriendo un volumen de {total_garrafones} unidades.")
            st.write(f"- Ejecución de entregas en ventana horaria establecida (L-V 9:00 a 17:00 h).")

        with st.expander("📤 3. Salidas (Outputs) - Ver resultados"):
            st.write(f"- Entrega final satisfactoria en hogares y comercios minoristas.")
            st.write(f"- Recolección simultánea de envases vacíos para reingresar al ciclo de lavado.")
            st.write(f"- Estatus del servicio: **{estatus_flota}**.")

        with st.expander("🔄 4. Retroalimentación (Feedback) - Ver avisos"):
            if "Calor" in clima:
                st.warning("⚠️ **Alerta de Retroalimentación:** Aumento drástico de consumo. Se agotan inventarios antes de concluir la ruta programada; se sugiere enviar una unidad de refuerzo.")
            else:
                st.success("✅ **Retroalimentación favorable:** Cumplimiento del 100% de las rutas sin reportes de desabasto ni demoras extraordinarias.")

# Pie de página
st.markdown("---")
st.markdown("📌 *Simulador interactivo basado en la teoría general de sistemas aplicada al transporte.*")
