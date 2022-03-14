import matplotlib.pyplot as plt
import numpy as np

plt.subplot(3,2,1)

x1 = np.arange(0.0,2.0,0.01)
y1 = np.cos(x1)

plt.plot(x1,y1,'--')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Cosine Plot')


plt.subplot(3,2,2)

x2 = np.arange(1,6)
np.random.seed(101)
y2 = np.random.randint(1,100,5)
languages = ['Python','Java','C','C++','Php']

plt.bar(x2,y2,tick_label=languages,width=0.7,color=['green','blue'])
plt.xlabel('Language')
plt.ylabel('No Of Users')
plt.title('Programming Trends')

plt.subplot(3,2,3)
np.random.seed(101)
x3 = np.random.randint(1,100,10)
range = (1,100)
bins = 10

plt.hist(x3 , bins , range , color='green' , histtype='bar' , rwidth=0.7)
plt.xlabel('Marks')
plt.ylabel('No Of Students')
plt.title('Marks Of Student In English')

plt.subplot(3,2,4)

x4 = np.arange(1,11)
np.random.seed(101)
y4 = np.random.randint(1,100,10)

plt.plot(x4,y4)
plt.scatter(x4,y4,label='Stars',color='green',marker='*',s=30)
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.title('Plot Merging')
plt.legend()

plt.subplot(3,2,5)
activities = ['eat','sleep','conquerer','repeat']
slices = [5,2,5,9]
colors = ['r','g','m','b']
plt.pie(slices,labels=activities,colors=colors,startangle=90,shadow=True,explode=(0.1,0,0,0),autopct='%1.2f%%')
plt.legend()

plt.show()
