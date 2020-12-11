import numpy as np
import load_csv


def create_new_matrix(x):   # nieczytelna nazwa
    ones = np.ones((x.shape[0], 1))
    x_1 = np.append(x.copy(), ones, axis=1)
    return x_1


class Perceptron:
    def __init__(self, eta, epochs):    # warto dodawać wartości domyślne
        self.eta = eta
        self.epochs = epochs
        self.error_list = []
        self.weights = None

    def predict(self, vector):
        total_stimulation = np.dot(vector, self.weights)    # a gdzie bias?
        if total_stimulation > 0:
            y_predict = 1
        else:
            y_predict = 0
        return y_predict

    def train(self, x, y):
        self.error_list = []
        x_1 = create_new_matrix(x)
        self.weights = np.random.rand(x_1.shape[1])

        for e in range(self.epochs):
            errors_counter = 0
            for x, y_target in zip(x_1, y):
                y_predict = self.predict(x)
                delta_w = self.eta * (y_target - y_predict) * x # nie opłaciłoby się tego wciągnąć do if'a dwie linie dalej?
                self.weights += delta_w
                if y_target != y_predict:
                    errors_counter += 1
                else:
                    errors_counter = 0  # naprawdę?
            self.error_list.append(errors_counter)
            print("Epoch: {} \n weights: {} \n number of errors {} \n".format(
                e, self.weights, errors_counter))

    def test(self, x, y):
        errors_counter = 0
        x_1 = create_new_matrix(x)
        for x, y_target in zip(x_1, y):
            y_predict = self.predict(x)
            if y_target != y_predict:
                errors_counter += 1

        error_rate = errors_counter / len(x_1)

        return str(error_rate * 100) + '%'


data, labels = load_csv.load_data("sample1.csv", ";", -1)
train_data, train_labels, test_data, test_labels = load_csv.divide_data_to_train_and_test(data, labels, 60)

perceptron = Perceptron(0.2, 1000)
perceptron.train(train_data, train_labels)

print(perceptron.test(test_data, test_labels))
