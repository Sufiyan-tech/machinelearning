import numpy as np

arr = np.arange(0,11,2)

arr = np.zeros(5)
arr = np.zeros((2,5))

arr = np.ones(5)
arr = np.ones((5,2))

arr = np.random.randint(0,10)

arr = np.random.randint(0,100,(2,3))

np.random.seed(101)

arr = np.random.randint(0,100,10)

arr = np.arange(0,100).reshape(10,10)

print(arr)
print(arr[0,0])
print(arr[1,2:6])
print(arr[0:6 , 0:2])
print(arr[1,:])
print(arr[:,-1])
# print(arr.max())
# print(arr.min())
# print(arr.mean())
# print(arr.argmax())
# print(arr.argmin())
# print(arr.reshape((5,2)))