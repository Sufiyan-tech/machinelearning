import pandas as pd

nba = pd.read_csv('nba.csv')

print(nba.head())

print(nba['Salary'].add(50000).head())
print((nba['Salary']+50000).head())

print(nba['Salary'].sub(50000).head())
print((nba['Salary']-50000).head())

print(nba['Salary'].mul(2).head())
print((nba['Salary']*2).head())

nba['Weight In KG'] = nba['Weight']*0.453

print(nba.head())
