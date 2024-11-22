import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Cargar los datos
file_path = "spotify_songs_dataset.csv"  # Reemplazar con la ruta del archivo
data = pd.read_csv(file_path, delimiter=';')

# Título de la aplicación
st.title("Distribución de Idiomas por Género")

# Filtro de géneros
selected_genres = st.multiselect("Selecciona los géneros que deseas analizar:", options=data['genre'].unique())

# Filtrar los datos
filtered_data = data[data['genre'].isin(selected_genres)] if selected_genres else data

# Contar los idiomas
language_counts = filtered_data['language'].value_counts()

# Crear el gráfico de pie
fig, ax = plt.subplots()
ax.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
ax.axis('equal')  # Asegura que el gráfico sea circular

# Mostrar el gráfico
st.pyplot(fig)
