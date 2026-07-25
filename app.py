import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos Prácticos - Teoría de Sistemas",
    page_icon="💧",
    layout="wide",
)

# Estilos CSS avanzados con colores vibrantes y efectos visuales integrados en cascada
st.markdown("""
    <style>
    /* Estilos personalizados para el botón desplegable / expansor de alta visibilidad */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #fff9c4 0%, #ffe082 100%) !important;
        border: 2px solid #ff8f00 !important;
        border-radius: 12px !important;
        color: #d84315 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        box-shadow: 0 4px 15px rgba(255, 143, 0, 0.3);
    }

    /* Contenedor principal que simula el AMBIENTE circundante con colores vibrantes */
    .sistema-ambiente-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border: 4px dashed #0288d1;
        border-radius: 24px;
        padding: 35px 25px;
        margin: 25px 0;
        position: relative;
        box-shadow: 0 12px 30px rgba(2, 136, 209, 0.2);
        animation: pulseEnvironment 4s ease-in-out infinite;
    }

    /* Etiqueta superior del AMBIENTE */
    .ambiente-label {
        text-align: center;
        font-size: 26px;
        font-weight: 900;
        color: #c62828;
        letter-spacing: 2px;
        margin-bottom: 25px;
        text-transform: uppercase;
        text-shadow: 3px 3px 6px rgba(198, 40, 40, 0.2);
    }

    /* Tarjetas dinámicas hiper-coloridas y llamativas para Entrada, Proceso, Salida y Retroalimentación */
    .nodo-entrada {
        background: linear-gradient(135deg, #ffffff 0%, #e1f5fe 100%);
        border: 4px solid #0288d1;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(2, 136, 209, 0.25);
        margin-bottom: 15px;
    }

    .nodo-proceso {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: #ffffff;
        border: 4px solid #f59e0b;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(245, 158, 11, 0.3);
        margin-bottom: 15px;
    }

    .nodo-salida {
        background: linear-gradient(135deg, #ffffff 0%, #e8f5e9 100%);
        border: 4px solid #2e7d32;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(46, 125, 50, 0.25);
        margin-bottom: 15px;
    }

    .nodo-retro {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border: 4px solid #f57c00;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(245, 124, 0, 0.25);
    }

    /* Flechas verticales de flujo integradas y llamativas */
    .flecha-vertical {
        text-align: center;
        font-size: 32px;
        font-weight: 900;
        color: #ff6f00;
        margin: 5px 0 15px 0;
        animation: bounceArrowVertical 1.5s ease-in-out infinite;
        text-shadow: 2px 2px 4px rgba(255, 111, 0, 0.3);
    }

    @keyframes pulseEnvironment {
        0% { border-color: #0288d1; box-shadow: 0 12px 30px rgba(2, 136, 209, 0.2); }
        50% { border-color: #ff8f00; box-shadow: 0 18px 40px rgba(255, 143, 0, 0.3); }
        100% { border-color: #0288d1; box-shadow: 0 12px 30px rgba(2, 136, 209, 0.2); }
    }

    @keyframes bounceArrowVertical {
        0%, 100% { transform: translateY(0); opacity: 0.7; }
        50% { transform: translateY(6px); opacity: 1; }
    }

    .moving-banner {
        overflow: hidden;
        white-space: nowrap;
        background: linear-gradient(90deg, #e1f5fe 0%, #fff9c4 50%, #e8f5e9 100%);
        padding: 12px;
        border-radius: 10px;
        font-weight: 800;
        color: #d84315;
        margin-bottom: 20px;
        border: 2px solid #ffb300;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    .floating-icon {
        display: inline-block;
        font-size: 26px;
        margin: 0 6px;
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
with st.expander("👉 ¡REVISA AQUÍ LAS INDICACIONES! (Guía Interactiva)", expanded=True):
    st.markdown("""
    <div style="background-color: #fffde7; padding: 12px; border-radius: 8px; border: 1px solid #ffd54f;">
        <p style="color: #3e2723; font-size: 15px; margin-bottom: 10px; font-weight: bold;">
            ¡Bienvenida! Instrucciones de uso para el modelo sistémico integrado:
        </p>
        <ol style="color: #4e342e; margin: 0; padding-left: 20px;">
            <li><strong>Selecciona una pestaña abajo:</strong> Elige entre el caso de pasajeros (CETRAM) o el de mercancías (Agua en garrafón).</li>
            <li><strong>Usa los controles deslizantes:</strong> Modifica los valores de flota y demanda para ver el comportamiento en tiempo real.</li>
            <li><strong>Visualización Integrada en Cascada:</strong> Los componentes se despliegan automáticamente uno debajo de otro conectados por flechas verticales, revelando el ciclo completo (Entrada ➔ Proceso ➔ Salida ➔ Retroalimentación).</li>
        </ol>
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
        <div style="background-color: #e0f7fa; padding: 12px 18px; border-radius: 10px; border-left: 6px solid #00acc1; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,172,193,0.15);">
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
        <div style="background-color: #ffebee; border: 2px solid #ef5350; padding: 15px; border-radius: 10px; color: #c62828; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(239,83,80,0.2);">
            ⚠️ <strong>ESTATUS OPERATIVO (ALERTA):</strong> Capacidad de flota: <strong>{capacidad_oferta} pasajeros</strong> | Demanda actual: <strong>{pasajeros_flota} pasajeros</strong><br>
            <em>Diagnóstico: {estado_operativo}</em>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color: #e8f5e9; border: 2px solid #66bb6a; padding: 15px; border-radius: 10px; color: #2e7d32; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(102,187,106,0.2);">
            ✅ <strong>ESTATUS OPERATIVO (ÓPTIMO):</strong> Capacidad de flota: <strong>{capacidad_oferta} pasajeros</strong> | Demanda actual: <strong>{pasajeros_flota} pasajeros</strong><br>
            <em>Diagnóstico: {estado_operativo}</em>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🔄 Modelo Sistémico Dinámico Integrado en Cascada (CETRAM El Rosario)")

    # ==========================================
    # CONTENEDOR INTEGRADO EN CASCADA VERTICAL (CASO A)
    # ==========================================
    st.markdown("""
        <div class="sistema-ambiente-box">
            <div class="ambiente-label">🌐 AMBIENTE: Entorno Urbano / Zona Norte del Valle de México (Azcapotzalco)</div>
    """, unsafe_allow_html=True)

    # 1. ENTRADA
    st.markdown(f"""
    <div class="nodo-entrada">
        <h3 style="color: #0288d1; margin-bottom: 10px; font-weight: 900;">📥 1. ENTRADA</h3>
        <p style="font-size: 14px; color: #1e293b; margin: 0; font-weight: 600;">
            <strong>Recursos Iniciales:</strong> {num_trenes} trenes activos (L6/L7), {num_buses} unidades de superficie.<br>
            <strong>Demanda Entrante:</strong> <span style="color: #d32f2f; font-weight: bold;">{pasajeros_flota} Pasajeros</span> ingresando al sistema multimodal.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="flecha-vertical">⬇️</div>', unsafe_allow_html=True)

    # 2. PROCESO
    st.markdown(f"""
    <div class="nodo-proceso">
        <h3 style="color: #fbbf24; margin-bottom: 10px; font-weight: 900;">⚙️ 2. PROCESO DE TRANSFORMACIÓN</h3>
        <p style="font-size: 14px; color: #f8fafc; margin: 0;">
            Regulación de flujos peatonales, correspondencia multimodal y despacho sincronizado en andenes.<br>
            <em>Condición operativa: {horario_operativo}</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="flecha-vertical">⬇️</div>', unsafe_allow_html=True)

    # 3. SALIDA
    st.markdown(f"""
    <div class="nodo-salida">
        <h3 style="color: #2e7d32; margin-bottom: 10px; font-weight: 900;">📤 3. SALIDA</h3>
        <p style="font-size: 14px; color: #1e293b; margin: 0; font-weight: 600;">
            <strong>Resultado del Sistema:</strong><br>
            <span style="color: #2e7d32; font-weight: bold;">{pasajeros_flota} Pasajeros transferidos</span> de forma segura hacia sus destinos en la red de transporte.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="flecha-vertical">⬇️</div>', unsafe_allow_html=True)

    # 4. RETROALIMENTACIÓN
    if pasajeros_flota > capacidad_oferta:
        texto_retro = f"⚠️ Retroalimentación de Alerta: Saturación detectada ({pasajeros_flota} pax > Capacidad {capacidad_oferta}). Requiere ajuste de frecuencias."
    elif nivel_alerta:
        texto_retro = f"🔄 Retroalimentación Operativa: Monitoreo activo por alta concentración en {horario_operativo}."
    else:
        texto_retro = "✅ Retroalimentación Estable: Flujo continuo y óptimo en transbordos modales."

    st.markdown(f"""
    <div class="nodo-retro">
        <h3 style="color: #e65100; margin-bottom: 10px; font-weight: 900;">🔄 4. RETROALIMENTACIÓN (FEEDBACK)</h3>
        <p style="font-size: 14px; color: #bf360c; margin: 0; font-weight: 700;">
            {texto_retro}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True) # Cierre de ambiente box

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
    st.markdown("📸 **Ilustrativo 1.** *Diagrama sistémico integrado en cascada para el sistema multimodal en CETRAM El Rosario*")

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
        <div class="moving-banner" style="background: linear-gradient(90deg, #e8f5e9 0%, #c8e6c9 100%); color: #1b5e20; border-color: #66bb6a;">
            <span>Ruta Logística en Tránsito: </span>
            <span class="floating-icon">🚚</span>
            <span class="floating-icon">💧</span>
            <span class="floating-icon">📦</span> Reparto Local y Abastecimiento Continuo
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: #e8f5e9; padding: 12px 18px; border-radius: 10px; border-left: 6px solid #2e7d32; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(46,125,50,0.15);">
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
        <div style="background-color: #ffebee; border: 2px solid #ef5350; padding: 15px; border-radius: 10px; color: #c62828; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(239,83,80,0.2);">
            ⚠️ <strong>ESTATUS LOGÍSTICO (ALERTA):</strong> Capacidad de flota: <strong>{capacidad_total_flota} garrafones</strong> | Demanda de pedidos: <strong>{pedidos_diarios} garrafones</strong><br>
            <em>Diagnóstico: Operación bajo alta exigencia o déficit de cobertura por {demanda_estacional}.</em>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color: #e8f5e9; border: 2px solid #66bb6a; padding: 15px; border-radius: 10px; color: #2e7d32; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(102,187,106,0.2);">
            ✅ <strong>ESTATUS LOGÍSTICO (ESTABLE):</strong> Capacidad de flota: <strong>{capacidad_total_flota} garrafones</strong> | Demanda de pedidos: <strong>{pedidos_diarios} garrafones</strong><br>
            <em>Diagnóstico: Cobertura óptima dentro de los parámetros de ruta habituales.</em>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🔄 Modelo Sistémico Dinámico Integrado en Cascada (Distribución de Carga)")

    # ==========================================
    # CONTENEDOR INTEGRADO EN CASCADA VERTICAL (CASO B)
    # ==========================================
    st.markdown("""
        <div class="sistema-ambiente-box" style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-color: #16a34a; box-shadow: 0 12px 30px rgba(22, 163, 74, 0.2);">
            <div class="ambiente-label" style="color: #15803d;">🌐 AMBIENTE: Entorno Urbano / Suburbano de la U.H. El Rosario</div>
    """, unsafe_allow_html=True)

    # 1. ENTRADA
    st.markdown(f"""
    <div class="nodo-entrada" style="border-color: #16a34a; background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);">
        <h3 style="color: #15803d; margin-bottom: 10px; font-weight: 900;">📥 1. ENTRADA</h3>
        <p style="font-size: 14px; color: #1e293b; margin: 0; font-weight: 600;">
            <strong>Recursos Iniciales:</strong> {unidades_reparto} vehículos de redilas en ruta.<br>
            <strong>Insumos / Demanda:</strong> <span style="color: #15803d; font-weight: bold;">{pedidos_diarios} Pedidos</span> diarios de garrafones.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="flecha-vertical" style="color: #16a34a;">⬇️</div>', unsafe_allow_html=True)

    # 2. PROCESO
    st.markdown(f"""
    <div class="nodo-proceso" style="background: linear-gradient(135deg, #14532d 0%, #052e16 100%); border-color: #22c55e;">
        <h3 style="color: #4ade80; margin-bottom: 10px; font-weight: 900;">⚙️ 2. PROCESO DE TRANSFORMACIÓN</h3>
        <p style="font-size: 14px; color: #f0fdf4; margin: 0;">
            Envasado, planeación de rutas de entrega domiciliaria y carga física de unidades vehiculares.<br>
            <em>Condición estacional: {demanda_estacional}</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="flecha-vertical" style="color: #16a34a;">⬇️</div>', unsafe_allow_html=True)

    # 3. SALIDA
    st.markdown(f"""
    <div class="nodo-salida" style="border-color: #16a34a; background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);">
        <h3 style="color: #15803d; margin-bottom: 10px; font-weight: 900;">📤 3. SALIDA</h3>
        <p style="font-size: 14px; color: #1e293b; margin: 0; font-weight: 600;">
            <strong>Resultado del Sistema:</strong><br>
            <span style="color: #15803d; font-weight: bold;">{pedidos_diarios} Garrafones entregados</span> con éxito en hogares y recolección de envases vacíos.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="flecha-vertical" style="color: #16a34a;">⬇️</div>', unsafe_allow_html=True)

    # 4. RETROALIMENTACIÓN
    if pedidos_diarios > capacidad_total_flota:
        texto_retro_b = f"⚠️ Retroalimentación de Alerta Logística: Demanda ({pedidos_diarios}) supera capacidad ({capacidad_total_flota}). Requiere refuerzo de flota."
    elif "Calor" in demanda_estacional:
        texto_retro_b = f"🔄 Retroalimentación Estacional: Operación intensiva por alta demanda debido a {demanda_estacional}."
    else:
        texto_retro_b = "✅ Retroalimentación Estable: Flujo de distribución cumplido en tiempo y forma."

    st.markdown(f"""
    <div class="nodo-retro" style="border-color: #15803d; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);">
        <h3 style="color: #15803d; margin-bottom: 10px; font-weight: 900;">🔄 4. RETROALIMENTACIÓN (FEEDBACK)</h3>
        <p style="font-size: 14px; color: #064e3b; margin: 0; font-weight: 700;">
            {texto_retro_b}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True) # Cierre de ambiente box B

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
    st.markdown("📸 **Ilustrativo 2.** *Diagrama sistémico integrado en cascada para el sistema de distribución local de agua*")
