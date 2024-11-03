
# Análise de Dados com Pandas: Tratamento de Valores Faltantes

## Descrição
Este projeto aborda o tratamento de valores faltantes utilizando a biblioteca Pandas em Python. É fundamental compreender como lidar com dados ausentes em análise de dados, uma vez que eles podem impactar significativamente os resultados e as análises estatísticas.

## Pré-processamento
O pré-processamento é uma etapa crucial na análise de dados, pois garante que os dados estejam limpos e prontos para a modelagem. No contexto de valores faltantes, as seguintes técnicas foram empregadas:

1. **Detecção de Valores Faltantes:**
   - **`isnull()`**: Identifica valores nulos (retorna `True` para `NaN` e `None`).
   - **`notnull()`**: Identifica valores não nulos (retorna `True` para valores presentes).

2. **Remoção de Valores Faltantes:**
   - **`dropna()`**: Remove linhas ou colunas que contêm valores nulos.
     - Exemplo: `df.dropna(axis=0)` remove linhas; `df.dropna(axis=1)` remove colunas.

3. **Substituição de Valores Faltantes:**
   - **`fillna()`**: Substitui valores nulos por um valor específico ou pelo valor anterior (forward fill) ou seguinte (backward fill).
   - **`replace()`**: Substitui valores específicos, incluindo `NaN`.
   - **`interpolate()`**: Preenche valores nulos com base em métodos de interpolação, útil para dados sequenciais.

4. **Estatísticas Básicas:**
   - O cálculo de estatísticas básicas, como média, mediana, desvio padrão e variância, é realizado para entender a distribuição dos dados após o tratamento de valores faltantes.

5. **Visualização:**
   - Gráficos de dispersão, boxplots e gráficos de linhas e barras são utilizados para visualizar as distribuições e relações entre as variáveis, ajudando a identificar padrões e outliers.

## Conclusão
O tratamento de valores faltantes é uma etapa essencial no pré-processamento de dados. As técnicas apresentadas neste projeto são apenas algumas das várias abordagens disponíveis em Pandas. A escolha do método adequado depende do contexto dos dados e da análise desejada.

## Referências
- [Documentação do Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [Jupyter Notebook](https://jupyter.org/)
- [Google Colab](https://colab.research.google.com/)
