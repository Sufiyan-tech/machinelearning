import pandas as pd

nba = pd.read_csv('nba.csv')

print(nba.head())

print(nba.tail())

print(nba.dropna())

print(nba.dropna(how='any'))

print(nba.dropna(how='all'))

print(nba.dropna(axis=1))

print(nba.dropna(axis=0))

nba.dropna(subset=['Salary'],inplace=True)

print(nba.head())