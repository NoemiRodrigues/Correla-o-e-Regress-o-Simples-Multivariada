import numpy as np
import statsmodels as md
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd

'''1. Codique e exiba a matriz de correlação entre as variáveis numéricas.
Além disso, qual é a correlação entre o preço price e o número de
quartos bedrooms? Existe alguma diferença na correlação quando
consideramos apenas casas com uma área total sqft_living superior a
2000 pés quadrados?'''

df_house = pd.read_csv('kc_house_data.csv')


corr = df_house.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()


corr_geral = df_house[['price', 'bedrooms']].corr().iloc[0, 1]
print(f"Correlação entre 'price' e 'bedrooms' (geral): {corr_geral:.2f}")

df_filtrado = df_house[df_house['sqft_living'] > 2000]
corr_filtrado = df_filtrado[['price', 'bedrooms']].corr().iloc[0, 1]
print(f"Correlação entre 'price' e 'bedrooms' (sqft_living > 2000): {corr_filtrado:.2f}")