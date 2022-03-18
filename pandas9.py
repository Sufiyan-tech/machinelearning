import pandas as pd

pokemon = pd.read_csv('pokemon.csv',index_col='Pokemon',squeeze=True)

pokemon.sort_index(inplace=True)

print(pokemon.head())

print(pokemon.get('Abra'))

print(pokemon.get(['Abra','Pikachu']))

print(pokemon.get(key='Abra'))

print(pokemon.get(key=['Abra','Pikachu']))

print(pokemon.get(key='Dolie' , default='This Is A Not A Pokemon'))

print(pokemon.get(key=['Abra','Dolie'] , default='This Is A Not A Pokemon'))