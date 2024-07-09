import plotly.express as px


def grafico_gastos_por_curso(valor_gasto_por_curso):
    fig_barra = px.bar(valor_gasto_por_curso, x='Nome do Curso', y='Preço Unitário', 
                       title='Gastos por Curso',
                       labels={'Nome do Curso': 'Nome do Curso', 'Preço Unitário': 'Valor Gasto'},
                       color='Nome do Curso', 
                       color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig_barra

def grafico_gastos_ao_longo_do_tempo(gastos_ao_longo_do_tempo):
    fig_linha = px.line(gastos_ao_longo_do_tempo, x='Data', y='Quantidade de Vendas', title='Distribuição das Vendas ao Longo do Tempo', labels={'data_compra': 'Data', 'Quantidade de Vendas': 'Valor Gasto'})
    return fig_linha
