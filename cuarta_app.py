import streamlit as st
import pandas as pd

# Inicialización de session_state si es la primera vez que se carga
if "materias" not in st.session_state:
    st.session_state["materias"] = []

# Función para registrar las materias, calificaciones y créditos
def registrar_materia():
    nombre = st.text_input("Nombre de la materia")
    calificacion = st.number_input("Calificación (0-5)", min_value=0.0, max_value=5.0, step=0.1)
    creditos = st.number_input("Créditos", min_value=1, step=1)
    
    # Lista de tipos de materias actualizada
    tipos_materias = [
        "Disciplinar Obligatoria", "Disciplinar Optativa", 
        "Libre Elección", "Nivelación", 
        "Fundamental Obligatoria", "Fundamental Optativa"
    ]
    
    tipo = st.selectbox("Tipo de materia", tipos_materias)
    
    if st.button("Registrar materia"):
        nueva_materia = {
            "Nombre": nombre,
            "Calificación": calificacion,
            "Créditos": creditos,
            "Tipo": tipo
        }
        st.session_state["materias"].append(nueva_materia)
        st.success(f"Materia {nombre} registrada exitosamente.")

# Función para calcular el PAPA global
def calcular_papa_global():
    if not st.session_state["materias"]:
        st.error("No hay materias registradas.")
        return None

    # Crear un DataFrame con los datos de las materias
    df = pd.DataFrame(st.session_state["materias"])
    # Calcular el valor ponderado para cada materia
    df["Valor Ponderado"] = df["Calificación"] * df["Créditos"]
    # Calcular el PAPA global
    papa_global = df["Valor Ponderado"].sum() / df["Créditos"].sum()
    return papa_global

# Función para calcular el PAPA por tipología de asignatura
def calcular_papa_por_tipo():
    if not st.session_state["materias"]:
        st.error("No hay materias registradas.")
        return None

    # Crear un DataFrame con los datos de las materias
    df = pd.DataFrame(st.session_state["materias"])
    # Calcular el valor ponderado para cada materia
    df["Valor Ponderado"] = df["Calificación"] * df["Créditos"]
    
    # Calcular el PAPA por tipo de materia
    papa_por_tipo = df.groupby("Tipo").apply(
        lambda x: x["Valor Ponderado"].sum() / x["Créditos"].sum()
    ).reset_index(name="PAPA")
    
    return papa_por_tipo

# Interfaz de usuario
st.title("Cálculo del PAPA (Promedio Académico)")

# Registro de materias
st.header("Registrar Materias")
registrar_materia()

# Botón para calcular el PAPA global
if st.button("Calcular PAPA Global"):
    papa_global = calcular_papa_global()
    if papa_global is not None:
        st.subheader(f"PAPA Global: {papa_global:.2f}")

# Botón para calcular el PAPA por tipo de asignatura
if st.button("Calcular PAPA por Tipo de Asignatura"):
    papa_por_tipo = calcular_papa_por_tipo()
    if papa_por_tipo is not None:
        st.subheader("PAPA por Tipo de Asignatura")
        st.dataframe(papa_por_tipo)

# Mostrar las materias registradas
st.subheader("Materias Registradas")
if st.session_state["materias"]:
    df_materias = pd.DataFrame(st.session_state["materias"])
    st.dataframe(df_materias)

