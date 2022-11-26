import numpy as np

n = 7

t = np.zeros(n)
t[2] = -0.40584515
t[1] = -0.74153119
t[0] = -0.94910791
t[3] = 0
t[4] = 0.40584515
t[5] = 0.74153119
t[6] = 0.94910791

a = np.zeros(n)
a[0] = a[6] = 0.12948496
a[1] = a[5] = 0.27970540
a[2] = a[4] = 0.38183006
a[3] = 0.41795918


def f(x):
    #return (x / 2 + 1) * np.sin(x / 2)
    return [1] * len(x)


a, b = 1, 2

x = (b + a) / 2 + ((b - a) / 2) * t

res = (b - a) / 2 * sum(a * x)
print(res)
