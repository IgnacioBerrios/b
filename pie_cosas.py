import pandas as pd
import streamlit as st
import plotly.express as px

ruta = "spotify_songs_dataset.csv" 
data = pd.read_csv(ruta, delimiter=';')

if 'language' not in data.columns:
    st.error("La columna 'language' no se encuentra en el dataset.")
else:
    st.title("Distribución de Idiomas por Género")

    seleccionar_genero = st.multiselect(
        "Selecciona los géneros que deseas analizar:",
        options=data['genre'].dropna().unique()
    )

    filtrar_data = data[data['genre'].isin(seleccionar_genero)] if seleccionar_genero else data

    if filtrar_data.empty:
        st.warning("No hay datos para los géneros seleccionados.")
    else:
        contar_lenguaje = filtrar_data['language'].dropna().value_counts().reset_index()
        contar_lenguaje.columns = ['language', 'count']

        fig = px.pie(
            contar_lenguaje,
            names='language',
            values='count',
            title='Distribución de Idiomas'
        )

        st.plotly_chart(fig)
