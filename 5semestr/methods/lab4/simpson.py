import numpy as np
import sympy as sp

a, b = 1, 2
x0 = a


def f(x):
    return (x / 2 + 1) * np.sin(x / 2)
    #return [1] * len(x)


def diff4(i):
    x = sp.symbols('x')
    func = (x / 2 + 1) * sp.sin(x / 2)
    #func = 1
    yprime = sp.diff(func, x, 4)
    yprime = yprime.subs({x: i})
    return abs(yprime.evalf())

print(f"для отрезка [{a}, {b}]")
print("функция: (x / 2 + 1) * sp.sin(x / 2)")
n = int(input("введите n->"))
if n%2 !=0:
    print("нужен только чётный шаг")
    exit(0)

h = (b - a) / n
x = np.arange(a, b + 0.000001, h)
y = f(x)

#print(f"x =", *x)
#print(f"y =", *y)

y_p = []
for i in y:
    y_p.append(diff4(i))

m = max(y_p)
print(f"M4 = {m}")

r = (-(b - a) / 180) * m * h ** 4
print(f"R(h) = {r}")

s = 0
t = 1
for i in range(len(y) - 1):
    if (i + 1) % 2 == 0:t = 2
    else: t = 4
    s += y[i + 1] * t
print(s)
#s += y[0]
#print(s)

res = (h / 3) * s + r
print(f"J = {res}")
