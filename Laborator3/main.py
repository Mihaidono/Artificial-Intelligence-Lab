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
def printfunction_a(number_of_iterations, next_value_x, initial_value_x, next_value_y, initial_value_y):
    print("Xn+1= %s\tXn= %s\nFunction value: %s\n"
          % (next_value_x, initial_value_x,
             2 * initial_value_x))

    print("Yn+1= %s\tYn= %s\nFunction value: %s\n"
          % (next_value_y, initial_value_y,
             4 * initial_value_y))


def printfunction_b(next_value_x, initial_value_x, next_value_y, initial_value_y):
    print("Xn+1= %s\tXn= %s\nFunction value: %s\n"
          % (next_value_x, initial_value_x,
             -2 * (1 - initial_value_x) + 200 * (initial_value_x - pow(initial_value_y, 2))))

    print("Yn+1= %s\tYn= %s\nFunction value: %s\n"
          % (next_value_y, initial_value_y,
             -400 * (initial_value_x - pow(initial_value_y, 2)) * initial_value_y))


def exercise2():
    initial_value_x = random.uniform(0.0, 100.0)
    initial_value_y = random.uniform(0.0, 100.0)

    print("Input the learning step: ")
    learning_step = float(input())  # 0.01 for example
    print("Input the threshold: ")  # the lower the learning step the more accurate
    threshold = float(input())  # 0.00001 for example
    print("Choose function:\n1->g(x,y) = x^2 +2y^2\n2->h(x,y) = (1-x)^2+100(x-y^2)^2")
    function_chosen = int(input())
    next_value_x = 0
    next_value_y = 0
    number_of_iterations = 1
    while True:  # modify these functions after the learning_step* to change the function for which is calculates
        print("Iteration number: %s\n" % number_of_iterations)
        if function_chosen == 1:
            # g(x,y) = x^2 +2y^2
            next_value_x = initial_value_x - learning_step * (2 * initial_value_x)
            next_value_y = initial_value_y - learning_step * (4 * initial_value_y)

            printfunction_a(number_of_iterations, next_value_x, initial_value_x, next_value_y, initial_value_y)
        elif function_chosen == 2:
            # h(x,y) = (1-x)^2+100(x-y^2)^2
            next_value_x = initial_value_x - learning_step * (
                    -2 * (1 - initial_value_x) + 200 * (initial_value_x - pow(initial_value_y, 2)))
            next_value_y = initial_value_y - learning_step * (
                    -400 * (initial_value_x - pow(initial_value_y, 2)) * initial_value_y)

            printfunction_b(number_of_iterations, next_value_x, initial_value_x, next_value_y, initial_value_y)
        else:
            print("Function not chosen properly")
            break

        if abs(next_value_x - initial_value_x) < threshold and abs(next_value_y - initial_value_y) < threshold:
            break
        initial_value_x = next_value_x
        initial_value_y = next_value_y
        number_of_iterations += 1
    print("\nThe function's min for x is ", next_value_x)
    print("\nThe function's min for y is ", next_value_y)


print("Choose an option:"
      "\n1.Gradient method for one member function f(x) = 6x^2-12x+1"
      "\n2.Gradient method for two member functions")
user_input = int(input())
if user_input == 1:
    exercise1()
elif user_input == 2:
    exercise2()
else:
    print("Not a valid choice")
