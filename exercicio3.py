import numpy as np
import statsmodels as md
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd

''' Como a quantidade de banheiros bathrooms influencia na correlação
entre a área total da casa sqft_living e o preço price?'''
df_house = pd.read_csv('kc_house_data.csv')

("Banheiros únicos:", sorted(df_house['bathrooms'].unique()))
correlacoes = {}


for b in sorted(df_house['bathrooms'].unique()):
    grupo = df_house[df_house['bathrooms'] == b]
    if len(grupo) >= 10: 
        corr = grupo[['sqft_living', 'price']].corr().iloc[0, 1]
        correlacoes[b] = corr

for b, c in correlacoes.items():
    print(f"Banheiros: {b} -> Correlação sqft_living vs price: {c:.2f}")
    
print("")