import pandas as pd


# pokemon = pd.read_csv('pokemon.csv' , squeeze=True , usecols=['Name'])

# pokemon = pokemon.sort_values(ascending=True).head()

# pokemon = pokemon.sort_values(ascending=False)

# print(pokemon)


google = pd.read_csv('google_stock_price.csv',squeeze=True)

# google = google.sort_values()

google.sort_values(ascending=False , inplace=True)

print(google.head())