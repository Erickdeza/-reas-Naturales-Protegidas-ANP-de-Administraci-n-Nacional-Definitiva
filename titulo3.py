import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargar los datos desde el archivo CSV
filename = 'PARTE3.csv'
df = pd.read_csv(filename)

# Configurar la aplicación con Streamlit
st.title('Áreas Naturales Protegidas por Regiones')

# Obtener las opciones únicas de la columna ANP_UBPO (regiones)
regiones = df['ANP_UBPO'].unique()

# Mostrar el selector de regiones debajo del título
st.header('Selecciona una región:')
selected_region = st.selectbox('', regiones)

# Filtrar el DataFrame por la región seleccionada
filtered_data = df[df['ANP_UBPO'] == selected_region]

# Calcular la cantidad de áreas protegidas por categoría
category_counts = filtered_data['ANP_CATE'].value_counts()

# Convertir a entero si no lo está y asegurarse de quitar los decimales
category_counts = category_counts.astype(int)

# Crear una gráfica de barras con la cantidad de áreas protegidas por categoría
st.subheader(f'Gráfica: Cantidad de áreas protegidas por categoría en {selected_region}')
fig = go.Figure(data=[go.Bar(x=category_counts.index, y=category_counts.values)])

# Configurar el diseño de la gráfica
fig.update_layout(
    xaxis_title='Categoría',
    yaxis_title='Cantidad de áreas protegidas',
    title=f'Cantidad de áreas protegidas por categoría en {selected_region}',
    showlegend=False  # Ocultar la leyenda si no se necesita
)

# Mostrar la gráfica de barras en Streamlit
st.plotly_chart(fig, use_container_width=True)

# Mostrar el nombre de las áreas protegidas en un cuadro
st.subheader(f'Áreas protegidas en {selected_region}:')
areas_protegidas = filtered_data['ANP_NOMB'].unique()
for area in areas_protegidas:
    st.markdown(f"- {area}")  # Mostrar cada área protegida como un elemento de lista

# Mostrar el video
st.subheader('Video de ejemplo')
video_file = open('Video1.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# Cerrar el archivo de video
video_file.close()




