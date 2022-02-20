import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,7)

y = np.random.randint(0,100,6)

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('First Plot')
plt.show()