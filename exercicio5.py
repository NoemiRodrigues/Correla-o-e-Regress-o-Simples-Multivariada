import numpy as np
import statsmodels as md
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd


'''Existe alguma correlação entre a localização geográca lat e long e o
preço price para casas com pelo menos três quartos bedrooms?'''
df_house = pd.read_csv('kc_house_data.csv')
df_filtrado = df_house[df_house['bedrooms'] >= 3]
corr_geo = df_filtrado[['lat', 'long', 'price']].corr()
print(f"Correlação entre latitude e preço:, {corr_geo.loc['lat', 'price']:.2f}")
print(f"Correlação entre longitude e preço:, {corr_geo.loc['long', 'price']:.2f}")
print ("Com os dados puxados, podemos notar que as correlações são muito baixas. Indicando que não há uma influencia da localização no caso mencionado no enunciado.")