# 🧪 Projeto ETL com Validação de Dados e Dashboard Interativo

Este projeto implementa um processo ETL completo para análise de dados de campanhas de marketing, combinando validação robusta, análise exploratória e visualização interativa.

## 🚀 Tecnologias Utilizadas
| Categoria         | Ferramentas                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **Linguagem**     | Python 3                                                                    |
| **ETL**           | Pandas                                                                      |
| **Validação**     | Pydantic                                                                    |
| **Análise**       | YData Profiling                                                             |
| **Visualização**  | Streamlit, Plotly Express                                                   |

---

## 🧱 Estrutura do Projeto
| Arquivo                 | Descrição                                                                 |
|-------------------------|---------------------------------------------------------------------------|
| `main.py`               | Gera relatório exploratório (`output.html`) com YData Profiling           |
| `app_dashboard.py`      | Dashboard interativo com KPIs de campanhas (Streamlit)                    |
| `validador.py`          | Modelo Pydantic para validação de `planilha_vendas`                       |
| `aplicacao_completa.py` | Interface completa: upload, validação e exportação de dados               |

---

## ⚙️ Configuração do Ambiente
```bash
# 1. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 2. Instalar dependências
pip install pandas streamlit ydata-profiling pydantic plotly
Arquivo .gitignore:

gitignore
__pycache__/
.env/
*.html
*.csv
venv/

## 🧪 Como Usar
1. Análise Exploratória
bash
python main.py
▶️ Gera output.html com análise do data.csv

2. Dashboard Interativo
bash
streamlit run app_dashboard.py
📊 Features:

Upload de CSV

Visualização de KPIs (CTR, CPA, CPM)

Gráficos interativos

3. Validação Completa
bash
streamlit run aplicacao_completa.py

✅ Valida dados e exporta para dados_validados.csv

## 📌 Modelo de Validação
python
class planilha_vendas(BaseModel):
    Organizador: int
    Ano_Mes: str
    Dia_da_Semana: str
    Tipo_Dia: str
    Objetivo: str
    Date: str
    AdSet_name: Optional[str]
    Amount_spent: float
    Link_clicks: Optional[float]
    Impressions: Optional[float]
    Conversions: Optional[float]
    Segmentação: str
    Tipo_de_Anúncio: str
    Fase: str

## 🐞 Problemas Resolvidos
Case sensitivity nos modelos Pydantic

Integração entre validação manual/automática

Tratamento de dados opcionais

ℹ️ Observações
🔹 YData Profiling como ferramenta complementar
🔹 Dupla camada de validação (Pydantic + manual)
🔹 Projeto desenvolvido para fins educacionais