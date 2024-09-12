import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados (nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open ("clientes.csv" , "a", encoding= "utf-8") as file:
            file.write (f"{nome}, {dt_nasc}, {tipo} \n")
        st.session_state ["sucesso"] = True
    else:
        st.session_state ["sucesso"] = False

st.set_page_config(
    page_title= "Cadastro de Cliente"
)

st.title ("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente", key="nome")
dt_nasc = st.date_input("Selecione a data de nascimento", format= "DD/MM/YYYY" , key= "data_nasc")
tipo = st.selectbox ("Tipo de pessoa", ["PF", "PJ"], key = "tipo")
btn_cadastrar = st.button ("Cadastrar" , on_click= gravar_dados, args= [nome, dt_nasc, tipo])

if btn_cadastrar:
    if st.session_state ["sucesso"]:
        st.success("Cadastro Realizado com Sucesso")
    else:
        st.error ("Erro de cadastro")