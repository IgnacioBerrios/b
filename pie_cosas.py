import pandas as pd
import streamlit as st
import plotly.express as px

ruta_archivo = "spotify_songs_dataset.csv" 
datos = pd.read_csv(ruta_archivo, delimiter=';')

if 'language' not in datos.columns:
    st.error("La columna 'language' no se encuentra en el conjunto de datos.")
else:
    st.title("Distribución de Idiomas por Género")

    generos_seleccionados = st.multiselect(
        "Selecciona los géneros que deseas analizar:",
        options=datos['genre'].dropna().unique()
    )

    datos_filtrados = datos[datos['genre'].isin(generos_seleccionados)] if generos_seleccionados else datos

    if datos_filtrados.empty:
        st.warning("No hay datos para los géneros seleccionados.")
    else:
        conteo_idiomas = datos_filtrados['language'].dropna().value_counts().reset_index()
        conteo_idiomas.columns = ['idioma', 'cantidad']

        figura = px.pie(
            conteo_idiomas,
            names='idioma',
            values='cantidad',
            title='Distribución de Idiomas',
            color_discrete_sequence=px.colors.qualitative.Set3
        )

        st.plotly_chart(figura)
