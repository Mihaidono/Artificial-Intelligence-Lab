import random

import numpy as np


def GetRandomPopulationMembers(ppl_size):
    it1 = random.randint(0, ppl_size - 1)
    while True:
        it2 = random.randint(0, ppl_size - 1)
        if it2 != it1:
            break
    return it1, it2


def mutatePopulation(ppl_array, member_number):
    index_array = [random.randint(0, len(ppl_array) - 1)]
    while True:
        rand = random.randint(0, len(ppl_array) - 1)
        for index in index_array:
            if index == rand:
                continue
        index_array.append(rand)
        if len(index_array) == member_number:
            break

    for index in index_array:
        rand = random.randint(0, len(card_value_array) - 1)
        if ppl_array[index][rand] == 0:
            ppl_array[index][rand] = 1
        else:
            ppl_array[index][rand] = 0

    return ppl_array


def crossOver(array1, array2):
    aux_array1 = []
    aux_array2 = []

    for i in range(0, int(len(array1) / 2)):
        aux_array1.append(array1[i])
        aux_array2.append(array2[i])
    for i in range(int(len(array1) / 2), len(array1)):
        aux_array1.append(array2[i])
        aux_array2.append(array1[i])

    return aux_array1, aux_array2


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

generation_count = 100  # change this to change how many times the algorithm is repeated for a data set
count = 1
population_array = formPopulationArray(population_size)
while count <= generation_count:
    found = 0
    selection_prob_array = GetSelectionProbabilityArray(population_array)
    # for testing:
    # print(population_array)
    # print("\n", selection_prob_array)
    # ordering the arrays considering the best results:
    population_array, selection_prob_array = SortSelectionProbabilityResults(population_array, selection_prob_array)
    # for testing:
    # print(population_array)
    # print("\n", selection_prob_array)
    # now I'm going to cut off some members of the population for the selection

    population_array.pop(len(population_array) - 1)
    selection_prob_array.pop(len(selection_prob_array) - 1)

    population_array.pop(len(population_array) - 1)
    selection_prob_array.pop(len(selection_prob_array) - 1)
    # cut the last 2 elements off of the selection probability and population array which are consistent with one another

    population_array.append(population_array[0])
    selection_prob_array.append(selection_prob_array[0])

    population_array.append(population_array[1])
    selection_prob_array.append(selection_prob_array[1])

    print(f"The best card arrangement for iteration{count} is:{population_array[0]}")
    aux_array = population_array[0]
    aux_sum = 0
    aux_prod = 1
    for j in range(0, len(aux_array)):
        if aux_array[j] == 0:
            aux_sum += card_value_array[j]
        else:
            aux_prod *= card_value_array[j]
    if wanted_sum == aux_sum and wanted_prod == aux_prod:
        print(f"Sum is {aux_sum}, product is {aux_prod}")
        found = 1
        break
    index1, index2 = GetRandomPopulationMembers(population_size)
    crossOver(population_array[index1], population_array[index2])  # cross over for two members

    population_array = mutatePopulation(population_array, 5)
    # I chose the number 5 just because. There was nothing else to it
    # Change number 5 to change how many members of the population mutate (one value changes from 0 to 1 or from 1 to 0)
    count += 1
if found == 0:
    print("Exact arrangement was not found")
