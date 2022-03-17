import pandas as pd

pokemon = pd.read_csv('pokemon.csv'  , index_col='Pokemon' , squeeze=True)

print(pokemon['Bulbasaur'])

print(pokemon[['Bulbasaur','Pikachu']])

print(pokemon['Bulbasaur':'Pikachu'])