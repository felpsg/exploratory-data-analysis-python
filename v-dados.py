import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_histplot(dataframe, column, title, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=dataframe, x=column, bins=20, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_boxplot(dataframe, x, y, title, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=dataframe, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_scatterplot(dataframe, x, y, hue, title, xlabel, ylabel):
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=dataframe, x=x, y=y, hue=hue)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_countplot(dataframe, column, title, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=dataframe, x=column)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


# Carregar os dados
df = pd.read_csv('seguros.csv')

# Visualizar a distribuição da idade dos pacientes
plot_histplot(df, 'age', 'Distribuição da Idade dos Pacientes', 'Idade', 'Contagem')

# Visualizar a distribuição dos custos entre fumantes e não fumantes
plot_boxplot(df, 'smoker', 'charges', 'Custos de Seguro para Fumantes e Não Fumantes', 'Fumante', 'Custos')

# Visualizar a relação entre idade, custo e status de fumante
plot_scatterplot(df, 'age', 'charges', 'smoker', 'Custos de Seguro em Relação à Idade e Status de Fumante', 'Idade', 'Custos')

# Visualizar a distribuição de indivíduos por região
plot_countplot(df, 'region', 'Distribuição de Indivíduos por Região', 'Região', 'Contagem')

# Visualizar a idade média de pessoas com pelo menos um filho
df_at_least_one_child = df[df['children'] >= 1]
plot_histplot(df_at_least_one_child, 'age', 'Distribuição da Idade dos Pacientes com Pelo Menos Um Filho', 'Idade', 'Contagem')

# Gráfico de barras para 'sex'
plot_countplot(df, 'sex', 'Distribuição de Sex', 'Sexo', 'Contagem')

# Gráfico de barras para 'smoker'
plot_countplot(df, 'smoker', 'Distribuição de Fumantes', 'Fumante', 'Contagem')

# Gráfico de barras para 'region'
plot_countplot(df, 'region', 'Distribuição de Região', 'Região', 'Contagem')
