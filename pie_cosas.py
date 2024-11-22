import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

pf = pd.read_csv('spotify_songs_dataset.csv')

contador_lenguaje = pf["language"].value_counts()
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(contador_lenguaje, labels=contador_lenguaje.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
ax.set_title('Distribución de Canciones por Idioma')
st.pyplot(fig)
