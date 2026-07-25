import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Modelos Prácticos - Teoría de Sistemas",
    page_icon="🚍",
    layout="wide",
)

# Estilos CSS para tarjetas y flujo animado
st.markdown("""
    <style>
    .system-box {
        background-color: #f8f9fa;
        border: 2px dashed #0083B8;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .flow-arrow {
        text-align: center;
        font-size: 28px;
        color: #0083B8;
        font-weight: bold;
        margin: 5px 0;
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
    *“La construcción de un Centro de Transferencia Modal (Cetram) es quizá uno de los proyectos más complejos que se han desarrollado en los últimos años en la ciudad. Su principal objetivo es concentrar y reorganizar los diferentes sistemas de transporte de la ciudad en un solo lugar. Con base en las estrategias de distribución y control de flujos y circulaciones, se busca mejorar la calidad de vida de quienes se trasladan de un lugar a otro de la ciudad”*.
    """)

    # Controles interactivos con desglose de horarios (Mañana, Tarde, Noche)
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        horario_operativo = st.selectbox(
            "Seleccionar Franja Horaria de Operación:",
            [
                "Hora Pico Matutina (Mañana)", 
                "Hora Valle / Intermedia (Tarde)", 
                "Hora Pico Vespertina / Nocturna (Noche)"
            ]
        )
    with col_c2:
        if "Matutina" in horario_operativo:
            nivel_pax = 12500
            estado_operativo = "Saturación alta por ingresos pendulares hacia zonas laborales y escolares."
        elif "Valle" in horario_operativo:
            nivel_pax = 4500
            estado_operativo = "Operación fluida, estable y con tiempos de espera mínimos."
        else:
            nivel_pax = 11000
            estado_operativo = "Saturación por retornos masivos de la tarde-noche."
        
        st.markdown(f"**Estatus del Sistema:** {estado_operativo}")

    st.markdown("---")
    st.subheader("🔄 Diagrama Sistémico Interactivo con Movimiento de Flujos")

    # Esquema visual paso a paso con iconos
    c_in, c_arrow1, c_proc, c_arrow2, c_out = st.columns([2, 0.5, 2, 0.5, 2])

    with c_in:
        st.markdown("### 📥 1. Entradas")
        st.markdown("""
        <div class="system-box">
        🚆 Trenes (Líneas 6 y 7)<br>
        🚍 Trolebús y Metrobús<br>
        🚐 Combis y microbuses<br>
        🚲 Infraestructura de ciclovías<br>
        🎟️ Andenes y tarifas de acceso
        </div>
        """, unsafe_allow_html=True)

    with c_arrow1:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>🔄</div>", unsafe_allow_html=True)

    with c_proc:
        st.markdown("### ⚙️ 2. Conversión")
        st.markdown(f"""
        <div class="system-box">
        ⚙️ Regulación de flujos peatonales<br>
        ⏱️ Programación de correspondencias<br>
        📋 Control de despacho en andenes<br>
        🕒 <em>Fase activa: {horario_operativo}</em>
        </div>
        """, unsafe_allow_html=True)

    with c_arrow2:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>🔄</div>", unsafe_allow_html=True)

    with c_out:
        st.markdown("### 📤 3. Salidas")
        st.markdown("""
        <div class="system-box">
        👥 Pasajeros transferidos eficientemente<br>
        🌿 Reducción de emisiones por viaje<br>
        🏙️ Ordenamiento del espacio público
        </div>
        """, unsafe_allow_html=True)

    # Bloque de Retroalimentación Interactiva con franjas horarias
    st.markdown("### 🔄 4. Retroalimentación (Feedback)")
    if "Valle" not in horario_operativo:
        st.warning(f"⚠️ **Alerta activa de retroalimentación ({horario_operativo}):** Se detectan demoras en transbordos y alta acumulación de usuarios en andenes. Se requiere reforzar frecuencias de despacho.")
    else:
        st.success(f"✅ **Retroalimentación óptima ({horario_operativo}):** Flujo continuo reportado por los usuarios sin saturación crítica en la correspondencia.")

    st.markdown("---")
    st.markdown("📸 **Ilustrativo 1.** *Diagrama sistémico y evidencia fotográfica del sistema multimodal de transporte de personas en el CETRAM El Rosario (Sussman, 2000; UnADM, 2026).*")

# ==========================================
# PESTAÑA B: DISTRIBUCIÓN DE AGUA EN GARRAFÓN
# ==========================================
with tab2:
    st.header("B. Distribución local de agua embotellada (Transporte de mercancías / Garrafón)")
    
    st.markdown("""
    > **Identificación sistémica:** Ámbito urbano/suburbano, medio terrestre, modo vehículos de redilas de reparto local, especialización carga.  
    > **Descripción técnica:** Modelo logístico de alta capilaridad y frecuencia (Lunes a Viernes de 9:00 a.m. a 5:00 p.m. y Sábados de 9:00 a.m. a mediodía), priorizando seguridad, regularidad y flexibilidad de ruteo.
    """)

    col_d1, col_d2 = st.columns(2)
    with col_d1:
        unidades_reparto = st.slider("Vehículos de redilas en ruta", 1, 8, 3, key="slider_camiones")
    with col_d2:
        demanda_estacional = st.selectbox("Variación de Demanda Estacional", ["Temporada Regular", "Temporada de Calor (Alta Demanda)"])

    total_entregas = unidades_reparto * 45 if "Regular" in demanda_estacional else unidades_reparto * 60

    st.markdown("---")
    st.subheader("🔄 Esquema Sistémico Dinámico de Carga")

    b_in, b_arrow1, b_proc, b_arrow2, b_out = st.columns([2, 0.5, 2, 0.5, 2])

    with b_in:
        st.markdown("### 📥 1. Entradas")
        st.markdown("""
        <div class="system-box">
        💧 Agua purificada en planta<br>
        🔄 Envases de garrafón vacíos<br>
        🚚 Vehículos de redilas<br>
        📋 Pedidos programados de clientes
        </div>
        """, unsafe_allow_html=True)

    with b_arrow1:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>📦</div>", unsafe_allow_html=True)

    with b_proc:
        st.markdown("### ⚙️ 2. Conversión")
        st.markdown(f"""
        <div class="system-box">
        🏭 Proceso de envasado y ruteo<br>
        ⏰ Ventana: L-V (9:00 a 17:00 h) / S (9:00 a 14:00 h)<br>
        <em>Reparto activo: {total_entregas} garrafones</em>
        </div>
        """, unsafe_allow_html=True)

    with b_arrow2:
        st.markdown("<br><br><div class='flow-arrow'>⬇️<br>📦</div>", unsafe_allow_html=True)

    with b_out:
        st.markdown("### 📤 3. Salidas")
        st.markdown("""
        <div class="system-box">
        🏠 Garrafones entregados con éxito<br>
        🔄 Recolección de envases vacíos<br>
        📄 Notas de venta y control
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔄 4. Retroalimentación (Feedback)")
    if "Calor" in demanda_estacional:
        st.warning("⚠️ **Alerta logística:** Incremento por demanda estacional de calor. Se registran tiempos muertos en ruta por mayor tiempo de descarga en puntos de venta.")
    else:
        st.success("✅ **Operación estable:** Cumplimiento del 100% de las rutas programadas sin devoluciones extraordinarias por calidad.")
