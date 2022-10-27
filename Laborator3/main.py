import math


# !!!this the algorithm generates the minimum for the function you multiply with the learning step in the while!!!
def exercise1():
    print("Input a number: ")
    initial_value = float(input())
    print("Input the learning step: ")
    learning_step = float(input())  # 0.01 for example
    print("Input the threshold: ")  # the lower the learning step the more accurate
    threshold = float(input())  # 0.00001 for example

    next_value = 0

    number_of_iterations = 1
    while True:
        next_value = initial_value - learning_step * (12 * initial_value - 12)
        print("Number of iterations: %s\nXn+1= %s\tXn= %s\nFunction value: %s\n"
              % (number_of_iterations, next_value, initial_value, 6 * pow(initial_value, 2) - 12 * initial_value + 1))
        if abs(next_value - initial_value) < threshold:
            break
        initial_value = next_value
        number_of_iterations += 1
    print("\nThe function's min is ", next_value)
