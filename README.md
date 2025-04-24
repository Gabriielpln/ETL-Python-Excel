
# 🧪 ETL-Python-Excel
### Validador de Dados com Análise Exploratória e Insights Rápidos
Este projeto implementa um processo ETL com foco em análise de dados a partir de planilhas Excel (CSV). São utilizados `Python`, `Pandas`, `Pydantic`, `Streamlit` e `YData Profiling` para construir uma solução completa que **valida**, **analisa** e **visualiza** dados de forma prática e interativa.

## 🔄 Processo ETL

**🔹 Extract (Extração)**  
Os dados são extraídos de arquivos CSV, como `data.csv` e `data_teste_erros.csv`, que são carregados para análise e validação. Essa é a etapa de obtenção das informações de uma fonte externa.

**🔹 Transform (Transformação)**  
A transformação acontece principalmente no arquivo `validador.py`, onde os dados passam por validação com o modelo `planilha_vendas` da biblioteca `Pydantic`. Essa etapa garante que os dados estejam no formato correto e atendam a critérios definidos, como:    
- campos obrigatórios preenchidos  
- tipos de dados coerentes
- colunas não esperadas ou ausentes

**🔹 Load (Carregamento)**  
Após a validação:
- Os dados válidos são exportados para um novo arquivo CSV (`dados_validados.csv`)  
- Um relatório exploratório em HTML (`output.html`) pode ser gerado pelo `main.py` usando `ProfileReport`  
- Dashboards interativos são criados com `Streamlit` via `app_dashboard.py` para facilitar a visualização das métricas
  
---

## 📝 Resumo

Basta rodar o `aplicacao_completa.py` para utilizar o validador de dados. O usuário pode fazer o upload de um dataset e a aplicação retornará, de forma clara, se há erros ou não no arquivo, além de exportar apenas os dados válidos.

O script `main.py` utiliza o `ydata_profiling` para gerar automaticamente um arquivo `.html` com uma análise exploratória detalhada do dataset configurado no código.

Já o `app_dashboard.py` é uma aplicação `Streamlit` que permite carregar dados e exibe uma análise rápida com gráficos e indicadores importantes sobre o dataset fornecido.

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

### 1. Validação de Dados com Pydantic (`aplicacao_completa.py`)
```bash
streamlit run src/aplicacao_completa.py
```

- Permite o upload de um arquivo CSV  
- Realiza validação linha a linha com feedback detalhado  
- Exporta apenas os dados válidos para `dados_validados.csv`

---

### 2. Análise Exploratória (`main.py`)

```bash
python main.py
```

Gera o arquivo `output.html` com uma análise exploratória do arquivo `data.csv`.

---

### 3. Dashboard com KPIs (`app_dashboard.py`)

```bash
streamlit run app_dashboard.py
```

- Permite o upload de um arquivo CSV  
- Exibe KPIs e gráficos interativos: Gasto, CTR, CPA, CPM, entre outros

---

## ✅ Validador de Dados – Exemplo de Modelo
O script `validador.py` define um modelo de validação utilizando `Pydantic`, onde é possível configurar como cada dado deverá ser aceito. Por exemplo: campos que devem conter apenas inteiros, valores float, strings com opções específicas, campos opcionais, entre outros. Esse modelo é usado para garantir a consistência dos dados antes de qualquer análise ou visualização.
```python
class planilha_vendas(BaseModel):
    Organizador: int = Field(..., description="Identificador do Organizador")
    Ano_Mes: str = Field(..., description="Ano e mês no formato")
    Dia_da_Semana: Literal["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"] = Field(..., description="Classificação do dia da semana.")
    Tipo_Dia: Literal["Dia útil", "Feriado", "Final de Semana"] = Field(..., description="Classificação do dia: útil, feriado, etc.")
    Objetivo: str = Field(..., description="Objetivo da campaha ou ação")
    Date: date = Field(..., description="Data da entrada no formato YYYY-MM-DD")
    AdSet_name: Optional[str] = Field(description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(0.0, ge=0, le=1200.00, description="Valor gasto no anúncio (mínimo 0, máximo 589.96")
    Link_clicks: Optional[float] = Field(None, description="Número de cliques no link", nullable=True)
    Impressions: Optional[int] = Field(0, description="Número de impressões do anúncio", nullable=True)
    Conversions: Optional[float] = Field(None, description="Número de conversões", nullable=True)
    Segmentação: str = Field(None, description="Segmentação usada")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de anúncio")
    Fase: str = Field(..., description="Fase do funil de vendas")

    class Config:
        validate_default: True
```

---

## 📌 Colunas Esperadas no CSV
Colunas do CSV esperadas pelo validador
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
