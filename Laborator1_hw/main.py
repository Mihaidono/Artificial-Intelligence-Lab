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

# exercise 5

binary_numbers_file = open("optdigits-orig.tra")
# skip first 22 lines in the file
for i in range(0, 21):
    print(binary_numbers_file.readline())


def checkValues(value1, value2, value3, value4):
    counter = 0
    value_vector = [value1, value2, value3, value4]
    for value in value_vector:
        if value == '0':
            counter += 1
    if counter > 2:
        return '0'
    return '1'


def scaleFunction(binary_number_array):
    new_binary_number_array = []
    for row in range(0, 32, 2):
        new_row = []
        for column in range(0, 32, 2):
            new_row.append(checkValues(binary_number_array[row][column], binary_number_array[row][column + 1],
                                       binary_number_array[row + 1][column], binary_number_array[row + 1][column + 1]))
        new_binary_number_array.append(new_row)
    return new_binary_number_array


def imageToString(binary_image):
    new_string = ""
    for row in binary_image:
        for character in row:
            new_string += character
        new_string += "\n"
    return new_string


counter = 1
binary_number_array = []

new_file = open("newBinaryFile.txt", "w")
new_file.close()

for line in binary_numbers_file:
    if len(line) < 31:
        new_file = open("newBinaryFile.txt", "a")
        new_line = "\n->" + line
        new_file.write(new_line)
        new_file.close()
        continue

    row = []
    for i in range(0, len(line) - 1):
        row.append(line[i])
    binary_number_array.append(row)

    if counter % 32 == 0:
        new_file = open("newBinaryFile.txt", "a")
        new_file.write(imageToString(scaleFunction(binary_number_array)))
        new_file.close()

        binary_number_array = []
    counter += 1
binary_numbers_file.close()
