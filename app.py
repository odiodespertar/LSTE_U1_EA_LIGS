import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos Prácticos - Teoría de Sistemas",
    page_icon="💧",
    layout="wide",
)

# Estilos CSS avanzados para replicar exactamente el modelo sistémico dinámico de la imagen (Entrada, Proceso, Salida, Retroalimentación y Ambiente)
st.markdown("""
    <style>
    /* Estilos personalizados para el botón desplegable / expansor de alta visibilidad */
    .streamlit-expanderHeader {
        background-color: #fff8e1 !important;
        border: 2px solid #ffb300 !important;
        border-radius: 10px !important;
        color: #e65100 !important;
        font-weight: bold !important;
        font-size: 16px !important;
        box-shadow: 0 4px 12px rgba(255, 179, 0, 0.2);
    }

    /* Contenedor principal que simula el AMBIENTE circundante */
    .sistema-ambiente-box {
        background: linear-gradient(135deg, #f0f4f8 0%, #e2e8f0 100%);
        border: 3px dashed #64748b;
        border-radius: 20px;
        padding: 30px 20px;
        margin: 20px 0;
        position: relative;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        animation: pulseEnvironment 4s ease-in-out infinite;
    }

    /* Etiqueta superior del AMBIENTE */
    .ambiente-label {
        text-align: center;
        font-size: 28px;
        font-weight: 900;
        color: #d32f2f;
        letter-spacing: 2px;
        margin-bottom: 25px;
        text-transform: uppercase;
        text-shadow: 2px 2px 4px rgba(211, 47, 47, 0.15);
        animation: bounceTitle 2s ease-in-out infinite;
    }

    /* Tarjetas dinámicas para Entrada, Proceso y Salida */
    .nodo-sistema {
        background: #ffffff;
        border: 3px solid #1e293b;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        position: relative;
    }
    .nodo-sistema:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
    }

    .nodo-proceso {
        background: #1e293b;
        color: #ffffff;
        border: 3px solid #0f172a;
        border-radius: 14px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(30, 41, 59, 0.3);
        animation: floatProcess 3s ease-in-out infinite;
    }

    /* Flechas animadas de flujo horizontal */
    .flecha-flujo {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #0284c7;
        align-self: center;
        animation: moveArrow 1.5s ease-in-out infinite;
    }

    /* Bloque inferior de RETROALIMENTACIÓN con arco visual */
    .retroalimentacion-container {
        margin-top: 30px;
        border-top: 3px dashed #0284c7;
        padding-top: 20px;
        text-align: center;
        position: relative;
    }
    
    .retroalimentacion-badge {
        display: inline-block;
        background: #0284c7;
        color: white;
        padding: 10px 25px;
        border-radius: 30px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
        animation: pulseRetro 2s infinite;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Animaciones CSS personalizadas */
    @keyframes pulseEnvironment {
        0% { border-color: #64748b; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08); }
        50% { border-color: #0284c7; box-shadow: 0 15px 35px rgba(2, 132, 199, 0.15); }
        100% { border-color: #64748b; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08); }
    }

    @keyframes bounceTitle {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-4px); }
    }

    @keyframes floatProcess {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-6px); }
    }

    @keyframes moveArrow {
        0%, 100% { transform: translateX(0); opacity: 0.7; }
        50% { transform: translateX(6px); opacity: 1; }
    }

    @keyframes pulseRetro {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }

    .moving-banner {
        overflow: hidden;
        white-space: nowrap;
        background: #e1f5fe;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
        color: #01579b;
        margin-bottom: 15px;
    }
    
    .floating-icon {
        display: inline-block;
        font-size: 24px;
        margin: 0 5px;
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
    st.title("4. Diseño o modelo de transporte aplicando teoría de sistemas en mi localidad")
    st.markdown("**Estudiante:** Liliana García Solís | **Matrícula:** ES251101336 | **Bloque:** 1 | **Asignatura:** Sistemas de Transporte")

st.markdown("---")

# ==========================================
# BOTÓN DESPLEGABLE DE ALTA VISIBILIDAD PARA INDICACIONES
# ==========================================
with st.expander("👉 ¡REVISA AQUÍ LAS INDICACIONES! (Guía de Navegación Interactiva)", expanded=True):
    st.markdown("""
    <div style="background-color: #fffde7; padding: 10px; border-radius: 6px;">
        <p style="color: #3e2723; font-size: 15px; margin-bottom: 10px;">
            Para aprovechar al máximo esta aplicación y evitar perderte ningún detalle, sigue estos pasos:
        </p>
        <ul>
            <li><strong>1. Selecciona una pestaña abajo:</strong> Elige entre el caso de pasajeros (CETRAM) o el de mercancías (Agua en garrafón).</li>
            <li><strong>2. Utiliza los controles deslizantes (Sliders):</strong> Modifica los valores de flota y demanda para ver el comportamiento en tiempo real.</li>
            <li><strong>3. Analiza el modelo dinámico estilo croquis:</strong> Observa las tarjetas interactivas de Entrada, Proceso, Salida, Retroalimentación y el entorno (Ambiente) que se actualizan de forma inmediata según tus ajustes.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# Pestañas principales con los 2 casos de estudio
tab1, tab2 = st.tabs([
    "A. Sistema Multimodal: CETRAM El Rosario (Pasajeros)",
    "B. Distribución de Carga: Agua en Garrafón en U.H. El Rosario (Mercancías)"
])

# ==========================================
# PESTAÑA A: CETRAM EL ROSARIO
# ==========================================
with tab1:
    st.header("A. Sistema multimodal de transporte de pasajeros en CETRAM El Rosario")
    
    st.info("""
    📖 **Contexto Teórico (Van Gigch, 2006):**  
    *“La construcción de un Centro de Transferencia Modal (CETRAM) es quizá uno de los proyectos más complejos... Los sistemas contienen componentes estructurados para satisfacer necesidades y cumplir objetivos específicos de movilidad.”*
    """)

    st.markdown("""
        <div class="moving-banner">
            <span>Flujo Dinámico Activo: </span>
            <span class="floating-icon">🚆</span>
            <span class="floating-icon">🚍</span>
            <span class="floating-icon">👥</span> Sincronización en Andenes y Redes de Transporte
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: #e0f7fa; padding: 10px 15px; border-radius: 8px; border-left: 5px solid #00acc1; margin-bottom: 15px;">
            🎛️ <strong>Panel de Control Activo:</strong> Mueve los selectores y controles deslizantes de abajo para simular diferentes escenarios de saturación o fluidez:
        </div>
    """, unsafe_allow_html=True)

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

    capacidad_oferta = (num_trenes + num_buses) * 110
    balance_pasajeros = capacidad_oferta - pasajeros_flota

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
    st.subheader("🔄 Modelo Sistémico Dinámico (Estilo Croquis Interactivo)")

    # ==========================================
    # CONTENEDOR ESTILO IMAGEN (AMBIENTE, ENTRADA, PROCESO, SALIDA, RETROALIMENTACIÓN)
    # ==========================================
    st.markdown("""
        <div class="sistema-ambiente-box">
            <div class="ambiente-label">🌐 AMBIENTE: Entorno Urbano / Zona Norte del Valle de México (Azcapotzalco)</div>
    """, unsafe_allow_html=True)

    col_e, col_f1, col_p, col_f2, col_s = st.columns([2.2, 0.6, 2.6, 0.6, 2.2])

    with col_e:
        st.markdown(f"""
        <div class="nodo-sistema">
            <h4 style="color: #0284c7; margin-bottom: 8px;">📥 ENTRADA</h4>
            <p style="font-size: 13px; color: #334155; margin: 0;">
                <strong>Recursos:</strong> {num_trenes} trenes (L6/L7), {num_buses} buses.<br>
                <strong>Demanda:</strong> <strong>{pasajeros_flota} Pasajeros</strong> ingresando al sistema.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_f1:
        st.markdown('<div class="flecha-flujo"><br>➡️</div>', unsafe_allow_html=True)

    with col_p:
        st.markdown(f"""
        <div class="nodo-proceso">
            <h4 style="color: #38bdf8; margin-bottom: 8px;">⚙️ PROCESO</h4>
            <p style="font-size: 13px; color: #f8fafc; margin: 0;">
                Regulación de flujos peatonales, correspondencia multimodal y despacho en andenes.<br>
                <em>({horario_operativo})</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_f2:
        st.markdown('<div class="flecha-flujo"><br>➡️</div>', unsafe_allow_html=True)

    with col_s:
        st.markdown(f"""
        <div class="nodo-sistema">
            <h4 style="color: #16a34a; margin-bottom: 8px;">📤 SALIDA</h4>
            <p style="font-size: 13px; color: #334155; margin: 0;">
                <strong>Resultado:</strong><br>
                <strong>{pasajeros_flota} Pasajeros transferidos</strong> con éxito a sus destinos finales en la red.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Bloque inferior de Retroalimentación dentro del Ambiente
    if pasajeros_flota > capacidad_oferta:
        texto_retro = f"⚠️ Retroalimentación de Alerta: Saturación detectada ({pasajeros_flota} pax > Capacidad {capacidad_oferta}). Ajustar frecuencias."
    elif nivel_alerta:
        texto_retro = f"🔄 Retroalimentación Operativa: Monitoreo activo por alta concentración en {horario_operativo}."
    else:
        texto_retro = "✅ Retroalimentación Estable: Flujo continuo y óptimo en transbordos modales."

    st.markdown(f"""
        <div class="retroalimentacion-container">
            <div class="retroalimentacion-badge">🔄 Retroalimentación</div>
            <p style="margin-top: 10px; font-weight: bold; color: #1e293b; font-size: 14px;">
                {texto_retro}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Haz clic aquí para ver el Marco Completo de los 11 Componentes (Van Gigch, 2006) en el CETRAM El Rosario"):
        st.markdown(f"""
        1. **Elementos:** Trenes de L6 y L7, autobuses de superficie, usuarios, andenes y torniquetes.
        2. **Proceso de conversión:** Regulación de flujos peatonales y sincronización de transbordos entre modos de transporte.
        3. **Entradas y recursos:** {num_trenes} trenes, {num_buses} unidades, {pasajeros_flota} pasajeros en demanda e infraestructura eléctrica.
        4. **Salidas o resultados:** Pasajeros transferidos de manera segura hacia sus destinos finales en la red.
        5. **El medio:** Entorno urbano de alta densidad en la zona norte del Valle de México (Alcaldía Azcapotzalco).
        6. **Propósitos y función:** Concentrar, articular y agilizar la transferencia multimodal de pasajeros eficientemente de un punto a otro.
        7. **Atributos:** Capacidad de la flota ({capacidad_oferta} pas.), tiempos de espera y frecuencias de salida (medibles cuantitativamente).
        8. **Metas y objetivos:** Minimizar tiempos de transbordo y evitar saturación en andenes durante {horario_operativo}.
        9. **Componentes, programas y misiones:** Programas operativos de despacho, mantenimiento preventivo de vías y trenes, con la misión de garantizar movilidad segura.
        10. **Administración, agentes y tomadores de decisiones:** Sistema de Transporte Colectivo (Metro), operadores de corredores viales y autoridades de movilidad.
        11. **Estructura (Compleja):** Jerarquía organizacional y física que interconecta la superficie con el sistema subterráneo.
        """)

    st.markdown("---")
    st.markdown("📸 **Ilustrativo 1.** *Diagrama sistémico interactivo del sistema multimodal de transporte de personas en el CETRAM El Rosario*")

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA EN GARRAFÓN
# ==========================================
with tab2:
    st.header("B. Distribución local de agua embotellada en U.H. El Rosario (Transporte de mercancías / Garrafón)")
    
    st.markdown("""
    > **Identificación sistémica:** Ámbito urbano/suburbano, medio terrestre, modo vehículos de redilas de reparto local en U.H. El Rosario, especialización carga.  
    > **Descripción técnica:** Modelo logístico de alta capilaridad y frecuencia (Lunes a Viernes de 9:00 a.m. a 5:00 p.m. y Sábados de 9:00 a.m. a mediodía), priorizando seguridad y regularidad de ruteo.
    """)

    st.markdown("""
        <div class="moving-banner" style="background: #e8f5e9; color: #1b5e20;">
            <span>Ruta Logística en Tránsito: </span>
            <span class="floating-icon">🚚</span>
            <span class="floating-icon">💧</span>
            <span class="floating-icon">📦</span> Reparto Local y Abastecimiento Continuo
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: #e8f5e9; padding: 10px 15px; border-radius: 8px; border-left: 5px solid #2e7d32; margin-bottom: 15px;">
            🎛️ <strong>Panel de Logística Activa:</strong> Modifica la cantidad de vehículos y la demanda para evaluar el cumplimiento de las entregas:
        </div>
    """, unsafe_allow_html=True)

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
    st.subheader("🔄 Modelo Sistémico Dinámico de Carga (Estilo Croquis Interactivo)")

    # ==========================================
    # CONTENEDOR ESTILO IMAGEN (AMBIENTE, ENTRADA, PROCESO, SALIDA, RETROALIMENTACIÓN) - CASO B
    # ==========================================
    st.markdown("""
        <div class="sistema-ambiente-box" style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-color: #16a34a;">
            <div class="ambiente-label" style="color: #15803d;">🌐 AMBIENTE: Entorno Urbano / Suburbano de la U.H. El Rosario</div>
    """, unsafe_allow_html=True)

    col_e2, col_f3, col_p2, col_f4, col_s2 = st.columns([2.2, 0.6, 2.6, 0.6, 2.2])

    with col_e2:
        st.markdown(f"""
        <div class="nodo-sistema" style="border-color: #15803d;">
            <h4 style="color: #15803d; margin-bottom: 8px;">📥 ENTRADA</h4>
            <p style="font-size: 13px; color: #334155; margin: 0;">
                <strong>Recursos:</strong> {unidades_reparto} vehículos de redilas.<br>
                <strong>Insumo/Demanda:</strong> <strong>{pedidos_diarios} Pedidos</strong> de garrafones.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_f3:
        st.markdown('<div class="flecha-flujo" style="color: #16a34a;"><br>➡️</div>', unsafe_allow_html=True)

    with col_p2:
        st.markdown(f"""
        <div class="nodo-proceso" style="background: #14532d; border-color: #052e16;">
            <h4 style="color: #4ade80; margin-bottom: 8px;">⚙️ PROCESO</h4>
            <p style="font-size: 13px; color: #f0fdf4; margin: 0;">
                Envasado, planeación de rutas de entrega domiciliaria y carga física de unidades.<br>
                <em>({demanda_estacional})</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_f4:
        st.markdown('<div class="flecha-flujo" style="color: #16a34a;"><br>➡️</div>', unsafe_allow_html=True)

    with col_s2:
        st.markdown(f"""
        <div class="nodo-sistema" style="border-color: #15803d;">
            <h4 style="color: #15803d; margin-bottom: 8px;">📤 SALIDA</h4>
            <p style="font-size: 13px; color: #334155; margin: 0;">
                <strong>Resultado:</strong><br>
                <strong>{pedidos_diarios} Garrafones entregados</strong> y retorno de envases vacíos.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Bloque inferior de Retroalimentación dentro del Ambiente para Carga
    if pedidos_diarios > capacidad_total_flota:
        texto_retro_b = f"⚠️ Retroalimentación de Alerta Logística: Demanda ({pedidos_diarios}) supera capacidad ({capacidad_total_flota}). Requiere refuerzo."
    elif "Calor" in demanda_estacional:
        texto_retro_b = f"🔄 Retroalimentación Estacional: Operación intensiva por alta demanda debido a {demanda_estacional}."
    else:
        texto_retro_b = "✅ Retroalimentación Estable: Flujo de distribución cumplido en tiempo y forma."

    st.markdown(f"""
        <div class="retroalimentacion-container" style="border-top-color: #16a34a;">
            <div class="retroalimentacion-badge" style="background: #16a34a; box-shadow: 0 4px 12px rgba(22, 163, 74, 0.3);">🔄 Retroalimentación</div>
            <p style="margin-top: 10px; font-weight: bold; color: #1e293b; font-size: 14px;">
                {texto_retro_b}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Haz clic aquí para ver el Marco Completo de los 11 Componentes (Van Gigch, 2006) en Distribución de Agua en U.H. El Rosario"):
        st.markdown(f"""
        1. **Elementos:** Vehículos de redilas, garrafones, choferes repartidores, planta purificadora y clientes residenciales.
        2. **Proceso de conversión:** Envasado, planeación de rutas de entrega domiciliaria y carga física de unidades.
        3. **Entradas y recursos:** Agua purificada, envases vacíos, {unidades_reparto} unidades vehiculares y {pedidos_diarios} pedidos diarios.
        4. **Salidas o resultados:** Garrafones entregados con éxito en los hogares y recolección de envases vacíos.
        5. **El medio:** Entorno vial urbano y suburbano de la Unidad Habitacional El Rosario.
        6. **Propósitos y función:** Abastecer de forma oportuna y segura agua purificada de consumo humano a nivel local.
        7. **Atributos:** Capacidad de carga por unidad (50 garrafones), tiempos de entrega y ventanas horarias de servicio.
        8. **Metas y objetivos:** Cumplir al 100% con los requerimientos diarios optimizando el consumo de combustible y tiempos de ruta.
        9. **Componentes, programas y misiones:** Programas diarios de ruteo, control de inventarios y mantenimiento preventivo de flotilla con la misión de abastecer sin demoras.
        10. **Administración, agentes y tomadores de decisiones:** Administrador de la distribuidora local, choferes repartidores y clientes.
        11. **Estructura (Simple):** Relación operativa lineal y secuencial entre la planta de suministro, la flota de transporte y los puntos de entrega final.
        """)

    st.markdown("---")
    st.markdown("📸 **Ilustrativo 2.** *Diagrama sistémico interactivo del sistema de transporte de mercancías y distribución local de agua en garrafón*")
