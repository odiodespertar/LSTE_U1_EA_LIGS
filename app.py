import streamlit as st
import numpy as np
import math


# ==========================================================
# FUNCIONES DEL MODELO SISTÉMICO
# ==========================================================

def calcular_modelo_manheim(T, A, capacidad_total):
    """
    Modelo simplificado basado en Manheim (1979)

    T = Sistema de Transporte
    A = Sistema de Actividades
    V = Volumen de flujo
    S = Nivel de servicio
    F0 = Equilibrio operativo
    """

    V = A

    if capacidad_total > 0 and V > 0:
        S = capacidad_total / V
    else:
        S = 0

    saturacion = (V / capacidad_total) * 100 if capacidad_total else 0

    if saturacion <= 85:
        estado = "🟢 Homeostasis óptima"
    elif saturacion <= 100:
        estado = "🟡 Cercano a saturación"
    else:
        estado = "🔴 Sistema saturado"

    F0 = {
        "Volumen": V,
        "Nivel_servicio": S,
        "Saturacion": saturacion,
        "Estado": estado
    }

    return F0


def recomendar_unidades(deficit, capacidad_unidad):
    """
    Calcula unidades adicionales necesarias
    """
    if deficit <= 0:
        return 0

    return math.ceil(deficit / capacidad_unidad)


# ==========================================================
# CONFIGURACIÓN DE STREAMLIT
# ==========================================================

st.set_page_config(
    page_title="Modelos Prácticos - Enfoque Sistémico Interactivo",
    page_icon="💧",
    layout="wide",
)

# Estilos CSS avanzados
st.markdown("""
    <style>
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #e0f2fe 100%, #bae6fd 0%) !important;
        border: 2px solid #0284c7 !important;
        border-radius: 12px !important;
        color: #0369a1 !important;
        font-weight: 800 !important;
        font-size: 20px !important;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.2);
    }

    .instrucciones-box {
        background-color: #f0f9ff;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #7dd3fc;
        font-size: 19px !important;
        color: #0c4a6e;
    }
    
    .instrucciones-box p, .instrucciones-box li {
        font-size: 19px !important;
        line-height: 1.6 !important;
    }

    .nota-calculo {
        background-color: #fffbeb;
        border-left: 4px solid #f59e0b;
        padding: 10px 14px;
        border-radius: 6px;
        font-size: 14px;
        color: #b45309;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .ambiente-titulo-naranja {
        text-align: center;
        font-size: 22px;
        font-weight: 900;
        color: #7c2d12;
        background: linear-gradient(90deg, #ffedd5 0%, #fed7aa 100%);
        padding: 14px 20px;
        border-radius: 12px;
        border: 2px solid #f97316;
        margin-bottom: 22px;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(249, 115, 22, 0.2);
    }

    .ambiente-titulo-b {
        text-align: center;
        font-size: 22px;
        font-weight: 900;
        color: #064e3b;
        background: linear-gradient(90deg, #d1fae5 0%, #a7f3d0 100%);
        padding: 14px 20px;
        border-radius: 12px;
        border: 2px solid #10b981;
        margin-bottom: 22px;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
    }

    .card-paso {
        border-radius: 18px;
        padding: 24px;
        text-align: center;
        min-height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: all 0.5s ease-in-out;
    }

    .card-inactiva {
        background: #ffffff;
        border: 2px dashed #cbd5e1;
        color: #475569;
        opacity: 0.75;
        transform: scale(0.97);
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }
    
    .card-inactiva h4 {
        font-size: 18px !important;
        font-weight: 800 !important;
        color: #334155 !important;
    }

    .card-inactiva p {
        font-size: 16px !important;
        color: #475569 !important;
        font-weight: 600 !important;
    }

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

    .dynamic-banner {
        background: linear-gradient(90deg, #e0f2fe 0%, #fef3c7 50%, #dcfce7 100%);
        padding: 16px 22px;
        border-radius: 12px;
        font-weight: 800;
        color: #0369a1;
        margin-bottom: 18px;
        border: 2px solid #0284c7;
        font-size: 17px;
        text-align: center;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
    }
    
    .floating-icon {
        display: inline-block;
        font-size: 26px;
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
    st.markdown("### 4. Diseño o modelo de transporte aplicando Teoría de Sistemas en mi localidad")
    st.markdown("<p style='font-size:16px; margin:0;'><strong>Estudiante:</strong> Liliana García Solís | <strong>Matrícula:</strong> ES251101336 | <strong>Asignatura:</strong> Sistemas de Transporte</p>", unsafe_allow_html=True)

st.markdown("---")

with st.expander("👉 Indicaciones de navegación", expanded=False):
    st.markdown("""
    <div class="instrucciones-box">
        <p style="margin: 0 0 8px 0; font-weight: bold; color: #0369a1; font-size: 20px !important;">Instrucciones de Uso:</p>
        <ul style="margin: 0; padding-left: 20px; color: #0c4a6e;">
            <li style="margin-bottom: 8px;"><strong>Controles interactivos:</strong> Modifica los sliders, la franja horaria y la temporada; observa cómo el procesamiento y las alertas dinámicas superiores se actualizan de inmediato.</li>
            <li><strong>Avance secuencial por clics:</strong> Utiliza el botón de "Avanzar secuencia" para recorrer la secuencia paso a paso de entradas, proceso, salida y retroalimentación.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2 = st.tabs([
    "A. Sistema Multimodal: CETRAM El Rosario (Pasajeros)",
    "B. Distribución de Carga: Agua en Garrafón U.H. El Rosario (Mercancías)"
])

if "paso_seq_a" not in st.session_state:
    st.session_state.paso_seq_a = 1
if "paso_seq_b" not in st.session_state:
    st.session_state.paso_seq_b = 1

# ==========================================
# PESTAÑA A: CETRAM EL ROSARIO
# ==========================================
with tab1:
    st.markdown("<p style='font-weight: bold; color: #ea580c; font-size: 18px; margin-bottom: 8px;'>A. Sistema multimodal de pasajeros en CETRAM El Rosario (Sistema Abierto)</p>", unsafe_allow_html=True)

    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    with col_c1:
        num_trenes = st.slider("🚆 Trenes (L6/L7)", 10, 50, 25, key="t_pax_c")
    with col_c2:
        num_buses = st.slider("🚍 Unidades", 5, 40, 20, key="b_pax_c")
    with col_c3:
        pasajeros_flota = st.slider("👥 Demanda Base (Pax)", 500, 5000, 2000, step=100, key="p_flota_c")
    with col_c4:
        horario_operativo = st.selectbox("🕒 Franja Horaria:", ["Pico Matutina", "Hora Valle", "Pico Nocturna"], key="h_pax_c")

    if horario_operativo == "Pico Matutina":
        factor_franja = 1.35
        desc_franja = "Alta congestión (+35% demanda)"
    elif horario_operativo == "Pico Nocturna":
        factor_franja = 1.20
        desc_franja = "Demanda moderada (+20% demanda)"
    else:
        factor_franja = 0.85
        desc_franja = "Flujo regular / Valle (-15% demanda)"

    matriz_capacidad = np.array([
        ["Metro Línea 6", num_trenes, 110],
        ["Metro Línea 7", num_trenes, 110],
        ["Autobuses", num_buses, 80]
    ], dtype=object)

    capacidad_l6 = int(matriz_capacidad[0, 1]) * int(matriz_capacidad[0, 2])
    capacidad_l7 = int(matriz_capacidad[1, 1]) * int(matriz_capacidad[1, 2])
    capacidad_bus = int(matriz_capacidad[2, 1]) * int(matriz_capacidad[2, 2])

    capacidad_oferta = capacidad_l6 + capacidad_l7 + capacidad_bus
    demanda_ajustada = int(pasajeros_flota * factor_franja)

    # Nota explicativa sobre el cálculo de la franja horaria
    st.markdown(f"""
        <div class="nota-calculo">
            💡 <strong>Nota del modelo sistémico:</strong> La demanda base seleccionada ({pasajeros_flota} pax) se multiplica por el factor de la franja horaria <strong>{horario_operativo} ({factor_franja}x)</strong>, resultando en una <strong>demanda real de procesamiento de {demanda_ajustada} pax</strong>.
        </div>
    """, unsafe_allow_html=True)

    modelo_pasajeros = calcular_modelo_manheim(
        T=capacidad_oferta,
        A=demanda_ajustada,
        capacidad_total=capacidad_oferta
    )

    tasa_saturacion = modelo_pasajeros["Saturacion"]
    deficit_pasajeros = demanda_ajustada - capacidad_oferta
    trenes_extra = recomendar_unidades(deficit_pasajeros, 110)
    autobuses_extra = recomendar_unidades(deficit_pasajeros, 80)

    # BANNER DINÁMICO ACTUALIZADO SEGÚN LOS VALORES DE LAS BARRAS
    if tasa_saturacion > 100:
        alerta_banner_a = f"⚠️ ALERTA SISTÉMICA: Sobresaturación ({tasa_saturacion:.1f}%). Se sugieren {trenes_extra} tren(es) o {autobuses_extra} autobús(es) extra."
        color_b_a = "#dc2626"
    elif tasa_saturacion > 85:
        alerta_banner_a = f"⚠️ ADVERTENCIA: Sistema cerca del límite ({tasa_saturacion:.1f}% de saturación)."
        color_b_a = "#d97706"
    else:
        alerta_banner_a = f"✅ ESTABILIDAD OPERATIVA: {modelo_pasajeros['Estado']} con {tasa_saturacion:.1f}% de ocupación."
        color_b_a = "#0369a1"

    st.markdown(f"""
        <div class="dynamic-banner" style="color: {color_b_a}; border-color: {color_b_a};">
            🚀 FLUJO ACTIVO: <span class="floating-icon">🚆</span> {num_trenes} Trenes | <span class="floating-icon">🚍</span> {num_buses} Buses | <span class="floating-icon">👥</span> {demanda_ajustada} Pax<br>
            <span style="font-size: 15px;">{alerta_banner_a}</span>
        </div>
    """, unsafe_allow_html=True)

    col_btn_seq1, col_btn_seq2, col_btn_seq3 = st.columns([2, 2, 3])
    with col_btn_seq1:
        if st.button("▶️ Avanzar Secuencia (Siguiente Paso)", use_container_width=True, key="avanzar_a"):
            st.session_state.paso_seq_a = (st.session_state.paso_seq_a % 4) + 1
    with col_btn_seq2:
        if st.button("🔄 Reiniciar Ciclo", use_container_width=True, key="reiniciar_a"):
            st.session_state.paso_seq_a = 1
    with col_btn_seq3:
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #ea580c; font-size: 17px; padding-top: 8px;'>Paso activo: {st.session_state.paso_seq_a} / 4</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sistema-compacto-box" style="border-color: #f97316; background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%); border-radius: 20px; padding: 26px; margin: 16px 0; box-shadow: 0 10px 25px rgba(249, 115, 22, 0.15);">
            <div class="ambiente-titulo-naranja">🌐 AMBIENTE: Entorno Urbano / Zona Norte (Azcapotzalco)</div>
    """, unsafe_allow_html=True)

    col_n1, col_n2, col_n3, col_n4 = st.columns(4)

    with col_n1:
        if st.session_state.paso_seq_a == 1:
            st.markdown(f"""
            <div class="card-paso card-activa-entrada">
                <h4 style="color: #0284c7; margin: 0 0 12px 0; font-size: 21px; font-weight: 900;">📥 1. ENTRADA (Insumos)</h4>
                <p style="font-size: 17px; margin: 0; line-height: 1.6;">
                    <strong>Recursos:</strong> {num_trenes} trenes, {num_buses} buses.<br>
                    <strong>Demanda Base:</strong> <span style="color: #0284c7; font-weight: bold;">{pasajeros_flota} pax</span><br>
                    <em>Oferta: ({num_trenes}+{num_buses})×110 = {capacidad_oferta} pax</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📥 1. ENTRADA</h4>
                <p>En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n2:
        if st.session_state.paso_seq_a == 2:
            st.markdown(f"""
            <div class="card-paso card-activa-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 12px 0; font-size: 21px; font-weight: 900;">⚙️ 2. PROCESAMIENTO</h4>
                <p style="font-size: 17px; margin: 0; line-height: 1.6; color: #f8fafc;">
                    <strong>Franja:</strong> {horario_operativo} ({desc_franja})<br>
                    <strong>Demanda Real:</strong> <span style="color: #fbbf24; font-weight: bold;">{demanda_ajustada} pax</span><br>
                    <em>Carga: ({demanda_ajustada}/{capacidad_oferta})×100 = {tasa_saturacion:.1f}%</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>⚙️ 2. PROCESO</h4>
                <p>En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n3:
        if st.session_state.paso_seq_a == 3:
            st.markdown(f"""
            <div class="card-paso card-activa-salida">
                <h4 style="color: #16a34a; margin: 0 0 12px 0; font-size: 21px; font-weight: 900;">📤 3. SALIDA (Producto)</h4>
                <p style="font-size: 17px; margin: 0; line-height: 1.6;">
                    <strong>Exportación al medio:</strong><br>
                    <span style="color: #16a34a; font-weight: bold;">{demanda_ajustada} pax</span> atendidos y transferidos con éxito a la red multimodal.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📤 3. SALIDA</h4>
                <p>En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n4:
        if st.session_state.paso_seq_a == 4:
            if demanda_ajustada > capacidad_oferta:
                txt_r = (
                    f"⚠️ Sistema saturado ({tasa_saturacion:.1f}%). "
                    f"Demanda superior a capacidad. "
                    f"Se requieren aprox. {trenes_extra} tren(es) "
                    f"o {autobuses_extra} autobús(es) adicionales "
                    f"para restablecer el nivel de servicio."
                )
            else:
                txt_r = (
                    f"✅ {modelo_pasajeros['Estado']} "
                    f"({tasa_saturacion:.1f}% de ocupación). "
                    f"El flujo se mantiene dentro de la capacidad operativa."
                )

            st.markdown(f"""
            <div class="card-paso card-activa-retro">
                <h4 style="color: #ea580c; margin: 0 0 12px 0; font-size: 21px; font-weight: 900;">🔄 4. RETROALIMENTACIÓN</h4>
                <p style="font-size: 17px; margin: 0; line-height: 1.6; color: #9a3412; font-weight: 800;">
                    {txt_r}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>🔄 4. RETRO</h4>
                <p>En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA
# ==========================================
with tab2:
    st.markdown("<p style='font-weight: bold; color: #16a34a; font-size: 18px; margin-bottom: 8px;'>B. Distribución de agua en garrafón en U.H. El Rosario (Logística de Carga)</p>", unsafe_allow_html=True)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        unidades_reparto = st.slider("🚚 Vehículos de redilas", 1, 10, 3, key="slider_camiones_c")
    with col_d2:
        pedidos_diarios = st.slider("💧 Pedidos Base (Garrafones)", 50, 400, 150, step=10, key="slider_pedidos_c")
    with col_d3:
        demanda_estacional = st.selectbox("🌤️ Temporada:", ["Regular", "Calor (Alta)"], key="d_estacional_c")

    if demanda_estacional == "Calor (Alta)":
        factor_temp = 1.30
        desc_temp = "Alta demanda por calor (+30%)"
    else:
        factor_temp = 1.00
        desc_temp = "Demanda normal / estándar"

    matriz_logistica = np.array([
        ["Camión de redilas", unidades_reparto, 50]
    ], dtype=object)

    capacidad_total_flota = int(matriz_logistica[0, 1]) * int(matriz_logistica[0, 2])
    pedidos_ajustados = int(pedidos_diarios * factor_temp)

    # Nota explicativa sobre el cálculo estacional
    st.markdown(f"""
        <div class="nota-calculo">
            💡 <strong>Nota del modelo logístico:</strong> Los pedidos base ({pedidos_diarios} garrafones) se multiplican por el factor de temporada <strong>{demanda_estacional} ({factor_temp}x)</strong>, resultando en una <strong>demanda real de distribución de {pedidos_ajustados} garrafones</strong>.
        </div>
    """, unsafe_allow_html=True)

    modelo_garrafones = calcular_modelo_manheim(
        T=capacidad_total_flota,
        A=pedidos_ajustados,
        capacidad_total=capacidad_total_flota
    )

    eficiencia_flota = modelo_garrafones["Saturacion"]
    deficit_garrafones = pedidos_ajustados - capacidad_total_flota
    vehiculos_extra = recomendar_unidades(deficit_garrafones, 50)

    # BANNER DINÁMICO ACTUALIZADO PARA MERCANCÍAS
    if eficiencia_flota > 100:
        alerta_banner_b = f"⚠️ ALERTA LOGÍSTICA: Flota saturada ({eficiencia_flota:.1f}%). Se sugieren {vehiculos_extra} vehículo(s) adicional(es)."
        color_b_b = "#dc2626"
    elif eficiencia_flota > 85:
        alerta_banner_b = f"⚠️ ADVERTENCIA: Flota al límite de su capacidad ({eficiencia_flota:.1f}%)."
        color_b_b = "#d97706"
    else:
        alerta_banner_b = f"✅ ESTABILIDAD LOGÍSTICA: {modelo_garrafones['Estado']} con {eficiencia_flota:.1f}% de utilización."
        color_b_b = "#16a34a"

    st.markdown(f"""
        <div class="dynamic-banner" style="background: linear-gradient(90deg, #dcfce7 0%, #fef3c7 50%, #e0f2fe 100%); color: {color_b_b}; border-color: {color_b_b};">
            🚚 RUTA LOGÍSTICA: <span class="floating-icon">🚚</span> {unidades_reparto} Unidades | <span class="floating-icon">💧</span> {pedidos_ajustados} Garrafones<br>
            <span style="font-size: 15px;">{alerta_banner_b}</span>
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
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #16a34a; font-size: 17px; padding-top: 8px;'>Paso activo: {st.session_state.paso_seq_b} / 4</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sistema-compacto-box" style="border-color: #10b981; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-radius: 20px; padding: 26px; margin: 16px 0; box-shadow: 0 10px 25px rgba(16, 185, 129, 0.15);">
        <div class="ambiente-titulo-b">🌐 AMBIENTE: U.H. El Rosario (Zona Suburbana)</div>
    """, unsafe_allow_html=True)

    col_bn1, col_bn2, col_bn3, col_bn4 = st.columns(4)

    with col_bn1:
        if st.session_state.paso_seq_b == 1:
            st.markdown(f"""
            <div class="card-paso card-activa-entrada">
                <h4 style="color: #0284c7; margin: 0 0 12px 0; font-size: 21px; font-weight: 900;">📥 1. ENTRADA (Insumos)</h4>
                <p style="font-size: 17px; margin: 0; line-height: 1.6;">
                    <strong>Vehículos:</strong> {unidades_reparto} unidades.<br>
                    <strong>Demanda Base:</strong> <span style="color: #0284c7; font-weight: bold;">{pedidos_diarios} garrafones</span><br>
                    <em>Capacidad: {unidades_reparto}×50 = {capacidad_total_flota} un.</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📥 1. ENTRADA</h4>
                <p>En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn2:
        if st.session_state.paso_seq_b == 2:
            st.markdown(f"""
            <div class="card-paso card-activa-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 12px 0; font-size: 21px; font-weight: 900;">⚙️ 2. PROCESAMIENTO</h4>
                <p style="font-size: 17px; margin: 0; line-height: 1.6; color: #f0fdf4;">
                    <strong>Temporada:</strong> {demanda_estacional} ({desc_temp})<br>
                    <strong>Demanda Real:</strong> <span style="color: #fbbf24; font-weight: bold;">{pedidos_ajustados} garrafones</span><br>
                    <em>Uso de flota: ({pedidos_ajustados}/{capacidad_total_flota})×100 = {eficiencia_flota:.1f}%</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>⚙️ 2. PROCESO</h4>
                <p>En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn3:
        if st.session_state.paso_seq_b == 3:
            st.markdown(f"""
            <div class="card-paso card-activa-salida">
                <h4 style="color: #16a34a; margin: 0 0 12px 0; font-size: 21px; font-weight: 900;">📤 3. SALIDA (Producto)</h4>
                <p style="font-size: 17px; margin: 0; line-height: 1.6;">
                    <strong>Exportación:</strong><br>
                    <span style="color: #16a34a; font-weight: bold;">{pedidos_ajustados} garrafones</span> entregados con éxito en hogares.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📤 3. SALIDA</h4>
                <p>En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn4:
        if st.session_state.paso_seq_b == 4:
            if pedidos_ajustados > capacidad_total_flota:
                txt_rb = (
                    f"⚠️ Sistema logístico saturado ({eficiencia_flota:.1f}%). "
                    f"La demanda supera la capacidad. "
                    f"Se requieren aprox. {vehiculos_extra} vehículo(s) "
                    f"adicional(es) para mantener el servicio."
                )
            else:
                txt_rb = (
                    f"✅ {modelo_garrafones['Estado']} "
                    f"({eficiencia_flota:.1f}% de utilización). "
                    f"La distribución mantiene equilibrio operativo."
                )

            st.markdown(f"""
            <div class="card-paso card-activa-retro">
                <h4 style="color: #ea580c; margin: 0 0 12px 0; font-size: 21px; font-weight: 900;">🔄 4. RETROALIMENTACIÓN</h4>
                <p style="font-size: 17px; margin: 0; line-height: 1.6; color: #9a3412; font-weight: 800;">
                    {txt_rb}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>🔄 4. RETRO</h4>
                <p>En espera de secuencia...</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
