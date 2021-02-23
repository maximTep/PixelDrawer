from NeuralNetwork import *
import pygame
import numpy as np


def pixel_reader(image_: pygame.Surface, H, W, scale):
    grid_ = [[image_.get_at([y * scale, x * scale])[0] / 255 for x in range(W // scale)] for y in range(H // scale)]
    return grid_


def matrix_to_array(matrix: np.ndarray):
    n_ = len(matrix)
    m_ = len(matrix[0])
    lst = [matrix[i][j] for j in range(m_) for i in range(n_)]
    arr = np.ndarray(shape=n_ * m_)
    for i in range(n_ * m_):
        arr[i] = lst[i]
    return arr




image = pygame.image.load('Data\\0-0.png')
grid = pixel_reader(image, 300, 300, 10)
pixels = matrix_to_array(grid)

NN = NeuralNetwork()

NN.add_layer(pixels)
NN.add_layer(np.zeros(shape=16))
NN.add_layer(np.zeros(shape=16))
NN.add_layer(np.zeros(shape=10))


# NN.rand_all_weights()
# NN.rand_all_biases()
#
# # print(NN.weights[1])
# NN.calculate_all_layers()
#
# result = np.argmax(NN.layers[-1])
# #print(result)
# # NN.save_settings()
NN.set_settings('NeuralSettings.txt')

print(NN.biases)




