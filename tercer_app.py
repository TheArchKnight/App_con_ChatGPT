import streamlit as st


categorias = ["Transporte", "Alimentacion", "Deporte", "Educacion"]
st.title("Gestor de finanzas, creado por Angel Mazo")
st.selectbox("¿Gasto o ingreso?", ["Gasto", "Ingreso"])
st.selectbox("Seleccione la categoria", categorias)
