# script aula02 do Curso Python do Zero ao DS do Meigarom (Seja um Datascientist).
#
# importar/declarar a library Pandas e carregar o DataFrame para memória
#
import pandas as pd

#data = pd.read_csv('datasets/kc_house_data.csv')

# função que converte de object (string) -> date
#data['date'] = pd.to_datetime(data['date'])

# mostrar na tela os tipos de variáveis de cada coluna
#print(data.dtypes)

# ===================================
# Como converter os tipos de variáveis
# ===================================
#
# Inteiro -> Float
#data['bedrooms'] = data['bedrooms'].astype(float)

# Inteiro -> Float
#data['bedrooms'] = data['bedrooms'].astype(float)

# Float -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(Int64)

# Inteiro -> String
#data['bedrooms'] = data['bedrooms'].astype(str)

#print(data.dtypes)

# Inteiro -> Float
#data['bedrooms'] = data['bedrooms'].astype(float)

# String -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(Int64)

# String -> Data
#data['date'] = pd.to_datetime(data['date'])

# ===================================
# Criando novas variáveis
# ===================================

#data = pd.read_csv('datasets/kc_house_data.csv')

#data['nome_do_meigarom'] = "meigarom" 

#data['comunidade_ds'] = 80
#data['data_abertura_comunidade_ds'] = pd.to_datetime('2020-02-28')

#print(data.columns)

#print(data[['id','date','nome_do_meigarom','comunidade_ds','data_abertura_comunidade_ds']].head())

##print(data.dtypes)

# ===================================
# Deletando variáveis
# ===================================

#print(data.columns)
#data = data.drop('nome_do_meigarom')
#cols = ['nome_do_meigarom','comunidade_ds','data_abertura_comunidade_ds']
#data = data.drop(cols, axis=1)
#print(data.columns)

# ===================================
# Selecionar dados, forma 01: Direto pelo nome das colunas
# ===================================

#data = pd.read_csv('datasets/kc_house_data.csv')
#print(data[['price','id','date']])

# ===================================
# Selecionar dados, forma 02: Pelos índices das linhas e colunas
# ===================================
# DADOS [LINHAS, COLUNAS]

#print(data.iloc[0:10,0:3])

#todas colunas, por exemplo

#print(data.iloc[0:10,:])

# ===================================
# Selecionar dados, forma 03: Pelos índices das linhas e nome das colunas
# ===================================

#cols = ['price','id','date']
#print(data.loc[0:10,cols])

# ===================================
# Selecionar dados, forma 04: Pelos índices booleanos
# ===================================

# 1, 0
# True, False

#cols = [True, False, True, True, False, False,False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

#print(data.loc[0:10,cols])

#print(data.columns)

# ===================================
# Respondendo as perguntas de negócio
# ===================================

data = pd.read_csv('datasets/kc_house_data.csv')

# 1. Qual a data do imóvel mais antigo do portfólio?

#data['date'] = pd.to_datetime(data['date'])
#print(data.sort_values('date', ascending=True))

# 2. Quantos imóveis possuem o numero máximo de andares?

#print(data['floors'].unique()
#print(data[data['floors'] == 3.5].shape)

# 3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com o preço.
# 	Acima de 540.000 -> Alto Padrão
# 	Abaixo de 540.000 -> Baixo Padrão

#data['level'] = 'standard'

#data.loc[data['price'] > 540000, 'level'] = 'high_level'
#data.loc[data['price'] < 540000, 'level'] = 'low_level'

# 4. Gostaria de um relatório ordenado pelo preço e contendo as seguintes informações:
#    ( id do imóvel, data em que ficou disponível para compra, o numero de quartos, o tamanho total do terreno, o preço e a classificação do imóvel ( alto e baixo padrão ) ).


#report = data[['id', 'date', 'price', 'bedrooms', 'sqft_lot', 'level']].sort_values('price', ascending=False)

#print(data.columns)

#print(report.head())

 #Não se pode esquecer de usar o parâmetro ", index=False", pois se não ele vai exportar com os index's originais e na hora de fazer a leitura desse CSV os dados ficarão totalmente embaralhados

#report.to_csv('datasets/report_aula02.csv', index=False)

# 5. Gostaria de um mapa indicando onde as casas estão localizadas geograficamente.
# Plotly - Biblioteca que armazena uma funcao que desenha mapa
#Para instalar, via terminal: pip install plotly
# Scatter MapBox - Funcao que desenha mapa

#import plotly.express as px

#data_mapa = data[['id', 'lat', 'long', 'price']]

#mapa = px.scatter_mapbox (data_mapa, lat= 'lat', lon = 'long', hover_name='id', hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300)

#mapa.update_layout( mapbox_style='open-street-map')
#mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
#mapa.show()

#mapa.write_html('datasets/mapa_house_rocket.html')
#testar arquivo gerado em HTML com mais calma, pois o atual não está abrindo nos navegadores Android.

# linha apenas para testar DF
#print(data.head())

# ===================================
# Exercícios Práticos abaixo
# ===================================

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#	1. Crie uma nova coluna chamada: "house_age".
#		- Se o valor da coluna date for maior que 2014-01-01 => "new_house"
#		- Se o valor da coluna date for menor que 2014-01-01 => "old_house"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#print(data.dtypes)

#print(data['date'].head())

import numpy as np

data['date'] = pd.to_datetime(data['date'])

#data['date'] = pd.to_datetime(data['date'])
#print(data.sort_values('date', ascending=True))

#print(data['date'].head())

#conditions = [
#    (df['Set'] == 'Z') & (df['Type'] == 'A'),
#    (df['Set'] == 'Z') & (df['Type'] == 'B'),
#    (df['Type'] == 'B')]
#choices = ['yellow', 'blue', 'purple']
#df['color'] = np.select(conditions, choices, default='black')
#print(df)
###
CondsQ1 = [ (data['date'] > '2014-01-01'), (data['date'] < '2014-01-01') ]

SelsQ1 = ['new_house', 'old_house']

data['house_age'] = np.select(CondsQ1,SelsQ1)

#print(data.head())
###
#print(data[data['house_age'] == 'new_house'].shape)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 1 finalizado
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#2. Crie uma nova coluna chamada: "dormitory_type"
#		- Se o valor da coluna "bedrooms" for igual a 1 => "studio"
#		- Se o valor da coluna "bedrooms" for igual a 2 => "apartament"
#		- Se o valor da coluna "bedrooms" for maior que 2 => "house"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

CondsQ2 = [(data['bedrooms'] == 1), (data['bedrooms'] == 2), (data['bedrooms'] > 2)]

SelsQ2 = ['studio', 'apartment', 'house']

data['dormitory_type'] = np.select (CondsQ2, SelsQ2)

#print(data.head())

#print(data[data['dormitory_type'] == 'house'].shape)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 2 finalizado
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# 3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com o preço.
	#Acima de 540.000 -> Alto Padrão
#	Abaixo de 540.000 -> Baixo Padrão
#	
#	- Criar uma nova coluna no conjunto de dados chamada "standard"
#		- Para cada linha, eu vou comparar com a coluna "price"
#			- Se "price" for maior que 540.000, eu vou escrever "high_standard" na coluna "standard"
#			- Se "price" for menor que 540.000, eu vou escrever "low_standard" na coluna "standard"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#<<<<<<< HEAD < colocado pelado git quando removi o commit "Fazendo Q4."
#print(data.dtypes)
#print(data['price'].head())
###
CondsQ3 = [(data['price'] > 540000), (data['price'] < 540000)]

SelsQ3 = ['high_standard', 'low_standard']

data['standard'] = np.select(CondsQ3, SelsQ3)

#print(data.head())
###
#print(data[['id','price','standard']].head())

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 3 repetido finalizado, logo abaixo o exercício 3 correto.
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#3. Crie uma nova coluna chamada: "condition_type"
#		- Se o valor da coluna "condition" for menor ou igual a 2 => "bad"
#		- Se o valor da coluna "condition" for igual a 3 ou 4 => "regular"
#		- Se o valor da coluna "condition" for igual a 5 => "good"

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

###
data['condition_type'] = 'condition'

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[((data['condition'] == 3) | (data['condition'] == 4)), 'condition_type'] = 'regular'
data.loc[data['condition'] == 5, 'condition_type'] = 'good'
###

#ColsQ3 = ['id','condition','condition_type']

#print(data.loc[0:20,ColsQ3])

#cols = ['price','id','date']
#print(data.loc[0:10,cols])

#data['level'] = 'standard'

#data.loc[data['price'] > 540000, 'level'] = 'high_level'

#
#print(data.columns)

#id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
#       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
#       'lat', 'long', 'sqft_living15', 'sqft_lot15', 'standard'

#=======
#>>>>>>> parent of 76f1d75 (Finalizando Q4.)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 3 finalizado acima
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 4 abaixo
# 4. Modifique o tipo da coluna "condition" para STRING
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#print(data.dtypes)
# atualmente a coluna 'condition' e Int64. Farei a conversão abaixo para ficar apenas temporariamente em memória

data['condition'] = data['condition'].astype(str)

#print(data.dtypes)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 4 finalizado acima
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 5 abaixo
#5. Delete as colunas "sqft_living15" e "sqft_lot15"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

ColsQ5 = ['sqft_living15', 'sqft_lot15']

data = data.drop(ColsQ5, axis=1)

#print(data.columns)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 5 finalizado acima
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 6 abaixo
#  6. Modifique o tipo da coluna "yr_built" para date
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#print(data.dtypes)

#q6 solution below
#print('Original data:\n')
#print(data['yr_built'].loc[0:10,])

#data['yr_built'] = (data['yr_built'].astype(str))
#print(data['yr_built'].loc[0:10,])

#print('\nNew date format as str:\n')
data['yr_built'] = ('01/01/' + data['yr_built'].map(str))
#print(data['yr_built'].loc[0:10,])

#print('\nAbove format converted to datetime:')
data['yr_built'] = pd.to_datetime(data['yr_built'], infer_datetime_format=True)
#print(data['yr_built'].loc[0:10,])
#q6 solution above



#print(data.dtypes)

#print('\nDatetime > str > Datetime:')
#data['yr_built'] = (data['yr_built'].astype(str))
#data['yr_built'] = pd.to_datetime(data['yr_built'], infer_datetime_format=True)
#print(data['yr_built'].loc[0:10,])

# falta testar converter agora para datetime novamente

#DataView = data[['id', 'yr_built']]
#print(DataView.loc[0:10,])

#print(data.dtypes)

# apesar da função abaixo deixar o valor apenas do ano conforme eu queria, tem 2 erros. 1o que o tipo da coluna volta a ser Int64, 2o que os valores ficaram errados, todos ficaram 1970.
#data['yr_built'] = data['yr_built'].dt.year

# , format='%Y'
# , infer_datetime_format=True

# em futuras aplicações, seguir guidelines desse link a seguir 'https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime', pois só de você especificar o formato no qual você quer que fique os dados após a conversão, você aumenta o desempenho dessa conversão em 5x (usando o parâmetro 'infer_datetime_format=True' já se tem esse ganho de acordo com a documentação oficial do pandas.

#print(data.dtypes)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 6 finalizado acima
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 7 abaixo
# 7. Modifique o tipo da coluna "yr_renovated" para date
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#print(data.dtypes)
#print('\n')
#ColsQ7 = ['id','yr_renovated']

#print('\n')

#import datetime as dt

#data['yr_renovated'] = (data['yr_renovated'].astype(str))

#print(data['yr_renovated'].dtypes)
#print(data.loc[0:30,ColsQ7])

#print(data.dtypes)

#pd.to_datetime(data['yr_renovated'], format='%Y%m%d', errors='ignore')

#print(data['yr_renovated'])

#print(data.dtypes)


#print((data['yr_renovated'].unique) != 0)

#Q7Sel = pd.to_datetime('2010-01-01')
#data['yr_']

#print(data['yr_renovated'].unique)
#print('Before the data manipulation:\n')
#print(np.unique(data['yr_renovated']))


#q7 solution below
#print('Current, as str:')
data['yr_renovated'] = data['yr_renovated'].astype(str)

#print(data['yr_renovated'].head())

data['yr_renovated'] = (data['yr_renovated'].replace('0',np.nan))

data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])

#print('\nAfter the data manipulation:\n')
#print(np.unique(data['yr_renovated']))

#print(data['yr_renovated'].head())

#print(data.dtypes)
#q7 solution up

#print('\n')
#print('Current after conversion plus new datetime value added:')
#data['yr_renovated'] = (data.loc[1,'yr_renovated'] + '0101')
#print(data.loc[1,'yr_renovated'])
#print('\n')
#print('Current converted as datetime format:')
#print(pd.to_datetime(data.loc[1,'yr_renovated']))



#for index in data.index:
#	if data.loc[index,'yr_renovated']

#for index in df.index:   if df.loc[index,'Name']=='Mr. Elon R. Musk':   df.loc[index,'Title'] = 'The Boss Man'  
#elif df.loc[index,'Name']=='Mr. Zachary J. Kirkhorn':   df.loc[index,'Title'] = 'The Money Man'  
#else:   df.loc[index,'Title'] = 'Another Dude'


#data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])


#, format='%Y%m%d', errors='coerce'
#print('\n')
#print(pd.DatetimeIndex(data['yr_renovated']).year)

#data['yr_renovated'] = pd.to_datetime(data['yr_renovated'].astype(str), format='%Y%m%d')

#print(data.dtypes)
#print('\n')
#print(data.loc[0:30,ColsQ7])

#day is out of range for month

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 7 finalizado acima
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 8 abaixo
# 8. Qual a data de construção mais antiga de um imóvel?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#q8 solution down
#DataQ7 = data[['id', 'yr_built']]
#print((DataQ7.sort_values('yr_built', ascending=True)))
#q8 solution up

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 9 abaixo
# 9. Qual a data de renovação mais antiga de um imóvel?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#q9 solution down
#DataQ8 = data[['id', 'yr_renovated']]
#print((DataQ8.sort_values('yr_renovated', ascending=True)))
#q9 solution up

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 10 abaixo
# 10. Quantos imóveis tem 2 andares?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#q10 solution down
#DataQ10 = data[['id', 'floors']]
#SelQ10 = (DataQ10['floors'] == 2.0)

#print((data[SelQ10]).shape)
#q10 solution up

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 11 abaixo
# 11. Quantos imóveis estão com a condição igual a "regular"?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


#print((data.loc[:,'condition_type'] == 'regular'))
#print(data['condition_type'].count('regular'))

#collections2 as colls2
#from collections2 import Counter

#q11 solution down
#Q11Sel = (data.loc[:,'condition_type'] == 'regular')
#Q11Selected = data[Q11Sel]

#print(Q11Selected.shape)
#q11 solution up

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 12 abaixo
# 12. Quantos imóveis estão com a condição igual a "bad" e possuem "vista para a agua"?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#Q12Sel = ((data.loc[:,'condition_type'] == 'bad')) & (data.loc[:,'waterfront'] =='1')

#print(Q12Sel)

#Q12wct = ((data['waterfront'] == 1) & (data['condition_type'] == 'bad'))
#Q12wOk = data[Q12wct]

#print(Q12wOk.shape)
#q12 solution up

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 13 abaixo
# 13. Quantos imóveis estão com a condição igual a "good" e são "new house"?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#melhorar solucao dessa questao, usando a logica da linha abaixo:
	#print(data[data['floors'] == 3.5].shape)
	
Q13sel = ((data['condition_type'] == 'good') & (data['house_age'] == 'new_house'))
#Q13sel2 = (data['condition_type'] == 'good')

Q13 = data[Q13sel]

#print(Q13['condition_type'].shape)
#q13 solution up

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 14 abaixo
# 14. Qual imóvel mais caro do tipo "studio"?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#print(data[data['floors'] == 3.5].shape)

Q14sel = (data['dormitory_type'] == 'studio')
Q14 = data[Q14sel]

#print(Q14[['id','dormitory_type','price']].sort_values('price',ascending=False))

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 15 abaixo
# Quantos imóveis do tipo "apartment" foram reformados em 2015?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#print(data.dtypes)

#(data['dormitory_type'] == 'apartment')
# yr_renovated

#print(data['yr_renovated'])

#q15 solution down
#Q15_id1 = (data[data['dormitory_type'] == 'apartment'])
#Q15_id2 = (data[data['yr_renovated'] == '2015-01-01'])
#Q15_id3 = (Q15_id1[Q15_id1['yr_renovated'] == '2015-01-01T00:00:00.000000000'])
#print(Q15_id3)
#q15 solution up

#extra
#print(data[data['floors'] == 3.5].shape)

# teste de validacao down
#q15test = data[['id','dormitory_type','yr_renovated']]
#print('Q15 validando reformados em 2015:\n')
#print(q15test[q15test['yr_renovated'] == '2015-01-01T00:00:00.000000000'])
# teste de validacao up

#cols = ['price','id','date']
#print(data.loc[0:10,cols])

#Q15cols = ['id',id1,id2]
#print(data.loc[0:10,Q15cols])
#print(Q15_id1['dormitory_type'],'\n')

#print(Q15_id2['yr_renovated'],'\n')


#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 16 abaixo
# Qual maior número de quartos que um imóvel do tipo "house" possui?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

Q16 = data[data['dormitory_type'] == 'house']

#print(Q16[['dormitory_type','bedrooms']].sort_values('bedrooms',ascending=False))

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 17 abaixo
# Quantos imóveis "new house" foram reformados em 2014?
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

Q17age = data[data['house_age'] == 'new_house']

#print('\nQ17 yr_renovated uniques:\n')
#print(np.unique(Q17age['yr_renovated']))

Q17 = Q17age[Q17age['yr_renovated'] == '2014-01-01T00:00:00.000000000']

#print(Q17[['id','house_age','yr_renovated']])

#print(Q17.shape)

#print(data[['id','house_age','yr_renovated']])

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#
# Exercício 18
# 18. Selecione as colunas: "id", "date", "price", "floors", "zipcode" pelos métodos:
#		18.1. Direto pelo nome das colunas
#		18.2. Pelos índices
#		18.3. Pelos índices das linhas e os nomes das colunas
#		18.4. Pelos índices booleanos
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#Colunas:
#'id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
#       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
#       'lat', 'long', 'house_age', 'dormitory_type', 'standard',
#       'condition_type'

#dataQ18 = data.iloc[0:15,:]

#print('18.1) Resposta:')
#print(dataQ18[['id','date','price','floors','zipcode']])

#print('\n18.2) Resposta:')
#print(dataQ18.iloc[:, [0,1,2,7,16]])

#cols183 = ['id','date','price','floors','zipcode']
#print('\n18.3) Resposta:')
#print(dataQ18.loc[0:10,cols183])

#cols184 = [True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False]
#print('\n18.4) Resposta:')
#print(data.loc[0:10,cols184])

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 19
# Salve um arquivo ".csv" somente com as colunas do item 10
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

Q19 = (data[data['floors'] == 2.0])

#validando
#print(Q19[['id','floors']])

#Q19.to_csv('datasets/reportQ19_aula02.csv', index=False)
#print('Report gerado com sucesso.')

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 20
# 20. Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

# Plotly - Biblioteca que armazena uma funcao que desenha mapa
#Para instalar, via terminal: pip install plotly
# Scatter MapBox - Funcao que desenha mapa

import plotly.express as px

#data_mapa = data[['id', 'lat', 'long', 'price']]

Q20DTMap = data[['id','lat','long','price']]

#mapa = px.scatter_mapbox (data_mapa, lat= 'lat', lon = 'long', hover_name='id', hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300)

Q20Map = px.scatter_mapbox (Q20DTMap, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['darkgreen'], zoom=3, height=300)

#mapa.update_layout( mapbox_style='open-street-map')
#mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
#mapa.show()

Q20Map.update_layout(mapbox_style='open-street-map')
Q20Map.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
Q20Map.show()

#mapa.write_html('datasets/mapa_house_rocket.html')
#testar arquivo gerado em HTML com mais calma, pois o atual não está abrindo nos navegadores Android.

# Q20Map.write_html('datasets/mapa_a2_q20.html')
# testei agora, 07/04/22, e o dado mapa abriu no Android 12 corrramente.