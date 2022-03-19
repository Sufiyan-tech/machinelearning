import pandas as pd
import numpy as np

google = pd.read_csv('google_stock_price.csv',squeeze=True)

print(google.head())

print(google.count())

print(len(google))

print(google.sum())

print(google.mean())

print(google.sum()/google.count())

print(google.std())

print(google.min())

print(google.max())

print(google.median())