import csv
import numpy as np

data_set = []

# exercise 1
with open('iris.data') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if len(row) == 5:
            data_set.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])

data_array = np.array(data_set)
print(data_array)

col_min_array = []
col_max_array = []
col_average_array = []
col_median_array = []

# exercise 2
for i in range(0, 4):
    col_min_array.append(np.min(data_array[:, i]))
    col_max_array.append(np.max(data_array[:, i]))
    col_average_array.append(np.median(data_array[:, i]))
    col_median_array.append(np.average(data_array[:, i]))

print("\nMin values of corresponding columns:", col_min_array)
print("\nMax values of corresponding columns:", col_max_array)
print("\nAverage values of corresponding columns:", col_average_array)
print("\nMedian values of corresponding columns:", col_median_array)

# exercise 3
normed_data_set = np.array([])
for i in range(0, 4):
    normed_data_set = (data_array[:, i] - min(data_array[:, i])) / (max(data_array[:, i]) - min(data_array[:, i]))

print("\nThe data set with each column normed value: \n", normed_data_set)

# exercise 4
weights_array = [0.2, 1.1, -0.9, 1]

new_column_array = []

print("New columns to be added:")
for i in range(0, np.shape(data_array)[0]):
    row_sum = 0
    for j in range(0, 4):
        row_sum += row_sum + data_array[i][j] * weights_array[j]
    new_column_array.append(row_sum)
    print("[%s]" % row_sum)

print("New data set with added column:")

new_data_set = np.array(new_column_array)
new_data_array = np.insert(data_array, 0, new_data_set, axis=1)

print(new_data_array)

#exercise 5
