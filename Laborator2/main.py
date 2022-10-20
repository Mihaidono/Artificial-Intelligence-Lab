import math

import numpy as np

# exercise 1

x = [2, 1, 2]
y = [1, -1, 4]

x_length = len(x)
y_length = len(y)

xTransposed = np.transpose(x)
yTransposed = np.transpose(y)

scalar_prod = 0
for i in range(0, x_length):
    scalar_prod += xTransposed[i] * y[i]
print("This is the dot product of x,y: ", scalar_prod)

sum = 0
for i in range(0, x_length):
    sum += pow(x[i], 2)
xNorm = math.sqrt(sum)

print("This is the euclidian norm of the x value: ", xNorm)
sum = 0
for i in range(0, y_length):
    sum += pow(y[i], 2)
yNorm = math.sqrt(sum)
print("This is the euclidian norm of the y value: %.2f" % yNorm)

x_y_angle = (scalar_prod) / (xNorm * yNorm)

print("The angle between x and y is %.4f " % x_y_angle)

# exercise 2

