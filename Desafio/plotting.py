import plotly.express as px


def grafico_gastos_por_curso(valor_gasto_por_curso):
    fig_barra = px.bar(valor_gasto_por_curso, x='Nome do Curso', y='Preço Unitário', 
                       title='Gastos por Curso',
                       labels={'Nome do Curso': 'Nome do Curso', 'Preço Unitário': 'Valor Gasto R$'},
                       color='Nome do Curso', 
                       color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig_barra

def grafico_gastos_ao_longo_do_tempo(gastos_ao_longo_do_tempo):
    fig_linha = px.line(gastos_ao_longo_do_tempo, x='Data', y='Quantidade de Vendas', title='Distribuição das Vendas ao Longo do Tempo', labels={'data_compra': 'Data', 'Quantidade de Vendas': 'Valor Gasto'})
    return fig_linha

def grafico_curso_mais_vendidos(top_cursos):
    fig_ranking_vendas = px.bar(top_cursos, x='Quantidade de Vendas', y='Nome do Curso', 
                                orientation='h', 
                                title='Ranking dos Cursos Mais Vendidos',
                                labels={'Nome do Curso': 'Nome do Curso', 'Quantidade de Vendas': 'Quantidade de Vendas'},
                                color='Nome do Curso', 
                                color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig_ranking_vendas
    
    