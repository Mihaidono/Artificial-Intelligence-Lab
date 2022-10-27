import math
import random

import numpy as np


def my_sgn(nr):
    if nr > 0:
        return 1
    return 0


# exercise 1
def exercise1():
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
def exercise2():
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


# exercise 3
def exercise3():
    binary_number_array = [[0, 1, 1, 1, 0, 1, 1, 0, 0],  # [1, 1, 1, 1, 0, 1, 1, 1, 1] <- original data
                           [0, 1, 0, 1, 0, 1, 0, 1, 0],
                           [0, 1, 0, 0, 1, 0, 0, 1, 0],
                           [1, 1, 0, 0, 1, 0, 0, 1, 0]]

    weight_array = [-0.14, 0.06, -0.28, -0.93, -0.08, 0.28, -0.64, 0.47, -0.85]

    output_array = []
    for number in range(0, len(binary_number_array)):
        output_array.append(my_sgn(np.dot(binary_number_array[number], weight_array)))

    for i in range(0, 4):
        if output_array[i] == 1:
            print("Numarul din matricea %s este 1" % i)
        elif output_array[i] == 0:
            print("Numarul din matricea %s este 0" % i)


# exercise 4

initial_output = []
next_output = []


def getOutput(output1, output2, output3):
    if output2 - output3 == 0:
        return output1
    return np.sign(output2 - output3)


iterations = 0
while abs(next_output[0] - initial_output[0]) + abs(next_output[1] - initial_output[1]) + abs(
        next_output[2] - initial_output[2]) > 0:
    iterations += 1
    next_output[0] = getOutput(next_output[0], initial_output[1], initial_output[2])
    next_output[1] = getOutput(next_output[1], initial_output[0], initial_output[2])
    next_output[2] = getOutput(next_output[2], initial_output[0], initial_output[1])
    print("Outputs for iteration %s:\n %s\n%s\n%s" % (iterations, next_output[0], next_output[1], next_output[2]))
