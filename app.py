import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos Prácticos - Teoría de Sistemas",
    page_icon="💧",
    layout="wide",
)

# Estilos CSS avanzados para tarjetas, globos/insignias y notificaciones estilizadas
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
    
    /* Estilos para notificaciones estilizadas */
    .alert-card-success {
        background-color: #e8f5e9;
        border-left: 6px solid #2e7d32;
        padding: 15px 20px;
        border-radius: 8px;
        margin: 15px 0;
        font-size: 15px;
        color: #1b5e20;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .alert-card-warning {
        background-color: #fff3e0;
        border-left: 6px solid #ef6c00;
        padding: 15px 20px;
        border-radius: 8px;
        margin: 15px 0;
        font-size: 15px;
        color: #e65100;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    @keyframes pulseBadge {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera institucional con Logo y Título en columnas
col_logo, col_txt = st.columns([1, 5])
with col_logo:
    try:
        st.image("UnADM LOGO.png", width=140)
    except Exception:
        st.warning("⚠️ Coloca la imagen 'UnADM LOGO.png' en la carpeta.")

with col_txt:
    st.title("4. Modelos prácticos adaptados a la localidad")
    st.markdown("**Estudiante:** Liliana García Solís | **Matrícula:** ES251101336 | **Bloque:** 1 | **Asignatura:** Sistemas de Transporte")

st.markdown("---")

# Pestañas principales
tab1, tab2 = st.tabs([
    "A. Sistema Multimodal: CETRAM El Rosario (Pasajeros)",
    "B. Distribución de Carga: Agua en Garrafón en U.H. El Rosario (Mercancías)"
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

    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    with col_c1:
        num_trenes = st.slider("🚆 Trenes activos (L6 y L7)", 10, 50, 25, key="t_pax")
    with col_c2:
        num_buses = st.slider("🚍 Unidades de superficie", 5, 40, 20, key="b_pax")
    with col_c3:
        pasajeros_flota = st.slider("👥 Pasajeros a trasladar", 500, 5000, 2000, step=100, key="p_flota")
    with col_c4:
        horario_operativo = st.selectbox(
            "🕒 Franja Horaria:",
            [
                "Hora Pico Matutina (Mañana)", 
                "Hora Valle / Intermedia (Tarde)", 
                "Hora Pico Vespertina / Nocturna (Noche)"
            ],
            key="h_pax"
        )

    # Cálculo matemático de capacidad de oferta de pasajeros total
    capacidad_oferta = (num_trenes + num_buses) * 110
    balance_pasajeros = capacidad_oferta - pasajeros_flota

    # Bloque de apoyo visual con Fórmulas Matemáticas en LaTeX
    st.markdown("📐 **Soporte Matemático y Modelo de Cálculo de Pasajeros:**")
    st.latex(r"C_{\text{oferta}} = (\text{Trenes} + \text{Unidades}) \times \text{Capacidad Promedio}")
    st.latex(r"C_{\text{oferta}} = (" + str(num_trenes) + " + " + str(num_buses) + r") \times 110 = " + str(capacidad_oferta) + r" \text{ pasajeros}")
    st.latex(r"\Delta_{\text{pax}} = C_{\text{oferta}} - \text{Pasajeros a trasladar}")
    st.latex(r"\Delta_{\text{pax}} = " + str(capacidad_oferta) + " - " + str(pasajeros_flota) + " = " + str(balance_pasajeros) + r" \text{ margen}")

    if "Valle" in horario_operativo:
        estado_operativo = "Operación fluida, estable y con tiempos de espera mínimos."
        nivel_alerta = False
    else:
        estado_operativo = f"Saturación activa por alta demanda pendular ({horario_operativo})."
        nivel_alerta = True

    # Notificación estilizada para la Pestaña A
    if nivel_alerta or pasajeros_flota > capacidad_oferta:
        st.markdown(f"""
        <div class="alert-card-warning">
            ⚠️ <strong>ESTATUS OPERATIVO (ALERTA):</strong> Capacidad de flota: <strong>{capacidad_oferta} pasajeros</strong> | Demanda actual: <strong>{pasajeros_flota} pasajeros</strong><br>
            <em>Diagnóstico: {estado_operativo}</em>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="alert-card-success">
            ✅ <strong>ESTATUS OPERATIVO (ÓPTIMO):</strong> Capacidad de flota: <strong>{capacidad_oferta} pasajeros</strong> | Demanda actual: <strong>{pasajeros_flota} pasajeros</strong><br>
            <em>Diagnóstico: {estado_operativo}</em>
        </div>
        """, unsafe_allow_html=True)

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
        👥 <strong>{pasajeros_flota} Pasajeros en demanda</strong><br>
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
        st.markdown(f"""
        <div class="system-box">
        👥 <strong>{pasajeros_flota} Pasajeros transferidos</strong><br>
        🌿 Reducción de emisiones<br>
        🏙️ Ordenamiento urbano
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔄 4. Retroalimentación (Feedback)")
    if pasajeros_flota > capacidad_oferta:
        st.warning(f"⚠️ **Alerta de saturación:** La demanda de {pasajeros_flota} pasajeros rebasa la capacidad de oferta de la flota ({capacidad_oferta} pasajeros). Se requiere incrementar frecuencias.")
    elif nivel_alerta:
        st.warning(f"⚠️ **Alerta activa de retroalimentación ({horario_operativo}):** Demoras en andenes por alta concentración de usuarios.")
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
    > **Identificación sistémica:** Ámbito urbano/suburbano, medio terrestre, modo vehículos de redilas de reparto local en U.H. El Rosario, especialización carga.  
    > **Descripción técnica:** Modelo logístico de alta capilaridad y frecuencia (Lunes a Viernes de 9:00 a.m. a 5:00 p.m. y Sábados de 9:00 a.m. a mediodía), priorizando seguridad y regularidad de ruteo.
    """)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        unidades_reparto = st.slider("🚚 Vehículos de redilas en ruta", 1, 10, 3, key="slider_camiones")
    with col_d2:
        pedidos_diarios = st.slider("💧 Número de Pedidos (Garrafones)", 50, 400, 150, step=10, key="slider_pedidos")
    with col_d3:
        demanda_estacional = st.selectbox("🌤️ Variación de Demanda Estacional", ["Temporada Regular", "Temporada de Calor (Alta Demanda)"], key="d_estacional")

    capacidad_total_flota = unidades_reparto * 50
    balance_operativo = capacidad_total_flota - pedidos_diarios

    st.markdown("📐 **Soporte Matemático y Modelo de Ruteo de Carga:**")
    st.latex(r"C_{\text{flota}} = \text{Unidades Activas} \times \text{Capacidad Unitaria}")
    st.latex(r"C_{\text{flota}} = " + str(unidades_reparto) + r" \times 50 = " + str(capacidad_total_flota) + r" \text{ garrafones máx.}")
    st.latex(r"\Delta_{\text{demanda}} = C_{\text{flota}} - \text{Pedidos Programados}")
    st.latex(r"\Delta_{\text{demanda}} = " + str(capacidad_total_flota) + " - " + str(pedidos_diarios) + " = " + str(balance_operativo) + r" \text{ margen}")

    # Notificación estilizada para la Pestaña B
    if pedidos_diarios > capacidad_total_flota or "Calor" in demanda_estacional:
        st.markdown(f"""
        <div class="alert-card-warning">
            ⚠️ <strong>ESTATUS LOGÍSTICO (ALERTA):</strong> Capacidad de flota: <strong>{capacidad_total_flota} garrafones</strong> | Demanda de pedidos: <strong>{pedidos_diarios} garrafones</strong><br>
            <em>Diagnóstico: Operación bajo alta exigencia o déficit de cobertura por {demanda_estacional}.</em>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="alert-card-success">
            ✅ <strong>ESTATUS LOGÍSTICO (ESTABLE):</strong> Capacidad de flota: <strong>{capacidad_total_flota} garrafones</strong> | Demanda de pedidos: <strong>{pedidos_diarios} garrafones</strong><br>
            <em>Diagnóstico: Cobertura óptima dentro de los parámetros de ruta habituales.</em>
        </div>
        """, unsafe_allow_html=True)

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
