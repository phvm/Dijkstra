import streamlit as st
from Grafo import *
from insert import insert

path = "Dataset"
data = insert(4941, path)
grafo = Grafo(data)

st.title("Reconectando")
#st.write("")

options = list(range(1, 4942))
st.subheader("Buscar menor caminho")
src = st.selectbox("Inicio do caminho", options, index=0)
dest = st.selectbox("Fim do caminho", options, index=0)
if st.button("Buscar"):
    caminho = grafo.dijkstra(int(src), int(dest))
    st.write(caminho)
st.subheader("Informar falha em um conexão")
dot1 = st.selectbox("Primeiro ponto", options, index=0)
dot2 = st.selectbox("Segundo ponto", options, index=0)
if st.button("Informar falha."):
    msg = grafo.remover_ares(int(dot1), int(dot2))
    st.write(msg)
