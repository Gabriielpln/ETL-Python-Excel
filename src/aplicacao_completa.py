import pandas as pd
import streamlit as st
from validador import planilha_vendas
from pydantic import ValidationError


# Lista de Colunas Esperadas
colunas_esperadas = {
    "Organizador", "Ano_Mes", "Dia_da_Semana", "Tipo_Dia", "Objetivo",
    "Date", "AdSet_name", "Amount_spent", "Link_clicks", "Impressions",
    "Conversions", "Segmentação", "Tipo_de_Anúncio", "Fase"
}


def validador_dados(df):
    erros = []
    dados_validados = []

    # Verifica se todas as colunas esperadas estão presentes no DataFrame
    colunas_faltando = colunas_esperadas - set(df.columns)
    if colunas_faltando:
        return [], [f"Erro: A sequintes colunas estão faltando: {', '.join(colunas_faltando)}"]

    for index, row in df.iterrows():
        try:
            # Converte a linha do DataFrame em um dicionário
            dados = row.to_dict()

            #Valida os dados usando o modelo User
            usuario_valido = planilha_vendas(**dados)
            dados_validados.append(usuario_valido)

        except ValidationError as e:
            erros.append(f"Erro na linha {index + 2}: {str(e)}")

    return dados_validados, erros

def main():
    st.title("Validador de Dados")
    st.write("Upload de um arquivo CSV para validar os dados.")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    if uploaded_file is not None:
        try:
            # Lê o arquivo CSV
            df = pd.read_csv(uploaded_file)

            st.write("Preview de dados: ")
            st.dataframe(df.head())
            
            if st.button("Validar Dados"):
                with st.spinner("Validando dados..."):
                    dados_validados, erros = validador_dados(df)

                if erros:
                    st.error("Erros encontrados na validação: ")
                    for erro in erros:
                        st.write(erro)
                else:
                    st.success("Todos os dados são válidos!")

                    # Mostra a quatidade de registros validados
                    st.write(f"Total de registros validados: {len(dados_validados)}")

                    # Opção para download dos dados validados 
                    df_validados = pd.DataFrame([dados.dict() for dados in dados_validados])
                    st.download_button(
                        label="Download dos dados validados",
                        data=df_validados.to_csv(index=False),
                        file_name='dados_validados.csv',
                        mime='text/csv'
                    )

        except Exception as e:
            st.error(f"Erro ao ler o arquivo CSV: {str(e)}")
if __name__ == "__main__":
    main()