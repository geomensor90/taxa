import streamlit as st
import pandas as pd

# Dados fornecidos
dados = {
    "Ano": [2020, 2021, 2022, 2023, 2024, 2025],
    "Coluna 2": [1.71, 1.8, 2, 2.12, 2.2, 2.31],
    "Coluna 3": [0.23, 0.24, 0.27, 0.29, 0.3, 0.31],
    "Coluna 4": [0.15, 0.16, 0.17, 0.18, 0.19, 0.2]
}

df = pd.DataFrame(dados)

def pagina_teo():
    st.title("Taxa de Execução de Obras (TEO)")

    # Entrada do usuário para a área da construção
    campo1 = st.number_input("Insira a área da construção em m²:", min_value=0.0, step=1.0, format="%.2f")

    if campo1 <= 0:
        st.warning("Insira uma área válida para continuar.")
        return
    
    # Seleção dos anos
    st.subheader("Selecione os anos:")
    anos_selecionados = [ano for ano in df["Ano"] if st.checkbox(str(ano))]
    
    if not anos_selecionados:
        st.warning("Por favor, selecione ao menos um ano.")
        return
    
    # Filtrando os dados
    dados_filtrados = df[df["Ano"].isin(anos_selecionados)]
    
    if dados_filtrados.empty:
        st.warning("Nenhum dado encontrado para os anos selecionados.")
        return
    
    # Cálculo dos valores
    resultados = []
    soma_total = 0
    exct = 0
    area_real = 0 
    
    for _, row in dados_filtrados.iterrows():
        if campo1 <= 1000:
            resultado = campo1 * row["Coluna 2"]
            area_real = campo1
            exct = 0
        else:
            resultado = 1000 * row["Coluna 2"] + ((campo1 - 1000) * row["Coluna 3"])
            area_real = 1000
            exct = campo1 - 1000

        soma_total += resultado

        # Exibição dos resultados
        st.subheader(f"**Ano {int(row['Ano'])}**")
        st.write(f"Fica o responsável pela execução da obra, AUTUADO por não efetuar a declaração da Taxa de Execução de Obras - TEO, referente ao exercício {int(row['Ano'])}")
        st.write(f"Memória de Cálculo:")        
        st.write(f"Metro quadrado até áreas de 1000m²= R$ {row['Coluna 2']:.2f}")
        st.write(f"Valor excedente = R$ {row['Coluna 3']:.2f}")
        st.write(f"Área (m²): {campo1:.2f}")
        st.write(f"Valor até 1000m² = {area_real:.2f} X {row['Coluna 2']:.2f} = R$ {(area_real * row['Coluna 2']):.2f}")
        st.write(f"Valor excedente = {exct:.2f} X {row['Coluna 3']:.2f} = R$ {(exct * row['Coluna 3']):.2f}")
        st.write(f"Valor total para {int(row['Ano'])}: R$ {resultado:.2f}")     
        st.write(f"Prazo: 30 dias")  
        st.write(f"--------------------------------------")


if __name__ == "__main__":
    pagina_teo()
