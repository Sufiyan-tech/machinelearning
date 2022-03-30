import pandas as pd

nba = pd.read_csv('nba.csv')

print(nba.head())

print(nba.sort_values(['Team','Name']).head())

print(nba.sort_values(['Team' , 'Name'] , ascending=False).head())

nba.sort_values(['Team','Name'],ascending=[True,False],inplace=True)

print(nba.head())