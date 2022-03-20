import pandas as pd

pokemon = pd.read_csv('pokemon.csv',index_col='Pokemon',squeeze=True)

print(pokemon.head())

print(pokemon.value_counts())

print(pokemon.value_counts().sum())

print(pokemon.value_counts(ascending=True))