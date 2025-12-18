import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2 - 25 / 16


zeros = np.array([5 / 4, -5 / 4])

x_values = np.linspace(-2, 2, 400)
y_values = f(x_values)

plt.figure(figsize=(8, 6))
