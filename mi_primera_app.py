import streamlit as st

# Título de la app
st.title("Mi primera app")

# Información del autor
st.write("Esta app fue elaborada por **Angel Mazo**.")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Mostrar mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
