import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd

'''11. Crie um modelo de Regressão Multivariada, exiba a Tabela de Regressão
e exiba o gráco dos resíduos do modelo.'''

df_carros=pd.read_csv("car_price.csv")
df = df_carros[['Price', 'Kilometer', 'Year']].dropna()
df = pd.get_dummies(df, drop_first=True)
X = sm.add_constant(df.drop('Price', axis=1)) 
y = df['Price']
modelo = sm.OLS(y, X).fit()
print(modelo.summary())
y_pred = modelo.predict(X)
residuos = y - y_pred

plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_pred, y=residuos, alpha=0.6, color='blue')
plt.axhline(y=0, color='red', linestyle='--')  
plt.xlabel('Valores Previstos')
plt.ylabel('Resíduos')
plt.title('Gráfico dos Resíduos da Regressão Multivariada')
plt.tight_layout()
plt.show()