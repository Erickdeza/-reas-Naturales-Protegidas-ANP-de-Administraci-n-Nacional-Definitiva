import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Áreas Naturales Protegidas (ANP) de Administración Nacional Definitiva")
df = pd.read_excel("PARTE2.xlsx")
categorias = {}
for categori in df['ANP_CATE']:
    if categori not in categorias:
        categorias[categori] = 1
    else:
        categorias[categori] += 1
categorias_series = pd.Series(categorias)
st.bar_chart(categorias_series)
st.subheader("1. Parque Nacional")
st.write("Área protegida para conservar biodiversidad y paisajes, con recreación controlada y educación ambiental.")
st.subheader("2. Reserva Nacional")
st.write("Área para conservación, investigación y uso sostenible de recursos naturales bajo normativas específicas.")
st.subheader("3. Santuario Nacional")
st.write("Área protegida para conservar especies o hábitats únicos, restringiendo la actividad humana para su preservación a largo plazo.")
st.subheader("4. Santuario Histórico")
st.write("Espacio designado para proteger y conservar sitios importantes relacionados con eventos, personas o culturas significativas de la historia.")
st.subheader("5. Refugio de Vida Silvestre")
st.write("Espacio para conservar hábitats y especies amenazadas, fomenta investigación y educación ambiental.")
st.subheader("6. Bosque de Protección")
st.write("Área forestal para conservar ecosistemas y biodiversidad.")
st.subheader("7. Reserva Paisajista")
st.write("Reserva que permite el uso y aprovechamiento sostenible de recursos por poblaciones locales mediante planes de manejo. Actualmente hay dos en Perú.")
st.subheader("8. Reserva Comunales")
st.write("Son áreas naturales protegidas de uso directo. Actualmente existen en el Perú 10 Reservas Comunales.")
st.subheader("9. Coto de Caza")
st.write("Espacios destinados al aprovechamiento de la fauna silvestre. Son áreas naturales protegidas de uso directo. Actualmente existen en el Perú 2 Cotos de Caza.")
st.title(" Cntidades Áreas Naturales Protegidas")
categorias_percentage = categorias_series / categorias_series.sum() * 100
fig, ax = plt.subplots()
ax.pie(categorias_percentage, labels=categorias_percentage.index, autopct='%1.1f%%')
st.pyplot(fig) 

