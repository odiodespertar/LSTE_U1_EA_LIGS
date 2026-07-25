import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos Prácticos - Teoría de Sistemas",
    page_icon="💧",
    layout="wide",
)

# Estilos CSS avanzados para tarjetas y globos/insignias flotantes individuales
st.markdown("""
    <style>
    .system-box {
        background-color: #f8f9fa;
        border: 2px dashed #0083B8;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        transition: transform 0.3s ease-in-out;
    }
    .system-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 131, 184, 0.2);
    }
    .flow-arrow {
        text-align: center;
        font-size: 28px;
        color: #0083B8;
        font-weight: bold;
        margin: 5px 0;
    }
    /* Estilo para las burbujas o globos flotantes de señalamiento */
    .stage-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        color: white;
        margin-bottom: 8px;
        animation: pulseBadge 2s infinite;
    }
    .badge-input { background-color: #0288d1; }
    .badge-process { background-color: #f57c00; }
    .badge-output { background-color: #388e3c; }
    
    @keyframes pulseBadge {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
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
    *“La construcción de un Centro de Transferencia Modal (CETRAM) es quizá uno de los proyectos más complejos que se han desarrollado en los últimos años en la ciudad. Su principal objetivo es concentrar y reorganizar los diferentes sistemas de transporte de la ciudad en un solo lugar...”*
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
            ],
            key="h_pax"
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
    st.subheader("🔄 Diagrama Sistémico Interactivo")

    c_in, c_arrow1, c_proc, c_arrow2, c_out = st.columns([2, 0.5, 2, 0.5, 2])

    with c_in:
        st.markdown('<div class="stage-badge badge-input">🔵 SEÑAL: ENTRADAS ACTIVAS</div>', unsafe_allow_html=True)
        st.markdown("### 📥 1. Entradas")
        st.markdown(f"""
        <div class="system-box">
        🚆 {num_trenes} Trenes activos (L6 y L7)<br>
        🚍 {num_buses} Unidades de superficie<br>
        🚲 Infraestructura ciclista<br>
        🎟️ Andenes y torniquetes
        </div>
        """, unsafe_allow_html=True)

    with c_arrow1:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>🔄</div>", unsafe_allow_html=True)

    with c_proc:
        st.markdown('<div class="stage-badge badge-process">🟠 SEÑAL: PROCESO / CONVERSIÓN</div>', unsafe_allow_html=True)
        st.markdown("### ⚙️ 2. Conversión")
        st.markdown(f"""
        <div class="system-box">
        ⚙️ Regulación de flujos peatonales<br>
        ⏱️ Sincronización de transbordos<br>
        📋 Despacho en andenes<br>
        🕒 <em>{horario_operativo}</em>
        </div>
        """, unsafe_allow_html=True)

    with c_arrow2:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>🔄</div>", unsafe_allow_html=True)

    with c_out:
        st.markdown('<div class="stage-badge badge-output">🟢 SEÑAL: SALIDAS / FLUJO FINAL</div>', unsafe_allow_html=True)
        st.markdown("### 📤 3. Salidas")
        st.markdown("""
        <div class="system-box">
        👥 Pasajeros transferidos con éxito<br>
        🌿 Reducción de emisiones<br>
        🏙️ Ordenamiento urbano
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔄 4. Retroalimentación (Feedback)")
    if nivel_alerta:
        st.warning(f"⚠️ **Alerta activa de retroalimentación ({horario_operativo}):** Se detectan demoras en andenes por alta concentración de usuarios. Se requiere ajustar frecuencias de despacho.")
    else:
        st.success(f"✅ **Retroalimentación óptima ({horario_operativo}):** Tránsito fluido y continuo en las líneas de correspondencia.")

    st.markdown("---")
    st.markdown("📸 **Ilustrativo 1.** *Diagrama sistémico del sistema multimodal de transporte de personas en el CETRAM El Rosario*")

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA EN GARRAFÓN
# ==========================================
with tab2:
    st.header("B. Distribución local de agua embotellada (Transporte de mercancías / Garrafón)")
    
    st.markdown("""
    > **Identificación sistémica:** Ámbito urbano/suburbano, medio terrestre, modo vehículos de redilas de reparto local, especialización carga.  
    > **Descripción técnica:** Modelo logístico de alta capilaridad y frecuencia (Lunes a Viernes de 9:00 a.m. a 5:00 p.m. y Sábados de 9:00 a.m. a mediodía), priorizando seguridad y regularidad de ruteo.
    """)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        unidades_reparto = st.slider("Vehículos de redilas en ruta", 1, 10, 3, key="slider_camiones")
    with col_d2:
        pedidos_diarios = st.slider("Número de Pedidos (Garrafones)", 50, 400, 150, step=10, key="slider_pedidos")
    with col_d3:
        demanda_estacional = st.selectbox("Variación de Demanda Estacional", ["Temporada Regular", "Temporada de Calor (Alta Demanda)"], key="d_estacional")

    capacidad_total_flota = unidades_reparto * 50

    st.markdown(f"**📊 Capacidad de la flota ({unidades_reparto} camiones):** {capacidad_total_flota} garrafones máx. | **Demanda a cubrir:** {pedidos_diarios} garrafones")
    st.markdown("---")
    st.subheader("🔄 Esquema Sistémico Dinámico de Carga")

    b_in, b_arrow1, b_proc, b_arrow2, b_out = st.columns([2, 0.5, 2, 0.5, 2])

    with b_in:
        st.markdown('<div class="stage-badge badge-input">🔵 SEÑAL: ENTRADAS DE CARGA</div>', unsafe_allow_html=True)
        st.markdown("### 📥 1. Entradas")
        st.markdown(f"""
        <div class="system-box">
        💧 Agua purificada en planta<br>
        🔄 Envases vacíos recolectados<br>
        🚚 {unidades_reparto} Unidades de redilas<br>
        📋 <strong>{pedidos_diarios} Pedidos asignados</strong>
        </div>
        """, unsafe_allow_html=True)

    with b_arrow1:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>📦</div>", unsafe_allow_html=True)

    with b_proc:
        st.markdown('<div class="stage-badge badge-process">🟠 SEÑAL: PROCESO / CONVERSIÓN</div>', unsafe_allow_html=True)
        st.markdown("### ⚙️ 2. Conversión")
        st.markdown(f"""
        <div class="system-box">
        🏭 Proceso de envasado y ruteo<br>
        ⏰ Ventana: L-V / Sábados<br>
        <em>Ruta activa ({demanda_estacional})</em>
        </div>
        """, unsafe_allow_html=True)

    with b_arrow2:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>📦</div>", unsafe_allow_html=True)

    with b_out:
        st.markdown('<div class="stage-badge badge-output">🟢 SEÑAL: SALIDAS / ENTREGAS</div>', unsafe_allow_html=True)
        st.markdown("### 📤 3. Salidas")
        st.markdown(f"""
        <div class="system-box">
        🏠 <strong>{pedidos_diarios} Garrafones entregados</strong><br>
        🔄 Retorno de envases vacíos<br>
        📄 Notas de venta controladas
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔄 4. Retroalimentación (Feedback)")
    if pedidos_diarios > capacidad_total_flota:
        st.warning(f"⚠️ **Alerta logística:** Los {pedidos_diarios} pedidos superan la capacidad de la flota actual ({capacidad_total_flota} unidades). Se requiere incorporar al menos { (pedidos_diarios - capacidad_total_flota) // 50 + 1 } vehículo(s) adicional(es).")
    elif "Calor" in demanda_estacional:
        st.warning(f"⚠️ **Alerta estacional ({demanda_estacional}):** La flota opera bajo alta exigencia para cumplir puntualmente con los {pedidos_diarios} garrafones solicitados.")
    else:
        st.success(f"✅ **Operación estable:** Las {unidades_reparto} unidades cubren perfectamente los {pedidos_diarios} pedidos dentro de la ventana horaria establecida.")

    st.markdown("---")
    st.markdown("📸 **Ilustrativo 2.** *Diagrama sistémico del sistema de transporte de mercancías y distribución local de agua en garrafón*")
