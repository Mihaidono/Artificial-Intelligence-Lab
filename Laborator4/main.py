import numpy as np


# exercise 1

def continuous_function(var):
    return (1 - np.exp(-var)) / (1 + np.exp(-var))


switch_variable = False  # switch this : false -> exercise 7 ; true -> example 4
print("Choose example 4 or exercise 7 by inserting 4 or 7")
user_input = int(input())
if user_input == 4:
    switch_variable = True
elif user_input == 7:
    switch_variable = False
else:
    print("Option invalid going with the default case : exercise 7")

if switch_variable is True:
    weights_array = np.array([1, -1, 0, 0.5])  # for example 4

    entries = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])  # for example 4
    # using the sign function
    for id in range(0, len(entries)):
        net = np.dot(entries[id], weights_array)
        print(f"\n{id + 1} Iteration net:", net)
        print("before", weights_array)
        weights_array = np.add(weights_array, np.multiply(np.sign(net), entries[id]))
        print("after", weights_array)

    weights_array = np.array([1, -1, 0, 0.5])

    entries = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])
    # using the continuous function

    for itr in range(0, 20):
        print(f"\n=====Time gone through the set: {itr + 1}=====\n")
        for id in range(0, len(entries)):
            net = np.dot(entries[id], weights_array)
            print(f"\n{id + 1} Iteration net: %.3f" % continuous_function(net))
            print("before", weights_array)
            weights_array = np.add(weights_array, np.multiply(continuous_function(net), entries[id]))
            print("after", weights_array)
else:
    weights_array = np.array([1, -1])  # for exercise 7

    entries = np.array([[1, -2], [0, 1], [2, 3], [1, -1]])  # for exercise 7

    for id in range(0, len(entries)):
        net = np.dot(entries[id], weights_array)
        print(f"\n{id + 1} Iteration net:", net)
        print("before", weights_array)
        weights_array = np.add(weights_array, np.multiply(np.sign(net), entries[id]))
        print("after", weights_array)

    for itr in range(0, 20):
        print(f"\n=====Time gone through the set: {itr + 1}=====\n")
        for id in range(0, len(entries)):
            net = np.dot(entries[id], weights_array)
            print(f"\n{id + 1} Iteration net: %.3f" % continuous_function(net))
            print("before", weights_array)
            weights_array = np.add(weights_array, np.multiply(continuous_function(net), entries[id]))
            print("after", weights_array)
