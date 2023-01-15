import time
import numpy as np


# the following code works only for the example I had in the material, that meaning 2 inputs with -1
# going into one hidden layer formed out of 3 neurons which go into a single output

def normalizeDataSet(dset):
    return (dset - dset.min(axis=0)) / (dset.max(axis=0) - dset.min(axis=0))


# def decreaseLearningStep(step):
#    if step > 1:
#        step -= 1
#    if 1 >= step > 0.2:
#        step -= 0.1
#    return step


def initHLWeightArray():
    aux_array = []
    while len(aux_array) < len(dataset[0]):
        mini_array = []
        while len(mini_array) < len(dataset[0]):
            mini_array.append(np.random.uniform(-1, 1))
        aux_array.append(mini_array)
    return np.array(aux_array)


def initOLWeightArray():
    aux_array = []
    while len(aux_array) < len(dataset[0]) + 1:
        aux_array.append(np.random.uniform(-1, 1))
    return np.array(aux_array)


def bipolar_function(x):
    return 2 / (1 + np.exp(-x)) - 1


def GetHLOutput(subset, weight):
    output_array = []

    for i in range(0, len(subset)):
        input_sum = 0
        for j in range(0, len(subset)):
            input_sum += subset[j] * weight[i][j]
        output_array.append(bipolar_function(input_sum))
    output_array.append(-1)
    return np.array(output_array)


def GetOLOutput(prev_output, weight):
    output = 0
    for i in range(0, len(prev_output)):
        output += prev_output[i] * weight[i]
    return bipolar_function(output)


def calculateDelta():
    odt = 0.5 * (wanted_output[dt_index] - ol_output) * (1 - ol_output ** 2)  # outer layer delta
    hdt = []  # hidden layer delta
    for j in range(0, len(hl_output) - 1):
        hdt.append(0.5 * (1 - hl_output[j] ** 2) * (odt * ol_weights[j]))
    return hdt, odt


def updateWeights():
    next_hl_weight = hl_weights
    next_ol_weight = ol_weights

    for j in range(0, len(hl_output)):
        next_ol_weight[j] = ol_weights[j] + learning_step * ol_delta * hl_output[j]

    for j in range(0, len(hl_output) - 1):
        for i in range(0, len(hl_output) - 1):
            next_hl_weight[j][i] = hl_weights[j][i] + learning_step * hl_delta[j] * dataset[dt_index][i]

    return next_hl_weight, next_ol_weight


def calculateNextError(old_error):
    next_error = 0.5 * ((wanted_output[dt_index] - ol_output) ** 2)
    return old_error + next_error


learning_step = 0.1  # for a faster learning rate, its value will decrease in time

max_error_value = 0.01  # change this to modify the accuracy of the output

dataset = np.array([[45, 85], [50, 43], [40, 80], [187, 107], [55, 42], [200, 43], [48, 40], [195, 41],
                    [43, 87], [192, 105], [190, 40], [188, 100]])

wanted_output = [1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1]

dataset = normalizeDataSet(dataset)
dataset = np.hstack((dataset, np.full((len(dataset), 1), -1)))  # added the column of -1's
print(f"Normalized data set :\n{dataset}\n")

hl_weights = initHLWeightArray()  # hidden layer weights
print(f"Hidden layer weights:\n{hl_weights}\n")

ol_weights = initOLWeightArray()  # outer layer weights
print(f"Outer layer weights:\n{ol_weights}\n")

count = 0
while True:
    error_value = 0  # initialized error value which will be compared with the max allowed error
    dt_index = 0  # dataset index -> tells us which subset we're using
    while dt_index < len(dataset):
        print(f"\n\nSUBSET {dt_index + 1}:")

        hl_output = GetHLOutput(dataset[dt_index], hl_weights)
        print(f"Hidden layer output: {hl_output}\n")

        ol_output = GetOLOutput(hl_output, ol_weights)
        print(f"Outer layer output: {ol_output}\n")

        hl_delta, ol_delta = calculateDelta()
        print(f"Outer layer delta: {ol_delta}\nHidden layer delta: {hl_delta}\n")

        print(f"OLD Weights:\n\tHidden layer weights:\n{hl_weights}\n\tOuter layer weights:\n{ol_weights}\n")
        hl_weights, ol_weights = updateWeights()
        print(f"NEW Weights:\n\tHidden layer weights:\n{hl_weights}\n\tOuter layer weights:\n{ol_weights}\n")

        error_value = calculateNextError(error_value)
        print(f"MAX error value: {max_error_value}\nCurrent error value: {error_value}")
        dt_index += 1

    count += 1
    # learning_step = decreaseLearningStep(learning_step)
    if error_value < max_error_value:
        break
    # time.sleep(0.5)
print(f"Solution found after {count} iterations")

print_dataset = [[45, 85], [50, 43], [40, 80], [187, 107], [55, 42], [200, 43], [48, 40], [195, 41],
                 [43, 87], [192, 105], [190, 40], [188, 100]]

print(f"For the dataset:\n{print_dataset}\n We have:")
time.sleep(4)
for i in range(0, len(dataset)):
    hl_output = GetHLOutput(dataset[i], hl_weights)
    ol_output = GetOLOutput(hl_output, ol_weights)
    print(f"Subset {print_dataset[i]}:\nWanted output:\n{wanted_output[i]}\nActual output:\n{ol_output}\n")
    time.sleep(2)
