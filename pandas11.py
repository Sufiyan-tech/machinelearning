import pandas as pd

google = pd.read_csv('google_stock_price.csv',squeeze=True)

print(google.head())

print(google.max())
print(google.idxmax())

print(google.min())
print(google.idxmin())