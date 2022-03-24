import pandas as pd

nba = pd.read_csv('nba.csv')

print(nba.head())

nba['Sport'] = 'BasketBall'

print(nba.head())

nba['League'] = 'Super BasketBall League'

print(nba.head())

def calculateWeight(weight):
    if weight >= 100 and weight <= 150:
        return 'Normal'
    elif weight >= 151 and weight <= 200:
        return 'Good'
    elif weight >= 201 and weight <= 250:
        return 'Healthy'
    elif weight >= 251 and weight <= 300:
        return 'Obese'
    else:
        return 'Invalid'

nba['WeightStatus'] = nba['Weight'].apply(calculateWeight)

print(nba.tail(20))