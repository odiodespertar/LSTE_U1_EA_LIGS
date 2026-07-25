import streamlit as st
import numpy as np
import math


# ==========================================================
# FUNCIONES DEL MODELO DE MANHEIM (T - A - F)
# ==========================================================

def calcular_modelo_manheim(T_oferta, A_demanda, capacidad_total):
    V = A_demanda  # Volumen de flujo generado por las actividades
    if capacidad_total > 0 and V > 0:
        S = capacidad_total / V
    else:
        S = 0

    saturacion = (V / capacidad_total) * 100 if capacidad_total else 0

    if saturacion <= 85:
        estado = "🟢 Homeostasis óptima (Equilibrio T-A-F)"
    elif saturacion <= 100:
        estado = "🟡 Cercano a saturación"
    else:
        estado = "🔴 Sistema saturado (Desequilibrio)"

    return {
        "Flujo": V,
        "Nivel_servicio": S,
        "Saturacion": saturacion,
        "Estado": estado
    }


def recomendar_unidades(deficit, capacidad_unidad):
    if deficit <= 0:
        return 0
    return math.ceil(deficit / capacidad_unidad)


# ==========================================================
# CONFIGURACIÓN DE STREAMLIT
# ==========================================================

st.set_page_config(
    page_title="Modelo de Interacción Manheim (T - A - F)",
    page_icon="🔄",
    layout="wide",
)

# Estilos CSS para el diagrama interactivo de Manheim (T, A, F)
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

    /* Contenedor del Diagrama de Manheim */
    .manheim-container {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 3px solid #0284c7;
        border-radius: 22px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(2, 132, 199, 0.15);
    }

    .manheim-title {
        text-align: center;
        font-size: 20px;
        font-weight: 900;
        color: #0369a1;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .nodo-manheim {
        background: #ffffff;
        border: 3px solid #0284c7;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 6px 15px rgba(0,0,0,0.05);
        height: 100%;
        transition: all 0.3s ease;
    }

    .nodo-manheim:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 25px rgba(2, 132, 199, 0.25);
    }

    .nodo-t { border-color: #0284c7; background: linear-gradient(135deg, #ffffff 0%, #e0f2fe 100%); }
    .nodo-a { border-color: #f59e0b; background: linear-gradient(135deg, #ffffff 0%, #fef3c7 100%); }
    .nodo-f { border-color: #16a34a; background: linear-gradient(135deg, #ffffff 0%, #dcfce7 100%); }

    .conexion-badge {
        background: #0f172a;
        color: #38bdf8;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 800;
        font-size: 14px;
        display: inline-block;
        margin: 10px 0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
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

    .sistema-macro-container {
        border: 3px dashed #0284c7;
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 25px;
        position: relative;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }

    .supersistema-label {
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        color: #64748b;
        text-align: center;
        margin-bottom: 15px;
        letter-spacing: 2px;
    }

    .card-paso {
        border-radius: 18px;
        padding: 20px;
        text-align: left;
        min-height: 380px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        transition: all 0.5s ease-in-out;
    }

    .card-inactiva {
        background: #ffffff;
        border: 2px dashed #cbd5e1;
        color: #475569;
        opacity: 0.75;
        transform: scale(0.97);
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        text-align: center;
        justify-content: center;
        align-items: center;
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
    }

    .card-activa-proceso {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 4px solid #f59e0b;
        color: #ffffff;
        box-shadow: 0 12px 30px rgba(245, 158, 11, 0.35);
        transform: scale(1.04);
    }

    .card-activa-salida {
        background: linear-gradient(135deg, #ffffff 0%, #dcfce7 100%);
        border: 4px solid #16a34a;
        color: #0f172a;
        box-shadow: 0 12px 30px rgba(22, 163, 74, 0.35);
        transform: scale(1.04);
    }

    .card-activa-retro {
        background: linear-gradient(135deg, #ffffff 0%, #ffedd5 100%);
        border: 4px solid #ea580c;
        color: #0f172a;
        box-shadow: 0 12px 30px rgba(234, 88, 12, 0.35);
        transform: scale(1.04);
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
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera institucional completa con logo y datos de estudiante
col_logo, col_txt = st.columns([1, 6])
with col_logo:
    try:
        st.image("UnADM LOGO.png", width=110)
    except Exception:
        pass

with col_txt:
    st.markdown("### 4. Diseño o modelo de transporte aplicando Teoría de Sistemas en mi localidad")
    st.markdown("<p style='font-size:16px; margin:0;'><strong>Estudiante:</strong> Liliana García Solís | <strong>Matrícula:</strong> ES251101336 | <strong>Actividad:</strong> Evidencia de Aprendizaje | <strong>Asignatura:</strong> Sistemas de Transporte</p>", unsafe_allow_html=True)

st.markdown("---")

with st.expander("👉 Indicaciones de navegación y modelos teóricos", expanded=False):
    st.markdown("""
    <div class="instrucciones-box">
        <p style="margin: 0 0 8px 0; font-weight: bold; color: #0369a1; font-size: 20px !important;">Instrucciones de Uso:</p>
        <ul style="margin: 0; padding-left: 20px; color: #0c4a6e;">
            <li style="margin-bottom: 8px;"><strong>Diagrama de Manheim (T - A - F):</strong> Visualiza la interacción sistémica entre el Sistema de Transporte, el Sistema de Actividades y los Flujos de transporte.</li>
            <li style="margin-bottom: 8px;"><strong>Pestañas A y B:</strong> Explora el sistema multimodal de pasajeros y la distribución de carga en garrafones.</li>
            <li><strong>Avance secuencial:</strong> Utiliza el botón de "Avanzar Secuencia Teórica" para recorrer las dimensiones de Entrada, Proceso, Salida y Retroalimentación.</li>
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
    st.markdown("<p style='font-weight: bold; color: #ea580c; font-size: 18px; margin-bottom: 8px;'>A. Sistema Multimodal de Pasajeros - CETRAM El Rosario [Diagrama de Manheim T-A-F + Modelo Sistémico]</p>", unsafe_allow_html=True)

    # Diagrama de Interacción de Manheim (T - A - F) Estilizado
    st.markdown("""
        <div class="manheim-container">
            <div class="manheim-title">🔄 Modelo de Interacción del Sistema de Transporte (Manheim, 1979)</div>
    """, unsafe_allow_html=True)
    
    ma1, ma2, ma3 = st.columns(3)
    with ma1:
        st.markdown("""
            <div class="nodo-manheim nodo-t">
                <strong style="color: #0284c7; font-size: 16px;">Sistema de Transporte (T)</strong><br>
                <span class="conexion-badge">Oferta / Capacidad</span><br>
                <span style="font-size: 14px; color: #334155;">Infraestructura CETRAM + Metro L6/L7 + Buses</span>
            </div>
        """, unsafe_allow_html=True)
    with ma2:
        st.markdown("""
            <div class="nodo-manheim nodo-a">
                <strong style="color: #d97706; font-size: 16px;">Sistema de Actividades (A)</strong><br>
                <span class="conexion-badge" style="background: #f59e0b; color: #ffffff;">Demanda / Patrones</span><br>
                <span style="font-size: 14px; color: #334155;">Dinámica urbana y movilidad poblacional local</span>
            </div>
        """, unsafe_allow_html=True)
    with ma3:
        st.markdown("""
            <div class="nodo-manheim nodo-f">
                <strong style="color: #16a34a; font-size: 16px;">Flujos (F)</strong><br>
                <span class="conexion-badge" style="background: #16a34a; color: #ffffff;">Interacción T ⇄ A</span><br>
                <span style="font-size: 14px; color: #334155;">Volumen real de pasajeros transportados y servicio</span>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

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
            • <strong>Volumen [V / F]:</strong> Condicionado por la actividad urbano-poblacional [A] en horario <strong>{horario_operativo}</strong> ➔ <strong>{demanda_ajustada:,} pax</strong>.
        </div>
    """, unsafe_allow_html=True)

    modelo_pasajeros = calcular_modelo_manheim(
        T_oferta=capacidad_oferta,
        A_demanda=demanda_ajustada,
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
            🚀 FLUJO ACTIVO [F]: <span class="floating-icon">🚆</span> {num_trenes*2} Trenes | <span class="floating-icon">🚍</span> {num_buses} Buses | <span class="floating-icon">👥</span> {demanda_ajustada:,} Pax<br>
            <span style="font-size: 15px;">{alerta_banner_a}</span>
        </div>
    """, unsafe_allow_html=True)

    col_btn_seq1, col_btn_seq2, col_btn_seq3 = st.columns([2, 2, 3])
    with col_btn_seq1:
        if st.button("▶️ Avanzar Secuencia Teórica", use_container_width=True, key="avanzar_a"):
            st.session_state.paso_seq_a = (st.session_state.paso_seq_a % 4) + 1
            st.rerun()
    with col_btn_seq2:
        if st.button("🔄 Reiniciar Ciclo", use_container_width=True, key="reiniciar_a"):
            st.session_state.paso_seq_a = 1
            st.rerun()
    with col_btn_seq3:
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #ea580c; font-size: 17px; padding-top: 8px;'>Dimensión Activa: {st.session_state.paso_seq_a} / 4</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sistema-macro-container">
            <div class="supersistema-label">🌎 Ambiente Externo (Supersistema): Hora pico/valle, tráfico y entorno urbano</div>
            <div class="ambiente-titulo-naranja" style="margin-bottom: 15px;">🔄 LÍMITE DEL SISTEMA: CETRAM EL ROSARIO (PASAJEROS)</div>
    """, unsafe_allow_html=True)

    col_n1, col_n2, col_n3, col_n4 = st.columns(4)

    with col_n1:
        if st.session_state.paso_seq_a == 1:
            st.markdown(f"""
            <div class="card-paso card-activa-entrada">
                <h4 style="color: #0284c7; margin: 0 0 8px 0; font-size: 17px; font-weight: 900;">📥 ENTRADA (Recursos/Energía)</h4>
                <p style="font-size: 13px; margin: 0; line-height: 1.4;">
                    <strong>Elementos:</strong><br>
                    • 🚆 {num_trenes*2} Trenes activos<br>
                    • 🚍 {num_buses} Autobuses<br>
                    • 👨‍✈️ Operadores y personal<br>
                    • ⛽ Energía y combustible<br>
                    • 👥 Demanda: {pasajeros_flota:,} pax<br>
                    <strong>Oferta Total [T]:</strong> {capacidad_oferta:,} pax.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📥 ENTRADA</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n2:
        if st.session_state.paso_seq_a == 2:
            st.markdown(f"""
            <div class="card-paso card-activa-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 8px 0; font-size: 17px; font-weight: 900;">⚙️ SUBSISTEMAS Y PROCESO [F]</h4>
                <p style="font-size: 13px; margin: 0; line-height: 1.4; color: #f8fafc;">
                    <strong>Componentes:</strong><br>
                    • Planeación de frecuencias<br>
                    • Asignación de unidades<br>
                    • Control operativo<br>
                    • Transporte de pasajeros<br>
                    <strong>Volumen [F] ({horario_operativo}):</strong> <strong>{demanda_ajustada:,} pax</strong>.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>⚙️ PROCESO [F]</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n3:
        if st.session_state.paso_seq_a == 3:
            st.markdown(f"""
            <div class="card-paso card-activa-salida">
                <h4 style="color: #16a34a; margin: 0 0 8px 0; font-size: 17px; font-weight: 900;">📤 SALIDA (Información/Recursos)</h4>
                <p style="font-size: 13px; margin: 0; line-height: 1.4;">
                    <strong>Elementos:</strong><br>
                    • Pasajeros transportados<br>
                    • Nivel de servicio [S]<br>
                    • Flujo de pasajeros activo<br>
                    <strong>Índice de Servicio:</strong> <strong>{nivel_servicio_s:.2f}</strong>. Transferencia eficiente a red masiva.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📤 SALIDA</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_n4:
        if st.session_state.paso_seq_a == 4:
            if demanda_ajustada > capacidad_oferta:
                txt_r = (
                    f"⚠️ <strong>Saturación ({tasa_saturacion:.1f}%):</strong> "
                    f"Exige ajuste de frecuencias o incorporación de unidades. "
                    f"Sugerencia: {trenes_extra} tren(es) o {autobuses_extra} autobús(es) extra."
                )
            else:
                txt_r = (
                    f"✅ <strong>Homeostasis estable ({tasa_saturacion:.1f}%):</strong> "
                    f"El sistema opera óptimamente dentro del CETRAM."
                )

            st.markdown(f"""
            <div class="card-paso card-activa-retro">
                <h4 style="color: #ea580c; margin: 0 0 8px 0; font-size: 16px; font-weight: 900;">🔄 RETROALIMENTACIÓN</h4>
                <p style="font-size: 12px; margin: 0; line-height: 1.35; color: #9a3412; font-weight: 700;">
                    <strong>Control del Sistema:</strong><br>
                    • Saturación del sistema<br>
                    • Ajuste de frecuencias<br>
                    • Incorporación de unidades<br><br>
                    {txt_r}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>🔄 RETROALIMENTACIÓN</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA
# ==========================================
with tab2:
    st.markdown("<p style='font-weight: bold; color: #16a34a; font-size: 18px; margin-bottom: 8px;'>B. Distribución de Carga (Garrafones) - U.H. El Rosario [Diagrama de Manheim T-A-F + Modelo Logístico]</p>", unsafe_allow_html=True)

    # Diagrama de Interacción de Manheim (T - A - F) para Carga Estilizado
    st.markdown("""
        <div class="manheim-container" style="border-color: #10b981; box-shadow: 0 10px 25px rgba(16, 185, 129, 0.15);">
            <div class="manheim-title" style="color: #064e3b;">🔄 Modelo de Interacción del Sistema de Transporte (Manheim, 1979) — Carga</div>
    """, unsafe_allow_html=True)
    
    mb1, mb2, mb3 = st.columns(3)
    with mb1:
        st.markdown("""
            <div class="nodo-manheim nodo-t" style="border-color: #10b981;">
                <strong style="color: #10b981; font-size: 16px;">Sistema de Transporte (T)</strong><br>
                <span class="conexion-badge" style="background: #10b981; color: #ffffff;">Flota / Capacidad</span><br>
                <span style="font-size: 14px; color: #334155;">Vehículos de redilas y rutas de reparto local</span>
            </div>
        """, unsafe_allow_html=True)
    with mb2:
        st.markdown("""
            <div class="nodo-manheim nodo-a" style="border-color: #f59e0b;">
                <strong style="color: #d97706; font-size: 16px;">Sistema de Actividades (A)</strong><br>
                <span class="conexion-badge" style="background: #f59e0b; color: #ffffff;">Demanda / Pedidos</span><br>
                <span style="font-size: 14px; color: #334155;">Consumo diario de agua en U.H. El Rosario</span>
            </div>
        """, unsafe_allow_html=True)
    with mb3:
        st.markdown("""
            <div class="nodo-manheim nodo-f" style="border-color: #16a34a;">
                <strong style="color: #16a34a; font-size: 16px;">Flujos (F)</strong><br>
                <span class="conexion-badge" style="background: #16a34a; color: #ffffff;">Interacción T ⇄ A</span><br>
                <span style="font-size: 14px; color: #334155;">Volumen real de garrafones distribuidos y entregas</span>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

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
            • <strong>Volumen por demanda estacional [F / A]:</strong> {pedidos_ajustados:,} garrafones (Temporada {demanda_estacional}).<br>
            • Ventanas de reparto controladas (Lun-Vie 9:00-17:00, Sáb hasta mediodía).
        </div>
    """, unsafe_allow_html=True)

    modelo_garrafones = calcular_modelo_manheim(
        T_oferta=capacidad_total_flota,
        A_demanda=pedidos_ajustados,
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
            🚚 RUTA LOGÍSTICA [F]: <span class="floating-icon">🚚</span> {unidades_reparto} Unidades ({capacidad_total_flota:,} cap.) | <span class="floating-icon">💧</span> {pedidos_ajustados:,} Garrafones<br>
            <span style="font-size: 15px;">{alerta_banner_b}</span>
        </div>
    """, unsafe_allow_html=True)

    col_btn_seqb1, col_btn_seqb2, col_btn_seqb3 = st.columns([2, 2, 3])
    with col_btn_seqb1:
        if st.button("▶️ Avanzar Secuencia Teórica (B)", use_container_width=True, key="avanzar_b"):
            st.session_state.paso_seq_b = (st.session_state.paso_seq_b % 4) + 1
            st.rerun()
    with col_btn_seqb2:
        if st.button("🔄 Reiniciar Ciclo (B)", use_container_width=True, key="reiniciar_b"):
            st.session_state.paso_seq_b = 1
            st.rerun()
    with col_btn_seqb3:
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #16a34a; font-size: 17px; padding-top: 8px;'>Dimensión Activa: {st.session_state.paso_seq_b} / 4</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sistema-macro-container" style="border-color: #10b981; background: linear-gradient(135deg, #f0fdf4 0%, #e6f4ea 100%);">
            <div class="supersistema-label">🌎 Ambiente Externo (Supersistema): Clima, tráfico y accesos a U.H. El Rosario</div>
            <div class="ambiente-titulo-b" style="margin-bottom: 15px;">🔄 LÍMITE DEL SISTEMA: U.H. EL ROSARIO (DISTRIBUCIÓN DE CARGA)</div>
    """, unsafe_allow_html=True)

    col_bn1, col_bn2, col_bn3, col_bn4 = st.columns(4)

    with col_bn1:
        if st.session_state.paso_seq_b == 1:
            st.markdown(f"""
            <div class="card-paso card-activa-entrada">
                <h4 style="color: #0284c7; margin: 0 0 8px 0; font-size: 17px; font-weight: 900;">📥 ENTRADA (Recursos/Energía)</h4>
                <p style="font-size: 13px; margin: 0; line-height: 1.4;">
                    <strong>Elementos:</strong><br>
                    • 🚚 {unidades_reparto} Vehículos de redilas<br>
                    • 👨‍✈️ Operadores de reparto<br>
                    • ⛽ Combustible y recursos<br>
                    • 💧 Pedidos: {pedidos_diarios} garrafones<br>
                    <strong>Capacidad Flota [T]:</strong> {capacidad_total_flota:,} garrafones.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📥 ENTRADA</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn2:
        if st.session_state.paso_seq_b == 2:
            st.markdown(f"""
            <div class="card-paso card-activa-proceso">
                <h4 style="color: #fbbf24; margin: 0 0 8px 0; font-size: 17px; font-weight: 900;">⚙️ SUBSISTEMAS Y PROCESO [F]</h4>
                <p style="font-size: 13px; margin: 0; line-height: 1.4; color: #f0fdf4;">
                    <strong>Componentes:</strong><br>
                    • Planeación de rutas de entrega<br>
                    • Asignación de vehículos<br>
                    • Control operativo en U.H.<br>
                    • Distribución de carga<br>
                    <strong>Volumen [F] ({demanda_estacional}):</strong> <strong>{pedidos_ajustados:,} garrafones</strong>.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>⚙️ PROCESO [F]</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn3:
        if st.session_state.paso_seq_b == 3:
            st.markdown(f"""
            <div class="card-paso card-activa-salida">
                <h4 style="color: #16a34a; margin: 0 0 8px 0; font-size: 17px; font-weight: 900;">📤 SALIDA (Recursos/Información)</h4>
                <p style="font-size: 13px; margin: 0; line-height: 1.4;">
                    <strong>Elementos:</strong><br>
                    • Garrafones entregados<br>
                    • Nivel de servicio en ventanas horarias<br>
                    • Flujo de distribución exitoso<br>
                    <strong>Total Distribuido:</strong> <span style="color: #16a34a; font-weight: bold;">{pedidos_ajustados:,} garrafones</span>.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>📤 SALIDA</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_bn4:
        if st.session_state.paso_seq_b == 4:
            if pedidos_ajustados > capacidad_total_flota:
                txt_rb = (
                    f"⚠️ <strong>Adaptación ({eficiencia_flota:.1f}%):</strong> "
                    f"Demanda supera la flota. Se requiere incorporar unidades adicionales o rediseñar rutas. "
                    f"Sugerencia: {vehiculos_extra} vehículo(s) extra."
                )
            else:
                txt_rb = (
                    f"✅ <strong>Homeostasis logística ({eficiencia_flota:.1f}%):</strong> "
                    f"El suministro diario opera estable en la unidad habitacional."
                )

            st.markdown(f"""
            <div class="card-paso card-activa-retro">
                <h4 style="color: #ea580c; margin: 0 0 8px 0; font-size: 16px; font-weight: 900;">🔄 RETROALIMENTACIÓN</h4>
                <p style="font-size: 12px; margin: 0; line-height: 1.35; color: #9a3412; font-weight: 700;">
                    <strong>Control del Sistema:</strong><br>
                    • Saturación de flota<br>
                    • Ajuste de frecuencias de reparto<br>
                    • Incorporación de vehículos<br><br>
                    {txt_rb}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card-paso card-inactiva">
                <h4>🔄 RETROALIMENTACIÓN</h4>
                <p>Haz clic en avanzar para revisar esta dimensión teórica.</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
