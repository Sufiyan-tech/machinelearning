import pandas as pd

nba = pd.read_csv('nba.csv').dropna(how='all')

nba['Salary'] = nba['Salary'].fillna(0).astype(int)

nba['SalaryRank'] = nba['Salary'].rank(ascending=False).astype(int)

nba.sort_values(by='SalaryRank' ,inplace=True)

print(nba.head())