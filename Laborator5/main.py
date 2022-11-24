import math
import random

import numpy as np

epoch_number = 5  # switch this one for how many times you want the dataset to be iterated through

learning_step = 0.1  # switch this one for the accuracy of the learning step, the lower the value, the better

dataset_array = [[45, 85], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41], [43, 87], [190, 40]]

dataset_array = np.array(dataset_array)

min_x_axis = dataset_array.min(axis=0)[0]
max_x_axis = dataset_array.max(axis=0)[0]

min_y_axis = dataset_array.min(axis=0)[1]
max_y_axis = dataset_array.max(axis=0)[1]

# calculated the prototypes' axis coordinates considering the min and max values of each axis to have the
# prototype in range of the nodes

prototype1 = [random.randint(min_x_axis, max_x_axis), random.randint(min_y_axis, max_y_axis)]
prototype2 = [random.randint(min_x_axis, max_x_axis), random.randint(min_y_axis, max_y_axis)]
prototype3 = [random.randint(min_x_axis, max_x_axis), random.randint(min_y_axis, max_y_axis)]

prototypes = [prototype1, prototype2, prototype3]

print("Original set for the random generated prototypes: ", prototypes)
# going through the epochs
for i in range(0, epoch_number):
    for j in range(0, len(dataset_array)):
        distance = []
        for k in range(0, len(prototypes)):
            distance.append(math.sqrt(
                pow(dataset_array[j][0] - prototypes[k][0], 2) + pow(dataset_array[j][1] - prototypes[k][1], 2)))
        winner_prototype = prototypes[distance.index(np.min(distance))]
        # print("array :", prototypes, " -->\n", winner_prototype, " is the winner prototype")
        # print("array diff between\n", dataset_array[j], "\nand\n", winner_prototype, "\nis\n",
        #     dataset_array[j] - winner_prototype, "\nlearning step*dif is\n",
        #     learning_step * (dataset_array[j] - winner_prototype), "\nresult is\n",
        #    winner_prototype + learning_step * (dataset_array[j] - winner_prototype))
        winner_prototype = winner_prototype + learning_step * (dataset_array[j] - winner_prototype)
        prototypes[distance.index(np.min(distance))] = winner_prototype
        # print(" new array: ", prototypes)
        # lines commented for debug in console

app_array = [[], [], []]
for j in range(0, len(dataset_array)):
    distance = []
    for k in range(0, len(prototypes)):
        distance.append(math.sqrt(
            pow(dataset_array[j][0] - prototypes[k][0], 2) + pow(dataset_array[j][1] - prototypes[k][1], 2)))
    app_array[distance.index(np.min(distance))].append(dataset_array[j])

print("New prototypes: ", prototypes)
print("For the updated prototype set:")
for i in range(0, len(app_array)):
    print("For prototype ", i, " belong: ", app_array[i])
