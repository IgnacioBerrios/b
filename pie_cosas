import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Cargar el archivo CSV
file_path = st.file_uploader("Sube tu archivo CSV", type=["csv"])  # Para cargar desde la interfaz de Streamlit
if file_path is not None:
    try:
        # Leer el archivo CSV
        df = pd.read_csv(file_path)
        
        # Asegurarse de que existe la columna "language"
        if "language" in df.columns:
            # Contar la cantidad de canciones por idioma
            contador_lenguaje = df["language"].value_counts()
            
            # Crear el gráfico de pastel
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.pie(
                contador_lenguaje, 
                labels=contador_lenguaje.index, 
                autopct='%1.1f%%', 
                startangle=140, 
                colors=plt.cm.tab20.colors
            )
            ax.set_title('Distribución de Canciones por Idioma')
            
            # Mostrar el gráfico en Streamlit
            st.pyplot(fig)
        else:
            st.error("El archivo no contiene una columna llamada 'language'.")
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
else:
    st.info("Por favor, sube un archivo CSV para continuar.")
