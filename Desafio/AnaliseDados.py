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

###### CÁLCULOS DAS ESTATÍSTICAS DESCRITIVAS ######

# Calcular as métricas necessárias das estatísticas descritivas
receita_total = (df['Quantidade de Vendas'] * df['Preço Unitário']).sum()
quantidade_total_vendida = df['Quantidade de Vendas'].sum()

# Calcular o Total de Vendas por Curso com formatação
df['Total de Vendas'] = df['Quantidade de Vendas'] * df['Preço Unitário']
df['Total de Vendas Formatado'] = df['Total de Vendas'].apply(lambda x: '{:,.2f}'.format(x).replace(',', ';').replace('.', ',').replace(';', '.'))


# Formatando a receita_total 
receita_formatada = '{:,.2f}'.format(receita_total).replace(',', ';').replace('.', ',').replace(';', '.')

# Encontrar os cursos mais vendidos
top_cursos = df.nlargest(5, 'Quantidade de Vendas')[['Nome do Curso', 'Quantidade de Vendas']]

# Criar um DataFrame com os resultados das estatísticas descritivas
resultados = pd.DataFrame({
    'Métrica': [ 'Média de Preço', 'Mediana de Preço', 'Preço Mínimo', 'Preço Máximo', 'Desvio Padrão de Preço'],
    'Valor': [f'R$ {df["Preço Unitário"].mean():,.2f}', 
              f'R$ {df["Preço Unitário"].median():,.2f}', 
              f'R$ {df["Preço Unitário"].min():,.2f}', 
              f'R$ {df["Preço Unitário"].max():,.2f}', 
              f'R$ {df["Preço Unitário"].std():,.2f}']
})

####### GRÁFICOS ######
# Gráfico de barras dos gastos por curso
valor_gasto_por_curso = df.groupby('Nome do Curso')['Preço Unitário'].sum().reset_index()
fig_barra_curso = plotting.grafico_gastos_por_curso(valor_gasto_por_curso)

# Gráfico de linha do valor total gasto ao longo do tempo
gastos_ao_longo_do_tempo = df.groupby('Data')['Quantidade de Vendas'].sum().reset_index()
fig_linha = plotting.grafico_gastos_ao_longo_do_tempo(gastos_ao_longo_do_tempo)

# Gráfico de barras horizontais dos cursos mais vendidos (usando função definida em plotting)
fig_ranking_vendas = plotting.grafico_curso_mais_vendidos(top_cursos)

###### INTERFACE DO STREAMLIT ######
# Centralizar o texto e mudar a cor usando CSS inline
st.markdown(
    """
    <h1 style='text-align: center; color: #008080;'>Análise de Dados: Vendas de Cursos Online</h1>
    """,
    unsafe_allow_html=True
)

# Seção de Receita Total
st.subheader(f'Receita Total')
st.markdown(f'R$ {receita_formatada}')

st.subheader("Quantidade Total vendida")
st.markdown(f'{quantidade_total_vendida}')

# Seção de Estatísticas Descritivas
with st.expander("Estatísticas Descritivas"):
    st.header('Estatísticas Descritivas')
    st.markdown('<h4 style="font-size:16px;">Resumo Geral</h4>', unsafe_allow_html=True)
    st.write(resultados.to_html(index=False), unsafe_allow_html=True)

# Seção de Gráficos
st.header('Gráficos')

st.subheader('Gastos por Curso')
st.plotly_chart(fig_barra_curso, use_container_width=True)

st.subheader('Valor Total Gasto ao Longo do Tempo')
st.plotly_chart(fig_linha,use_container_width=True)

st.subheader('Ranking dos Cursos Mais Vendidos')
st.plotly_chart(fig_ranking_vendas, use_container_width=True)

# Seção de Informações Gerais
st.header('Informações Gerais')
st.dataframe(df[['Nome do Curso', 'Quantidade de Vendas', 'Preço Unitário', 'Total de Vendas Formatado']], width=1024)

