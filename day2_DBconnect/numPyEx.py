import numpy as np
import sys

number = np.array([7, 8, 9])
print(number)
print(type(number))
print("One's array", np.ones((2, 2)))
print("Empty array", np.empty((2, 2)))
npRange = np.arange(100)  # A range - you can specify limit as arrange(30,60) so will print b/w 30 and 60
print(npRange)
print("The size of npRange variable is: ", (sys.getsizeof(npRange)))

myArray = np.array([[1, 2], [3, 5], [6, 7]])
print(myArray)
print(myArray.dtype)  # DataType of the array
print(myArray.shape)  # Dimension of the array

""" The below code is comparison of memory used by list and numpy"""
n = range(1000)
print("Memory occupied by List - single element", sys.getsizeof(5)*len(n))
m = np.arange(1000)
print("Memory occupied by numPy - single element", m.size*m.itemsize)


