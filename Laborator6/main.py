import random

import numpy as np


def formCluster(dictionary):


def checkCentroids(centroid_array):


number_of_clusters = 3
# usually it needs to be calculated but for this
# example I already knew how many clusters there are

node_array = [[45, 85], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41], [43, 87], [190, 40]]
node_array = np.array(node_array)

# initialized the nodes to be clustered
centroid_array = []
last_rand = -1
while True:
    new_rand = random.randint(0, len(node_array) - 1)
    if last_rand is not new_rand:
        centroid_array.append(node_array[new_rand])
        last_rand = new_rand
    if len(centroid_array) == number_of_clusters:
        break

countIsSame = 0  # check if the centroids change, if they don't then I found the clusters
while countIsSame < 3:  # chose a random value for the number of comparisons
    clusters = {}
    for i in range(0, len(node_array)):
        print("Centroids chosen for this iteration: ", centroid_array)
        cluster_value = []
        for j in range(0, number_of_clusters):
            cluster_value.append(
                abs(centroid_array[j][0] - node_array[i][0]) + abs(centroid_array[j][1] - node_array[i][1]))
            # finding out who the closest centroid is by storing the distance of the point from all the centroids
        clusters[cluster_value.index(np.min(cluster_value))] = node_array[i]
        # stored the value using the index of the centroid as identification for the clusters
    # de implementat: in functie de indexu pe care il au datele in dictionar trebuie sa fac o medie sa aflu noii centroizi
