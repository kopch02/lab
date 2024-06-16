import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from runge import get_runge123

# euler mod, runge, mhogoshag(любой из 2)(после 4 шагов рунге берется 5ая точка)


def y_strikh(x, y):
    return np.e ** x * y ** 2 - 2 * y


def y_toch(x, y):
    return (np.e ** (-2 * x)) / (1 + np.e ** -x)


y1 = 1 / 2
x_range = [0, 2]
x1 = x_range[0]
n = 20
h = (x_range[1] - x_range[0]) / n

y_values = []
x_values = []
y_t_values = []

runge_123 = get_runge123()
for i in range(3):
    x_values.append(x1)
    y_values.append(runge_123.iloc[i, 1])
    y_t_values.append(runge_123.iloc[i, 2])
    x1 += h


def adams(x_values, y_values, x1, y1):

    for i in range(2, n, 1):
        y1_p = y1 + h * (55. * y_strikh(x1, y1) - 59. *
                         y_values[i] + 37. * y_values[i - 1] - 9. * y_values[i - 2]) / 24.
        f1_p = y_strikh(x1 + h, y1_p)
        y1 = y1 + h * (9. * f1_p + 19. * y_strikh(x1, y1) -
                   5. * y_values[i] + y_values[i - 1]) / 24.

        y_values.append(y1)
        x1 += h
        x_values.append(x1)
        y_t_values.append(y_toch(x1, y1))

    R = [np.abs(y_t_values[i] - y_values[i]) for i in range(len(y_values))]

    df = pd.DataFrame([x_values, y_values, y_t_values, R],
                      index=["x", "y", "y_t", "R"]).T

    return df


def adams2(x_values, y_values, x1, y1):

    for i in range(2, n, 1):
        y1 += h * y_strikh(x1, y1)

        y_values.append(y1)
        x1 += h
        x_values.append(x1)
        y_t_values.append(y_toch(x1, y1))

    R = [np.abs(y_t_values[i] - y_values[i]) for i in range(len(y_values))]

    df = pd.DataFrame([x_values, y_values, y_t_values, R],
                      index=["x", "y", "y_t", "R"]).T

    return df


print(adams(x_values, y_values, x_values[2], y_values[2]))
