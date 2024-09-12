import streamlit as st
import pandas as pd


dados = pd.read_csv ("clientes.csv")

st.title ("Consulta")

st.dataframe (dados)

nome = dados ["nome"].value_counts()

mostrar = st.toggle ("Mostrar")

if mostrar:
    st.bar_chart (nome)
