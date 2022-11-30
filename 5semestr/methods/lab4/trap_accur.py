import numpy as np
import sympy as sp

a, b = 1, 2
x0 = a

E = 10 ** -3


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
print(f"E = {E}")
print("функция: (x / 2 + 1) * sp.sin(x / 2)")

res = 1
res2 = 100
n = 1
s = 0
while abs(res2 - res) >= E:
    n += 1
    s += 1
    n2 = n * 2

    h = (b - a) / n
    h2 = (b - a) / n2
    x = np.arange(a, b + 0.000001, h)
    x2 = np.arange(a, b + 0.000001, h2)
    y = f(x)
    y2 = f(x2)

    #print(f"x =", *x)
    #print(f"y =", *y)

    y_p = []
    y_p2 = []
    for i in range(len(y)):
        y_p.append(diff2(y[i]))
        y_p2.append(diff2(y2[i]))

    m = max(y_p)
    m2 = max(y_p2)


    r = (-(b - a) / 12) * m * h**2
    r2 = (-(b - a) / 12) * m2 * h2**2

    res = h * (((y[0] + y[-1]) / 2) + sum(y[1:-1])) + r
    res2 = h2 * (((y2[0] + y2[-1]) / 2) + sum(y2[1:-1])) + r2
    #print("для n")
    #print(f"M2 = {m}")
    #print(f"R(h) = {r}")
    #print(f"J = {res}")

    #print("для 2n")
    #print(f"M2 = {m2}")
    #print(f"R(h) = {r2}")
    #print(f"J = {res2}")

    #print(f"|J2n - Jn| = {abs(res2 - res)}")
    

print(f"\n\nn = {n}\n2n = {n * 2}")
print(f"количество повторений: {s}")
print(f"|J2n - Jn| = {abs(res2 - res)}")