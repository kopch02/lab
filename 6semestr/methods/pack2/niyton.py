import numpy as np


def funk1(x, y):
    return np.sin(x + 1) - y - 1.2



def funk2(x, y):
    return 2 * x + np.cos(y) - 2


def funk1_pr_x(x):
    return np.cos(x + 1)

def funk1_pr_y(y):
    return -1

def funk2_pr_x(x):
    return 2

def funk2_pr_y(y):
    return -np.sin(y)

def J(x,y):
    return funk1_pr_x(x) * funk2_pr_y(y) - funk1_pr_y(y) * funk2_pr_x(x)


def h(x, y):
    return (-1/J(x, y))*(funk1(x, y)*funk2_pr_y(y)-funk2(x, y)*funk1_pr_y(y))

def l(x, y):
    return (-1/J(x, y))*(funk1_pr_x(x)*funk2(x, y)-funk2_pr_x(x)*funk1(x, y))


print("Метод Ньютона")
f1 = "sin(x + 1) - y = 1.2"
f2 = "2 * x + cos(y) = 2"
print(f"{f1 = }")
print(f"{f2 = }")
#Fi1 = "np.sin(x + 1) - 1.2"
#Fi2 = "(np.cos(y) - 2) / -2"
#print(f"{Fi1 = }")
#print(f"{Fi2 = }")

Eps = 10 ** -5
x = np.pi / 6
y = -0.18
count = 0

print(f"начальный {x = }")
print(f"начальный {y = }")
print(f"{Eps = }")

while True:
    new_x = x + h(x, y)
    new_y = y + l(x, y)
    if (abs(new_x - x) < Eps) and (abs(new_y - y) < Eps):
        break
    
    count += 1
    x = new_x
    y = new_y


print(f"{new_x = }")
print(f"{new_y = }")
print(f"{count = }")

print(f"Проверка 1:{funk1(new_x,new_y)}")
print(f"Проверка 2:{funk2(new_x, new_y)}")
