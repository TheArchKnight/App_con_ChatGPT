import streamlit as st

# Diccionario de funciones de conversión
def celsius_to_fahrenheit(value): return (value * 9 / 5) + 32
def fahrenheit_to_celsius(value): return (value - 32) * 5 / 9
def celsius_to_kelvin(value): return value + 273.15
def kelvin_to_celsius(value): return value - 273.15

def pies_to_metros(value): return value * 0.3048
def metros_to_pies(value): return value / 0.3048
def pulgadas_to_cm(value): return value * 2.54
def cm_to_pulgadas(value): return value / 2.54

def libras_to_kg(value): return value * 0.453592
def kg_to_libras(value): return value / 0.453592
def onzas_to_gramos(value): return value * 28.3495
def gramos_to_onzas(value): return value / 28.3495

def galones_to_litros(value): return value * 3.78541
def litros_to_galones(value): return value / 3.78541
def pulgadas_cubicas_to_cm3(value): return value * 16.3871
def cm3_to_pulgadas_cubicas(value): return value / 16.3871

def horas_to_minutos(value): return value * 60
def minutos_to_segundos(value): return value * 60
def dias_to_horas(value): return value * 24
def semanas_to_dias(value): return value * 7

def mph_to_kph(value): return value * 1.60934
def kph_to_mps(value): return value / 3.6
def nudos_to_mph(value): return value * 1.15078
def mps_to_fps(value): return value * 3.28084

def m2_to_ft2(value): return value * 10.7639
def ft2_to_m2(value): return value / 10.7639
def km2_to_mi2(value): return value * 0.386102
def mi2_to_km2(value): return value / 0.386102

def julios_to_calorias(value): return value * 0.239006
def calorias_to_kj(value): return value * 0.004184
def kwh_to_mj(value): return value * 3.6
def mj_to_kwh(value): return value / 3.6

def pascales_to_atm(value): return value / 101325
def atm_to_pascales(value): return value * 101325
def barras_to_psi(value): return value * 14.5038
def psi_to_bares(value): return value / 14.5038

def mb_to_gb(value): return value / 1024
def gb_to_tb(value): return value / 1024
def kb_to_mb(value): return value / 1024
def tb_to_pb(value): return value / 1024

# Diccionario de categorías y conversiones
conversiones = {
    "Temperatura": {
        "Celsius a Fahrenheit": celsius_to_fahrenheit,
        "Fahrenheit a Celsius": fahrenheit_to_celsius,
        "Celsius a Kelvin": celsius_to_kelvin,
        "Kelvin a Celsius": kelvin_to_celsius,
    },
    "Longitud": {
        "Pies a metros": pies_to_metros,
        "Metros a pies": metros_to_pies,
        "Pulgadas a centímetros": pulgadas_to_cm,
        "Centímetros a pulgadas": cm_to_pulgadas,
    },
    "Peso/Masa": {
        "Libras a kilogramos": libras_to_kg,
        "Kilogramos a libras": kg_to_libras,
        "Onzas a gramos": onzas_to_gramos,
        "Gramos a onzas": gramos_to_onzas,
    },
    "Volumen": {
        "Galones a litros": galones_to_litros,
        "Litros a galones": litros_to_galones,
        "Pulgadas cúbicas a centímetros cúbicos": pulgadas_cubicas_to_cm3,
        "Centímetros cúbicos a pulgadas cúbicas": cm3_to_pulgadas_cubicas,
    },
    "Tiempo": {
        "Horas a minutos": horas_to_minutos,
        "Minutos a segundos": minutos_to_segundos,
        "Días a horas": dias_to_horas,
        "Semanas a días": semanas_to_dias,
    },
    "Velocidad": {
        "Millas por hora a kilómetros por hora": mph_to_kph,
        "Kilómetros por hora a metros por segundo": kph_to_mps,
        "Nudos a millas por hora": nudos_to_mph,
        "Metros por segundo a pies por segundo": mps_to_fps,
    },
    "Área": {
        "Metros cuadrados a pies cuadrados": m2_to_ft2,
        "Pies cuadrados a metros cuadrados": ft2_to_m2,
        "Kilómetros cuadrados a millas cuadradas": km2_to_mi2,
        "Millas cuadradas a kilómetros cuadrados": mi2_to_km2,
    },
    "Energía": {
        "Julios a calorías": julios_to_calorias,
        "Calorías a kilojulios": calorias_to_kj,
        "Kilovatios-hora a megajulios": kwh_to_mj,
        "Megajulios a kilovatios-hora": mj_to_kwh,
    },
    "Presión": {
        "Pascales a atmósferas": pascales_to_atm,
        "Atmósferas a pascales": atm_to_pascales,
        "Barras a libras por pulgada cuadrada": barras_to_psi,
        "Libras por pulgada cuadrada a bares": psi_to_bares,
    },
    "Tamaño de datos": {
        "Megabytes a gigabytes": mb_to_gb,
        "Gigabytes a Terabytes": gb_to_tb,
        "Kilobytes a megabytes": kb_to_mb,
        "Terabytes a petabytes": tb_to_pb,
    },
}

# Interfaz Streamlit
st.title("Conversor Universal")
st.write("Selecciona una categoría, el tipo de conversión y el valor.")

# Selección de categoría y tipo de conversión
categoria = st.selectbox("Selecciona la categoría:", list(conversiones.keys()))
tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                               list(conversiones[categoria].keys()))

# Ingreso de valor
valor = st.number_input("Ingresa el valor a convertir:")

# Realizar conversión
if valor:
    resultado = conversiones[categoria][tipo_conversion](valor)
    st.write(f"El resultado de la conversión es: {resultado:.4f}")
