import random

import numpy as np


def bipolar_function(x):
    return 2 / (1 + np.exp(-x)) - 1


def initWeightArray(dataset_variable_number, dataset_size):
    r_array = [-1, 0, 1]
    aux_array = []
    while len(aux_array) < dataset_size:
        mini_array = []
        while len(mini_array) < dataset_variable_number:
            mini_array.append(r_array[random.randint(0, len(r_array) - 1)])
        aux_array.append(mini_array)
    return aux_array


error_value = 0  # initialized error value which will be compared with the max allowed error

max_error_value = 0.001  # change this to modify the accuracy of the output

learning_step = 0.1  # change this for more iterations and more accurate results

dataset_array = [[45, 85, -1], [50, 43, -1], [40, 80, -1], [55, 42, -1], [200, 43, -1], [48, 40, -1], [195, 41, -1],
                 [43, 87, -1], [190, 40, -1]]

weight_array = initWeightArray(len(dataset_array[1]), len(dataset_array))

wanted_output = [[1, -1, -1], [-1, 1, -1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1],
                 [-1, -1, 1]]

print("Data set:\n", dataset_array)
print("Weights set:\n", weight_array)
print("Wanted outputs are:\n", wanted_output)
