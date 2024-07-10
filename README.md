![Código Certo Coders](https://utfs.io/f/3b2340e8-5523-4aca-a549-0688fd07450e-j4edu.jfif)

# 📚 Trilha Inicial Ciência de Dados Jr
Este projeto realiza uma análise exploratória dos dados de vendas de cursos online, utilizando Python com as bibliotecas Pandas, Matplotlib, Streamlit e Plotly para visualização interativa.

Disponível para visualização em: [Análise de Dados: Vendas de Cursos Online](https://trilhadadosjr-jun15-python-dados-cursos.streamlit.app/)

## Requisitos Funcionais:

- **Leitura e pré-processamento dos dados**: Carrega um arquivo CSV contendo dados de vendas de cursos e converte a coluna de datas para o formato adequado.

- **Cálculos de estatísticas descritivas**: Calcula a receita total gerada pelas vendas, média, mediana, mínimo, máximo e desvio padrão dos preços dos cursos.

- **Identificação do curso mais vendido**: Determina qual curso teve o maior número de vendas.

- **Visualização de dados**: Utiliza gráficos interativos (gerados com Plotly) para mostrar os gastos por curso e o valor total gasto ao longo do tempo.

## Estrutura do Projeto:
projeto/
│
├── Executa_Analise.bat       # Script para executar a análise
├── README.md                 # Este arquivo
├── plotting.py               # Script com funções de plotagem
├── vendas_cursos.csv         # Arquivo CSV com dados de vendas de cursos
└── AnaliseDados.py           # Script principal para análise de dados

   #### Análise de Dados: Vendas de Cursos Online
   ![Demonstração](imagens/Gráfico_cursos.png)

## Desafios Propostos:
   1. Calcular a receita total gerada pela venda dos cursos.
   2. Identificar o curso com o maior número de vendas.
   3. Visualizar a distribuição das vendas ao longo do tempo através de gráficos.

### **Configuração do Ambiente:**
1. **Instalar Python:** Certifique-se de ter o Python instalado em sua máquina.
2. **Instalar Bibliotecas:** Utilize o comando `pip install streamlit` `pip install pandas matplotlib seaborn scikit-learn`
`pip install plotting` para instalar as bibliotecas necessárias. Você pode instalar todos os pacotes necessários utilizando o arquivo `requirements.txt` fornecido.

   pip install -r requirements.txt 

4. **Criar Repositório no GitHub:** Crie um repositório público para o projeto.
5. **Clonar o Repositório:** Clone o repositório para a sua máquina local e configure o ambiente de trabalho. Exemplo:

git clone https://github.com/seu-usuario/TrilhaDadosJR-JUN15.git

cd nome-do-repositorio

### **Execução do Projeto:***
Certifique-se de que o arquivo plotting.py esteja no mesmo diretório do script principal.

- **Execução via streamlit**:
   
   streamlit run AnaliseDados.py

- **Execução via arquivo .bat**: Se estiver usando Windows, você pode executar o arquivo `Executa_Analise.bat` para iniciar o Streamlit, certifique-se de ajustar o caminho conforme a instalação específica do Python na sua máquina. Por exemplo:

"%USERPROFILE%\AppData\Local\Programs\Python\Python312\Scripts\streamlit.exe" run AnaliseDados.py

### Documentação Adicional
Para mais detalhes sobre o funcionamento do código e as análises realizadas, consulte o arquivo [Analise de dados](AnaliseDados.py)  e os scripts adicionais no diretório do projeto.

---

### Autor do projeto
[Larissa Thalia](https://github.com/ltsilva23)

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### Como Contribuir

Fique à vontade para contribuir com novas funcionalidades, melhorias de código ou correções de bugs. Sinta-se livre para abrir uma issue ou enviar um pull request.


---

🔗 **Mantenha-se Conectado:**
- [Discord](https://discord.gg/wzA9FGZHNv)
- [Website](http://www.codigocertocoders.com.br/)
- [LinkedIn](https://www.linkedin.com/company/codigocerto/)
  
🌐 **Contato:**
- Codigo Certo - Email: codigocertocoders@gmail.com
- Larissa - E-mail: ltsilva.ti@gmail.com
---

**Construindo o amanhã, hoje.**
