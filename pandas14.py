import pandas as pd

nba = pd.read_csv('nba.csv')

print(nba)

print(nba.head())

print(nba.tail())

print(nba.index)

print(nba.shape)

print(nba.dtypes)

print(nba.columns)

print(nba.axes)

print(nba.info)

print(nba.info())

print(nba.get_dtype_counts())