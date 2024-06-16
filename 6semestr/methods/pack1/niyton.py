import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return x ** 3 - 6 * x - 8


def der_func(x):
    return 3 * (x ** 2) - 6 


def der_func2(x):
    return 6 * x


E = 10 ** -12

x_values = np.arange(-5, 5, 0.1)
y_values = func(x_values)

a = 2.5
b = 3.5  # changed

print(f"{func(a) = }")
print(f"{func(b) = }")
print(f"{der_func2(a) = }")
print(f"{der_func2(b) = }")

print(f"{func(a) * der_func2(a) = }")
print(f"{func(b) * der_func2(b) = }")

x = a

count = 0
print("func = x ** 3 - 6 * x - 8")
print("Метод Ньютона")
print(f"{a = }")
print(f"{b = }")
print(f"{E = }")

while True:
    count += 1

    x_1 = x - func(x) / der_func(x)

    if np.abs(x - x_1) <= E:
        break
    x = x_1


print(f"{count = }")
print(f"{x = }")
print(f"{func(x) = }")

# plt.grid(True)
# plt.plot(x_values, y_values)

# plt.show()
