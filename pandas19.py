import pandas as pd

nba = pd.read_csv('nba.csv')

# print(nba.head())
#
# print(nba.fillna(0).head())

nba['Salary'].fillna(0,inplace=True)

nba['College'].fillna('No College',inplace=True)

print(nba.head())


