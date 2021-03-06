import pandas as pd


google = pd.read_csv('google_stock_price.csv',squeeze=True)

def classify_performance(number):
    if number < 300:
        return 'OK'
    elif number >= 300 and number < 650:
        return 'Satisfactory'
    else:
        return 'Incredible'

print(google.apply(classify_performance))

print(google.apply(lambda stock_price:stock_price+1))