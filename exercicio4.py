import numpy as np
import statsmodels as md
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd


'''Qual é a relação entre a condição da casa condition e o preço price,
considerando apenas casas com uma área total sqft_living superior a
3000 pés quadrados?'''

df_house = pd.read_csv('kc_house_data.csv')
df_filtrado = df_house[df_house['sqft_living'] >= 3000]
corr_price_sqft = df_filtrado[['price', 'sqft_living']].corr().iloc[0, 1]
print(f"Correlação entre 'price' e 'sqft_living' (área total de 3000 pés): {corr_price_sqft:.2f} ou seja temos uma relação moderada para forte")