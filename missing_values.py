# -*- coding: utf-8 -*-
"""missing_values.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vnFn2FQBRuVOpC8dkvUEYFYcOHe5yEPa

# Como trabalhar com Missing Values em Python
- Jupyter Notebook ou Google Colab
- Biblioteca Pandas

Pandas permite o tratamento de dados faltosos, como valores `None` ou `NaN`.

A detecção, remoção e substituição de valores faltosos podem ser feitas com as seguintes funções do Pandas:

* `isnull()`: identifica valores nulos (retorna `True` para `NaN` e `None`).
* `notnull()`: identifica valores não nulos (retorna `True` para valores presentes).
* `dropna()`: remove linhas ou colunas com valores nulos.
* `fillna()`: substitui valores nulos por um valor específico.
* `replace()`: substitui valores específicos (pode ser usado para `NaN` e outros valores).
* `interpolate()`: preenche valores nulos com base em métodos de interpolação, útil para dados sequenciais.

# Importação das bibliotecas
"""

# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# Criação de um dicionário qualquer para Dataframe"""

# Criação de um dicionário com valores faltantes para exemplo
dicionario = {
    'Primeira': [96, np.nan, 85, 95],
    'Segunda': [45, 70, np.nan, 54],
    'Terceira': [np.nan, 50, np.nan, 100],
    'Quarta': [65, 50, 88, 100]
}

# Alimentar o DataFrame com os dados do dicionário
df = pd.DataFrame(dicionario)
print("DataFrame Original:")
print(df)

"""# Exibir gráfico de calor mostrando onde estão os valores faltantes"""

plt.figure(figsize=(8, 5))
sns.heatmap(df.isnull(), cmap='viridis', cbar=False, yticklabels=False)
plt.title("Mapa de calor dos valores faltantes")
plt.show()

"""# Checagem dos valores faltosos"""

# Checagem dos valores faltosos (isnull e notnull)
print("\nVerificar valores nulos:")
print(df.isnull())

print("\nVerificar valores não nulos:")
print(df.notnull())

"""Uma forma de utilizar apenas células com valores presentes de uma determinada coluna"""

valores_true = pd.notnull(df['Terceira'])
valores_true

df[valores_true]

"""# Comando 'dropna' para eliminação de registros nulos de uma linha"""

# Remover linhas com valores nulos
print("\nDataFrame sem linhas com valores nulos (dropna):")
print(df.dropna(axis=0))  # Remove linhas com qualquer valor nulo

# Remover colunas com valores nulos
print("\nDataFrame sem colunas com valores nulos (dropna):")
print(df.dropna(axis=1))

"""# Completando os valores faltosos"""

df

print("\nDataFrame com valores nulos preenchidos com o valor anterior (ffill):")
print(df.fillna(method='ffill'))

# Preencher valores nulos com o valor seguinte (método bfill)
print("\nDataFrame com valores nulos preenchidos com o valor seguinte (bfill):")
print(df.fillna(method='bfill'))

# Preenchendo valores nulos com diferentes métodos para cada coluna
df['Primeira'] = df['Primeira'].fillna(df['Primeira'].mean())  # Preenche com a média
df['Segunda'] = df['Segunda'].fillna(df['Segunda'].median())   # Preenche com a mediana
df['Terceira'] = df['Terceira'].ffill()                        # Preenche com o valor anterior
df['Quarta'] = df['Quarta'].fillna(0)                          # Preenche com zero

print("DataFrame após preenchimento condicional:")
print(df)

"""# Usando interpolação"""

# Interpolação linear (preenche com valores intermediários)
print("\nDataFrame com valores preenchidos por interpolação linear (forward):")
print(df.interpolate(method='linear', limit_direction='forward'))

# Interpolação para trás (valores seguintes preenchem os nulos anteriores)
print("\nDataFrame com valores preenchidos por interpolação linear (backward):")
print(df.interpolate(method='linear', limit_direction='backward'))

# Substituir valores nulos por um valor específico, como -30
print("\nDataFrame com valores nulos substituídos por -30:")
print(df.replace(to_replace=np.nan, value=-30))

df.interpolate(method= 'linear', limit_direction='backward', inplace=True) #salvar mudanças no df
df

"""# Cálculo de Estatísticas Básicas"""

# Média de cada coluna
print("Média de cada coluna:")
print(df.mean())

# Mediana de cada coluna
print("\nMediana de cada coluna:")
print(df.median())

# Desvio padrão de cada coluna
print("\nDesvio padrão de cada coluna:")
print(df.std())

# Variância de cada coluna
print("\nVariância de cada coluna:")
print(df.var())

"""# Filtrando Dados com Condições"""

# Seleciona linhas onde os valores da coluna 'Primeira' são maiores que 90
print("Linhas onde 'Primeira' > 90:")
print(df[df['Primeira'] > 90])

"""# Ordenação dos Dados"""

# Ordena o DataFrame pela coluna 'Segunda' em ordem crescente
print("DataFrame ordenado pela coluna 'Segunda':")
print(df.sort_values(by='Segunda'))

# Ordena o DataFrame pela coluna 'Quarta' em ordem decrescente
print("\nDataFrame ordenado pela coluna 'Quarta' (decrescente):")
print(df.sort_values(by='Quarta', ascending=False))

"""# Gráfico de Dispersão"""

# Gráfico de dispersão entre 'Primeira' e 'Segunda'
plt.figure(figsize=(10, 6))
plt.scatter(df['Primeira'], df['Segunda'], color='blue')

# Títulos e rótulos
plt.title('Relação entre Primeira e Segunda')
plt.xlabel('Primeira')
plt.ylabel('Segunda')
plt.grid()

# Mostrar o gráfico
plt.show()

"""# Boxplot"""

# Configurando o gráfico boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)

# Títulos e rótulos
plt.title('Boxplot')
plt.xlabel('dias')
plt.ylabel('valores')

# Mostrar o gráfico
plt.grid(axis='y')
plt.show()

"""# Gráfico de Linhas"""

# Configurando o gráfico de linhas
plt.figure(figsize=(10, 6))
for index, row in df.iterrows():
    plt.plot(df.columns[:-1], row[:-1], marker='o', label=f'Aluno {index}')

# Títulos e rótulos
plt.title('Grafico de linhas')
plt.xlabel('Dias')
plt.ylabel('valores')
plt.xticks(rotation=45)

# Mostrar o gráfico
plt.legend()
plt.grid()
plt.show()

"""# Gráfico de Barras"""

# Configurando o gráfico de barras
df.plot(kind='bar', figsize=(10, 6))

# Títulos e rótulos
plt.title('Grafico de barras')
plt.xlabel('Dias')
plt.ylabel('Valores')
plt.xticks(rotation=0)  # Rótulos do eixo X em horizontal

# Mostrar o gráfico
plt.legend(title='Ordem')
plt.grid(axis='y')
plt.show()