🧪 Projeto ETL com Validação de Dados e Dashboard Interativo
Este projeto implementa um processo ETL com foco em análise de dados de campanhas de marketing. Utilizando Python, Pandas, Pydantic, Streamlit e YData Profiling, construí uma solução completa que valida, analisa e visualiza dados a partir de arquivos CSV.

🚀 Tecnologias Utilizadas
Python 3

Pandas – Manipulação e análise de dados

Pydantic – Validação de dados com modelos

YData Profiling (ex-Pandas Profiling) – Geração de relatório exploratório automático

Streamlit – Criação de dashboards e interfaces interativas

Plotly Express – Visualizações interativas

🧱 Estrutura do Projeto

Arquivo	                    Descrição
main.py	                    Gera relatório exploratório (output.html) com YData Profiling
app_dashboard.py	        Dashboard com KPIs e gráficos interativos via Streamlit
validador.py	            Modelos com Pydantic para validação de dados (planilha_vendas)
aplicacao_completa.py	    Interface completa para upload, validação e exportação de dados válidos