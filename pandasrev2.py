import pandas as pd
import numpy as np

pokemon = pd.read_csv('pokemon.csv',index_col=['Pokemon'],squeeze=True)

print(pokemon['Hoopa'])
print(pokemon[['Hoopa','Pikachu']])
print(pokemon['Bulbasaur':'Pikachu'])