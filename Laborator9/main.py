import random
import numpy as np


def normalizeDataSet(dataset):
    return (dataset - dataset.min(axis=0)) / (dataset.max(axis=0) - dataset.min(axis=0))


def GetOutput(dataset, weight):
    output_array = []
    for i in range(0, len(dataset)):
        input_sum = 0
        for j in range(0, len(dataset[0])):
            input_sum += dataset[i, j] * weight[i, j]
        output_array.append(bipolar_function(input_sum))
    return np.array(output_array)


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
    return np.array(aux_array)


def calculateNewWeightArray():
    next_weights = []
    for i in range(0, len(dataset_array)):
        node_weight = []
        for j in range(0, len(dataset_array[0])):
            node_weight.append(weight_array[i][j] + learning_step * (wanted_output[i][j] - output[i]) *
                               (1 - wanted_output[i][j] ** 2) * dataset_array[i][j])
            # calculated using the formula in the documentation
        next_weights.append(node_weight)
    return np.array(next_weights)


error_value = 0  # initialized error value which will be compared with the max allowed error

max_error_value = 0.001  # change this to modify the accuracy of the output

learning_step = 0.1  # change this for more iterations and more accurate results

dataset_array = np.array(
    [[45, 85], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41],
     [43, 87], [190, 40]])

wanted_output = np.array(
    [[1, -1, -1], [-1, 1, -1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1],
     [-1, -1, 1]])

# normalizing data set
dataset_array = normalizeDataSet(dataset_array)
dataset_array = np.hstack((dataset_array, np.full((len(dataset_array), 1), -1)))  # added the column of -1's
print("Normalized data set :\n", dataset_array)

weight_array = initWeightArray(len(dataset_array[1]), len(dataset_array))
print("Weights set:\n", weight_array)
print("Wanted outputs are:\n", wanted_output)

while True:
    output = GetOutput(dataset_array, weight_array)
    next_weight_array = calculateNewWeightArray()
    break
