import random
import time

import numpy as np


def normalizeDataSet(dataset):
    return (dataset - dataset.min(axis=0)) / (dataset.max(axis=0) - dataset.min(axis=0))


def GetOutput(subset, weight):
    output_array = []

    for i in range(0, len(subset)):
        input_sum = 0
        for j in range(0, len(subset)):
            input_sum += subset[j] * weight[i][j]
        output_array.append(bipolar_function(input_sum))
    return np.array(output_array)


def bipolar_function(x):
    return 2 / (1 + np.exp(-x)) - 1


def initWeightArray():
    aux_array = []
    while len(aux_array) < len(dataset_array[0]):
        mini_array = []
        while len(mini_array) < len(dataset_array[0]):
            mini_array.append(np.random.uniform(-1, 1))
        aux_array.append(mini_array)
    return np.array(aux_array)


def calculateNewWeightArray():
    next_weights = weight_array
    for i in range(0, len(next_weights)):
        for j in range(0, len(output)):
            next_weights[j][i] = weight_array[j][i] + learning_step * (wanted_output[dt_index][j] - output[j]) * (
                    1 - output[j] ** 2) * dataset_array[dt_index][i]
    return np.array(next_weights)


def calculateNextError(old_error):
    next_error = 0
    for k in range(0, len(output)):
        next_error += (wanted_output[dt_index][k] - output[k]) ** 2
    return old_error + next_error


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

weight_array = initWeightArray()
print("Weights set:\n", weight_array)
print("Wanted outputs are:\n", wanted_output)

count = 0
while True:
    error_value = 0  # initialized error value which will be compared with the max allowed error
    dt_index = 0
    while dt_index < len(dataset_array):
        print(f"\n\nSUBSET {dt_index + 1}:")

        output = GetOutput(dataset_array[dt_index], weight_array)
        print("Output:\n", output)

        print(f"\nOld weights:\n{weight_array}\n")
        weight_array = calculateNewWeightArray()
        print(f"Next weights:\n{weight_array}")

        error_value = calculateNextError(error_value)
        print(f"MAX error value: {max_error_value}\nCurrent error value: {error_value}")

        dt_index += 1
    if error_value < max_error_value:
        break
    count += 1
    # time.sleep(0.5)
print(f"Solution found after {count} iterations")

print_dataset = [[45, 85], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41],
                 [43, 87], [190, 40]]

print(f"For the dataset:\n{print_dataset}\n We have:")
for i in range(0, len(dataset_array)):
    output = GetOutput(dataset_array[i], weight_array)
    print(f"Subset {dataset_array[i]}:\nWanted output:\n{wanted_output[i]}\nActual output:\n{output}\n")
