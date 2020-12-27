import cv2
import numpy as np


def mean_square_error(_input, _output):
    difference = cv2.subtract(_input, _output)
    squared_difference = cv2.pow(difference, 2)

    return np.sum(squared_difference)
