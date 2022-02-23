import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(0,100,20)

range = (0,100)

bins = 10

plt.hist(ages , bins , range , color='green' , histtype='bar' , rwidth=0.7)

plt.xlabel('Ages')
plt.ylabel('y-axis')

plt.title('Histogram Plot')

plt.show()