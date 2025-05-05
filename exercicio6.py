import numpy as np
import statsmodels as md
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pandas as pd

'''6. Calcule a correlação entre uma variável categórica(waterfront) e uma
variável numérica(price) usando ANOVA'''
df_house = pd.read_csv('kc_house_data.csv')
preco_sem_vista = df_house[df_house['waterfront'] == 0]['price']
preco_com_vista = df_house[df_house['waterfront'] == 1]['price']

f_stat, p_val = stats.f_oneway(preco_sem_vista, preco_com_vista)

print(f"Estatística F: {f_stat:.2f}")
print(f"Valor-p (p-value): {p_val:.4f}")

if p_val < 0.05:
    print("Diferença estatisticamente significativa entre os preços das casas com e sem vista para a água.")
else:
    print("Não há diferença estatisticamente significativa entre os preços.")