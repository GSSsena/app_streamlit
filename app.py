import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Cidades do Brasil")

st.title(" algumas Cidades do Brasil")
st.write("Ola vou ,mostra algumas Cidaes do brasil para voce")

nome = st.text_input("coloque seu nome:")

if st.button("Enviar"):
    if nome:
        st.success(f"Olá, {nome} Seja bem-vindo")
else:
        st.warning("Por favor, Não esqueça de coloca o nome antes de  clicar no botão.")


st.divider()

st.subheader("lista das Cidades do Brasil")

url_cidades = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
resposta = requests.get(url_cidades)

if resposta.status_code == 200:
    cidades = resposta.json()
    nomes_cidades = sorted([c["nome"] for c in cidades])

    cidade_escolhida = st.selectbox("Escolha uma cidade:", nomes_cidades)

    if cidade_escolhida:

        cidade_info = next(c for c in cidades if c["nome"] == cidade_escolhida)
        estado_nome = cidade_info["microrregiao"]["mesorregiao"]["UF"]["nome"]
        regiao_nome = cidade_info["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"]

        st.markdown(f"Cidade selecionada: **{cidade_escolhida}**")
        st.markdown(f"Estado: {estado_nome}")
        st.markdown(f"Região: {regiao_nome}")
    else:
        st.error("Erro ao acessar a API do IBGE") 

    


