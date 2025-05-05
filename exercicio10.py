import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd

'''Codique e exiba o gráco dos resíduos do modelo de Regressão
Simples.'''

df_carros =pd.read_csv("car_price.csv")
df = df_carros[['Price', 'Kilometer']].dropna()

X = sm.add_constant(df['Kilometer'])  
y = df['Price']

modelo = sm.OLS(y, X).fit()
y_pred = modelo.predict(X)
residuos = y - y_pred

plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_pred, y=residuos, alpha=0.6, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Valores Previstos')
plt.ylabel('Resíduos')
plt.title('Gráfico dos Resíduos da Regressão Linear Simples')
plt.tight_layout()
plt.show()