import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11)
y = np.random.randint(1,13,10)

plt.scatter(x,y,label='Stars',color='green',marker='*',s=30)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Scatter Plot')
plt.legend()

plt.show()
