import numpy as np


def bipolar_function(x):
    return 2 / (1 + np.exp(-x)) - 1


learning_step = 0.1  # change this for more iterations and more accurate results

max_error_value = 0.001  # change this to modify the accuracy of the output
