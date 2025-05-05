import numpy as np
import statsmodels as md
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd

'''8. Codique e exiba Grácos de Dispersão para cada uma das variáveis
numéricas em relação à variável de interesse Price.'''

df_carros =pd.read_csv("car_price.csv")
df_numericas = df_carros.select_dtypes(include=['int64', 'float64'])
variaveis_explicativas = df_numericas.drop(columns='Price', errors='ignore').columns

for coluna in variaveis_explicativas:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df_carros, x=coluna, y='Price', alpha=0.6)
    plt.title(f'Preço vs {coluna}')
    plt.xlabel(coluna)
    plt.ylabel('Preço')
    plt.tight_layout()
    plt.show()