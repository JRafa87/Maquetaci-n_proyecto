import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# ==========================
# LOGIN SIMPLE
# ==========================
if "login_status" not in st.session_state:
    st.session_state.login_status = False

def login(usuario, clave):
    if usuario == "admin" and clave == "1234":
        st.session_state.login_status = True
        st.success("✅ Login exitoso")
    else:
        st.error("Usuario o contraseña incorrectos")

if not st.session_state.login_status:
    st.markdown("<h1 style='text-align:center;'>🔑 Iniciar Sesión</h1>", unsafe_allow_html=True)
    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        login(usuario, clave)
    st.stop()

# ==========================
# MENÚ LATERAL (PÁGINAS)
# ==========================
with st.sidebar:
    selected = option_menu(
        menu_title="Menú Principal",
        options=["🏠 Dashboard", "📝 CRUD Empleados", "📂 Predicción Lote", "🧮 Simulación Manual"],
        icons=["house","pencil-square","file-earmark-text","calculator"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "darkblue", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": "#cce0ff"},
        }
    )

# ==========================
# DASHBOARD
# ==========================
if selected == "🏠 Dashboard":
    st.markdown("<h1 style='text-align:center;'>🏠 Dashboard</h1>", unsafe_allow_html=True)
    
    # Ejemplo de cards con KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Empleados", "120")
    col2.metric("Promedio Renuncia", "12%")
    col3.metric("Empleados en Riesgo", "8%")
    col4.metric("Satisfacción Salarial", "3.8/5")
    
    # Card visual
    st.markdown("""
    <div style='background-color:white; padding:20px; border-radius:12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-top:20px'>
    <h3>Resumen General</h3>
    <p>Aquí puedes mostrar gráficos, alertas, últimas novedades o indicadores clave de empleados.</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# CRUD EMPLEADOS
# ==========================
elif selected == "📝 CRUD Empleados":
    st.markdown("<h1 style='text-align:center;'>📝 Gestión de Empleados</h1>", unsafe_allow_html=True)
    
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
    <p>Sección donde el usuario sube su archivo para ejecutar predicciones masivas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Sube tu archivo", type=["csv","xlsx"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.dataframe(df.head())
        st.success(f"Archivo cargado: {len(df)} registros")

# ==========================
# SIMULACION MANUAL
# ==========================
elif selected == "🧮 Simulación Manual":
    st.markdown("<h1 style='text-align:center;'>🧮 Simulación Manual</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color:white; padding:20px; border-radius:12px; box-shadow:0 4px 8px rgba(0,0,0,0.1)'>
    <h3>Formulario de simulación</h3>
    <p>Sección donde se ingresan datos manuales para simular la predicción de un empleado.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Nombre")
        st.number_input("Edad", 18, 65, 30)
        st.selectbox("Departamento", ["Ventas","RRHH","Tecnología"])
    with col2:
        st.selectbox("Género", ["M","F"])
        st.number_input("Ingreso mensual", 1000, 20000, 3500)
        st.selectbox("¿Hace horas extra?", ["Sí","No"])
