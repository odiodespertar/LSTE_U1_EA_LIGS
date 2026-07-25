import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos Prácticos - Teoría de Sistemas",
    page_icon="💧",
    layout="wide",
)

# Estilos CSS avanzados para mantener todo en un solo plano horizontal/compacto sin desplazamiento excesivo
st.markdown("""
    <style>
    /* Estilos personalizados para el botón desplegable */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #fff9c4 0%, #ffe082 100%) !important;
        border: 2px solid #ff8f00 !important;
        border-radius: 12px !important;
        color: #d84315 !important;
        font-weight: 800 !important;
        font-size: 15px !important;
        box-shadow: 0 4px 15px rgba(255, 143, 0, 0.3);
    }

    /* Contenedor compacto de una sola vista horizontal para evitar scroll vertical */
    .sistema-compacto-box {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 3px solid #cbd5e1;
        border-radius: 20px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
    }

    .ambiente-titulo {
        text-align: center;
        font-size: 18px;
        font-weight: 900;
        color: #1e293b;
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Tarjetas de flujo horizontal compacto con animación de aparición */
    .card-paso {
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        color: #1e293b;
        box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        animation: fadeInScale 0.4s ease-in-out;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .card-entrada {
        background: linear-gradient(135deg, #ffffff 0%, #e1f5fe 100%);
        border: 3px solid #0288d1;
    }

    .card-proceso {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: #ffffff;
        border: 3px solid #f59e0b;
    }

    .card-salida {
        background: linear-gradient(135deg, #ffffff 0%, #e8f5e9 100%);
        border: 3px solid #2e7d32;
    }

    .card-retro {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border: 3px solid #f57c00;
    }

    @keyframes fadeInScale {
        0% { opacity: 0; transform: scale(0.95); }
        100% { opacity: 1; transform: scale(1); }
    }

    .moving-banner {
        overflow: hidden;
        white-space: nowrap;
        background: linear-gradient(90deg, #e1f5fe 0%, #fff9c4 50%, #e8f5e9 100%);
        padding: 8px 12px;
        border-radius: 8px;
        font-weight: 800;
        color: #d84315;
        margin-bottom: 12px;
        border: 2px solid #ffb300;
        font-size: 14px;
    }
    
    .floating-icon {
        display: inline-block;
        font-size: 20px;
        margin: 0 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera institucional compacta
col_logo, col_txt = st.columns([1, 6])
with col_logo:
    try:
        st.image("UnADM LOGO.png", width=110)
    except Exception:
        pass

with col_txt:
    st.markdown("### 4. Diseño o modelo de transporte aplicando teoría de sistemas")
    st.markdown("<p style='font-size:13px; margin:0;'><strong>Estudiante:</strong> Liliana García Solís | <strong>Matrícula:</strong> ES251101336 | <strong>Asignatura:</strong> Sistemas de Transporte</p>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# INDICACIONES EXPANDIBLE
# ==========================================
with st.expander("👉 Indicaciones y Guía Interactiva Compacta", expanded=False):
    st.markdown("""
    <div style="background-color: #fffde7; padding: 10px; border-radius: 6px; border: 1px solid #ffd54f; font-size: 13px;">
        <p style="margin: 0 0 5px 0; font-weight: bold; color: #3e2723;">Instrucciones:</p>
        <ul style="margin: 0; padding-left: 18px; color: #4e342e;">
            <li>Usa los botones horizontales de abajo para activar cada etapa del sistema paso a paso.</li>
            <li>Todo el diagrama interactivo cabe en una sola vista horizontal para evitar desplazamiento vertical.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Pestañas principales
tab1, tab2 = st.tabs([
    "A. Sistema Multimodal: CETRAM El Rosario (Pasajeros)",
    "B. Distribución de Carga: Agua en Garrafón (Mercancías)"
])

# ==========================================
# PESTAÑA A: CETRAM EL ROSARIO
# ==========================================
with tab1:
    st.markdown("<p style='font-weight: bold; color: #0288d1; margin-bottom: 5px;'>A. Sistema multimodal de pasajeros en CETRAM El Rosario</p>", unsafe_allow_html=True)

    # Controles compactos en una sola línea
    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    with col_c1:
        num_trenes = st.slider("🚆 Trenes (L6/L7)", 10, 50, 25, key="t_pax_c")
    with col_c2:
        num_buses = st.slider("🚍 Unidades", 5, 40, 20, key="b_pax_c")
    with col_c3:
        pasajeros_flota = st.slider("👥 Pasajeros", 500, 5000, 2000, step=100, key="p_flota_c")
    with col_c4:
        horario_operativo = st.selectbox("🕒 Horario:", ["Pico Matutina", "Valle", "Pico Nocturna"], key="h_pax_c")

    capacidad_oferta = (num_trenes + num_buses) * 110

    st.markdown("""
        <div class="moving-banner">
            <span>Flujo Activo: </span><span class="floating-icon">🚆</span><span class="floating-icon">🚍</span><span class="floating-icon">👥</span> Sincronización Interactiva en una sola vista
        </div>
    """, unsafe_allow_html=True)

    # Controles interactivos por botones en horizontal (simulando los botones que pidió)
    st.markdown("<p style='font-size: 13px; font-weight: bold; text-align: center; color: #334155; margin-bottom: 8px;'>👆 Haz clic en cada etapa para revelar el flujo paso a paso:</p>", unsafe_allow_html=True)

    b_col1, b_col2, b_col3, b_col4 = st.columns(4)
    
    # Inicializar estado de sesión para los clics interactivos si no existen
    if "ver_entrada_a" not in st.session_state:
        st.session_state.ver_entrada_a = True
    if "ver_proceso_a" not in st.session_state:
        st.session_state.ver_proceso_a = True
    if "ver_salida_a" not in st.session_state:
        st.session_state.ver_salida_a = True
    if "ver_retro_a" not in st.session_state:
        st.session_state.ver_retro_a = True

    with b_col1:
        if st.button("📥 1. Ver ENTRADA", use_container_width=True):
            st.session_state.ver_entrada_a = not st.session_state.ver_entrada_a
    with b_col2:
        if st.button("⚙️ 2. Pasar a PROCESO", use_container_width=True):
            st.session_state.ver_proceso_a = not st.session_state.ver_proceso_a
    with b_col3:
        if st.button("📤 3. Pasar a SALIDA", use_container_width=True):
            st.session_state.ver_salida_a = not st.session_state.ver_salida_a
    with b_col4:
        if st.button("🔄 4. Ver RETROALIMENTACIÓN", use_container_width=True):
            st.session_state.ver_retro_a = not st.session_state.ver_retro_a

    # Contenedor de visualización horizontal en un solo plano
    st.markdown("""
        <div class="sistema-compacto-box">
            <div class="ambiente-titulo">🌐 AMBIENTE: Entorno Urbano / Zona Norte (Azcapotzalco)</div>
    """, unsafe_allow_html=True)

    # Columnas horizontales para que todo quede en un mismo plano sin bajar la pantalla
    col_n1, col_n2, col_n3, col_n4 = st.columns(4)

    with col_n1:
        if st.session_state.ver_entrada_a:
            st.markdown(f"""
            <div class="card-paso card-entrada">
                <h4 style="color: #0288d1; margin: 0 0 8px 0; font-size: 15px; font-weight: 900;">📥 1. ENTRADA</h4>
                <p style="font-size: 12px; margin: 0; line-height: 1.3;">
                    <strong>Flota:</strong> {num_trenes} trenes, {num_buses} buses.<br>
                    <strong>Demanda:</strong> <span style="color: #d32f2f; font-weight: bold;">{pasajeros_flota} pax</span>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Entrada oculta")

    with col_n2:
        if st.session_state.ver_proceso_a:
            st.markdown(f"""
            <div class="card-paso card-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 8px 0; font-size: 15px; font-weight: 900;">⚙️ 2. PROCESO</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3; color: #f8fafc;">
                    Regulación de flujos y correspondencia multimodal.<br><em>{horario_operativo}</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Proceso oculto")

    with col_n3:
        if st.session_state.ver_salida_a:
            st.markdown(f"""
            <div class="card-paso card-salida">
                <h4 style="color: #2e7d32; margin: 0 0 8px 0; font-size: 15px; font-weight: 900;">📤 3. SALIDA</h4>
                <p style="font-size: 12px; margin: 0; line-height: 1.3;">
                    <strong>Resultado:</strong><br><span style="color: #2e7d32; font-weight: bold;">{pasajeros_flota} pax</span> transferidos con éxito a su destino.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Salida oculta")

    with col_n4:
        if st.session_state.ver_retro_a:
            if pasajeros_flota > capacidad_oferta:
                txt_r = "⚠️ Alerta: Saturación detectada en andenes."
            else:
                txt_r = "✅ Estable: Flujo óptimo y seguro."
            st.markdown(f"""
            <div class="card-paso card-retro">
                <h4 style="color: #e65100; margin: 0 0 8px 0; font-size: 14px; font-weight: 900;">🔄 4. RETROALIMENTACIÓN</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3; color: #bf360c; font-weight: 700;">
                    {txt_r}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Retro oculta")

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA
# ==========================================
with tab2:
    st.markdown("<p style='font-weight: bold; color: #15803d; margin-bottom: 5px;'>B. Distribución de agua en garrafón en U.H. El Rosario</p>", unsafe_allow_html=True)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        unidades_reparto = st.slider("🚚 Vehículos de redilas", 1, 10, 3, key="slider_camiones_c")
    with col_d2:
        pedidos_diarios = st.slider("💧 Pedidos (Garrafones)", 50, 400, 150, step=10, key="slider_pedidos_c")
    with col_d3:
        demanda_estacional = st.selectbox("🌤️ Temporada:", ["Regular", "Calor (Alta)"], key="d_estacional_c")

    capacidad_total_flota = unidades_reparto * 50

    st.markdown("""
        <div class="moving-banner" style="background: linear-gradient(90deg, #e8f5e9 0%, #c8e6c9 100%); color: #1b5e20; border-color: #66bb6a;">
            <span>Ruta Logística: </span><span class="floating-icon">🚚</span><span class="floating-icon">💧</span><span class="floating-icon">📦</span> Reparto Local Sincronizado en una vista
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size: 13px; font-weight: bold; text-align: center; color: #334155; margin-bottom: 8px;'>👆 Haz clic en cada etapa para revelar el flujo de mercancías:</p>", unsafe_allow_html=True)

    bb_col1, bb_col2, bb_col3, bb_col4 = st.columns(4)

    if "ver_entrada_b" not in st.session_state:
        st.session_state.ver_entrada_b = True
    if "ver_proceso_b" not in st.session_state:
        st.session_state.ver_proceso_b = True
    if "ver_salida_b" not in st.session_state:
        st.session_state.ver_salida_b = True
    if "ver_retro_b" not in st.session_state:
        st.session_state.ver_retro_b = True

    with bb_col1:
        if st.button("📥 1. Ver ENTRADA (B)", use_container_width=True):
            st.session_state.ver_entrada_b = not st.session_state.ver_entrada_b
    with bb_col2:
        if st.button("⚙️ 2. Pasar a PROCESO (B)", use_container_width=True):
            st.session_state.ver_proceso_b = not st.session_state.ver_proceso_b
    with bb_col3:
        if st.button("📤 3. Pasar a SALIDA (B)", use_container_width=True):
            st.session_state.ver_salida_b = not st.session_state.ver_salida_b
    with bb_col4:
        if st.button("🔄 4. Ver RETRO (B)", use_container_width=True):
            st.session_state.ver_retro_b = not st.session_state.ver_retro_b

    st.markdown("""
        <div class="sistema-compacto-box" style="border-color: #16a34a; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);">
            <div class="ambiente-titulo" style="color: #15803d;">🌐 AMBIENTE: U.H. El Rosario (Zona Suburbana)</div>
    """, unsafe_allow_html=True)

    col_bn1, col_bn2, col_bn3, col_bn4 = st.columns(4)

    with col_bn1:
        if st.session_state.ver_entrada_b:
            st.markdown(f"""
            <div class="card-paso" style="border: 3px solid #16a34a; background: #ffffff;">
                <h4 style="color: #15803d; margin: 0 0 8px 0; font-size: 15px; font-weight: 900;">📥 1. ENTRADA</h4>
                <p style="font-size: 12px; margin: 0; line-height: 1.3;">
                    <strong>Flota:</strong> {unidades_reparto} vehículos.<br>
                    <strong>Demanda:</strong> <span style="color: #15803d; font-weight: bold;">{pedidos_diarios} garrafones</span>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Oculto")

    with col_bn2:
        if st.session_state.ver_proceso_b:
            st.markdown(f"""
            <div class="card-paso" style="background: linear-gradient(135deg, #14532d 0%, #052e16 100%); border: 3px solid #22c55e; color: #ffffff;">
                <h4 style="color: #4ade80; margin: 0 0 8px 0; font-size: 15px; font-weight: 900;">⚙️ 2. PROCESO</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3; color: #f0fdf4;">
                    Ruteo domiciliario y carga vehicular.<br><em>{demanda_estacional}</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Oculto")

    with col_bn3:
        if st.session_state.ver_salida_b:
            st.markdown(f"""
            <div class="card-paso" style="border: 3px solid #16a34a; background: #ffffff;">
                <h4 style="color: #15803d; margin: 0 0 8px 0; font-size: 15px; font-weight: 900;">📤 3. SALIDA</h4>
                <p style="font-size: 12px; margin: 0; line-height: 1.3;">
                    <strong>Resultado:</strong><br><span style="color: #15803d; font-weight: bold;">{pedidos_diarios} entregados</span> con éxito en hogares.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Oculto")

    with col_bn4:
        if st.session_state.ver_retro_b:
            if pedidos_diarios > capacidad_total_flota:
                txt_rb = "⚠️ Alerta: Demanda supera capacidad de flota."
            else:
                txt_rb = "✅ Estable: Reparto cumplido al 100%."
            st.markdown(f"""
            <div class="card-paso" style="border: 3px solid #15803d; background: #f0fdf4;">
                <h4 style="color: #15803d; margin: 0 0 8px 0; font-size: 14px; font-weight: 900;">🔄 4. RETROALIMENTACIÓN</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3; color: #064e3b; font-weight: 700;">
                    {txt_rb}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Oculto")

    st.markdown("</div>", unsafe_allow_html=True)
