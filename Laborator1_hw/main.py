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
for i in range(0, 4):
    normed_data_set = (data_array[:, i] - min(data_array[:, i])) / (max(data_array[:, i]) - min(data_array[:, i]))
print("\nThe data set with each column normed value: \n", normed_data_set)
