import pandas as pd

pokemon = pd.read_csv('pokemon.csv' , squeeze=True , usecols=['Name'])

print(pokemon)

print(pokemon.head())
print(pokemon.head(10))

print(pokemon.tail())
print(pokemon.tail(10))

print(pokemon.values)
print(pokemon.index)
print(pokemon.dtype)

print(pokemon.is_unique)
print(pokemon.ndim)
print(pokemon.shape)
print(pokemon.size)

print(pokemon.name)
print(pokemon.head())
pokemon.name = 'Pokemon'
print(pokemon.head())