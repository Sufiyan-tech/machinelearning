import numpy as np
import matplotlib.pyplot as plt

np.random.seed(101)
x = np.random.randint(0,100,22)
range = (0,100)
bins = 10

plt.hist(x , bins , range , color='green' , histtype='bar' , rwidth=0.7)

plt.xlabel('Ages')
plt.ylabel('Bins')

plt.title('Histogram Plot')
plt.show()