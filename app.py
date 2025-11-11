import streamlit as st
import pandas as pd

st.set_page_config(page_title="Maqueta Visual", layout="wide")

# ===== Menú lateral =====
with st.sidebar:
    selected = st.radio(
        "Menú",
        ["👥 Gestión de Empleados", "📂 Predicción Lote", "🧮 Simulación Manual"]
    )

# ===== Gestión de Empleados =====
if selected == "👥 Gestión de Empleados":
    st.markdown("<h1 style='text-align:center;'>Gestión de Empleados</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background-color:#e0f7fa; padding:15px; border-radius:12px;'>
        <h3>Tabla de Empleados</h3>
        <p>Sección con datos de ejemplo (solo visual).</p>
    </div>
    """, unsafe_allow_html=True)

    df = pd.DataFrame({
        "ID": [1,2,3],
        "Nombre": ["Ana","Luis","Carlos"],
        "Departamento": ["Ventas","RRHH","Tecnología"],
        "Cargo": ["Analista","Especialista","Ingeniero"]
    })
    st.dataframe(df)

    st.markdown("""
    <div style='background-color:#fff3e0; padding:15px; border-radius:12px; margin-top:10px;'>
        <h3>Acciones (solo visual)</h3>
        <p>Espacio para Crear, Actualizar y Eliminar empleados.</p>
    </div>
    """, unsafe_allow_html=True)

# ===== Predicción desde archivo =====
elif selected == "📂 Predicción Lote":
    st.markdown("<h1 style='text-align:center;'>Predicción desde archivo</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background-color:#fff9c4; padding:15px; border-radius:12px;'>
        <h3>Instrucciones</h3>
        <p>Uploader simulado y tabla de resultados de ejemplo.</p>
    </div>
    """, unsafe_allow_html=True)

    # Tabla de ejemplo
    df = pd.DataFrame({
        "Empleado": ["Ana","Luis","Carlos"],
        "Probabilidad_Renuncia": ["30%","70%","45%"],
        "Recomendación": ["Satisfacción laboral","Revisar carga","Seguir monitoreo"]
    })
    st.dataframe(df)

# ===== Simulación Manual =====
elif selected == "🧮 Simulación Manual":
    st.markdown("<h1 style='text-align:center;'>Simulación Manual</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Nombre")
        st.slider("Edad", 18, 65, 30)
        st.selectbox("Departamento", ["Ventas","RRHH","Tecnología","Finanzas"])
    with col2:
        st.selectbox("Género", ["M","F"])
        st.number_input("Ingreso mensual", 1000, 20000, 3500)
        st.selectbox("¿Hace horas extra?", ["Sí","No"])

    st.markdown("""
    <div style='background-color:#f0f4c3; padding:15px; border-radius:12px; margin-top:10px;'>
        <h3>Resultado de simulación (visual)</h3>
        <p>Probabilidad de renuncia y recomendación solo para mostrar diseño.</p>
    </div>
    """, unsafe_allow_html=True)



