import pandas as pd

pokemon = pd.read_csv('pokemon.csv',usecols=['Name'],squeeze=True)

print(pokemon[30])
print(pokemon[[100,300,500]])
print(pokemon[70:101])
print(pokemon[:51])
print(pokemon[750:])
print(pokemon[-30:])
print(pokemon[:-10])