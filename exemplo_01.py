# #mostre na tela a frase "Hello World"
# print("Hello World")
#
# #mostre na tela o resultado da soma de 30+50
# print(30+50)
# soma_de_numeros = 30 + 50
#
# #mostre o conteudo da variavel soma_de_numeros
# print(soma_de_numeros)

# carregue o conjunto de dados chamado kc_house_data.csv do HD para a memória

# funcao - read_csv()
# bilioteca - pandas

import pandas as pd
import numpy as np

data = pd.read_csv('datasets/kc_house_data.csv')

# mostre as 5 primeiras linhas do conjunto de dados

#print(data.head())

# mostre na tela o numero de colunas e o número de linhas do conjunto de dados

# print(data.shape)
#
# # mostre na tela o nome das colunas do conjunto de dados
# # CTRL+/ hotkey para comentar linhas selecionadas
#
# print(data.columns)
#
# # mostre na tela o conjunto de dados ordenados pela coluna price
#
# # print(data[['id','price']].sort_values('price'))
#
# # mostre na tela o conjunto de dados ordenados pela coluna price do maior pro menor
#
# print(data[['id','price']].sort_values('price',ascending=False))

# 5 - Qual a casa com o maior número de quartos?

#print(data[['id','bedrooms']].sort_values('bedrooms',ascending=False))

# mostrar qual e o tipo de dado de cada coluna
#print(data.dtypes)

# soma total de cada coluna usando a funcao sum do pandas, resposta pergunta 6
#print(data.sum())

# 7. Quantas casas possuem 2 banheiros?
#print(data[['id','bathrooms']].sort_values('bathrooms',ascending=False))
#print(data.bathrooms>=2)
# criar novo DF contendo apenas casas com mais de 2 banheiros. Ira gerar um DF boolean

#baths2true = data.bathrooms==2
#baths2 = data[baths2true]

# como o resultado do filtro anterior é um DF boolean, entao se precisa criar um novo DF
# contendo apenas os resultados True, para so entao se poder manipular o mesmo
#baths2 = data[baths2true]

# agora se conta a QTD de linhas da dada coluna filtrada
#print(baths2['bathrooms'].count())

# 8 - Qual o preço medio de todas as casas do conjunto de dados?
# print(data['price'].mean())
#print(data.dtypes)
#
#================================================#
# 9. Qual o preço médio de casas com 2 banheiros?#
# q9 code below
##
#print(data.dtypes)
#data.bathrooms>=2
#baths2True = (data['bathrooms'] == 2)
#print(baths2true)
#bathsIn2 = data[baths2True]
#
# poderia ter sido usado o codigo abaixo, em parte, para responder a questao 7
# print(bathsIn2['bathrooms'].value_counts() & bathsIn2['price'])
#
#
#bathsOk = bathsIn2['bathrooms'].value_counts()
#
#print(bathsOk[:])
#print(bathsOk[:] , bathsIn2[['id','price']])
#
#print(bathsIn2['price'].mean())
#
# q9 code above ===============================#
# extra code
#d_q9 = data[data.bathrooms==2 & data.price]
#print(d_q9)
#
# ================================ #
# 10. Qual o preço mínimo entre as casas com 3 quartos? #
#
# q10 code below ==================================#
#
#beds3True = (data['bedrooms'] == 3)
#bedsIn3 = data[beds3True]
#print(bedsIn3[['id','bedrooms','price']].sort_values('price',ascending=True))
#
# q10 code above
#
# =================================#
#
# 11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?? #
#
# q11 code below
#
# =================================#
# Filtrar DF para ele conter apenas as casas com mais de 300 metros e contar esse resultado

# validando no visual se tem imóvel com menos de 300. E tem apenas 1.
# q11_lroom = data[['id','sqft_living']]
#print(q11_lroom.sort_values (by='sqft_living',ascending=True))
#print('Antes do filtro:')
#print(data.shape)

# relembrando colunas do DF
#print(data.dtypes)
#print('\n')
#print('Depois do filtro:')
# filtro original q11 abaixo
#q11_lroomFilter = (data['sqft_living'] >= 300)
#q11_lroomOk = data[q11_lroomFilter]
#
# filtro q11 modificado abaixo (para questão 15. Alterei a condição '>=' para '>' conforme é pedido na pergunta q15)
q11_lroomFilter = (data['sqft_living'] > 300)
q11_lroomOk = data[q11_lroomFilter]
#
#print('Depois do filtro:')
#print(q11_lroomOk.shape)
#
# q11 code above
#
# =================================#
#
# 12. Quantas casas tem mais de 2 andares?
#
# q12 code below
#
# =================================#
#
#print(data.dtypes)
# filtrar DF pela coluna floors > 2 e exibir apenas as colunas id e floors para conferir
# lógica da resposta correta:
#q12_DFfloors = data
#print((q12_DFfloors['floors'] > 2).value_counts())
# Considerar apenas os valores True como resposta.
#
#
## convertendo do tipo Float para int da coluna "floors", para conseguir efetuar o filtro em questão
#q12_DFfloors['floors'] = np.int64(q12_DFfloors['floors'])
#print(q12_DFfloors['floors'])
# Incluso o uso do numpy para fazer a devida conversao. Ele está importado no início deste script.
#q12_floorsFilter = (q12_DFfloors['floors'] > 2)
#print(q12_floorsFilter)
#q12_floors = data[q12_floorsFilter]
# nova lógica abaixo
#print(data['floors'].value_counts())
#q12_DFfloors.drop_duplicates(subset=['id'], keep=False)
#===print((q12_DFfloors['floors'] > 2).value_counts())
#q12_DFfloors = (q12_DFfloors['floors'] > 2)
#
#
### método q12 abaixo  incompleto ###
# https://www.geeksforgeeks.org/python-program-to-fetch-the-indices-of-true-values-in-a-boolean-list/
# Method 2
#
#
# Python program to fetch the indices
# of true values in a Boolean list
#    
# using enumerate() + list comprehension 
# to return true indices. 
#res = [i for i, val in enumerate(q12_DFfloors) if val] 
#
# printing result
#
# testando uso da função X library collections2
#from acollections import Counter
#
#print(Counter(res)) 
#print ("Indices having True values are : " +  str(res))
### método q12 acima incompleto ###

#q12 code above
#
# =================================#
#
# 13. Quantas casas tem vista para o mar?
#
# q13 code below
#
#q13_DF = data
#print(q13_DF.dtypes)
#print(q13_DF[['id','waterfront']])
#q13_DFfilter = (q13_DF['waterfront'] > 0)
#q13_DF = q13_DF[q13_DFfilter]
#print(q13_DF.shape)
#
# q13 code above
#
# =================================#
#
# 14. Das casas com vista para o mar, quantas tem 3 quartos?
#
# q14 code below
#
#q14_DF = q13_DF
#q14_DFfilter = (q14_DF['bedrooms'] == 3)
#q14_DF = q14_DF[q14_DFfilter]
##print(q14_DF[['id','waterfront','bedrooms']])
#print(q14_DF.shape)
#
# =================================#
#
# 15.  Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
#
# q15 code below
#
# habilitei a seção do código da q11 novamente para compor essa solução abaixo
#
q15_DF = q11_lroomOk
q15_DFfilter = (q15_DF['bathrooms'] > 2)
q15_DFfiltered = q15_DF[q15_DFfilter]
print(q15_DFfiltered.dtypes)
print(q15_DFfiltered[['id','sqft_living','bathrooms']])
#
# q15 code above
#
# Depois de prosseguir mais um pouco, se precisa organizar esse script! Atualmente (24/02) ele está uma bagunça!!!