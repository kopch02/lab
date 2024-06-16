import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = np.arange(-2, 0.025, 0.025)
y = np.log10(x**2 + x + 1)

h = 0.25

A = h
B = h * 4
G = h

p = [0, 0]
for i in range(2, 9):
    p.append(-G / (B + A * p[i - 1]))

a = y[::10]

f = [0]
for i in range(2, 9):
    f.append(6 * ((a[i] - a[i - 1]) / h - (a[i - 1] - a[i - 2]) / h))

q = [0, 0]
for i in range(1, 8):
    q.append((f[i] - A * q[i]) / (B + A * p[i]))

c = np.zeros(9)
for i in range(8, 1, -1):
    c[i - 1] = (p[i] * c[i] + q[i])

d = [0]
for i in range(1, 9):
    d.append((c[i - 1] - c[i]) / h)

b = [0]
for i in range(1, 9):
    b.append((a[i - 1] - a[i]) / h - c[i] * h / 2 - (c[i - 1] - c[i]) * h / 6)

res = []

for i in range(10, 81, 10):
    for j in range(10):
        res.append(a[i // 10] + b[i // 10] * (x[i] - x[(i - 10) + j]) +
                   (c[i // 10] * (x[i] - x[(i - 10) + j])**2) / 2 +
                   (d[i // 10] * (x[i] - x[(i - 10) + j])**3) / 6)

res.append(a[8] + b[8] * (x[80] - x[80]) + (c[8] * (x[80] - x[80])**2) / 2 +
           (d[8] * (x[80] - x[80])**3) / 6)

res = np.array(res)
print(res)

r_pract = abs(y - res)

print("x \t\t\t\t res \t\t\t\t r_pract")

for i in range(len(x)):
    print(x[i], "\t\t", res[i], "\t\t", r_pract[i])

figure = plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.plot(x, res)
plt.legend(["y", "splayn3"])

plt.subplot(2, 1, 2)
plt.plot(r_pract)
plt.legend(["r_pract"])

plt.subplots_adjust(top=0.9, bottom=0.2, wspace=0.25)
plt.show()
