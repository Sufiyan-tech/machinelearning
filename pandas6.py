import pandas as pd

pokemon = pd.read_csv('pokemon.csv' , squeeze=True , usecols=['Name'])

pokemon.sort_values(ascending=False , inplace=True)

pokemon.sort_index(ascending=False , inplace=True)

print(pokemon)

