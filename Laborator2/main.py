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


node_number = int(input("Select the number of nodes: "))

print("Nodes look like this: P(x,y,z).\n"
      "Input values in this way for correct results!"
      "\n->Input your nodes: ")
node_array = []

for i in range(0, node_number):
    print("Node %s: " % i)
    node_variables = []
    for j in range(0, 3):
        elem = int(input())
        node_variables.append(elem)
    node_array.append(node_variables)

node_array = np.array(node_array)

for i in range(0, node_number):
    if np.sign(np.sum(node_array[i])) == 1:
        print("Node %s (%s,%s,%s) belongs to Class 1 " % (i, node_array[i][0], node_array[i][1], node_array[i][2]))
    elif np.sign(np.sum(node_array[i])) == -1:
        print("Node %s (%s,%s,%s) belongs to Class 2 " % (i, node_array[i][0], node_array[i][1], node_array[i][2]))
