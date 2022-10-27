import math
import random


# !!!this the algorithm generates the minimum for the function you multiply with the learning step in the while!!!

def exercise1():
    initial_value = random.uniform(0, 100)
    print("Input the learning step: ")
    learning_step = float(input())  # 0.01 for example
    print("Input the threshold: ")  # the lower the learning step the more accurate
    threshold = float(input())  # 0.00001 for example

    next_value = 0

    number_of_iterations = 1
    while True:  # modify this function after the learning_step* to change the function for which is calculates
        next_value = initial_value - learning_step * (12 * initial_value - 12)
        print("Number of iterations: %s\nXn+1= %s\tXn= %s\nFunction value: %s\n"
              % (number_of_iterations, next_value, initial_value, 6 * pow(next_value, 2) - 12 * next_value + 1))
        if abs(next_value - initial_value) < threshold:
            break
        initial_value = next_value
        number_of_iterations += 1
    print("\nThe function's min is ", next_value)


# for functions of 2 parameters
def exercise2():
    initial_value_x = random.uniform(0.0, 100.0)
    initial_value_y = random.uniform(0.0, 100.0)

    print("Input the learning step: ")
    learning_step = float(input())  # 0.01 for example
    print("Input the threshold: ")  # the lower the learning step the more accurate
    threshold = float(input())  # 0.00001 for example

    next_value_x = 0
    next_value_y = 0
    number_of_iterations = 1
    while True:  # modify these functions after the learning_step* to change the function for which is calculates
        next_value_x = initial_value_x - learning_step * (
                -2 * (1 - initial_value_x) + 200 * (initial_value_x - pow(initial_value_y, 2)))
        next_value_y = initial_value_y - learning_step * (
                -400 * (initial_value_x - pow(initial_value_y, 2)) * initial_value_y)
        print("Number of iterations: %s\nXn+1= %s\tXn= %s\nFunction value: %s\n"
              % (number_of_iterations, next_value_x, initial_value_x,
                 -2 * (1 - initial_value_x) + 200 * (initial_value_x - pow(initial_value_y, 2))))
        print("Number of iterations: %s\nXn+1= %s\tXn= %s\nFunction value: %s\n"
              % (number_of_iterations, next_value_x, initial_value_x,
                 -400 * (initial_value_x - pow(initial_value_y, 2)) * initial_value_y))

        if abs(next_value_x - initial_value_x) < threshold and abs(next_value_y - initial_value_y) < threshold:
            break
        initial_value_x = next_value_x
        initial_value_y = next_value_y
        number_of_iterations += 1
    print("\nThe function's min for x is ", next_value_x)
    print("\nThe function's min for y is ", next_value_y)


exercise2()
