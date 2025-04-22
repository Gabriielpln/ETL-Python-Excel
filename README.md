# 🧪 Projeto ETL com Validação de Dados e Dashboard Interativo

Este projeto implementa um processo ETL com foco em análise de dados de campanhas de marketing. São utilizados **Python**, **Pandas**, **Pydantic**, **Streamlit** e **YData Profiling** para construir uma solução completa que valida, analisa e visualiza dados a partir de arquivos CSV.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Pandas** – manipulação de dados
- **Pydantic** – validação de dados com modelos
- **YData Profiling** – geração de relatório exploratório dos dados
- **Streamlit** – criação de dashboards e interfaces web
- **Plotly Express** – gráficos interativos

---

## 🧱 Estrutura do Projeto

| Arquivo                 | Descrição                                                                 |
|------------------------|---------------------------------------------------------------------------|
| `main.py`              | Geração de relatório exploratório (`output.html`) com YData Profiling     |
| `app_dashboard.py`     | Dashboard interativo para análise de KPIs com Streamlit                   |
| `validador.py`         | Definição do modelo `planilha_vendas` com Pydantic para validação de dados|
| `aplicacao_completa.py`| Validação de CSVs via Streamlit com feedback e opção de download          |

---

## ⚙️ Configuração do Ambiente

1. Crie um ambiente virtual (ex: no VSCode, `Ctrl + Shift + P` > “Python: Create Environment”)
2. Certifique-se de estar usando o terminal `cmd`
3. Instale as dependências:

```bash
pip install pandas streamlit ydata-profiling pydantic plotly

