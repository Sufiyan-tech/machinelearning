import pandas as pd

nba = pd.read_csv('nba.csv')

print(nba.head())

print(nba.sort_values('Name').head())

print(nba.sort_values('Name',ascending=False).head())

print(nba.sort_values('Age').head())

print(nba.sort_values('Age',ascending=False).head())

print(nba.sort_values('Salary',na_position='last').tail())

print(nba.sort_values('Salary',na_position='first').head())