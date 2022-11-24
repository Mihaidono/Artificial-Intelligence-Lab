import numpy as np

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

population_array=np.array()
