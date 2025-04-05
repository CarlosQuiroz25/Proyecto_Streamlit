import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

# 1. Ver las primeras y últimas 5 filas
st.subheader("Primeras y últimas 5 filas del dataset")
code = '''
import pandas as pd

# Cargar el dataset
df = pd.read_csv("static\datasets\estudiantes_colombia.csv")

# Mostrar primeras 5 filas
st.write("Primeras 5 filas:")
st.dataframe(df.head())

# Mostrar últimas 5 filas
st.write("Últimas 5 filas:")
st.dataframe(df.tail())'''

st.code(code, language="python")
st.write('Resultado:')

# Cargar el dataset
df = pd.read_csv("static\datasets\estudiantes_colombia.csv")

# Mostrar primeras 5 filas
st.write("Primeras 5 filas:")
st.dataframe(df.head())

# Mostrar últimas 5 filas
st.write("Últimas 5 filas:")
st.dataframe(df.tail())

# 2. Mostrar resumen con .info() y .describe()
st.subheader("Resumen del dataset")
code = '''
# Mostrar información del dataset
st.write("Información del dataset:")
st.write("Número de filas:", len(df))
st.write("Número de columnas:", len(df.columns))
st.write("Columnas:", df.columns.tolist())
st.write("Tipos de datos:")
st.dataframe(df.dtypes.to_frame('Tipo de dato'))

# Mostrar estadísticas descriptivas
st.write("Estadísticas descriptivas:")
st.dataframe(df.describe())'''

st.code(code, language="python")
st.write('Resultado:')

# Mostrar información del dataset
st.write("Información del dataset:")
st.write("Número de filas:", len(df))
st.write("Número de columnas:", len(df.columns))
st.write("Columnas:", df.columns.tolist())
st.write("Tipos de datos:")
st.dataframe(df.dtypes.to_frame('Tipo de dato'))

# Mostrar estadísticas descriptivas
st.write("Estadísticas descriptivas:")
st.dataframe(df.describe())

# 3. Selección de columnas específicas
st.subheader("Selección de columnas específicas")
code = '''
# Crear multiselect para elegir columnas
columnas_seleccionadas = st.multiselect(
    "Selecciona las columnas que deseas ver:",
    options=df.columns.tolist(),
    default=["nombre", "edad", "promedio"]
)

# Mostrar el dataframe con las columnas seleccionadas
if columnas_seleccionadas:
    st.dataframe(df[columnas_seleccionadas])'''

st.code(code, language="python")
st.write('Resultado:')

# Crear multiselect para elegir columnas
columnas_seleccionadas = st.multiselect(
    "Selecciona las columnas que deseas ver:",
    options=df.columns.tolist(),
    default=["nombre", "edad", "promedio"]
)

# Mostrar el dataframe con las columnas seleccionadas
if columnas_seleccionadas:
    st.dataframe(df[columnas_seleccionadas])

# 4. Filtrar por promedio
st.subheader("Filtrado por promedio")
code = '''
# Crear slider para seleccionar el promedio mínimo
promedio_minimo = st.slider(
    "Selecciona el promedio mínimo:",
    min_value=float(df["promedio"].min()),
    max_value=float(df["promedio"].max()),
    value=float(df["promedio"].mean()),
    step=0.1
)

# Filtrar y mostrar estudiantes con promedio mayor al seleccionado
estudiantes_filtrados = df[df["promedio"] > promedio_minimo]
st.write(f"Estudiantes con promedio mayor a {promedio_minimo}:")
st.dataframe(estudiantes_filtrados)'''

st.code(code, language="python")
st.write('Resultado:')

# Crear slider para seleccionar el promedio mínimo
promedio_minimo = st.slider(
    "Selecciona el promedio mínimo:",
    min_value=float(df["promedio"].min()),
    max_value=float(df["promedio"].max()),
    value=float(df["promedio"].mean()),
    step=0.1
)

# Filtrar y mostrar estudiantes con promedio mayor al seleccionado
estudiantes_filtrados = df[df["promedio"] > promedio_minimo]
st.write(f"Estudiantes con promedio mayor a {promedio_minimo}:")
st.dataframe(estudiantes_filtrados)

