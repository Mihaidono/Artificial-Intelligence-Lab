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
                aux_sum += card_value_array[j]
            else:
                aux_prod *= card_value_array[j]
        sp_array.append(objective_function(aux_sum, aux_prod))
    return sp_array


def SortSelectionProbabilityResults(ppl_array, sp_array):
    # both population array and selection probability array are the same size
    for i in range(0, len(sp_array) - 1):
        for j in range(i + 1, len(sp_array)):
            if sp_array[i] > sp_array[j]:
                aux_sp = sp_array[i]
                aux_ppl = ppl_array[i]
                # went for a classic sorting, so I can sort in parallel the first array considering the second one
                sp_array[i] = sp_array[j]
                ppl_array[i] = ppl_array[j]

                sp_array[j] = aux_sp
                ppl_array[j] = aux_ppl
    return ppl_array, sp_array


# for this card game we want to split the deck into 2 and sum the first half and make it as close as
# this input variable:
print("The values must be !Integers!")
print("Enter the sum you want the first half to have: ")
wanted_sum = int(input())
# and this input variable will be the product of the other half of the deck:
print("Enter the product you want the second half to have: ")
wanted_prod = int(input())

card_value_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # array for the values of the cards I'm about to use in the game


# the following function rates how close the values we found are to the wanted ones
# the closer to 0 the return is the better the results, 0 meaning the actual solution

def objective_function(sum_array, mult_array):
    return abs(np.sum(sum_array) - wanted_sum) / wanted_sum + abs(np.prod(mult_array) - wanted_prod) / wanted_prod


# now I generate as many rows in an array as the population size variable
# those rows are binary arrays with random generated values of 1 and 0

population_size = 50  # change this to change the number of elements in the array

population_array = formPopulationArray(population_size)

selection_prob_array = GetSelectionProbabilityArray(population_array)
# for testing:
print(population_array)
print("\n", selection_prob_array)
# ordering the arrays considering the best results:
population_array, selection_prob_array = SortSelectionProbabilityResults(population_array, selection_prob_array)
# for testing:
print(population_array)
print("\n", selection_prob_array)
# now I'm going to cut off some members of the population for the selection

population_array.pop(len(population_array))
selection_prob_array.pop(len(selection_prob_array))

population_array.pop(len(population_array))
selection_prob_array.pop(len(selection_prob_array))
# cut the last 2 elements off of the selection probability and population array which are consistent with one another


