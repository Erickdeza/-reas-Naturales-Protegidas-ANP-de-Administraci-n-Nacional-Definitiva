import streamlit as st
import pandas as pd
import numpy as np
import pip
pip.main(["istall", "openpyxl"])
st.title("Áreas Naturales Protegidas (ANP) de Administración Nacional Definitiva")
def = pd.read_excel("PRIMER-ARCHIVO.xlsx")
st.write(df)