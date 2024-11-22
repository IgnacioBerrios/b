import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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
        language_counts = filtered_data['language'].dropna().value_counts()

        # Crear el gráfico de pie
        fig, ax = plt.subplots()
        ax.pie(
            language_counts, 
            labels=language_counts.index, 
            autopct='%1.1f%%', 
            startangle=90, 
            colors=plt.cm.tab20.colors
        )
        ax.axis('equal')  # Asegura que el gráfico sea circular

        # Mostrar el gráfico
        st.pyplot(fig)
