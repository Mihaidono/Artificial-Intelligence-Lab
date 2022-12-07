import random

import numpy as np


def formRandomBinaryArray(length):
    binary_array = []
    for i in range(0, length):
        binary_array.append(random.randint(0, 1))
    return binary_array


def formPopulationArray(length):
    ppl_array = []
    for i in range(0, length):
        ppl_array.append(formRandomBinaryArray(10))
    return ppl_array


def GetSelectionProbabilityArray(ppl_array):
    sp_array = []
    for i in range(0, len(ppl_array)):
        aux_array = ppl_array[i]
        aux_sum = 0
        aux_prod = 1
        for j in range(0, len(aux_array)):
            if aux_array[j] == 0:
                aux_sum += aux_array[j]
            else:
                aux_prod *= aux_array[j]
        sp_array.append(objective_function(aux_sum, aux_prod))
    return sp_array


# for this card game we want to split the deck into 2 and sum the first half and make it as close as
# this input variable:
print("The values must be !Integers!")
print("Enter the sum you want the first half to have: ")
wanted_sum = int(input())
# and this input variable will be the product of the other half of the deck:
print("Enter the product you want the second half to have: ")
wanted_prod = int(input())


# the following function rates how close the values we found are to the wanted ones
# the closer to 0 the return is the better the results, 0 meaning the actual solution

def objective_function(sum_array, mult_array):
    return abs(np.sum(sum_array) - wanted_sum) / wanted_sum + abs(np.prod(mult_array) - wanted_prod) / wanted_prod


# now I generate as many rows in an array as the population size variable
# those rows are binary arrays with random generated values of 1 and 0

population_size = 50  # change this to change the number of elements in the array

population_array = np.array(formPopulationArray(population_size))

selection_prob_array = np.array(GetSelectionProbabilityArray(population_array))
