import random

import numpy as np


def printClustersFormed(cluster):
    print("Clusters formed:")
    for key, values in cluster.items():
        print("{} -> {}".format(key + 1, values))


def initMyDictionary(clusters_number):
    dictionary = {}
    for i in range(0, clusters_number):
        dictionary[i] = []
    return dictionary


def checkCentroids(old_centroids, new_centroids):
    for i in range(0, len(new_centroids)):
        if new_centroids[i][0] != old_centroids[i][0] or new_centroids[i][1] != old_centroids[i][1]:
            return -1  # returns -1 if the centroids have changed
    return 1  # returns 1 if the centroids are the same


def getNewCentroids(current_clusters):
    # current_clusters = {}
    new_centroids_array = []

    for key in current_clusters.keys():
        aux_array = np.array(current_clusters[key])

        if len(aux_array) == 0:
            new_centroids_array.append(np.array([0, 0]))
            continue

        avg_x = 0
        avg_y = 0
        for i in range(0, len(aux_array)):
            avg_x += aux_array[i][0]
            avg_y += aux_array[i][1]
        avg_x = int(avg_x / len(aux_array))
        avg_y = int(avg_y / len(aux_array))
        new_centroids_array.append(np.array([avg_x, avg_y]))
        # here I form the new centroids values using the cluster values

    return new_centroids_array


number_of_clusters = 3
# usually it needs to be calculated but for this
# example I already knew how many clusters there are

node_array = [[45, 85], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41], [43, 87], [190, 40]]
node_array = np.array(node_array)

print("Nodes we will cluster:\n", node_array)

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
last_centroids = centroid_array  # check if the centroids have changed during iterations
fail_safe = 1  # in case it doesn't find the correct centroids

print("Centroids chosen : ", centroid_array)
while countIsSame < 3 and fail_safe != 100:  # chose a random value for the number of comparisons
    clusters = initMyDictionary(number_of_clusters)
    for i in range(0, len(node_array)):
        cluster_value = []
        for j in range(0, number_of_clusters):
            cluster_value.append(
                abs(centroid_array[j][0] - node_array[i][0]) + abs(centroid_array[j][1] - node_array[i][1]))
            # finding out who the closest centroid is by storing the distance of the point from all the centroids
        clusters[cluster_value.index(np.min(cluster_value))].append(node_array[i])
        # stored the value using the index of the centroid as identification for the clusters
    printClustersFormed(clusters)
    centroid_array = getNewCentroids(clusters)
    print("\nNew centroid array: ", centroid_array)

    if checkCentroids(last_centroids, centroid_array) == 1:
        countIsSame += 1
    else:
        countIsSame = 0
    fail_safe += 1
