# Análise de Dados: Vendas de Cursos Online

Este projeto realiza uma análise exploratória dos dados de vendas de cursos online, utilizando Python com as bibliotecas Pandas, Matplotlib, Streamlit e Plotly para visualização interativa.

## Funcionamento do Projeto

### 1. Pré-requisitos

Certifique-se de ter os seguintes pacotes instalados:

- pandas
- matplotlib
- streamlit
- plotting

Você pode instalar todos os pacotes necessários utilizando o arquivo `requirements.txt` fornecido.

pip install -r requirements.txt 

### 2. Executando o Projeto

Para executar o projeto localmente:

1. Clone o repositório:

git clone https://github.com/seu-usuario/TrilhaDadosJR-JUN15.git

cd nome-do-repositorio

2. Execute o script principal usando Streamlit no local onde esta o arquivo AnaliseDados.py:

streamlit run AnaliseDados.py

- **Execução via arquivo .bat**: Se estiver usando Windows, você pode executar o arquivo `Executa_Analise.bat` para iniciar o Streamlit, certifique-se de ajustar o caminho conforme a instalação específica do Python na sua máquina. Por exemplo:

"%USERPROFILE%\AppData\Local\Programs\Python\Python312\Scripts\streamlit.exe" run AnaliseDados.py

### 3. Funcionalidades

O projeto realiza as seguintes tarefas:

- **Leitura e pré-processamento dos dados**: Carrega um arquivo CSV contendo dados de vendas de cursos e converte a coluna de datas para o formato adequado.

- **Cálculos de estatísticas descritivas**: Calcula a receita total gerada pelas vendas, média, mediana, mínimo, máximo e desvio padrão dos preços dos cursos.

- **Identificação do curso mais vendido**: Determina qual curso teve o maior número de vendas.

- **Visualização de dados**: Utiliza gráficos interativos (gerados com Plotly) para mostrar os gastos por curso e o valor total gasto ao longo do tempo.

### 4. Estrutura do Repositório

├── README.md # Arquivo de documentação

├── AnaliseDados.py # Script principal usando Streamlit

├── vendas_cursos.csv # Arquivo CSV com dados de vendas de cursos

├── plotting.py # Arquivo com funções para criação de gráficos

├── Executa_Analise.bat # Arquivo .bat para executar o Streamlit (Windows)

├── requirements.txt # Arquivo de dependências

### 5. Como Contribuir

Fique à vontade para contribuir com novas funcionalidades, melhorias de código ou correções de bugs. Sinta-se livre para abrir uma issue ou enviar um pull request.

### 6. Autor

[Larissa Thalia](https://github.com/ltsilva23)

### 7. Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Resultados e Conclusões

- **Receita Total**: R$ 2097.50.
- **Curso Mais Vendido**: Introdução a Programação em Python.
- **Estatísticas Descritivas dos Preços**:
  - Média: R$ 83.90.
  - Mediana: R$ 79.90.
  - Mínimo: R$ 39.90.
  - Máximo: R$ 119.90.
  - Desvio Padrão: R$ 21.98.

Este projeto proporciona uma análise detalhada das vendas de cursos online, oferecendo insights valiosos através de visualizações interativas. Para mais detalhes, consulte a documentação completa e o código-fonte disponível neste repositório.

## Deploy 

[Meu Desploy de Analise de Dados](https://ltsilva23-trilhadadosjr-jun15-teste-useranalisedados-hswj4y.streamlit.app/)