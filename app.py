import streamlit as st
import numpy as np

# Configuración inicial de la página
st.set_page_config(
    page_title="Modelos Sistémicos - Logística y Transporte",
    page_icon="🚛",
    layout="wide"
)

# Inicializar estados de sesión
if "paso_seq_a" not in st.session_state:
    st.session_state.paso_seq_a = 1

# Función de cálculo para el modelo de Manheim
def calcular_modelo_manheim(T, A, capacidad_total):
    if capacidad_total > 0:
        saturacion = (A / capacidad_total) * 100
    else:
        saturacion = 100.0

    if saturacion <= 70:
        nivel_servicio = 5.0
        estado = "✅ Operación Óptima / Fluida"
    elif saturacion <= 90:
        nivel_servicio = 3.5
        estado = "⚠️ Operación Regular / Alta Demanda"
    elif saturacion <= 100:
        nivel_servicio = 2.0
        estado = "⚠️ Operación Saturada / Al Límite"
    else:
        nivel_servicio = 1.0
        estado = "❌ Colapso Operativo / Sobresaturación"

    return {
        "Saturacion": saturacion,
        "Nivel_servicio": nivel_servicio,
        "Estado": estado
    }

def recomendar_unidades(deficit, capacidad_unidad):
    if deficit <= 0:
        return 0
    return int(np.ceil(deficit / capacidad_unidad))

# Definición de pestañas principales
tab1, tab2 = st.tabs(["CETRAM El Rosario", "Distribución de Agua (Garrafones)"])

# ==========================================
# PESTAÑA A: CETRAM EL ROSARIO (ORIGINAL RESTAURADA + CSS REDONDO CORREGIDO)
# ==========================================
with tab1:
    st.markdown("<p style='font-weight: bold; color: #ea580c; font-size: 18px; margin-bottom: 8px;'>A. Sistema Multimodal de Pasajeros - CETRAM El Rosario [Modelo con variables T, A, V, S]</p>", unsafe_allow_html=True)

    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    with col_c1:
        num_trenes = st.slider("🚆 Trenes (L6/L7)", 10, 50, 25, key="trenes_cetram_a_orig")
    with col_c2:
        num_buses = st.slider("🚍 Autobuses", 5, 40, 20, key="buses_cetram_a_orig")
    with col_c3:
        pasajeros_flota = st.slider("👥 Demanda Base [A] (Pax)", 500, 5000, 1800, step=100, key="p_flota_a_orig")
    with col_c4:
        horario_operativo = st.selectbox("🕒 Franja Horaria:", ["Pico Matutina", "Hora Valle", "Pico Nocturna"], key="horario_a_orig")

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
        <div style="background: #fff7ed; border: 2px solid #ea580c; border-radius: 12px; padding: 15px; margin-bottom: 15px;">
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
        <div style="border: 2px solid {color_b_a}; background: #fff; padding: 12px; border-radius: 10px; color: {color_b_a}; font-weight: bold; margin-bottom: 15px;">
            🚀 FLUJO ACTIVO [V]: 🚆 {num_trenes*2} Trenes | 🚍 {num_buses} Buses | 👥 {demanda_ajustada:,} Pax<br>
            <span style="font-size: 14px; font-weight: normal; color: #334155;">{alerta_banner_a}</span>
        </div>
    """, unsafe_allow_html=True)

    col_btn_seq1, col_btn_seq2, col_btn_seq3 = st.columns([2, 2, 3])
    with col_btn_seq1:
        if st.button("▶️ Avanzar Secuencia Teórica", use_container_width=True, key="avanzar_a_orig"):
            st.session_state.paso_seq_a = (st.session_state.paso_seq_a % 4) + 1
    with col_btn_seq2:
        if st.button("🔄 Reiniciar Ciclo", use_container_width=True, key="reiniciar_a_orig"):
            st.session_state.paso_seq_a = 1
    with col_btn_seq3:
        st.markdown(f"<p style='text-align: right; font-weight: bold; color: #ea580c; font-size: 16px; padding-top: 8px;'>Dimensión Activa: {st.session_state.paso_seq_a} / 4</p>", unsafe_allow_html=True)

    # ================================
    # MODELO SISTÉMICO VISUAL CIRCULAR (CON POSICIONES AMPLIADAS PARA EVITAR ENCIMAMIENTO)
    # ================================
    st.markdown(f"""
    <style>
    .modelo-sistema {{
        position: relative;
        border: 5px solid #f97316;
        border-radius: 35px;
        padding: 20px;
        min-height: 520px;
        background: linear-gradient(135deg,#fff7ed,#ffedd5);
        margin-top: 25px;
        box-shadow: 0 10px 25px rgba(249, 115, 22, 0.15);
    }}
    .titulo-ambiente {{
        text-align: center;
        font-size: 24px;
        font-weight: 900;
        color: #c2410c;
        margin-bottom: 15px;
    }}
    .entrada-circulo {{
        position: absolute;
        left: 25px;
        top: 110px;
        background: #dbeafe;
        border: 3px solid #0284c7;
        padding: 15px;
        border-radius: 15px;
        width: 210px;
        text-align: center;
        font-weight: bold;
    }}
    .proceso-circulo {{
        position: absolute;
        left: 310px;
        top: 90px;
        background: #1e293b;
        color: white;
        border: 4px solid #f59e0b;
        padding: 20px;
        border-radius: 15px;
        width: 260px;
        text-align: center;
    }}
    .salida-circulo {{
        position: absolute;
        right: 25px;
        top: 110px;
        background: #dcfce7;
        border: 3px solid #16a34a;
        padding: 15px;
        border-radius: 15px;
        width: 210px;
        text-align: center;
        font-weight: bold;
    }}
    .retro-circulo {{
        position: absolute;
        bottom: 25px;
        left: 15%;
        width: 70%;
        background: #ffffff;
        border: 3px solid #ea580c;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        font-weight: bold;
    }}
    </style>

    <div class="modelo-sistema">
        <div class="titulo-ambiente">🌐 AMBIENTE: CETRAM EL ROSARIO</div>

        <div class="entrada-circulo">
            📥 ENTRADA<br><br>
            <strong>Oferta [T]</strong><br>
            🚆 {num_trenes*2} trenes<br>
            🚍 {num_buses} autobuses<br><br>
            Capacidad:<br>{capacidad_oferta:,} pasajeros
        </div>

        <div class="proceso-circulo">
            ⚙️ PROCESO<br><br>
            <strong>Flujo [V]</strong><br><br>
            Demanda ajustada:
            <h2 style="color: #ffb703; margin: 5px 0;">{demanda_ajustada:,}</h2>
            pasajeros<br>
            Horario: {horario_operativo}
        </div>

        <div class="salida-circulo">
            📤 SALIDA<br><br>
            <strong>Servicio [S]</strong><br><br>
            Nivel: <strong>{nivel_servicio_s:.2f}</strong><br><br>
            Saturación:<br><strong style="font-size: 18px;">{tasa_saturacion:.1f}%</strong>
        </div>

        <div class="retro-circulo">
            🔄 RETROALIMENTACIÓN<br>
            <p style="margin: 5px 0 3px 0; color: #1e293b; font-size: 15px;">{modelo_pasajeros["Estado"]}</p>
            <span style="font-size: 13px; color: #64748b; font-weight: normal;">El sistema ajusta frecuencias, capacidad y operación según la demanda.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA
# ==========================================
with tab2:
    st.markdown("<p style='font-weight: bold; color: #16a34a; font-size: 18px; margin-bottom: 8px;'>B. Distribución de Carga (Garrafones) - U.H. El Rosario [Control de Flota y Rutas]</p>", unsafe_allow_html=True)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        unidades_reparto = st.slider("🚚 Vehículos [T]", 1, 10, 3, key="slider_camiones_b_orig")
    with col_d2:
        pedidos_diarios = st.slider("💧 Pedidos Base [A] (Garrafones)", 50, 400, 150, step=10, key="slider_pedidos_b_orig")
    with col_d3:
        demanda_estacional = st.selectbox("🌤️ Temporada:", ["Regular", "Calor (Alta)"], key="d_estacional_b_orig")

    if demanda_estacional == "Calor (Alta)":
        factor_temp = 1.30
    else:
        factor_temp = 1.00

    matriz_logistica = np.array([
        ["Camión de redilas", unidades_reparto, 50]
    ], dtype=object)

    capacidad_total_flota = int(matriz_logistica[0, 1]) * int(matriz_logistica[0, 2])
    pedidos_ajustados = int(pedidos_diarios * factor_temp)

    modelo_agua = calcular_modelo_manheim(
        T=capacidad_total_flota,
        A=pedidos_ajustados,
        capacidad_total=capacidad_total_flota
    )

    st.markdown(f"""
        <div style="border: 4px solid #16a34a; border-radius: 25px; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 25px; margin-top: 20px;">
            <div style="text-align: center; font-size: 24px; font-weight: 900; color: #15803d; margin-bottom: 20px;">
                🌐 AMBIENTE: DISTRIBUCIÓN DE AGUA (U.H. EL ROSARIO)
            </div>
    """, unsafe_allow_html=True)

    col_b_ent, col_b_pro, col_b_sal = st.columns(3)

    with col_b_ent:
        st.markdown(f"""
            <div style="background: #e0f2fe; border: 3px solid #0284c7; padding: 20px; border-radius: 15px; text-align: center; height: 100%;">
                <h4 style="color: #0369a1; margin-top:0;">📥 ENTRADA</h4>
                <strong>Flota [T]</strong><br><br>
                🚚 {unidades_reparto} vehículos<br><br>
                <strong>Capacidad Flota:</strong><br>{capacidad_total_flota} garrafones
            </div>
        """, unsafe_allow_html=True)

    with col_b_pro:
        st.markdown(f"""
            <div style="background: #1e293b; color: white; border: 3px solid #f59e0b; padding: 20px; border-radius: 15px; text-align: center; height: 100%;">
                <h4 style="color: #fbbf24; margin-top:0;">⚙️ PROCESO</h4>
                <strong>Demanda [V]</strong><br><br>
                Pedidos ajustados:
                <h2 style="color: #ffb703; margin: 5px 0;">{pedidos_ajustados}</h2>
                garrafones<br><br>
                <strong>Temporada:</strong> {demanda_estacional}
            </div>
        """, unsafe_allow_html=True)

    with col_b_sal:
        st.markdown(f"""
            <div style="background: #fef9c3; border: 3px solid #ca8a04; padding: 20px; border-radius: 15px; text-align: center; height: 100%;">
                <h4 style="color: #854d0e; margin-top:0;">📤 SALIDA</h4>
                <strong>Servicio [S]</strong><br><br>
                Nivel: <strong>{modelo_agua["Nivel_servicio"]:.2f}</strong><br><br>
                Saturación: <br><strong style="font-size: 18px;">{modelo_agua["Saturacion"]:.1f}%</strong>
            </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
            <div style="background: #ffffff; border: 3px solid #16a34a; border-radius: 15px; padding: 18px; text-align: center; margin-top: 20px;">
                <h4 style="color: #16a34a; margin: 0 0 8px 0;">🔄 RETROALIMENTACIÓN</h4>
                <p style="margin: 0; font-weight: bold; color: #334155; font-size: 16px;">{modelo_agua["Estado"]}</p>
                <p style="margin: 5px 0 0 0; color: #64748b; font-size: 14px;">Reasignación de rutas y optimización de entrega domiciliaria según demanda.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
