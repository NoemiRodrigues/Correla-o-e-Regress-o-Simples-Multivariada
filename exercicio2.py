import numpy as np
import statsmodels as md
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as svd
import pandas as pd

'''Existe alguma correlação entre o preço price e a área total da casa
sqft_living, considerando apenas casas com pelo menos dois
banheiros bathrooms?'''

df_house = pd.read_csv('kc_house_data.csv')
df_filtrado = df_house[df_house['bathrooms'] >= 2]
corr_price_sqft = df_filtrado[['price', 'sqft_living']].corr().iloc[0, 1]
print(f"Correlação entre 'price' e 'sqft_living' (com bathrooms >= 2): {corr_price_sqft:.2f}")