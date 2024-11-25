import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar el archivo de datos
file_path = "spotify_songs_dataset.csv" 
data = pd.read_csv(file_path, delimiter=';')

# Verificar que la columna 'language' existe
if 'language' not in data.columns:
    st.error("La columna 'language' no se encuentra en el dataset.")
else:
    # Título principal
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Distribución de Idiomas por Género</h1>", unsafe_allow_html=True)
    st.write("Explora cómo se distribuyen los idiomas en tu dataset de Spotify según los géneros seleccionados.")

    # Sección para seleccionar géneros
    st.markdown("### 1. Selecciona los géneros que deseas analizar")
    selected_genres = st.multiselect(
        "Elige uno o más géneros:",
        options=data['genre'].dropna().unique(),
        help="Selecciona los géneros musicales que deseas incluir en el análisis."
    )

    # Filtrar datos según la selección
    filtered_data = data[data['genre'].isin(selected_genres)] if selected_genres else data

    if filtered_data.empty:
        st.warning("No hay datos disponibles para los géneros seleccionados. Prueba con otros géneros.")
    else:
        # Calcular la distribución de idiomas
        language_counts = filtered_data['language'].dropna().value_counts().reset_index()
        language_counts.columns = ['language', 'count']

        # Subtítulo para personalización de colores
        st.markdown("### 2. Personaliza los colores del gráfico")
        st.write("Selecciona un color para cada idioma del gráfico circular:")

        # Crear una interfaz de selección de colores en columnas
        color_cols = st.columns(len(language_counts))
        colors = {}
        for idx, lang in enumerate(language_counts['language']):
            with color_cols[idx % len(color_cols)]:
                colors[lang] = st.color_picker(f"Color para '{lang}'", "#FFFFFF")

        # Crear gráfico con los colores personalizados
        fig = px.pie(
            language_counts,
            names='language',
            values='count',
            title='Distribución de Idiomas',
            color_discrete_map=colors,  # Asignar colores personalizados
            hole=0.4  # Añadir un agujero para hacerlo tipo "donut"
        )

        # Estilizar el gráfico y mostrarlo
        st.markdown("### 3. Visualización del gráfico")
        st.plotly_chart(fig, use_container_width=True)

    # Pie de página decorativo
    st.markdown("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: gray;'>Gráfico interactivo creado con Streamlit y Plotly. ¡Disfruta explorando tus datos!</p>",
        unsafe_allow_html=True
    )
