import numpy as np


class MyExaption(Exception):
    pass


def funk1(x, y):
    return np.sin(x + 1) - y - 1.2


def funk2(x, y):
    return 2 * x + np.cos(y) - 2


def fi1(x):
    return np.sin(x + 1) - 1.2


def fi2(y):
    return (np.cos(y) - 2) / -2


def fi1_pr_x(x):
    return abs(np.cos(x + 1))


def fi1_pr_y(y):
    return 0


def fi2_pr_x(x):
    return 0


def fi2_pr_y(y):
    return abs(np.sin(y) / 2)

print("Метод простой итерации")
f1 = "sin(x + 1) - y = 1.2"
f2 = "2 * x + cos(y) = 2"
print(f"{f1 = }")
print(f"{f2 = }")
Fi1 = "np.sin(x + 1) - 1.2"
Fi2 = "(np.cos(y) - 2) / -2"
print(f"{Fi1 = }")
print(f"{Fi2 = }")

x = np.pi / 6
y = -0.18
print(f"начальный {x = }")
print(f"начальный {y = }")
a = np.pi / 9
b = 2 * np.pi / 9
c = -0.15
d = -0.25

#print((b - a) * abs(d - c))

Eps = 10 ** -12
print(f"{Eps = }")
count = 0
while True:
    count += 1
    new_x = fi2(y)
    new_y = fi1(x)
    p1 = (fi1_pr_x(new_x) + fi1_pr_y(new_y)) < 1 and (fi2_pr_x(new_x) + fi2_pr_y(new_y)) < 1
    if not(p1) :
        raise MyExaption(new_x, new_y)
    if (abs(x - new_x) < Eps) and (abs(y - new_y) < Eps):
        break

    x = new_x
    y = new_y

print(f"{new_x = }")
print(f"{new_y = }")
print(f"{count = }")

print(f"Проверка 1:{funk1(new_x,new_y)}")
print(f"Проверка 2:{funk2(new_x, new_y)}")
