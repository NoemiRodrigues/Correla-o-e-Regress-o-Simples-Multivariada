import numpy as np
import statsmodels as md
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd

'''Codique e exiba a Matriz de correlação para as variáveis numéricas e
dê exemplos de correlações positivas, negativas e neutras.'''

df_carros = pd.read_csv('car_price.csv')
corr = df_carros.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()
