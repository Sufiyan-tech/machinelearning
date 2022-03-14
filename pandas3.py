import pandas as pd
import numpy as np

np.random.seed(11)
rates = np.random.randint(1,10,5)

r = pd.Series(rates)

print(r)

print(r.sum())
print(r.product())
print(r.mean())

fruits = ['Apple','Mango','Strawberry','Pineapple','Orange']
weekdays = ['Mon','Tue','Wed','Thurs','Fri']

print(pd.Series(fruits,weekdays))
print(pd.Series(data=fruits,index=weekdays))
print(pd.Series(fruits,index=weekdays))