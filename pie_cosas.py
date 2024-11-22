import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar los datos
file_path = "spotify_songs_dataset.csv"  # Ajustar la ruta si es necesario
data = pd.read_csv(file_path, delimiter=';')

# Verificar si la columna 'language' existe
if 'language' not in data.columns:
    st.error("La columna 'language' no se encuentra en el dataset.")
else:
    # Título de la aplicación
    st.title("Distribución de Idiomas por Género")

    # Filtro de géneros
    selected_genres = st.multiselect(
        "Selecciona los géneros que deseas analizar:",
        options=data['genre'].dropna().unique()
    )

    # Filtrar los datos
    filtered_data = data[data['genre'].isin(selected_genres)] if selected_genres else data

    # Verificar si hay datos después del filtro
    if filtered_data.empty:
        st.warning("No hay datos para los géneros seleccionados.")
    else:
        # Contar los idiomas, ignorando valores nulos
        language_counts = filtered_data['language'].dropna().value_counts().reset_index()
        language_counts.columns = ['language', 'count']

        # Crear el gráfico de pastel interactivo con Plotly
        fig = px.pie(
            language_counts,
            names='language',
            values='count',
            title='Distribución de Idiomas',
            color_discrete_sequence=px.colors.qualitative.Set3
        )

        # Mostrar el gráfico
        st.plotly_chart(fig)
