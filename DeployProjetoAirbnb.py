#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import streamlit as st
import joblib




#modelo = joblib.load('modelo.joblib')

#separação entre valores numéricos, verdadeiros ou falso e listas

x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'year': 0, 'mounth': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancelation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }
dicionario = {}
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0

for item in x_numericos:
    # como latitude e longitude tem 5 casa decimais precisam de formatação especial
    if item == 'latitude' or item == 'longitude' :
        valor = st.number_input(f'{item}', step = 0.00001, value = 0.0, format = '%.5f') 
        #step é de quanto em quanto o valor é acrescentado, value é o valor que começa (precisa ser um float então 0.0)
        #e format é quantas casas decimais vai ter o campo.
    elif item == 'extra_people':# tem duas casas decimais
        valor = st.number_input(f'{item}', step = 0.01, value = 0.0)#, format = '%.2f' já que o padrão é duas casas decimais exlcui o format 
        #step é de quanto em quanto o valor é acrescentado, value é o valor que começa (precisa ser um float então 0.0)
        #e format é quantas casas decimais vai ter o campo.
    else:
        valor = st.number_input(f'{item}', step = 1, value = 0)
    
    x_numericos[item] = valor
    
for item in x_tf:
    valor = st.selectbox(f'{item}',('yes', 'no'))
    if valor == 'yes':
        x_tf[item] = 1
    else:
        x_tf[item] = 0
        
        
for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[f'{item}'])
    dicionario[f'{item}_{valor}'] = 0

botao = st.button('Price prediction')

if botao:
    dicionario.update(x_numericos)
    dicionario.update(x_tf)
    valores_x = pd.DataFrame(dicionario, index=[0])
    modelo = joblib.load('modelo.joblib')#agora para carregar o modelo de IA
    preco = modelo.predict(valores_x)
    st.write(preco[0])#da forma st.write(preco) printa uma tabela com o preço. st.write(preco)[0] pega o elemento zero que é o valor.


# In[ ]:




