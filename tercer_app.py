import streamlit as st
import pandas as pd

# Inicialización de session_state si es la primera vez que se carga
if "finanzas" not in st.session_state:
    st.session_state["finanzas"] = True
    st.session_state["gastos"] = []
    st.session_state["ingresos"] = []
    st.session_state["presupuestos"] = {}


def registrar(tipo, categorias):
    categoria = st.selectbox(f"Seleccione la fuente del {tipo}:", categorias)
    monto = st.number_input(f"Ingrese el monto del {tipo}")
    fecha = st.date_input("Seleccione la fecha")

    if st.button(f"Registrar {tipo}"):
        nuevo_registro = {
            "categoria": categoria,
            "monto": monto,
            "fecha": fecha,
        }
        # Guardar el registro en session_state
        if tipo == "gasto":
            st.session_state["gastos"].append(nuevo_registro)
        elif tipo == "ingreso":
            st.session_state["ingresos"].append(nuevo_registro)
        st.success("¡Registro exitoso!")


def registrar_presupuesto():
    meses = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    categoria = st.selectbox("Seleccione la categoría para el presupuesto:",
                             categorias_gastos)
    monto_presupuesto = st.number_input(
        f"Ingrese el monto presupuestado para {categoria}",
        min_value=0.0, format="%.2f")
    mes = st.selectbox("Seleccione el mes:", meses)
    if st.button("Guardar presupuesto"):
        if mes not in st.session_state["presupuestos"]:
            st.session_state["presupuestos"][mes] = {}
        st.session_state["presupuestos"][mes][categoria] = monto_presupuesto
        st.success(
            f"Presupuesto para {categoria} en {mes} registrado exitosamente.")


def generar_tabla_comparativa():
    """
    Función para generar una tabla comparativa entre lo presupuestado y
    lo gastado.
    """
    datos_comparativos = []
    print(st.session_state["presupuestos"])
    # Recorrer los meses y categorías para mostrar los datos comparativos
    for mes, presupuestos in st.session_state["presupuestos"].items():
        for categoria, presupuesto in presupuestos.items():
            # Filtrar los gastos de cada categoría en el mes correspondiente
            gastos_categoria = sum(
                gasto["monto"] for gasto in st.session_state["gastos"]
                if gasto["categoria"] == categoria
                and gasto["fecha"].strftime('%B') == mes
            )
            # Crear la fila para el mes y la categoría
            datos_comparativos.append({
                "Mes": mes,
                "Categoría": categoria,
                "Presupuestado": presupuesto,
                "Gastado": gastos_categoria,
                "Diferencia": presupuesto - gastos_categoria
            })
    # Convertir los datos a un DataFrame de pandas
    df_comparativo = pd.DataFrame(datos_comparativos)
    return df_comparativo


def crear_tabla():
    df_comparativo = generar_tabla_comparativa()
    st.session_state["df_comparativo"] = df_comparativo


categorias_gastos = ["Transporte", "Alimentación",
                     "Deporte", "Educación", "Otros"]

st.title("Gestor de finanzas, creado por Angel Mazo")

# Selección del tipo de registro
tipo_registro = st.selectbox("¿Qué deseas registrar?", ["Gasto", "Ingreso",
                                                        "Presupuesto"])

if tipo_registro == "Gasto":
    registrar("gasto", categorias_gastos)
elif tipo_registro == "Ingreso":
    categorias = ["Salario", "Venta"]
    registrar("ingreso", categorias)
elif tipo_registro == "Presupuesto":
    registrar_presupuesto()

# Mostrar tabla comparativa
crear_tabla()
st.subheader("Comparativa entre lo Presupuestado y lo Gastado")
st.dataframe(st.session_state["df_comparativo"])
