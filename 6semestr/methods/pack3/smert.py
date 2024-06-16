import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# euler mod, runge, mhogoshag(любой из 2)(после 4 шагов рунге берется 5ая точка)


def y_strikh(x, y):
    return x * np.e**(-x**2) - 2 * x * y


def y_toch(x, y):
    return np.e**(-x**2) * (1 / 2 * x**2)


def euler2(x_values, y_values, x1, y1):
    for _ in range(n):
        y_values.append(y1)
        x_values.append(x1)
        y_t_values.append(y_toch(x1, y1))
        old_y1 = y1
        new_y1 = y1 + h * y_strikh(x1, y1)

        y1 = old_y1 + h / 2 * (y_strikh(x1, old_y1) + y_strikh(x1 + h, new_y1))

        x1 += h

    R = [np.abs(y_t_values[i] - y_values[i]) for i in range(len(y_values))]

    df = pd.DataFrame([x_values, y_values, y_t_values, R],
                      index=["x", "y", "y_t", "R"]).T

    print(df)


def runge(x_values, y_values, x1, y1):

    for _ in range(n):
        y_values.append(y1)
        x_values.append(x1)
        y_t_values.append(y_toch(x1, y1))
        k = [h * y_strikh(x1, y1)]  # k1
        k.append(h * y_strikh(x1 + h / 2, y1 + k[0] / 2))  # k2
        k.append(h * y_strikh(x1 + h / 2, y1 + k[1] / 2))  # k3
        k.append(h * y_strikh(x1 + h, y1 + k[2]))  # k4
        q = 4

        y1 += 1 / 6 * (k[0] + 2 * (k[1] + k[2]) + k[3])
        x1 += h

    R = [np.abs(y_t_values[i] - y_values[i]) for i in range(len(y_values))]

    df = pd.DataFrame([x_values, y_values, y_t_values, R],
                      index=["x", "y", "y_t", "R"]).T

    print(df)


def mhogoshaque(x, y):
    pass


y1 = y2 = 0
x_range = [0, 1]
x1 = x2 = x_range[0]
n = 8
h = (x_range[1] - x_range[0]) / n

y_values = []
x_values = []
y_t_values = []

euler2(x_values, y_values, x1, y1)
runge(x_values, y_values, x2, y2)
