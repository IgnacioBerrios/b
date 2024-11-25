import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar el archivo de datos
file_path = "spotify_songs_dataset.csv" 
data = pd.read_csv(file_path, delimiter=';')

if 'language' not in data.columns:
    st.error("La columna 'language' no se encuentra en el dataset.")
else:
    st.title("Distribución de Idiomas por Género")

    # Selección de géneros
    selected_genres = st.multiselect(
        "Selecciona los géneros que deseas analizar:",
        options=data['genre'].dropna().unique()
    )

    # Filtrar datos por géneros seleccionados
    filtered_data = data[data['genre'].isin(selected_genres)] if selected_genres else data

    if filtered_data.empty:
        st.warning("No hay datos para los géneros seleccionados.")
    else:
        # Contar idiomas en los datos filtrados
        language_counts = filtered_data['language'].dropna().value_counts().reset_index()
        language_counts.columns = ['language', 'count']

        # Crear gráfico
        fig = px.pie(
            language_counts,
            names='language',
            values='count',
            title='Distribución de Idiomas'
        )

        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig)
