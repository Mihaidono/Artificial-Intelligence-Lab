# dataset: https://archive.ics.uci.edu/ml/datasets/Daphnet+Freezing+of+Gait
import numpy as np
import keras as K
import tensorflow.compat.v2 as tf
from keras import backend


class MyLogger(K.callbacks.Callback):
    def __init__(self, n):
        self.n = n  # print loss & acc every n epochs

    def on_epoch_end(self, epoch, logs={}):
        if epoch % self.n == 0:
            curr_loss = logs.get('loss')
            curr_acc = logs.get('accuracy') * 100
            print("epoch = %4d  loss = %0.6f  acc = %0.2f%%" % \
                  (epoch, curr_loss, curr_acc))


def create_data_files():
    initial_file = './initial_data.csv'

    all_data = np.loadtxt(initial_file, delimiter=',',
                          usecols=[1, 2, 3], dtype=np.int32)

    all_classes = [0, 1, 2]
    class_dict = dict()
    for current_class in all_classes:
        class_dict[current_class] = all_data[all_data[:, 3] == current_class, :]

    train_data = []
    validation_data = []
    for current_class in all_classes:

        total_rows = class_dict[current_class].shape[0]
        for row in range(total_rows):

            if np.random.randint(low=1, high=10) <= 2:
                validation_data.append(class_dict[current_class][row])
            else:
                train_data.append(class_dict[current_class][row])

    validation_data = np.array(validation_data, dtype=np.int32)
    train_data = np.array(train_data, dtype=np.int32)

    np.savetxt("validation_data.txt", validation_data, fmt="%d")
    np.savetxt("train_data.txt", train_data, fmt="%d")


def get_files_data():
    train_file = "./train_data.txt"
    validation_file = "./validation_data.txt"

    train_x = np.loadtxt(train_file, delimiter=',',
                         usecols=[0, 1, 2], dtype=np.float32)
    train_y_decoded = np.loadtxt(train_file, delimiter=',',
                                 usecols=[2], dtype=np.float32)

    validation_x = np.loadtxt(validation_file, delimiter=',',
                              usecols=[0, 1, 2], dtype=np.float32)
    validation_y_decoded = np.loadtxt(validation_file, delimiter=',',
                                      usecols=[2], dtype=np.float32)

    train_y = []
    validation_y = []

    for row in range(train_y_decoded.shape[0]):
        if train_y_decoded[row] == 0:
            train_y.append([1, 0, 0])
        elif train_y_decoded[row] == 1:
            train_y.append([0, 1, 0])
        else:
            train_y.append([0, 0, 1])

    train_y = np.array(train_y)

    for row in range(validation_y_decoded.shape[0]):
        if validation_y_decoded[row] == 0:
            validation_y.append([1, 0, 0])
        elif validation_y_decoded[row] == 1:
            validation_y.append([0, 1, 0])
        else:
            validation_y.append([0, 0, 1])

    validation_y = np.array(validation_y)

    return train_x, train_y, validation_x, validation_y


def create_model():
    # my_init = K.initializers.glorot_uniform(seed=1)
    model = K.models.Sequential()
    model.add(K.layers.Dense(units=8, input_dim=3,
                             activation='relu'))
    model.add(K.layers.Dense(units=10, activation='relu'))
    model.add(K.layers.Dense(units=8, activation='relu'))
    model.add(K.layers.Dense(units=3, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
    return model


def train_model(model, train_x, train_y, validation_x, validation_y):
    # print(train_x.shape, train_y.shape)
    max_epochs = 50
    my_logger = MyLogger(n=5)
    h = model.fit(train_x, train_y, batch_size=32,
                  epochs=max_epochs, verbose=0, callbacks=[my_logger])

    # 5. evaluate model
    np.set_printoptions(precision=4, suppress=True)
    eval_results = model.evaluate(validation_x, validation_y, verbose=0)
    print("\nLoss, accuracy on test data: ")
    print("%0.4f %0.2f%%" % (eval_results[0], eval_results[1] * 100))

    return model


def save_model(model):
    mp = "best_model.h5"
    model.save(mp)


def predict(model, input):
    print(input.shape)
    pred = model.predict(input)
    print("\nPredicting the label for: ")
    print(input)
    print("Scores for classes:")
    print(pred)


if __name__ == "__main__":
    # se ruleaza doar daca nu exista cele doua fisiere
    # create_data_files()

    model = create_model()

    train_x, train_y, validation_x, validation_y = get_files_data()
    model = train_model(model, train_x, train_y, validation_x, validation_y)

    predict(model, np.array([[5, -5, 0.3]], dtype=np.int32))
