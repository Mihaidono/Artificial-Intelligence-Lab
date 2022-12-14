import csv
import random
import matplotlib.pyplot as plt
import numpy as np


def GetDataFromFile():
    obs_values_x = []
    obs_values_y = []
    with open("./Salary_Data.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            obs_values_x.append(float(row[0]))
            obs_values_y.append(float(row[1]))
    return np.array(obs_values_x), np.array(obs_values_y)


def GetFunctionForW1(w1, w2):
    sum = 0.0
    for i in range(0, len(x_observed_values)):
        sum += (y_observed_values[i] - (w1 * x_observed_values[i] + w2)) * x_observed_values[i]

    ans = (-1 / len(x_observed_values)) * sum
    return ans


def GetFunctionForW2(w1, w2):
    sum = 0
    for i in range(0, len(x_observed_values)):
        sum += (y_observed_values[i] - (w1 * x_observed_values[i] + w2))

    ans = (-1 / len(x_observed_values)) * sum
    return ans


def plot_regression_line(x, y):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="b",
                marker="o", s=30)

    # predicted response vector
    y_predicted = next_value_w1 * x + next_value_w2

    # plotting the regression line
    plt.plot(x, y_predicted, color="r")

    # putting labels
    plt.xlabel('YearsExperience[x]')
    plt.ylabel('Salary[y]')

    plt.xlim([0, int(x_observed_values[len(x_observed_values) - 1]) + 2])
    plt.ylim([0, int(y_observed_values[len(y_observed_values) - 1]) + 20])
    # function to show plot
    plt.show()


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
    number_of_iterations += 1

    next_value_w1 = initial_value_w1 - learning_step * (GetFunctionForW1(initial_value_w1, initial_value_w2))

    next_value_w2 = initial_value_w2 - learning_step * (GetFunctionForW2(initial_value_w1, initial_value_w2))

    if abs(next_value_w1 - initial_value_w1) < threshold_value and abs(
            next_value_w2 - initial_value_w2) < threshold_value:
        break
    initial_value_w1 = next_value_w1
    initial_value_w2 = next_value_w2

print(f"Final values after {number_of_iterations} iterations:\nw1 = {next_value_w1}\nw2 = {next_value_w2}")

plot_regression_line(x_observed_values, y_observed_values)
