import pandas as pd
import streamlit as st
import joblib 


##################################################################################
# defining funstions for dataset transformations
def aux_no_change(df):
    return df

 #feature: horas_trabalho_por_semana

    
def aux_horas_trab1(df):
    media_horas_semana = df['horas_trabalho_por_semana'].mean()
    df.loc[df['horas_trabalho_por_semana']==0] = media_horas_semana
    return df

def aux_horas_trabalho_zero(x): # In this case, x is a line value, not a DataFrame
    if x == 0:
        return 1
    else:
        return 0
    
def aux_add_horas_trab_zero(df):
    df['horas_trabalho_zero'] = df.horas_trabalho_por_semana.apply(aux_horas_trabalho_zero)
    return df
    
# feature: tamanho_da_empresa
def aux_empresa1(df): 
    for linha in df['tamanho_da_empresa']:
        if linha == 10: 
            linha = 5
        elif linha >=8:
            linha = 4
        elif linha >=6:
            linha = 3
        elif linha >=4:
            linha = 2
        else:
            linha = 1
    return df

# feature: faixa_etaria
def aux_faixa_etaria(df):
    df.loc[df['faixa_etaria']==1]=2
    return df

#############################################################################
           



dic_sexo = {'Masculino': 1, 'Feminino': 2}

dic_portador_def = {'Não': 0, 'Sim': 1}


dic_cor = {'Indígena': 1, 'Branca': 2, 'Preta': 4, 'Amarela': 6, 'Parda': 8, 'Não identificado': 9, 'Ignorado': 99}

dic_escolaridade = {'Analfabeto': 1, 'Até 5ª incompleto': 2, '5ª fundamental': 3, '5ª a 9ª fundamental': 4, 'Fundamental Completo': 5, 'Médio incompleto': 6, 'Médio Completo': 7, 'Superior incompleto': 8, 'Superior completo': 9, 'Mestrado': 10, 'Doutorado': 11}

dic_empresa = {'Até 4 funcionários': 2, 'De 5 a 9': 3, 'De 10 a 19': 4,'De 20 a 49': 5,'De 50 a 99': 6, 'De 100 a 249': 7, 'De 250 a 499': 8,'De 500 a 999': 9,'1000 ou mais': 10}

dic_faixa_etaria = {'De 10 a 14 anos': 1, 'De 15 a 17 anos': 2, 'De 18 a 24 anos': 3, 'De 25 a 29 anos': 4, 'De 30 a 39 anos': 5, 'De 40 a 49 anos': 6, '50 a 64 anos': 7, '65 anos ou mais': 8}


st.title('Modelo para previsão da remuneração')

st.markdown('---')

sexo = st.selectbox('Sexo', list(dic_sexo.keys()))
sexo = dic_sexo[sexo]

portador_deficiencia = st.selectbox('Portador de deficiência?', list(dic_portador_def.keys()))
portador_deficiencia = dic_portador_def[portador_deficiencia]

cor = st.selectbox('Cor/Raça', list(dic_cor.keys()))
cor = dic_cor[cor]

escolaridade = st.selectbox('Escolaridade', list(dic_escolaridade.keys()))
escolaridade = dic_escolaridade[escolaridade]

tamanho_empresa = st.selectbox('Quantos funcionários trabalham na empresa?', list(dic_empresa.keys()))
tamanho_empresa=dic_empresa[tamanho_empresa]

f_etaria = st.selectbox('Faixa Etária', list(dic_faixa_etaria.keys()))
f_etaria = dic_faixa_etaria[f_etaria]

tempo_emprego = st.number_input('Há quantos meses trabalha na empresa?', step = 0.1, value = 0.0, format = "%.1f", min_value = 0.0)

horas_trabalho = st.number_input('Qual sua carga horária semanal?', step = 1, value = 0, min_value = 0, max_value = 44)


dados_inputados = {'sexo': [sexo], 'faixa_etaria': [f_etaria], 'cor_raca': [cor], 'escolaridade': [escolaridade], 'horas_trabalho_por_semana': [horas_trabalho], 'portador_de_deficiencia': [portador_deficiencia], 'tamanho_da_empresa': [tamanho_empresa], 'tempo_no_emprego': [tempo_emprego]}

dados = pd.DataFrame(dados_inputados)

st.markdown('---')

botao_prever = st.button('Prever a remuneração')

if botao_prever:
	modelo = joblib.load('modelo_wage_7flai.joblib')
	predicao = float(modelo.predict(dados).round(2))
	saida = 'O valor predito para remuneração é de R${:.2f}'.format(predicao)
	st.subheader(saida)



