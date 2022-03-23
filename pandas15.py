import pandas as pd

# rev = pd.read_csv('revenue.csv' , index_col='Date')
#
# print(rev)
#
# print(rev.sum())
#
# print(rev.sum(axis=0))
# print(rev.sum(axis='index'))
#
# print(rev.sum(axis=1))
# print(rev.sum(axis='columns'))


nba = pd.read_csv('nba.csv')

# print(nba.head())

print(nba.Name.head(11))

print(nba['Name'].head())

print(nba[['Name','Team','Age']])

select = ['Name','Team' , 'Height']

print(nba[select].head(10))