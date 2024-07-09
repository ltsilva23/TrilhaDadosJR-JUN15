## Antes de rodar o código, é necessário instalar as bibliotecas abaixo
## O arquivo plotting.py tem que estar no mesmo diretório desse arquivo.

## pip install streamlit
## pip install pandas matplotlib seaborn scikit-lear
## pip install plotting
## Para executar o código, rode o arquivo Executa_Analise.bat certifique-se de ajustar o caminho conforme a instalação específica do Python na sua máquina.

import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotting

# Defina o diretório de trabalho para o diretório do script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Lendo o arquivo csv
df = pd.read_csv('vendas_cursos.csv')

# Convertendo a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

###### CALCULOS DAS ESTÁTICAS DESCRITIVAS ######
### Calcular a receita total gerada pela venda dos cursos. ###

# Calcular as métricas necessárias das estatísticas descritivas
receita_total = df['Preço Unitário'].sum()
media_preco = df['Preço Unitário'].mean()
mediana_preco = df['Preço Unitário'].median()
minimo_preco = df['Preço Unitário'].min()
maximo_preco = df['Preço Unitário'].max()
desvio_padrao_preco = df['Preço Unitário'].std()

# Criar um DataFrame com os resultados das estatísticas descritivas
resultados = pd.DataFrame({
    'Métrica': ['Receita Total', 'Média de Preço', 'Mediana de Preço', 'Preço Mínimo', 'Preço Máximo', 'Desvio Padrão de Preço'],
    'Valor': [f'R$ {receita_total:.2f}', f'R$ {media_preco:.2f}', f'R$ {mediana_preco:.2f}', f'R$ {minimo_preco:.2f}', f'R$ {maximo_preco:.2f}', f'R$ {desvio_padrao_preco:.2f}']
})

###### CALCULOS DAS INFORMAÇÕES DOS CURSOS ######
### Identificar o curso com o maior número de vendas. ###

# Calcular as métricas necessárias dos cursos
num_cursos_vendidos = df['Quantidade de Vendas'].sum()
curso_mais_vendido = df.groupby('Nome do Curso')['Quantidade de Vendas'].sum().idxmax()

# Criar um DataFrame com os resultados dos cursos vendidos
resultados_vendidos = pd.DataFrame({
    'Métrica dos cursos': ['Quantidade de cursos vendidos', 'Nome do curso mais vendido'],
    'Informação': [f'{num_cursos_vendidos}', f'{curso_mais_vendido}']
})

####### GRÁFICOS ######
### Pegando as funções grafico_gastos_por_curso e grafico_gastos_ao_longo_do_tempo criado no arquivo plotting.py ###

# Criar o gráfico de barras 
# Gráfico de barras dos gastos por categoria
valor_gasto_por_curso = df.groupby('Nome do Curso')['Preço Unitário'].sum().reset_index() # Agrupar os dados por curso e somar os valores de compra
fig_barra_curso = plotting.grafico_gastos_por_curso(valor_gasto_por_curso)

# Criar gráfico de dispersão baseado em linha 
# Gráfico de linha do valor total gasto ao longo do tempo
gastos_ao_longo_do_tempo = df.groupby('Data')['Quantidade de Vendas'].sum().reset_index()
fig_linha = plotting.grafico_gastos_ao_longo_do_tempo(gastos_ao_longo_do_tempo)


###### INTERFACE DO STREAMLIT ######

# Exibindo as primeiras linhas e informações básicas do conjunto de dados
st.title('Análise de Dados: Vendas de Cursos Online')
st.header('Informações Gerais')
st.dataframe(df)

# Exibir o DataFrame como uma tabela interativa das estatísticas descritivas
st.title('Estatísticas Descritivas')
st.markdown('<h3 style="font-size:20px;">Resumo Geral: Receita Total, Média, Mediana, Mínimo, Máximo e Desvio Padrão dos Preços dos Cursos Vendidos</h3>', unsafe_allow_html=True)
st.dataframe(resultados)

# Exibir o DataFrame como uma tabela interativa dos cursos vendidos
st.title("Informações sobre as vendas de cursos")
st.markdown('<h3 style="font-size:20px;">Resumo Geral: Quantidade de cursos vendidos e Curso mais vendido</h3>', unsafe_allow_html=True)
st.dataframe(resultados_vendidos)

st.header('Gráficos')
st.subheader('Gastos por Curso')
st.plotly_chart(fig_barra_curso)

st.subheader('Valor Total Gasto ao Longo do Tempo')
st.plotly_chart(fig_linha)
