import csv
import numpy as np


def load_data(path, delimit, label_col):
    with open(path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimit)
        data_matrix = np.asarray([row for row in csvreader], dtype=float)
        data_matrix_without_labels = np.delete(data_matrix, label_col, 1)
        matrix_labels = data_matrix[:, label_col]
    return data_matrix_without_labels, matrix_labels


def number_of_columns(data_matrix):
    return data_matrix.shape[1]


def number_of_rows(data_matrix):
    return data_matrix.shape[0]


def normalize_column(number, data_matrix):
    col_min = data_matrix[:, number].min()
    col_max = data_matrix[:, number].max()

    if(col_max - col_min) != 0:
        i = 0
        for v in data_matrix[:, number]:
            data_matrix[:, number][i] = (v - col_min) / (col_max - col_min)
            i += 1


def normalize_all_rows(data_matrix):
    for i in range(number_of_columns(data_matrix)):
        normalize_column(i, data_matrix)


def center_column(number, data_matrix):
    col_mean = data_matrix[:, number].mean()

    i = 0
    for _ in data_matrix[:, number]:
        data_matrix[:, number][i] -= col_mean
        i += 1


def center_all_rows(data_matrix):
    for i in range(number_of_columns(data_matrix)):
        center_column(i, data_matrix)


def divide_data_to_train_and_test(data_matrix, labels,  how_many_rows_to_train):
    rows_to_train = data_matrix[:how_many_rows_to_train]
    rows_to_test = data_matrix[how_many_rows_to_train:]

    labels_rows_to_train = labels[:how_many_rows_to_train]
    labels_rows_to_test = labels[how_many_rows_to_train:]

    return rows_to_train, labels_rows_to_train, rows_to_test, labels_rows_to_test
