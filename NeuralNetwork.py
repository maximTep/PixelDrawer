import numpy as np
import random
import math


class NeuralNetwork:
    def __init__(self):
        self.layers = []
        self.weights = []
        self.biases = []

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def size_of_layers(self):
        return len(self.layers)

    def add_layer(self, layer: np.ndarray):
        self.layers.append(layer)
        self.weights.append([])
        self.biases.append([])

    def rand_weights(self, lay_num):
        if lay_num == 0:
            raise ValueError('No previous layer')
        weights = np.ndarray(shape=(len(self.layers[lay_num]), len(self.layers[lay_num - 1])))
        for i in range(len(self.layers[lay_num])):
            for j in range(len(self.layers[lay_num - 1])):
                weights[i][j] = random.randint(-20, 20) / random.randint(1, 5)
        self.weights[lay_num] = weights

    def rand_biases(self, lay_num):
        biases = np.ndarray(shape=(len(self.layers[lay_num])))
        for i in range(len(self.layers[lay_num])):
            biases[i] = random.randint(-20, 20) / random.randint(1, 5)
        self.biases[lay_num] = biases

    def rand_all_weights(self):
        for i in range(1, len(self.layers)):
            self.rand_weights(i)

    def rand_all_biases(self):
        for i in range(1, len(self.layers)):
            self.rand_biases(i)

    def calculate_layer(self, lay_num):
        if lay_num == 0:
            raise ValueError('No previous layer')
        layer = np.dot(self.weights[lay_num], self.layers[lay_num - 1]) + self.biases[lay_num]
        for i in range(len(layer)):
            layer[i] = self.sigmoid(layer[i])
        self.layers[lay_num] = layer

    def calculate_all_layers(self):
        for i in range(1, len(self.layers)):
            self.calculate_layer(i)

    def save_settings(self):
        f = open('NeuralSettings.txt', 'w')
        f.write(str(len(self.weights)) + '\n')

        for i in range(1, len(self.weights)):
            f.write(str(len(self.weights[i])) + ' ' + str(len(self.weights[i][0])) + '\n')
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    f.write(str(self.weights[i][j][k]) + ' ')
                f.write('\n')
            f.write('\n')

        for i in range(1, len(self.biases)):
            f.write(str(len(self.biases[i])) + '\n')
            for j in range(len(self.biases[i])):
                f.write(str(self.biases[i][j]) + ' ')
            f.write('\n')


        f.close()

    def set_settings(self, file_name: str):
        f = open(file_name, 'r')
        num_of_layers = 0
        lines = f.read().split('\n')
        i = 0
        while i < len(lines):
            if lines[i] == ' ':
                lines.pop(i)
            else:
                i += 1
        it = 0
        num_of_layers = int(lines[0])
        it += 1
        for i in range(1, num_of_layers):
            n, m = map(int, lines[it].split(' '))
            new_weight = np.ndarray(shape=(n, m))
            it += 1
            for j in range(n):
                nums_in_row = lines[it].split(' ')
                nums_in_row.pop()
                row = list(map(float, nums_in_row))
                it += 1
                for k in range(m):
                    new_weight[j][k] = row[k]
            self.weights[i] = new_weight
            it += 1
        for i in range(1, num_of_layers):
            n = int(lines[it])
            new_bias = np.ndarray(shape=n)
            it += 1
            nums_in_row = lines[it].split(' ')
            nums_in_row.pop()
            row = list(map(float, nums_in_row))
            it += 1
            for j in range(n):
                new_bias[j] = row[j]
            self.biases[i] = new_bias




        f.close()






