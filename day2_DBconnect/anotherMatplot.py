import numpy as np
import matplotlib.pyplot as plt


arr = np.array([[ [1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 4, 4], [9, 10, 11, 12]], dtype=np.int64)
plt.hist(arr.ravel(), bins=12, color='red')

plt.title("Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()

"""
y = [1, 2, 4, 5, 6, 7]
n = len(y)
x = range(n)
width  = 1/1.5
plt.show()
"""