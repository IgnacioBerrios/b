import pandas as pd
import streamlit as st
import plotly.express as px

file_path = "spotify_songs_dataset.csv" 
data = pd.read_csv(file_path, delimiter=';')

if 'language' not in data.columns:
    st.error("La columna 'language' no se encuentra en el dataset.")
else:
    st.title("Distribución de Idiomas por Género")

    selected_genres = st.multiselect(
        "Selecciona los géneros que deseas analizar:",
        options=data['genre'].dropna().unique()
    )

    filtered_data = data[data['genre'].isin(selected_genres)] if selected_genres else data

    if filtered_data.empty:
        st.warning("No hay datos para los géneros seleccionados.")
    else:
        language_counts = filtered_data['language'].dropna().value_counts().reset_index()
        language_counts.columns = ['language', 'count']

        fig = px.pie(
            language_counts,
            names='language',
            values='count',
            title='Distribución de Idiomas',
            color_discrete_sequence=px.colors.qualitative.Set3
        )

        st.plotly_chart(fig)
