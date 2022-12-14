import csv
import random
import numpy as np


def GetDataFromFile():
    obs_values_x = []
    obs_values_y = []
    with open("./Salary_Data.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            obs_values_x.append(row[0])
            obs_values_y.append(row[1])
    return obs_values_x, obs_values_y


x_observed_values, y_observed_values = GetDataFromFile()

print("x values from csv:", x_observed_values, "\ny values from csv:", y_observed_values)

learning_step = 0.01

threshold_value = 0.0001
# both the learning step and threshold value are important factors for the accuracy of the results
# the lower the learning step the closer to a good result it can come
# the lower the threshold the less of an error between the wanted answer and actual answer will be

initial_value_w1 = random.uniform(0.0, 100.0)
initial_value_w2 = random.uniform(0.0, 100.0)

next_value_w1 = 0
next_value_w2 = 0
print("For the error function E(w1,w2)=(1/2n)*(SUM1->n(yi-(w1xi+w2))^2)")
number_of_iterations = 1
while True:
    print("Iteration ", number_of_iterations)
    number_of_iterations += 1

    next_value_w1 = initial_value_w1 - learning_step * ( )

    next_value_w2 = initial_value_w2 - learning_step * ( )

    if abs(next_value_w1 - initial_value_w1) < threshold_value and abs(
            next_value_w2 - initial_value_w2) < threshold_value:
        break
    initial_value_w1 = next_value_w1
    initial_value_w2 = next_value_w2
