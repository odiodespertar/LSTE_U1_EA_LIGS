import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos Prácticos - Enfoque Sistémico Interactivo y Secuencial",
    page_icon="💧",
    layout="wide",
)

# Estilos CSS avanzados con colores renovados, tarjetas interactivas, fórmulas y avance secuencial por clics
st.markdown("""
    <style>
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #e0f2fe 100%, #bae6fd 0%) !important;
        border: 2px solid #0284c7 !important;
        border-radius: 12px !important;
        color: #0369a1 !important;
        font-weight: 800 !important;
        font-size: 15px !important;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.2);
    }

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

    /* Tarjetas base de la secuencia */
    .card-paso {
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        min-height: 210px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: all 0.5s ease-in-out;
    }

    /* Tarjetas inactivas / atenuadas en la secuencia */
    .card-inactiva {
        background: #ffffff;
        border: 2px dashed #cbd5e1;
        color: #94a3b8;
        opacity: 0.5;
        transform: scale(0.97);
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }

    /* Tarjetas activas (con foco secuencial dinámico) */
    .card-activa-entrada {
        background: linear-gradient(135deg, #ffffff 0%, #e0f2fe 100%);
        border: 4px solid #0284c7;
        color: #0f172a;
        box-shadow: 0 12px 30px rgba(2, 132, 199, 0.35);
        transform: scale(1.04);
        animation: pulseActive 1.5s infinite alternate;
    }

    .card-activa-proceso {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 4px solid #f59e0b;
        color: #ffffff;
        box-shadow: 0 12px 30px rgba(245, 158, 11, 0.35);
        transform: scale(1.04);
        animation: pulseActive 1.5s infinite alternate;
    }

    .card-activa-salida {
        background: linear-gradient(135deg, #ffffff 0%, #dcfce7 100%);
        border: 4px solid #16a34a;
        color: #0f172a;
        box-shadow: 0 12px 30px rgba(22, 163, 74, 0.35);
        transform: scale(1.04);
        animation: pulseActive 1.5s infinite alternate;
    }

    .card-activa-retro {
        background: linear-gradient(135deg, #ffffff 0%, #ffedd5 100%);
        border: 4px solid #ea580c;
        color: #0f172a;
        box-shadow: 0 12px 30px rgba(234, 88, 12, 0.35);
        transform: scale(1.04);
        animation: pulseActive 1.5s infinite alternate;
    }

    @keyframes pulseActive {
        0% { transform: scale(1.02); }
        100% { transform: scale(1.06); }
    }

    /* Banner informativo estático superior */
    .static-banner {
        background: linear-gradient(90deg, #e0f2fe 0%, #fef3c7 50%, #dcfce7 100%);
        padding: 12px 18px;
        border-radius: 12px;
        font-weight: 800;
        color: #0369a1;
        margin-bottom: 15px;
        border: 2px solid #0284c7;
        font-size: 14px;
        text-align: center;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
    }
    
    .floating-icon {
        display: inline-block;
        font-size: 22px;
        margin: 0 6px;
        animation: floatIcon 2s ease-in-out infinite alternate;
    }

    @keyframes floatIcon {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-5px); }
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
    st.markdown("### 4. Modelo Sistémico Integral: Cálculos en Tiempo Real y Avance Secuencial")
    st.markdown("<p style='font-size:13px; margin:0;'><strong>Estudiante:</strong> Liliana García Solís | <strong>Matrícula:</strong> ES251101336 | <strong>Asignatura:</strong> Sistemas de Transporte</p>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# INDICACIONES EXPANDIBLE
# ==========================================
with st.expander("👉 Guía Interactiva, Fórmulas y Recorrido Secuencial", expanded=False):
    st.markdown("""
    <div style="background-color: #f0f9ff; padding: 10px; border-radius: 6px; border: 1px solid #7dd3fc; font-size: 13px;">
        <p style="margin: 0 0 5px 0; font-weight: bold; color: #0369a1;">Instrucciones de Uso:</p>
        <ul style="margin: 0; padding-left: 18px; color: #0c4a6e;">
            <li><strong>Cálculos dinámicos:</strong> Mueve las barras deslizantes (sliders) para actualizar instantáneamente las fórmulas de oferta, demanda y saturación.</li>
            <li><strong>Avance secuencial interactivo:</strong> Utiliza el botón de avance para recorrer la secuencia paso a paso (Entrada ➔ Proceso ➔ Salida ➔ Retroalimentación) con iluminación dinámica.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2 = st.tabs([
    "A. Sistema Multimodal: CETRAM El Rosario (Pasajeros)",
    "B. Distribución de Carga: Agua en Garrafón (Mercancías)"
])

# Inicializar estados de secuencia si no existen
if "paso_seq_a" not in st.session_state:
    st.session_state.paso_seq_a = 1
if "paso_seq_b" not in st.session_state:
    st.session_state.paso_seq_b = 1

# ==========================================
# PESTAÑA A: CETRAM EL ROSARIO
# ==========================================
with tab1:
    st.markdown("<p style='font-weight: bold; color: #0284c7; margin-bottom: 5px;'>A. Sistema multimodal de pasajeros en CETRAM El Rosario (Sistema Abierto)</p>", unsafe_allow_html=True)

    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    with col_c1:
        num_trenes = st.slider("🚆 Trenes (L6/L7)", 10, 50, 25, key="t_pax_c")
    with col_c2:
        num_buses = st.slider("🚍 Unidades", 5, 40, 20, key="b_pax_c")
    with col_c3:
        pasajeros_flota = st.slider("👥 Demanda (Pax)", 500, 5000, 2000, step=100, key="p_flota_c")
    with col_c4:
        horario_operativo = st.selectbox("🕒 Franja Horaria:", ["Pico Matutina", "Hora Valle", "Pico Nocturna"], key="h_pax_c")

    # Cálculos y fórmulas en tiempo real
    capacidad_oferta = (num_trenes + num_buses) * 110
    tasa_saturacion = (pasajeros_flota / capacidad_oferta) * 100 if capacidad_oferta > 0 else 0

    st.markdown("""
        <div class="static-banner">
            🚀 FLUJO ACTIVO SISTÉMICO: <span class="floating-icon">🚆</span> Trenes y <span class="floating-icon">🚍</span> Buses sincronizados con <span class="floating-icon">👥</span> Homeostasis Dinámica
        </div>
    """, unsafe_allow_html=True)

    # Controles de avance secuencial interactivo
    col_btn_seq1, col_btn_seq2, col_btn_seq3 = st.columns([2, 2, 3])
    with col_btn_seq1:
        if st.button("▶️ Avanzar Secuencia (Siguiente Paso)", use_container_width=True, key="avanzar_a"):
            st.session_state.paso_seq_a = (st.session_state.paso_seq_a % 4) + 1
    with col_btn_seq2:
        if st.button("🔄 Reiniciar Ciclo", use_container_width=True, key="reiniciar_a"):
            st.session_state.paso_seq_a = 1
    with col_btn_seq3:
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #0369a1; padding-top: 6px;'>Paso activo: {st.session_state.paso_seq_a} / 4</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sistema-compacto-box">
            <div class="ambiente-titulo">🌐 AMBIENTE: Entorno Urbano / Zona Norte (Azcapotzalco)</div>
    """, unsafe_allow_html=True)

    col_n1, col_n2, col_n3, col_n4 = st.columns(4)

    # 1. ENTRADA
    with col_n1:
        if st.session_state.paso_seq_a == 1:
            st.markdown(f"""
            <div class="card-paso card-activa-entrada">
                <h4 style="color: #0284c7; margin: 0 0 6px 0; font-size: 13px; font-weight: 900;">📥 1. ENTRADA (Insumos)</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3;">
                    <strong>Recursos:</strong> {num_trenes} trenes, {num_buses} buses.<br>
                    <strong>Demanda:</strong> <span style="color: #0284c7; font-weight: bold;">{pasajeros_flota} pax</span><br>
                    <em>Oferta: ({num_trenes}+{num_buses})×110 = {capacidad_oferta} pax</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700;">📥 1. ENTRADA</h4>
                <p style="font-size: 10px; margin: 0;">En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    # 2. PROCESAMIENTO
    with col_n2:
        if st.session_state.paso_seq_a == 2:
            st.markdown(f"""
            <div class="card-paso card-activa-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 6px 0; font-size: 13px; font-weight: 900;">⚙️ 2. PROCESAMIENTO</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3; color: #f8fafc;">
                    Regulación de flujos y transbordos.<br>
                    <strong>Franja:</strong> {horario_operativo}<br>
                    <em>Carga: ({pasajeros_flota}/{capacidad_oferta})×100 = {tasa_saturacion:.1f}%</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700;">⚙️ 2. PROCESO</h4>
                <p style="font-size: 10px; margin: 0;">En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    # 3. SALIDA
    with col_n3:
        if st.session_state.paso_seq_a == 3:
            st.markdown(f"""
            <div class="card-paso card-activa-salida">
                <h4 style="color: #16a34a; margin: 0 0 6px 0; font-size: 13px; font-weight: 900;">📤 3. SALIDA (Producto)</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3;">
                    <strong>Exportación al medio:</strong><br>
                    <span style="color: #16a34a; font-weight: bold;">{pasajeros_flota} pax</span> atendidos y transferidos con éxito a la red.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700;">📤 3. SALIDA</h4>
                <p style="font-size: 10px; margin: 0;">En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    # 4. RETROALIMENTACIÓN
    with col_n4:
        if st.session_state.paso_seq_a == 4:
            if pasajeros_flota > capacidad_oferta:
                txt_r = f"⚠️ Alerta: Demanda supera oferta ({tasa_saturacion:.1f}%). Requiere ajuste de frecuencias."
            else:
                txt_r = f"✅ Homeostasis óptima: Flujo estable ({tasa_saturacion:.1f}% de ocupación)."
            
            st.markdown(f"""
            <div class="card-paso card-activa-retro">
                <h4 style="color: #ea580c; margin: 0 0 6px 0; font-size: 12px; font-weight: 900;">🔄 4. RETROALIMENTACIÓN</h4>
                <p style="font-size: 10px; margin: 0; line-height: 1.3; color: #9a3412; font-weight: 700;">
                    {txt_r}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700;">🔄 4. RETRO</h4>
                <p style="font-size: 10px; margin: 0;">En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA
# ==========================================
with tab2:
    st.markdown("<p style='font-weight: bold; color: #16a34a; margin-bottom: 5px;'>B. Distribución de agua en garrafón en U.H. El Rosario (Logística de Carga)</p>", unsafe_allow_html=True)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        unidades_reparto = st.slider("🚚 Vehículos de redilas", 1, 10, 3, key="slider_camiones_c")
    with col_d2:
        pedidos_diarios = st.slider("💧 Pedidos (Garrafones)", 50, 400, 150, step=10, key="slider_pedidos_c")
    with col_d3:
        demanda_estacional = st.selectbox("🌤️ Temporada:", ["Regular", "Calor (Alta)"], key="d_estacional_c")

    # Cálculos logísticos en tiempo real
    capacidad_total_flota = unidades_reparto * 50
    eficiencia_flota = (pedidos_diarios / capacidad_total_flota) * 100 if capacidad_total_flota > 0 else 0

    st.markdown("""
        <div class="static-banner" style="background: linear-gradient(90deg, #dcfce7 0%, #fef3c7 50%, #e0f2fe 100%); color: #16a34a; border-color: #16a34a;">
            🚚 RUTA LOGÍSTICA ACTIVA: <span class="floating-icon">🚚</span> Flota de Reparto y <span class="floating-icon">💧</span> Garrafones en Avance Dinámico
        </div>
    """, unsafe_allow_html=True)

    col_btn_seqb1, col_btn_seqb2, col_btn_seqb3 = st.columns([2, 2, 3])
    with col_btn_seqb1:
        if st.button("▶️ Avanzar Secuencia (B)", use_container_width=True, key="avanzar_b"):
            st.session_state.paso_seq_b = (st.session_state.paso_seq_b % 4) + 1
    with col_btn_seqb2:
        if st.button("🔄 Reiniciar Ciclo (B)", use_container_width=True, key="reiniciar_b"):
            st.session_state.paso_seq_b = 1
    with col_btn_seqb3:
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #16a34a; padding-top: 6px;'>Paso activo: {st.session_state.paso_seq_b} / 4</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sistema-compacto-box" style="border-color: #16a34a; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);">
            <div class="ambiente-titulo" style="color: #16a34a;">🌐 AMBIENTE: U.H. El Rosario (Zona Suburbana)</div>
    """, unsafe_allow_html=True)

    col_bn1, col_bn2, col_bn3, col_bn4 = st.columns(4)

    # 1. ENTRADA B
    with col_bn1:
        if st.session_state.paso_seq_b == 1:
            st.markdown(f"""
            <div class="card-paso card-activa-entrada">
                <h4 style="color: #0284c7; margin: 0 0 6px 0; font-size: 13px; font-weight: 900;">📥 1. ENTRADA (Insumos)</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3;">
                    <strong>Vehículos:</strong> {unidades_reparto} unidades.<br>
                    <strong>Demanda:</strong> <span style="color: #0284c7; font-weight: bold;">{pedidos_diarios} garrafones</span><br>
                    <em>Capacidad: {unidades_reparto}×50 = {capacidad_total_flota} un.</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700;">📥 1. ENTRADA</h4>
                <p style="font-size: 10px; margin: 0;">En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    # 2. PROCESO B
    with col_bn2:
        if st.session_state.paso_seq_b == 2:
            st.markdown(f"""
            <div class="card-paso card-activa-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 6px 0; font-size: 13px; font-weight: 900;">⚙️ 2. PROCESAMIENTO</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3; color: #f0fdf4;">
                    Ruteo domiciliario y conversión.<br>
                    <strong>Temporada:</strong> {demanda_estacional}<br>
                    <em>Uso de flota: ({pedidos_diarios}/{capacidad_total_flota})×100 = {eficiencia_flota:.1f}%</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700;">⚙️ 2. PROCESO</h4>
                <p style="font-size: 10px; margin: 0;">En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    # 3. SALIDA B
    with col_bn3:
        if st.session_state.paso_seq_b == 3:
            st.markdown(f"""
            <div class="card-paso card-activa-salida">
                <h4 style="color: #16a34a; margin: 0 0 6px 0; font-size: 13px; font-weight: 900;">📤 3. SALIDA (Producto)</h4>
                <p style="font-size: 11px; margin: 0; line-height: 1.3;">
                    <strong>Exportación:</strong><br>
                    <span style="color: #16a34a; font-weight: bold;">{pedidos_diarios} garrafones</span> entregados con éxito en hogares.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700;">📤 3. SALIDA</h4>
                <p style="font-size: 10px; margin: 0;">En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    # 4. RETROALIMENTACIÓN B
    with col_bn4:
        if st.session_state.paso_seq_b == 4:
            if pedidos_diarios > capacidad_total_flota:
                txt_rb = f"⚠️ Ajuste necesario: Demanda supera capacidad ({eficiencia_flota:.1f}%). Requiere ruta extra."
            else:
                txt_rb = f"✅ Homeostasis lograda: Reparto y retorno estables ({eficiencia_flota:.1f}%)."
            
            st.markdown(f"""
            <div class="card-paso card-activa-retro">
                <h4 style="color: #ea580c; margin: 0 0 6px 0; font-size: 12px; font-weight: 900;">🔄 4. RETROALIMENTACIÓN</h4>
                <p style="font-size: 10px; margin: 0; line-height: 1.3; color: #9a3412; font-weight: 700;">
                    {txt_rb}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700;">🔄 4. RETRO</h4>
                <p style="font-size: 10px; margin: 0;">En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
