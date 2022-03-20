import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('fivethirtyeight')

fig1 = plt.figure()

ax1 = fig1.add_subplot(1,1,1)

def animate(p):
    google = pd.read_csv('google_stock_price.csv',squeeze=True)

    x1 = []
    y1 = []

    for i in range(0,google.count()):
        x = i+1
        y = google[i]

        x1.append(x)
        y1.append(y)

        ax1.clear()
        ax1.plot(x1,y1)


anime_data = animation.FuncAnimation(fig1,animate,interval=500)

plt.show()