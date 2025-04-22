
# 🧪 Projeto ETL com Validação de Dados e Dashboard Interativo

Este projeto implementa um processo ETL com foco em análise de dados de campanhas de marketing. São utilizados `Python`, `Pandas`, `Pydantic`, `Streamlit` e `YData Profiling` para construir uma solução completa que **valida**, **analisa** e **visualiza** dados a partir de arquivos CSV.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Pandas** – manipulação de dados
- **Pydantic** – validação de dados com modelos
- **YData Profiling (ex-Pandas Profiling)** – geração de relatório exploratório dos dados
- **Streamlit** – criação de dashboards e interfaces web
- **Plotly Express** – gráficos interativos

---

## 🧱 Estrutura do Projeto

| Arquivo                 | Descrição                                                                 |
|-------------------------|---------------------------------------------------------------------------|
| `main.py`               | Geração de relatório exploratório (`output.html`) com YData Profiling     |
| `app_dashboard.py`      | Dashboard interativo para análise de KPIs de anúncios com Streamlit       |
| `validador.py`          | Definição do modelo `planilha_vendas` com Pydantic para validação de dados |
| `aplicacao_completa.py` | Validação completa de arquivos CSV via Streamlit com feedback e download  |

---

## ⚙️ Configuração do Ambiente

```bash
# 1. Crie o ambiente virtual (VSCode)
Ctrl + Shift + P > "Python: Create Environment"

# 2. Verifique se o terminal está como CMD no VSCode

# 3. Instale as dependências
pip install pandas streamlit ydata-profiling pydantic plotly
```

Crie um arquivo `.gitignore` com o seguinte conteúdo:

```
__pycache__/
.env/
*.html
*.csv
```

---

## 🧪 Como Usar

### 1. Análise Exploratória (`main.py`)

```bash
python main.py
```

Gera o arquivo `output.html` com uma análise exploratória do arquivo `data.csv`.

---

### 2. Dashboard com KPIs (`app_dashboard.py`)

```bash
streamlit run app_dashboard.py
```

- Permite o upload de um arquivo CSV  
- Exibe KPIs e gráficos interativos: Gasto, CTR, CPA, CPM, entre outros

---

### 3. Validação de Dados com Pydantic (`aplicacao_completa.py`)

```bash
streamlit run aplicacao_completa.py
```

- Permite o upload de um arquivo CSV  
- Realiza validação linha a linha com feedback detalhado  
- Exporta apenas os dados válidos para `dados_validados.csv`

---

## ✅ Validador de Dados – Exemplo de Modelo

```python
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
```

---

## 📌 Colunas Esperadas no CSV

```python
{
    "Organizador", "Ano_Mes", "Dia_da_Semana", "Tipo_Dia", "Objetivo",
    "Date", "AdSet_name", "Amount_spent", "Link_clicks", "Impressions",
    "Conversions", "Segmentação", "Tipo_de_Anúncio", "Fase"
}
```

---

## 🐞 Problemas Corrigidos

- Erro de diferenciação entre maiúsculas/minúsculas nos nomes de classes no `validador.py`  
- Após padronização dos nomes, o Streamlit passou a reconhecer corretamente as validações

---

## 📌 Observações

- O **YData Profiling** não está incluído na interface principal de ETL, mas é uma ótima ferramenta complementar para análise de dados  
- A função `validador_dados()` faz a validação manual das colunas para permitir controle mais granular, mesmo com o uso de Pydantic

---

## ℹ️ Observação Importante

Este projeto foi desenvolvido como parte de um curso/laboratório prático. O objetivo é reforçar o aprendizado de ferramentas de análise, validação e visualização de dados em Python.

---

🔹 Projeto desenvolvido durante uma live prática com foco educacional
