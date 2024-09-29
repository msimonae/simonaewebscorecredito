import streamlit as st
import requests


# Função para fazer a requisição ao servidor Flask
def prever_score(dados):
    url = 'https://simonaiscorecredito.onrender.com/predict'
    response = requests.post(url, data=dados)
    return response.json()


# Título
st.title('Prever Score de Crédito')
st.header('By Marcelo Simonae - msimonae@gmail.com')

# Entradas de texto e seleção para os campos categóricos
UF = st.selectbox('UF', ['SP', 'MG', 'SC', 'PR', 'RJ'])
ESCOLARIDADE = st.selectbox('Escolaridade', ['Superior Cursando', 'Superior Completo', 'Segundo Grau Completo'])
ESTADO_CIVIL = st.selectbox('Estado Civil', ['Solteiro', 'Casado', 'Divorciado'])

# Sliders para campos numéricos
QT_FILHOS = st.slider('Quantidade de Filhos', 0, 10, 0)

# Entradas de texto Sim/Não
CASA_PROPRIA = st.radio('Possui Casa Própria?', ['Sim', 'Não'])

# Sliders para campos numéricos
QT_IMOVEIS = st.slider('Quantidade de Imóveis', 0, 5, 1)
VL_IMOVEIS = st.slider('Valor dos Imóveis (R$)', 0, 1000000, 300000, step=5000)

# Entradas de texto Sim/Não
OUTRA_RENDA = st.radio('Possui Outra Renda?', ['Sim', 'Não'])

OUTRA_RENDA_VALOR = 0
if OUTRA_RENDA == 'Sim':
    OUTRA_RENDA_VALOR = st.slider('Valor da Outra Renda (R$)', 0, 10000, 3000, step=500)

# Sliders para campos numéricos
TEMPO_ULTIMO_EMPREGO_MESES = st.slider('Tempo Último Emprego (meses)', 0, 360, 18)

# Campo de Sim/Não para "Trabalhando Atualmente" (caso você queira modificar)
TRABALHANDO_ATUALMENTE = st.radio('Está Trabalhando Atualmente?', ['Sim', 'Não'])

ULTIMO_SALARIO = st.slider('Último Salário (R$)', 0, 50000, 20400, step=1000)
QT_CARROS = st.slider('Quantidade de Carros', 0, 10, 1)
VALOR_TABELA_CARROS = st.slider('Valor Tabela dos Carros (R$)', 0, 200000, 60000, step=5000)

# Seleção da faixa etária
FAIXA_ETARIA = st.selectbox('Faixa Etária', ['18-25', '26-35', '36-45', '46-60', 'Acima de 60'])

# Botão para prever
if st.button('Prever'):
    # Montar dados para enviar
    dados = {
        'UF': UF,
        'ESCOLARIDADE': ESCOLARIDADE,
        'ESTADO_CIVIL': ESTADO_CIVIL,
        'QT_FILHOS': QT_FILHOS,
        'CASA_PROPRIA': CASA_PROPRIA,
        'QT_IMOVEIS': QT_IMOVEIS,
        'VL_IMOVEIS': VL_IMOVEIS,
        'OUTRA_RENDA': OUTRA_RENDA,
        'OUTRA_RENDA_VALOR': OUTRA_RENDA_VALOR,
        'TEMPO_ULTIMO_EMPREGO_MESES': TEMPO_ULTIMO_EMPREGO_MESES,
        'TRABALHANDO_ATUALMENTE': TRABALHANDO_ATUALMENTE,
        'ULTIMO_SALARIO': ULTIMO_SALARIO,
        'QT_CARROS': QT_CARROS,
        'VALOR_TABELA_CARROS': VALOR_TABELA_CARROS,
        'FAIXA_ETARIA': FAIXA_ETARIA
    }

    # Chamar a função para prever
    resultado = prever_score(dados)

    # Mostrar o resultado
    st.write('Score Previsto:', resultado['score_previsto'])
    st.write('Status:', resultado['status'])
