import numpy as np


def normalizeDataSet(dset):
    return (dset - dset.min(axis=0)) / (dset.max(axis=0) - dset.min(axis=0))


def bipolar_function(x):
    return 2 / (1 + np.exp(-x)) - 1


learning_step = 0.1  # change this for more iterations and more accurate results

max_error_value = 0.001  # change this to modify the accuracy of the output

dataset = np.array([[45, 85], [50, 43], [40, 80], [187, 107], [55, 42], [200, 43], [48, 40], [195, 41],
                    [43, 87], [192, 105], [190, 40], [188, 100]])

wanted_output = [1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1]

hl_weights = []

weights = []

dataset_array = normalizeDataSet(dataset)
dataset_array = np.hstack((dataset_array, np.full((len(dataset), 1), -1)))  # added the column of -1's
print("Normalized data set :\n", dataset_array)
