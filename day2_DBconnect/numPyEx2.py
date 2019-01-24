import numpy as np
import sys

x = np.array([7, 8, 9])
y = np.array([7, 8, 9])

print("Multiplication: ", x*y)
print("Division: ", x/y)
print("Addition", x+y)
print("Subtraction", x-y)

print("Max in x is :", x.max())
print("Max in x is :", x.min())
print("Sum of x is : ", x.sum())
print("Mean of x is :", x.mean())

print("Transpose", np.transpose(x))

try:
    print("Insert : ", np.insert(x, 1, 3))
    print((np.append(y, [[7], [2]], axis=0)))
except Exception as e:
    print("Something went wrong while inserting - ", e)


a = [[2, 3, 4], [1, 2, 3]]
print(np.ndim(a))
