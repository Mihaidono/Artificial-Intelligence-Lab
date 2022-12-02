import numpy as np

weight_array = np.array([0, 1, 0])

values_array = np.array([[2, 1, -1], [0, -1, -1]])

response_array = np.array([-1, 1])

learning_step = 0.1

# these values I will use for testing
# weight_array = np.array([1, -1, 0, 0.5])

# values_array = np.array([[1, -2, 0, -1], [0, 1.5, -0.5, -1], [-1, 1, 0.5, -1]])

# response_array = np.array([-1, -1, 1])

print("For values:\n", values_array, "\nWe have:\n the responses:\n ",
      response_array, "\n the weights:\n ", weight_array)

iteration_count = 1

iterations_wanted = 2  # change this, so it will iterate through all 3 net values again and again

while iteration_count <= iterations_wanted:
    print("For iteration ", iteration_count, " we have these net values:")
    print("Weight array at the beginning: ", weight_array)
    for i in range(0, len(values_array)):
        net = np.dot(weight_array, values_array[i])
        print("\tNet", i + 1, ": %.1f" % net)
        if np.sign(net) != response_array[i]:
            # here we correct the weight array if the output does not match with the response we have using the
            # perceptron learning rule -> changing the weight considering the wanted response and actual response
            weight_array = weight_array + learning_step * (response_array[i] - np.sign(net)) * values_array[i]
        # print("Weight array after calculating net value: ", weight_array)
    iteration_count += 1
