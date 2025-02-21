import streamlit as st
import pandas as pd
from io import BytesIO

# Título do aplicativo
st.title("Otimização de Corte - Upload de Arquivo CSV")

# Explicação para o usuário
st.write("Faça upload de um arquivo CSV contendo as informações das peças.")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    try:
        # Lendo o arquivo CSV com pandas
        df = pd.read_csv(BytesIO(uploaded_file.read()), encoding='utf-8')

        # Exibindo o conteúdo do arquivo
        st.write("Conteúdo do arquivo:")
        st.dataframe(df)

        # Verificando se as colunas esperadas estão no arquivo
        if 'width' in df.columns and 'height' in df.columns:
            st.success("Arquivo válido! Colunas 'width' e 'height' encontradas.")

            # Exemplo de processamento simples (você pode ajustar conforme necessário)
            total_area = (df['width'] * df['height']).sum()
            st.write(f"Área total necessária para as peças: {total_area}")

            # Simulação de otimização (substitua com seu algoritmo)
            st.subheader("Simulação de Otimização de Corte:")
            st.write("Este é apenas um exemplo. Substitua pelo seu algoritmo.")
            df['area'] = df['width'] * df['height']
            st.dataframe(df)
        else:
            st.error("O arquivo deve conter as colunas 'width' e 'height'.")
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
else:
    st.info("Aguardando o upload do arquivo.")
