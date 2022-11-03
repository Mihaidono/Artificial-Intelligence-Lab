import numpy as np


# exercise 1

def continuous_function(var):
    return (1 - np.exp(-var)) / (1 + np.exp(-var))


weights_array = np.array([1, -1, 0, 0.5])

entries = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])

for id in range(0, len(entries)):
    net = np.dot(entries[id], weights_array)
    print(f"\n{id + 1} Iteration net:", net)
    print("before", weights_array)
    weights_array = np.add(weights_array, np.multiply(np.sign(net), entries[id]))
    print("after", weights_array)

weights_array = np.array([1, -1, 0, 0.5])

entries = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])
for itr in range(0, 20):
    print(f"\n=====Time gone through the set: {itr + 1}=====\n")
    for id in range(0, len(entries)):
        net = np.dot(entries[id], weights_array)
        print(f"\n{id + 1} Iteration net: %.3f" % continuous_function(net))
        print("before", weights_array)
        weights_array = np.add(weights_array, np.multiply(continuous_function(net), entries[id]))
        print("after", weights_array)
