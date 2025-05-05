import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd

'''Crie um modelo de Regressão Linear Simples, exiba a Tabela de
Regressão e exiba o plot da Reta Estimada.'''

df_carros= pd.read_csv("car_price.csv")
df = df_carros[['Price', 'Kilometer']].dropna()
X = sm.add_constant(df['Kilometer'])
y = df['Price']
modelo = sm.OLS(y, X).fit()
print(modelo.summary())
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Kilometer'], y=df['Price'], alpha=0.6, label="Dados")
plt.plot(df['Kilometer'], modelo.predict(X), color='red', label="Reta Estimada")
plt.xlabel('Kilometer')
plt.ylabel('Price')
plt.title('Regressão Linear Simples: Price vs Kilometer')
plt.legend()
plt.tight_layout()
plt.show()

print ("A kilometragem utilizada como parametro não é uma variável para prever preço")