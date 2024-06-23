import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
st.title("Áreas Naturales Protegidas (ANP) de Administración Nacional Definitiva") 
with st.expander("¿Que es?"):
    st.write("Las Áreas Naturales Protegidas (ANP) de Administración Nacional en Perú, gestionadas por el SERNANP, buscan conservar la biodiversidad, los ecosistemas y el patrimonio cultural. Protegen especies en peligro de extinción y sitios arqueológicos importantes. El SERNANP regula actividades humanas y fomenta el turismo sostenible y la investigación científica. La red de ANP incluye diversos ecosistemas, desde la Amazonía hasta los Andes y la costa, asegurando la preservación del patrimonio natural y cultural del país.")
st.sidebar.title("Páginas")
pages = ["Conociendo mi Perú", "Áreas Protegidas por Regiones"]
selecion_pag = st.sidebar.radio("Selecciona una opción", pages)

# ESTO ES LA PRIEMRA OSE MI ARCHIVO TITULO1
if selecion_pag == "Conociendo mi Perú":
    goku1 = pd.read_excel("PARTE2.xlsx")
    categorias = goku1['ANP_CATE'].value_counts()
    categorias_percentage = categorias / categorias.sum() * 100
    fig, ax = plt.subplots()
    barras = ax.barh(categorias_percentage.index, categorias_percentage.values, color='skyblue')
    for bar in barras:
        ancho = bar.get_width()
        ax.annotate(f'{ancho:.2f}%', 
                    xy=(ancho, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0), 
                    textcoords='offset points',
                    ha='left', va='center')
    ax.set_xlabel('Porcentaje')
    ax.set_ylabel('Categoría de ANP')
    ax.set_title('Porcentaje de Áreas Naturales Protegidas por Categoría')
    st.title("Tipos de Áreas Naturales Protegidas en Perú")
    with st.expander("1. Parque Nacional"):
        st.write("Área protegida para conservar biodiversidad y paisajes, con recreación controlada y educación ambiental.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video1.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("2. Reserva Nacional"):
        st.write("Área para conservación, investigación y uso sostenible de recursos naturales bajo normativas específicas.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video2.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("3. Santuario Nacional"):
        st.write("Área protegida para conservar especies o hábitats únicos, restringiendo la actividad humana para su preservación a largo plazo.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video3.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("4. Santuario Histórico"):
        st.write("Espacio designado para proteger y conservar sitios importantes relacionados con eventos, personas o culturas significativas de la historia.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video4.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("5. Refugio de Vida Silvestre"):
        st.write("Espacio para conservar hábitats y especies amenazadas, fomenta investigación y educación ambiental.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video5.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("6. Bosque de Protección"):
        st.write("Área forestal para conservar ecosistemas y biodiversidad.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video6.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("7. Reserva Paisajista"):
        st.write("Reserva que permite el uso y aprovechamiento sostenible de recursos por poblaciones locales mediante planes de manejo. Actualmente hay dos en Perú.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video7.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("8. Reserva Comunales"):
        st.write("Son áreas naturales protegidas de uso directo. Actualmente existen en el Perú 10 Reservas Comunales.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video8.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("9. Coto de Caza"):
        st.write("Espacios destinados al aprovechamiento de la fauna silvestre. Son áreas naturales protegidas de uso directo. Actualmente existen en el Perú 2 Cotos de Caza.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video9.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    st.pyplot(fig)
    st.subheader('Número de Áreas Protegidas por Categoría:')
    st.write(categorias)
    st.image("IMAGEN1.jpeg", use_column_width=True)

# ESTO ES LA SEGUNDA OSE MI ARCHIVO TITULO3
elif selecion_pag == "Áreas Protegidas por Regiones":
    st.header("Áreas Protegidas por Regiones")
    goku2 = 'PARTE3.csv' 
    archivo = pd.read_csv(goku2)
    regiones = archivo['ANP_UBPO'].unique()
    st.header('Selecciona una región:')
    seleccion_region = st.selectbox('', regiones)
    archivo_filtrar = archivo[archivo['ANP_UBPO'] == seleccion_region]
    categoria2 = archivo_filtrar['ANP_CATE'].value_counts().astype(int)
    fig = go.Figure(data=[go.Bar(x=categoria2.index, y=categoria2.values)])
    fig.update_layout(
        xaxis_title='Categoría',
        yaxis_title='Cantidad de áreas protegidas',
        title=f'Cantidad de áreas protegidas por categoría en {seleccion_region}',
        showlegend=False, 
        autosize=False,
        margin=dict(l=0, r=0, t=30, b=0),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)
    st.subheader(f'Áreas protegidas en {seleccion_region}:')
    areas_protegidas = archivo_filtrar['ANP_NOMB'].unique()
    for area in areas_protegidas:
        st.markdown(f"- {area}")  

