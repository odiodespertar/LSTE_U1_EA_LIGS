import streamlit as st
import numpy as np
import math


# ==========================================================
# FUNCIONES DEL MODELO SISTÉMICO
# ==========================================================

def calcular_modelo_manheim(T, A, capacidad_total):
    """
    Modelo simplificado basado en Manheim (1979)
    T = Sistema de Transporte (Oferta / Capacidad)
    A = Sistema de Actividades (Demanda)
    V = Volumen de flujo
    S = Nivel de servicio
    F0 = Equilibrio operativo
    """
    V = A  # Volumen de flujo

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
        padding: 12px 16px;
        border-radius: 6px;
        font-size: 15px;
        color: #b45309;
        margin-top: 10px;
        margin-bottom: 15px;
        line-height: 1.5;
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
        padding: 22px;
        text-align: center;
        min-height: 330px;
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
        font-size: 15px !important;
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
            <li style="margin-bottom: 8px;"><strong>Controles interactivos:</strong> Modifica los sliders y franjas horarias; observa cómo el procesamiento y las alertas dinámicas superiores se actualizan de inmediato.</li>
            <li><strong>Avance secuencial teórico:</strong> Utiliza el botón de "Avanzar Secuencia" para recorrer paso a paso el modelo analítico (Oferta [T] ➔ Volumen [V] ➔ Salida [S] ➔ Equilibrio y Adaptación).</li>
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
    st.markdown("<p style='font-weight: bold; color: #ea580c; font-size: 18px; margin-bottom: 8px;'>A. Sistema Multimodal de Pasajeros - CETRAM El Rosario [Modelo con variables T, A, V, S]</p>", unsafe_allow_html=True)

    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    with col_c1:
        num_trenes = st.slider("🚆 Trenes (L6/L7)", 10, 50, 25, key="t_pax_c")
    with col_c2:
        num_buses = st.slider("🚍 Autobuses", 5, 40, 20, key="b_pax_c")
    with col_c3:
        pasajeros_flota = st.slider("👥 Demanda Base [A] (Pax)", 500, 5000, 1800, step=100, key="p_flota_c")
    with col_c4:
        horario_operativo = st.selectbox("🕒 Franja Horaria:", ["Pico Matutina", "Hora Valle", "Pico Nocturna"], key="h_pax_c")

    if horario_operativo == "Pico Matutina":
        factor_franja = 1.35
    elif horario_operativo == "Pico Nocturna":
        factor_franja = 1.20
    else:
        factor_franja = 0.85

    matriz_capacidad = np.array([
        ["Metro Línea 6", num_trenes, 110],
        ["Metro Línea 7", num_trenes, 110],
        ["Autobuses", num_buses, 80]
    ], dtype=object)

    capacidad_l6 = int(matriz_capacidad[0, 1]) * int(matriz_capacidad[0, 2])
    capacidad_l7 = int(matriz_capacidad[1, 1]) * int(matriz_capacidad[1, 2])
    capacidad_bus = int(matriz_capacidad[2, 1]) * int(matriz_capacidad[2, 2])

    capacidad_oferta = capacidad_l6 + capacidad_l7 + capacidad_bus
    total_unidades_a = (num_trenes * 2) + num_buses
    demanda_ajustada = int(pasajeros_flota * factor_franja)

    st.markdown(f"""
        <div class="nota-calculo">
            💡 <strong>Marco Analítico (Manheim):</strong> <br>
            • <strong>Oferta [T]:</strong> {total_unidades_a} unidades físicas ({num_trenes} trenes L6 + {num_trenes} trenes L7 + {num_buses} autobuses) ➔ <strong>{capacidad_oferta:,} pax</strong> de capacidad total.<br>
            • <strong>Volumen [V]:</strong> Condicionado por la actividad urbano-poblacional [A] en horario <strong>{horario_operativo}</strong> ➔ <strong>{demanda_ajustada:,} pax</strong>.
        </div>
    """, unsafe_allow_html=True)

    modelo_pasajeros = calcular_modelo_manheim(
        T=capacidad_oferta,
        A=demanda_ajustada,
        capacidad_total=capacidad_oferta
    )

    tasa_saturacion = modelo_pasajeros["Saturacion"]
    nivel_servicio_s = modelo_pasajeros["Nivel_servicio"]
    deficit_pasajeros = demanda_ajustada - capacidad_oferta
    trenes_extra = recomendar_unidades(deficit_pasajeros, 110)
    autobuses_extra = recomendar_unidades(deficit_pasajeros, 80)

    if tasa_saturacion > 100:
        alerta_banner_a = f"⚠️ ALERTA SISTÉMICA (Desequilibrio): Sobresaturación ({tasa_saturacion:.1f}%). Se requiere ajuste estructural o de frecuencias."
        color_b_a = "#dc2626"
    elif tasa_saturacion > 85:
        alerta_banner_a = f"⚠️ ADVERTENCIA: Sistema cerca del límite operativo ({tasa_saturacion:.1f}%)."
        color_b_a = "#d97706"
    else:
        alerta_banner_a = f"✅ ESTABILIDAD OPERATIVA: {modelo_pasajeros['Estado']} con {tasa_saturacion:.1f}% de ocupación."
        color_b_a = "#0369a1"

    st.markdown(f"""
        <div class="dynamic-banner" style="color: {color_b_a}; border-color: {color_b_a};">
            🚀 FLUJO ACTIVO [V]: <span class="floating-icon">🚆</span> {num_trenes*2} Trenes | <span class="floating-icon">🚍</span> {num_buses} Buses | <span class="floating-icon">👥</span> {demanda_ajustada:,} Pax<br>
            <span style="font-size: 15px;">{alerta_banner_a}</span>
        </div>
    """, unsafe_allow_html=True)

    col_btn_seq1, col_btn_seq2, col_btn_seq3 = st.columns([2, 2, 3])
    with col_btn_seq1:
        if st.button("▶️ Avanzar Secuencia Teórica", use_container_width=True, key="avanzar_a"):
            st.session_state.paso_seq_a = (st.session_state.paso_seq_a % 4) + 1
    with col_btn_seq2:
        if st.button("🔄 Reiniciar Ciclo", use_container_width=True, key="reiniciar_a"):
            st.session_state.paso_seq_a = 1
    with col_btn_seq3:
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #ea580c; font-size: 17px; padding-top: 8px;'>Dimensión Activa: {st.session_state.paso_seq_a} / 4</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sistema-compacto-box" style="border-color: #f97316; background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%); border-radius: 20px; padding: 26px; margin: 16px 0; box-shadow: 0 10px 25px rgba(249, 115, 22, 0.15);">
            <div class="ambiente-titulo-naranja">🌐 DIMENSIÓN 1 a 3: CETRAM El Rosario (Pasajeros)</div>
    """, unsafe_allow_html=True)

    col_n1, col_n2, col_n3, col_n4 = st.columns(4)

    with col_n1:
        if st.session_state.paso_seq_a == 1:
            st.markdown(f"""
            <div class="card-paso card-activa-entrada">
                <h4 style="color: #0284c7; margin: 0 0 10px 0; font-size: 19px; font-weight: 900;">📥 1. OFERTA Y DEMANDA</h4>
                <p style="font-size: 14px; margin: 0; line-height: 1.4;">
                    <strong>Teoría:</strong> Infraestructura (T) + Actividad (A).<br>
                    <strong>Caso Local:</strong> {total_unidades_a} unidades activas en CETRAM determinan la oferta frente a una base de {pasajeros_flota:,} pasajeros.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📥 1. OFERTA Y DEMANDA</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n2:
        if st.session_state.paso_seq_a == 2:
            st.markdown(f"""
            <div class="card-paso card-activa-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 10px 0; font-size: 19px; font-weight: 900;">⚙️ 2. FLUJO Y VOLUMEN [V]</h4>
                <p style="font-size: 14px; margin: 0; line-height: 1.4; color: #f8fafc;">
                    <strong>Teoría:</strong> Absorción de demanda sin colapsar.<br>
                    <strong>Caso Local:</strong> En horario <em>{horario_operativo}</em> el volumen asciende a <strong>{demanda_ajustada:,} pax</strong>, modificando la presión operativa.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>⚙️ 2. FLUJO Y VOLUMEN [V]</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n3:
        if st.session_state.paso_seq_a == 3:
            st.markdown(f"""
            <div class="card-paso card-activa-salida">
                <h4 style="color: #16a34a; margin: 0 0 10px 0; font-size: 19px; font-weight: 900;">📤 3. NIVEL DE SERVICIO [S]</h4>
                <p style="font-size: 14px; margin: 0; line-height: 1.4;">
                    <strong>Teoría:</strong> Intersección de flujos estables.<br>
                    <strong>Caso Local:</strong> Índice de servicio <strong>{nivel_servicio_s:.2f}</strong>. Los usuarios se transfieren a la red de transporte masivo.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📤 3. NIVEL DE SERVICIO [S]</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n4:
        if st.session_state.paso_seq_a == 4:
            if demanda_ajustada > capacidad_oferta:
                txt_r = (
                    f"⚠️ <strong>Homeostasis alterada ({tasa_saturacion:.1f}%):</strong> "
                    f"A largo plazo, el sistema exige transformación estructural (ampliación de andenes o reestructuración de carriles). "
                    f"Sugerencia operativa: {trenes_extra} tren(es) o {autobuses_extra} autobús(es) extra."
                )
            else:
                txt_r = (
                    f"✅ <strong>Homeostasis estable ({tasa_saturacion:.1f}%):</strong> "
                    f"El equilibrio operativo absorbe la demanda actual sin requerir modificaciones estructurales inmediatas."
                )

            st.markdown(f"""
            <div class="card-paso card-activa-retro">
                <h4 style="color: #ea580c; margin: 0 0 10px 0; font-size: 19px; font-weight: 900;">🔄 4. ADAPTACIÓN Y HOMEOSTASIS</h4>
                <p style="font-size: 13px; margin: 0; line-height: 1.4; color: #9a3412; font-weight: 700;">
                    {txt_r}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>🔄 4. ADAPTACIÓN</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA
# ==========================================
with tab2:
    st.markdown("<p style='font-weight: bold; color: #16a34a; font-size: 18px; margin-bottom: 8px;'>B. Distribución de Carga (Garrafones) - U.H. El Rosario [Control de Flota y Rutas]</p>", unsafe_allow_html=True)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        unidades_reparto = st.slider("🚚 Vehículos [T]", 1, 10, 3, key="slider_camiones_c")
    with col_d2:
        pedidos_diarios = st.slider("💧 Pedidos Base [A] (Garrafones)", 50, 400, 150, step=10, key="slider_pedidos_c")
    with col_d3:
        demanda_estacional = st.selectbox("🌤️ Temporada:", ["Regular", "Calor (Alta)"], key="d_estacional_c")

    if demanda_estacional == "Calor (Alta)":
        factor_temp = 1.30
    else:
        factor_temp = 1.00

    matriz_logistica = np.array([
        ["Camión de redilas", unidades_reparto, 50]
    ], dtype=object)

    capacidad_total_flota = int(matriz_logistica[0, 1]) * int(matriz_logistica[0, 2])
    pedidos_ajustados = int(pedidos_diarios * factor_temp)

    st.markdown(f"""
        <div class="nota-calculo">
            💡 <strong>Marco Analítico Logístico:</strong><br>
            • <strong>Flota [T]:</strong> {unidades_reparto} vehículos de redilas ➔ <strong>{capacidad_total_flota:,} garrafones</strong> de capacidad máxima.<br>
            • <strong>Volumen por demanda estacional [A]:</strong> {pedidos_ajustados:,} garrafones (Temporada {demanda_estacional}).<br>
            • Ventanas de reparto controladas (Lun-Vie 9:00-17:00, Sáb hasta mediodía).
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

    if eficiencia_flota > 100:
        alerta_banner_b = f"⚠️ ALERTA LOGÍSTICA (Desequilibrio): Flota sobrepasada ({eficiencia_flota:.1f}%). Se sugieren {vehiculos_extra} vehículo(s) adicional(es)."
        color_b_b = "#dc2626"
    elif eficiencia_flota > 85:
        alerta_banner_b = f"⚠️ ADVERTENCIA: Flota al límite de su capacidad máxima ({eficiencia_flota:.1f}%)."
        color_b_b = "#d97706"
    else:
        alerta_banner_b = f"✅ ESTABILIDAD LOGÍSTICA: {modelo_garrafones['Estado']} con {eficiencia_flota:.1f}% de utilización."
        color_b_b = "#16a34a"

    st.markdown(f"""
        <div class="dynamic-banner" style="background: linear-gradient(90deg, #dcfce7 0%, #fef3c7 50%, #e0f2fe 100%); color: {color_b_b}; border-color: {color_b_b};">
            🚚 RUTA LOGÍSTICA [T]: <span class="floating-icon">🚚</span> {unidades_reparto} Unidades ({capacidad_total_flota:,} cap.) | <span class="floating-icon">💧</span> {pedidos_ajustados:,} Garrafones<br>
            <span style="font-size: 15px;">{alerta_banner_b}</span>
        </div>
    """, unsafe_allow_html=True)

    col_btn_seqb1, col_btn_seqb2, col_btn_seqb3 = st.columns([2, 2, 3])
    with col_btn_seqb1:
        if st.button("▶️ Avanzar Secuencia Teórica (B)", use_container_width=True, key="avanzar_b"):
            st.session_state.paso_seq_b = (st.session_state.paso_seq_b % 4) + 1
    with col_btn_seqb2:
        if st.button("🔄 Reiniciar Ciclo (B)", use_container_width=True, key="reiniciar_b"):
            st.session_state.paso_seq_b = 1
    with col_btn_seqb3:
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #16a34a; font-size: 17px; padding-top: 8px;'>Dimensión Activa: {st.session_state.paso_seq_b} / 4</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sistema-compacto-box" style="border-color: #10b981; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-radius: 20px; padding: 26px; margin: 16px 0; box-shadow: 0 10px 25px rgba(16, 185, 129, 0.15);">
        <div class="ambiente-titulo-b">🌐 DIMENSIÓN 1 a 3: U.H. El Rosario (Distribución de Carga)</div>
    """, unsafe_allow_html=True)

    col_bn1, col_bn2, col_bn3, col_bn4 = st.columns(4)

    with col_bn1:
        if st.session_state.paso_seq_b == 1:
            st.markdown(f"""
            <div class="card-paso card-activa-entrada">
                <h4 style="color: #0284c7; margin: 0 0 10px 0; font-size: 19px; font-weight: 900;">📥 1. OFERTA Y DEMANDA</h4>
                <p style="font-size: 14px; margin: 0; line-height: 1.4;">
                    <strong>Teoría:</strong> Capacidad de flota (T) vs concentración vecinal (A).<br>
                    <strong>Caso Local:</strong> {unidades_reparto} vehículos de redilas abastecen la U.H. El Rosario frente a una base de {pedidos_diarios} pedidos.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📥 1. OFERTA Y DEMANDA</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn2:
        if st.session_state.paso_seq_b == 2:
            st.markdown(f"""
            <div class="card-paso card-activa-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 10px 0; font-size: 19px; font-weight: 900;">⚙️ 2. EQUILIBRIO OPERATIVO</h4>
                <p style="font-size: 14px; margin: 0; line-height: 1.4; color: #f0fdf4;">
                    <strong>Teoría:</strong> Intersección de servicio y demanda estacional.<br>
                    <strong>Caso Local:</strong> Por temporada <em>{demanda_estacional}</em>, el volumen de entrega se ajusta a <strong>{pedidos_ajustados:,} garrafones</strong> diarios.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>⚙️ 2. EQUILIBRIO OPERATIVO</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn3:
        if st.session_state.paso_seq_b == 3:
            st.markdown(f"""
            <div class="card-paso card-activa-salida">
                <h4 style="color: #16a34a; margin: 0 0 10px 0; font-size: 19px; font-weight: 900;">📤 3. NIVEL DE SERVICIO [S]</h4>
                <p style="font-size: 14px; margin: 0; line-height: 1.4;">
                    <strong>Teoría:</strong> Cumplimiento de ventanas horarias.<br>
                    <strong>Caso Local:</strong> <span style="color: #16a34a; font-weight: bold;">{pedidos_ajustados:,} garrafones</span> distribuidos sin exceder la capacidad de la flota.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📤 3. NIVEL DE SERVICIO [S]</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn4:
        if st.session_state.paso_seq_b == 4:
            if pedidos_ajustados > capacidad_total_flota:
                txt_rb = (
                    f"⚠️ <strong>Adaptación requerida ({eficiencia_flota:.1f}%):</strong> "
                    f"Ante el crecimiento poblacional de la unidad habitacional, el sistema exige incorporar unidades de mayor capacidad o rediseñar rutas. "
                    f"Sugerencia: {vehiculos_extra} vehículo(s) extra."
                )
            else:
                txt_rb = (
                    f"✅ <strong>Homeostasis logística ({eficiencia_flota:.1f}%):</strong> "
                    f"El suministro diario opera de forma estable dentro de los márgenes y horarios establecidos."
                )

            st.markdown(f"""
            <div class="card-paso card-activa-retro">
                <h4 style="color: #ea580c; margin: 0 0 10px 0; font-size: 19px; font-weight: 900;">🔄 4. ADAPTACIÓN Y HOMEOSTASIS</h4>
                <p style="font-size: 13px; margin: 0; line-height: 1.4; color: #9a3412; font-weight: 700;">
                    {txt_rb}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>🔄 4. ADAPTACIÓN</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
