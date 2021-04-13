import streamlit as st
from Grafo import *
from insert import insert

path = "Dataset"
data = insert(4941, path)
grafo = Grafo(data)

st.title("Reconectando")
st.text("Nesse projeto, usamos a base de dados que descreve a malha de conexões elétricas do \noeste dos Estados Unidos"
        ". Aqui você pode selecionar algumas opções, como buscar \na menor distância entre dois pontos,"
        " informar uma falha em uma das conexões entre dois \npontos ou um defeito em um ponto.")
st.text("Nesta aplicação, cada ponto representa um transformador, gerador ou uma subestação.\n"
        "Ao ser informado alguma falha ou defeito, a aplicação é capaz de modificar a base de \ndados e informar"
        " caso haja alguma outra conexão que possa ser feita para que uma \nregião não fique"
        " sem energia elétrica.")

options = list(range(1, 4942))
fct = st.sidebar.selectbox("Selecione uma função:", ("Buscar menor caminho", "Informar falha", "Informar defeito"))
if fct == "Buscar menor caminho":
    st.header("Buscar menor caminho")
    src = st.selectbox("Ponto inicial", options, index=0, key="fp")
    dest = st.selectbox("Ponto final", options, index=0, key="fp")
    if st.button("Buscar"):
        caminho = grafo.dijkstra(int(src), int(dest))
        st.write("O menor caminho é: " + caminho)
elif fct == "Informar falha":
    st.header("Informar falha em um conexão")
    st.subheader("Pontos de falha")
    vert1 = st.selectbox("Primeiro ponto de falha", options, index=0)
    vert2 = st.selectbox("Segundo ponto de falha", options, index=0)

    st.subheader("Pontos que está tentando conectar")
    src = st.selectbox("Ponto inicial", options, index=0, key="sp")
    dest = st.selectbox("Ponto final", options, index=0, key="sp")
    if st.button("Informar falha"):
        msg = grafo.remover_ares(int(vert1), int(vert2))
        caminho = grafo.dijkstra(int(src), int(dest))
        st.write(msg)
        st.write(caminho)
else:
    st.header("Informar defeito em um ponto")
    st.subheader("Ponto onde houve o defeito")
    vert = st.selectbox("Ponto de falha", options, index=0)

    st.subheader("Pontos que está tentando conectar")
    src = st.selectbox("Ponto inicial", options, index=0, key="tp")
    dest = st.selectbox("Ponto final", options, index=0, key="tp")
    if st.button("Informar defeito"):
        msg = grafo.remover_vert(int(vert))
        caminho = grafo.dijkstra(int(src), int(dest))
        st.write(msg)
        st.write(caminho)
