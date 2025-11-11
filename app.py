import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Maqueta App", layout="wide")

# ==========================
# MENÚ LATERAL
# ==========================
with st.sidebar:
    selected = st.radio(
        "Menú",
        ["📝 CRUD Empleados", "📂 Predicción Lote", "🧮 Simulación Manual"]
    )

# ==========================
# CRUD EMPLEADOS
# ==========================
if selected == "📝 CRUD Empleados":
    st.markdown("<h1 style='text-align:center;'>📝 CRUD de Empleados</h1>", unsafe_allow_html=True)
    
    crud_option = st.radio("Acción", ["Crear", "Leer", "Actualizar", "Eliminar"], horizontal=True)
    
    if crud_option == "Leer":
        # Tabla de ejemplo
        df_empleados = pd.DataFrame({
            "ID": [1,2,3],
            "Nombre": ["Ana","Luis","Carlos"],
            "Departamento": ["Ventas","RRHH","Tecnología"],
            "Cargo": ["Analista","Especialista","Ingeniero"]
        })
        st.dataframe(df_empleados)
    else:
        st.markdown(f"""
        <div style='background-color:white; padding:20px; border-radius:12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
        <h3>Formulario para {crud_option}</h3>
        <p>Aquí irán los campos para {crud_option.lower()} un empleado.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================
# PREDICCION DESDE ARCHIVO
# ==========================
elif selected == "📂 Predicción Lote":
    st.markdown("<h1 style='text-align:center;'>📂 Predicción desde archivo</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color:white; padding:20px; border-radius:12px; box-shadow:0 4px 8px rgba(0,0,0,0.1)'>
    <h3>Carga de archivo CSV o Excel</h3>
    <p>Sube un archivo para ver cómo se mostrarían los resultados de la predicción.</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Sube tu archivo", type=["csv","xlsx"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        # Simular columna de probabilidad y recomendación
        df['Probabilidad_Renuncia'] = np.random.rand(len(df))
        df['Recomendacion'] = ["Ejemplo de recomendación"]*len(df)
        st.dataframe(df.head())
        st.success(f"Archivo cargado: {len(df)} registros")

# ==========================
# SIMULACION MANUAL
# ==========================
elif selected == "🧮 Simulación Manual":
    st.markdown("<h1 style='text-align:center;'>🧮 Simulación Manual</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre")
        edad = st.slider("Edad", 18, 65, 30)
        departamento = st.selectbox("Departamento", ["Ventas","RRHH","Tecnología"])
    with col2:
        genero = st.selectbox("Género", ["M","F"])
        ingreso = st.number_input("Ingreso mensual", 1000, 20000, 3500)
        horas_extra = st.selectbox("¿Hace horas extra?", ["Sí","No"])
    
    if st.button("Simular predicción"):
        prob = np.random.rand()
        st.markdown(f"""
            <div style='background-color:#f0f2f6; padding:15px; border-radius:10px; text-align:center;'>
                <h3>Resultado de simulación</h3>
                <p>Probabilidad de renuncia: <b style='color:{"red" if prob>0.5 else "green"}'>{prob:.1%}</b></p>
                <p>Recomendación: Ejemplo de recomendación basada en datos ingresados.</p>
            </div>
        """, unsafe_allow_html=True)

