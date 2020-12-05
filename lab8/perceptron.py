import numpy as np
import load_csv


class Perceptron:
    def __init__(self, eta, epochs):
        self.eta = eta
        self.epochs = epochs
        self.error_list = []
        self.weights = None

    def predict(self, vector):
        total_stimulation = np.dot(vector, self.weights)
        if total_stimulation > 0:
            y_predict = 1
        else:
            y_predict = 0
        return y_predict

    def train(self, x, y):
        self.error_list = []
        ones = np.ones((x.shape[0], 1))
        x_1 = np.append(x.copy(), ones, axis=1)
        self.weights = np.random.rand(x_1.shape[1])

        for e in range(self.epochs):
            errors_counter = 0
            for x, y_target in zip(x_1, y):
                y_predict = self.predict(x)
                delta_w = self.eta * (y_target - y_predict) * x
                self.weights += delta_w
                errors_counter += 1 if y_target != y_predict else 0

            self.error_list.append(errors_counter)
            print("Epoch: {} \n weights: {} \n number of errors {} \n".format(
                e, self.weights, errors_counter))


a, b = load_csv.load_data("sample1.csv", ";", -1)
c, d, e, f = load_csv.divide_data_to_train_and_test(a, b, 30)

perceptron = Perceptron(0.1, 1000)
perceptron.train(c, d)

print(perceptron.predict(np.array([[20, 26, -2, 23, 14, -11, 14, 22, 1]])))
