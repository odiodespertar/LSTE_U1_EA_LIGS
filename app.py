import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos Prácticos - Teoría de Sistemas",
    page_icon="💧",
    layout="wide",
)

# Estilos CSS para tarjetas y flujo animado
st.markdown("""
    <style>
    .system-box {
        background-color: #f8f9fa;
        border: 2px dashed #0083B8;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .flow-arrow {
        text-align: center;
        font-size: 28px;
        color: #0083B8;
        font-weight: bold;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("4. Modelos prácticos adaptados a la localidad")
st.markdown("**Estudiante:** Liliana García Solís | **Matrícula:** ES251101336 | **Asignatura:** Fundamentos del Sistema de Transporte")
st.markdown("---")

# Pestañas principales
tab1, tab2 = st.tabs([
    "A. Sistema Multimodal: CETRAM El Rosario (Pasajeros)",
    "B. Distribución de Carga: Agua en Garrafón (Mercancías)"
])

# ==========================================
# PESTAÑA A: CETRAM EL ROSARIO
# ==========================================
with tab1:
    st.header("A. Sistema multimodal de transporte de pasajeros en la localidad (CETRAM El Rosario)")
    
    st.info("""
    📖 **Contexto Teórico:**  
    *“La construcción de un Centro de Transferencia Modal (Cetram) es quizá uno de los proyectos más complejos que se han desarrollado en los últimos años en la ciudad. Su principal objetivo es concentrar y reorganizar los diferentes sistemas de transporte de la ciudad en un solo lugar. Con base en las estrategias de distribución y control de flujos y circulaciones, se busca mejorar la calidad de vida de quienes se trasladan de un lugar a otro de la ciudad”*.
    """)

    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        num_trenes = st.slider("Trenes activos (L6 y L7)", 10, 50, 25, key="t_pax")
    with col_c2:
        num_buses = st.slider("Unidades (Metrobús / Trolebús / Combis)", 5, 40, 20, key="b_pax")
    with col_c3:
        horario_operativo = st.selectbox(
            "Franja Horaria de Operación:",
            [
                "Hora Pico Matutina (Mañana)", 
                "Hora Valle / Intermedia (Tarde)", 
                "Hora Pico Vespertina / Nocturna (Noche)"
            ]
        )

    capacidad_oferta = (num_trenes + num_buses) * 110
    if "Valle" in horario_operativo:
        estado_operativo = "Operación fluida, estable y con tiempos de espera mínimos."
        nivel_alerta = False
    else:
        estado_operativo = f"Saturación activa por alta demanda pendular ({horario_operativo})."
        nivel_alerta = True

    st.markdown(f"**📊 Capacidad operativa calculada por la flota:** {capacidad_oferta} pas/h | **Estatus:** {estado_operativo}")
    st.markdown("---")
    st.subheader("🔄 Diagrama Sistémico Interactivo con Movimiento de Flujos")

    c_in, c_arrow1, c_proc, c_arrow2, c_out = st.columns([2, 0.5, 2, 0.5, 2])

    with c_in:
        st.markdown("### 📥 1. Entradas")
        st.markdown(f"""
        <div class="system-box">
        🚆 {num_trenes} Trenes activos (L6 y L7)<br>
        🚍 {num_buses} Unidades (Trolebús/Metrobús/Combis)<br>
        🚲 Infraestructura de ciclovías<br>
        🎟️ Andenes y tarifas de acceso
        </div>
        """, unsafe_allow_html=True)

    with c_arrow1:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>🔄</div>", unsafe_allow_html=True)

    with c_proc:
        st.markdown("### ⚙️ 2. Conversión")
        st.markdown(f"""
        <div class="system-box">
        ⚙️ Regulación de flujos peatonales<br>
        ⏱️ Programación de correspondencias<br>
        📋 Control de despacho en andenes<br>
        🕒 <em>Fase activa: {horario_operativo}</em>
        </div>
        """, unsafe_allow_html=True)

    with c_arrow2:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>🔄</div>", unsafe_allow_html=True)

    with c_out:
        st.markdown("### 📤 3. Salidas")
        st.markdown("""
        <div class="system-box">
        👥 Pasajeros transferidos eficientemente<br>
        🌿 Reducción de emisiones por viaje<br>
        🏙️ Ordenamiento del espacio público
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔄 4. Retroalimentación (Feedback)")
    if nivel_alerta:
        st.warning(f"⚠️ **Alerta activa de retroalimentación ({horario_operativo}):** Se detectan demoras en transbordos y alta acumulación de usuarios en andenes debido a la saturación de la demanda. Se requiere reforzar frecuencias de despacho para la flota de {num_trenes} trenes.")
    else:
        st.success(f"✅ **Retroalimentación óptima ({horario_operativo}):** Flujo continuo reportado por los usuarios sin saturación crítica en la correspondencia con la configuración actual.")

    st.markdown("---")
    st.markdown("📸 **Ilustrativo 1.** *Diagrama sistémico del sistema multimodal de transporte de personas en el CETRAM El Rosario *")

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA EN GARRAFÓN
# ==========================================
with tab2:
    st.header("B. Distribución local de agua embotellada (Transporte de mercancías / Garrafón)")
    
    st.markdown("""
    > **Identificación sistémica:** Ámbito urbano/suburbano, medio terrestre, modo vehículos de redilas de reparto local, especialización carga.  
    > **Descripción técnica:** Modelo logístico de alta capilaridad y frecuencia (Lunes a Viernes de 9:00 a.m. a 5:00 p.m. y Sábados de 9:00 a.m. a mediodía), priorizando seguridad, regularidad y flexibilidad de ruteo.
    """)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        unidades_reparto = st.slider("Vehículos de redilas en ruta", 1, 10, 3, key="slider_camiones")
    with col_d2:
        pedidos_diarios = st.slider("Número de Pedidos (Garrafones)", 50, 400, 150, step=10, key="slider_pedidos")
    with col_d3:
        demanda_estacional = st.selectbox("Variación de Demanda Estacional", ["Temporada Regular", "Temporada de Calor (Alta Demanda)"])

    capacidad_total_flota = unidades_reparto * 50

    st.markdown(f"**📊 Capacidad de la flota ({unidades_reparto} camiones):** {capacidad_total_flota} garrafones máx. | **Demanda a cubrir:** {pedidos_diarios} garrafones")
    st.markdown("---")
    st.subheader("🔄 Esquema Sistémico Dinámico de Carga")

    b_in, b_arrow1, b_proc, b_arrow2, b_out = st.columns([2, 0.5, 2, 0.5, 2])

    with b_in:
        st.markdown("### 📥 1. Entradas")
        st.markdown(f"""
        <div class="system-box">
        💧 Agua purificada en planta<br>
        🔄 Envases de garrafón vacíos<br>
        🚚 {unidades_reparto} Vehículos de redilas activos<br>
        📋 <strong>{pedidos_diarios} Pedidos programados</strong>
        </div>
        """, unsafe_allow_html=True)

    with b_arrow1:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>📦</div>", unsafe_allow_html=True)

    with b_proc:
        st.markdown("### ⚙️ 2. Conversión")
        st.markdown(f"""
        <div class="system-box">
        🏭 Proceso de envasado y ruteo<br>
        ⏰ Ventana: L-V (9:00 a 17:00 h) / S (9:00 a 14:00 h)<br>
        <em>Distribución activa en ruta</em>
        </div>
        """, unsafe_allow_html=True)

    with b_arrow2:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>📦</div>", unsafe_allow_html=True)

    with b_out:
        st.markdown("### 📤 3. Salidas")
        st.markdown(f"""
        <div class="system-box">
        🏠 <strong>{pedidos_diarios} Garrafones entregados</strong><br>
        🔄 Recolección de envases vacíos<br>
        📄 Notas de venta y control
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔄 4. Retroalimentación (Feedback)")
    if pedidos_diarios > capacidad_total_flota:
        st.warning(f"⚠️ **Alerta logística:** Los {pedidos_diarios} pedidos superan la capacidad máxima de la flota actual ({capacidad_total_flota} unidades). Se generan tiempos muertos en ruta y retrasos; se requiere incorporar al menos { (pedidos_diarios - capacidad_total_flota) // 50 + 1 } vehículo(s) adicional(es).")
    elif "Calor" in demanda_estacional:
        st.warning(f"⚠️ **Alerta estacional ({demanda_estacional}):** La flota opera bajo alta exigencia para cumplir puntualmente con los {pedidos_diarios} garrafones solicitados dentro de la ventana horaria.")
    else:
        st.success(f"✅ **Operación estable:** Las {unidades_reparto} unidades cubren perfectamente los {pedidos_diarios} pedidos dentro de la ventana horaria establecida sin reportes extraordinarios.")

    st.markdown("---")
    st.markdown("📸 **Ilustrativo 2.** *Diagrama sistémico del sistema de transporte de mercancías y distribución local de agua en garrafón (UnADM, 2026).*")
