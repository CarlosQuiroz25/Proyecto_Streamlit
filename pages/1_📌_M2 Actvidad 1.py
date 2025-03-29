import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import json

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

# 1. Diccionario
st.subheader("DataFrame de Libros")
code = '''
libros = {
    "Título": ["1984", "Cien años de soledad", "El principito", "Fahrenheit 451"],
    "Autor": ["George Orwell", "Gabriel García Márquez", "Antoine de Saint-Exupéry", "Ray Bradbury"],
    "Año de Publicación": [1949, 1967, 1943, 1953],
    "Género": ["Distopía", "Realismo mágico", "Fábula", "Ciencia ficción"]
}
df_libros = pd.DataFrame(libros)
st.dataframe(df_libros)'''

st.code(code, language="python")

st.write('Resultado:')
libros = {
    "Título": ["1984", "Cien años de soledad", "El principito", "Fahrenheit 451"],
    "Autor": ["George Orwell", "Gabriel García Márquez", "Antoine de Saint-Exupéry", "Ray Bradbury"],
    "Año de Publicación": [1949, 1967, 1943, 1953],
    "Género": ["Distopía", "Realismo mágico", "Fábula", "Ciencia ficción"]
}
df_libros = pd.DataFrame(libros)
st.dataframe(df_libros)

# 2. Lista de diccionarios
st.subheader("Información de Ciudades")
code = '''
ciudades = [
    {"Nombre": "Nueva York", "Población": 8419600, "País": "EE.UU."},
    {"Nombre": "Tokio", "Población": 37400068, "País": "Japón"},
    {"Nombre": "Londres", "Población": 8982000, "País": "Reino Unido"}
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)'''

st.code(code, language="python")
st.write('Resultado:')
ciudades = [
    {"Nombre": "Nueva York", "Población": 8419600, "País": "EE.UU."},
    {"Nombre": "Tokio", "Población": 37400068, "País": "Japón"},
    {"Nombre": "Londres", "Población": 8982000, "País": "Reino Unido"}
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

# 3. Lista de listas
st.subheader("Productos en Inventario")
code = '''
productos = [
    ["Laptop", 1200, 10],
    ["Mouse", 25, 150],
    ["Teclado", 45, 80]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)'''

st.code(code, language="python")
st.write('Resultado:')
productos = [
    ["Laptop", 1200, 10],
    ["Mouse", 25, 150],
    ["Teclado", 45, 80]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)

# 4. Series
st.subheader("Datos de Personas")
code = '''
nombres = pd.Series(["Ana", "Carlos", "Beatriz", "David"])
edades = pd.Series([25, 30, 22, 28])
ciudades = pd.Series(["Madrid", "Bogotá", "Ciudad de México", "Buenos Aires"])
df_personas = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_personas)'''

st.code(code, language="python")
st.write('Resultado:')
nombres = pd.Series(["Ana", "Carlos", "Beatriz", "David"])
edades = pd.Series([25, 30, 22, 28])
ciudades = pd.Series(["Madrid", "Bogotá", "Ciudad de México", "Buenos Aires"])
df_personas = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_personas)

# 5. CSV local
st.subheader("Datos desde CSV")
code = '''
df_csv = pd.read_csv("data.csv")
st.dataframe(df_csv)'''

st.code(code, language="python")
st.write('Resultado:')
df_csv = pd.read_csv("data/data.csv")
st.dataframe(df_csv)

# 6. Excel local
st.subheader("Datos desde Excel")
code = '''
df_excel = pd.read_excel("data.xlsx")
st.dataframe(df_excel)'''

st.code(code, language="python")
st.write('Resultado:')
df_excel = pd.read_excel("data.xlsx")
st.dataframe(df_excel)

# 7. JSON
st.subheader("Datos de Usuarios desde JSON")
code = '''
with open("data.json") as f:
    data_json = json.load(f)
df_json = pd.DataFrame(data_json)
st.dataframe(df_json)'''

st.code(code, language="python")
st.write('Resultado:')
with open("data.json") as f:
    data_json = json.load(f)
df_json = pd.DataFrame(data_json)
st.dataframe(df_json)

# 8. URL (archivo CSV en línea)
st.subheader("Datos desde URL")
code = '''
csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
df_url = pd.read_csv(csv_url)
st.dataframe(df_url)'''

st.code(code, language="python")
st.write('Resultado:')
csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
df_url = pd.read_csv(csv_url)
st.dataframe(df_url)

# 9. SQLite
st.subheader("Datos desde SQLite")
code = '''
conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        nombre TEXT,
        calificacion INTEGER
    )
""")
cursor.execute("INSERT INTO estudiantes VALUES ('Juan', 85), ('Maria', 90), ('Pedro', 78)")
conn.commit()
df_sqlite = pd.read_sql("SELECT * FROM estudiantes", conn)
st.dataframe(df_sqlite)
conn.close()'''

st.code(code, language="python")
st.write('Resultado:')
conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        nombre TEXT,
        calificacion INTEGER
    )
""")
cursor.execute("INSERT INTO estudiantes VALUES ('Juan', 85), ('Maria', 90), ('Pedro', 78)")
conn.commit()
df_sqlite = pd.read_sql("SELECT * FROM estudiantes", conn)
st.dataframe(df_sqlite)
conn.close()

# 10. NumPy
st.subheader("Datos desde NumPy")
code = '''
array_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_numpy = pd.DataFrame(array_np, columns=["A", "B", "C"])
st.dataframe(df_numpy)'''

st.code(code, language="python")
st.write('Resultado:')
array_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_numpy = pd.DataFrame(array_np, columns=["A", "B", "C"])
st.dataframe(df_numpy)
