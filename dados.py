import pandas as pd
import numpy as np

df = pd.read_csv('seguros.csv')

print(df.head())
print(df.info())
print(df.describe())


age_mean = df['age'].mean()
print(f"A idade média dos pacientes é: {age_mean:.1f}")
region_counts = df['region'].value_counts()
most_common_region = region_counts.idxmax()
print(f"A maioria dos indivíduos vem de: {most_common_region}")

smoker_costs = df[df['smoker'] == 'yes']['charges'].mean()
non_smoker_costs = df[df['smoker'] == 'no']['charges'].mean()
print(f"Custo médio para fumantes: {smoker_costs:.2f}")
print(f"Custo médio para não fumantes: {non_smoker_costs:.2f}")

at_least_one_child = df[df['children'] >= 1]
age_mean_at_least_one_child = at_least_one_child['age'].mean()
print(f"A idade média das pessoas com pelo menos um filho é: {age_mean_at_least_one_child:.1f}")

results = {
    "idade_media": age_mean,
    "regiao_mais_comum": most_common_region,
    "custo_medio_fumantes": smoker_costs,
    "custo_medio_nao_fumantes": non_smoker_costs,
    "idade_media_pelo_menos_um_filho": age_mean_at_least_one_child,
}

print(results)
