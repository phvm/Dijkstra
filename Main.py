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
st.subheader("Buscar menor caminho")
src = st.selectbox("Inicio do caminho", options, index=0)
dest = st.selectbox("Fim do caminho", options, index=0)
if st.button("Buscar"):
    caminho = grafo.dijkstra(int(src), int(dest))
    st.write(caminho)
st.subheader("Informar falha em um conexão")
vert1 = st.selectbox("Primeiro ponto", options, index=0)
vert2 = st.selectbox("Segundo ponto", options, index=0)
if st.button("Informar falha"):
    msg = grafo.remover_ares(int(vert1), int(vert2))
    st.write(msg)
st.subheader("Informar defeito em um transformador, gerador ou subestação")
vert = st.selectbox("Ponto de falha", options, index=0)
if st.button("Informar defeito"):
    msg = grafo.remover_vert(int(vert))
    st.write(msg)
