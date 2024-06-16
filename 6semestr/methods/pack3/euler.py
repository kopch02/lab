import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# euler mod, runge, mhogoshag(любой из 2)(после 4 шагов рунге берется 5ая точка)


def y_strikh(x, y):
    return np.e ** x * y ** 2 - 2 * y


def y_toch(x, y):
    return (np.e ** (-2 * x)) / (1 + np.e ** -x)


def euler2(x_values, y_values, x1, y1):
    for _ in range(n + 1):
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


y1 = 1 / 2
x_range = [0, 2]
x1 = x_range[0]
n = 10
h = (x_range[1] - x_range[0]) / n

y_values = []
x_values = []
y_t_values = []



euler2(x_values, y_values, x1, y1)
