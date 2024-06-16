import numpy as np
import pandas as pd


def u_xi(x):
    return np.sin(np.pi * x)


a = 0
b = 1
n = 11
h = 0.1
T = 1

tau = 0.005
print(f"{h = }")
print(f"{tau = }")

u_xi_0 = []
x = a


for i in range(n):
    u_xi_0.append(round(u_xi(x), 4))
    x = round(x + h, 10)


U = [u_xi_0]


coef = tau / h**2

t = 0
i = 0
while(t <= T):
    new_U = []
    new_U.append(0)
    for j in range(1, n - 1):
        U_I_n1 = round(coef * (U[i][j + 1] - 2 * U[i]
                       [j] + U[i][j - 1]) + U[i][j], 4)
        new_U.append(U_I_n1)
    new_U.append(0)

    U.append(new_U)
    t = t + tau
    i += 1

df = pd.DataFrame(U, columns=[z * 0.1 for z in range(n)])
print(df)
