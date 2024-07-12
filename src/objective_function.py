# src/objective_function.py

import numpy as np

def rastrigin_function(x):
    A = 10
    n = len(x)
    return A * n + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])

def inverted_rastrigin_function(x):
    A = 10
    n = len(x)
    # Rastrigin function definition
    rastrigin_value = A * n + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])
    # Invert the function and set the maximum to 60
    inverted_value = 60 - rastrigin_value
    return inverted_value
