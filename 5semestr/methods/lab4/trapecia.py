import numpy as np
import sympy as sp

a, b = 1, 2
x0 = a


def f(x):
    return (x / 2 + 1) * np.sin(x / 2)
    #return [1] * len(x)


def diff2(i):
    x = sp.symbols('x')
    func = (x / 2 + 1) * sp.sin(x / 2)
    #func = 1
    yprime = sp.diff(func, x, 2)
    yprime = yprime.subs({x: i})
    return abs(yprime.evalf())

print(f"для отрезка [{a}, {b}]")
print("функция: (x / 2 + 1) * sp.sin(x / 2)")
n = int(input("введите n->"))

h = (b - a) / n
x = np.arange(a, b + 0.000001, h)
y = f(x)

#print(f"x =", *x)
#print(f"y =", *y)

y_p = []
for i in y:
    y_p.append(diff2(i))

m = max(y_p)
print(f"M2 = {m}")

r = (-(b - a) / 12) * m * h**2
print(f"R(h) = {r}")

res = h * (((y[0] + y[-1]) / 2) + sum(y[1:-1])) + r
print(f"J = {res}")
