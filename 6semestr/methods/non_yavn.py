import numpy as np
import pandas as pd


def u_xi(x):
    return np.sin(np.pi * x)


def mega_round(num, val=4):
    return float(str(num)[:val])


a = 0
b = 1
n = 11
h = 0.1
T = 1

# tau = round(h**2 * 0.5, 10)
tau = 0.005
print(f"{h = }")
print(f"{tau = }")

u_xi_0 = []
x = a


for i in range(n - 1):
    u_xi_0.append(round(u_xi(x), 2))
    x = round(x + h, 10)
u_xi_0.append(0)

U = [u_xi_0]
print(U)

coef = tau / (h**2)

Aj = tau / h**2
Bj = 1. + 2 * tau / h**2
Cj = tau / h**2
p = [0]
q = [0]
for j in range(1, n - 1):
    Fj = -U[0][-j - 1]
    # print(f"{-U[0][-j] = }")

    pj1 = -Cj / (Aj * p[j - 1] - Bj)
    qj1 = (Fj - Aj * q[j - 1]) / (Aj * p[j - 1] - Bj)
    p.append(mega_round(pj1))
    q.append(mega_round(qj1))

print(f"{p = }")
print(f"{q = }")


t = 0
i = n - 1

while(t <= T):
    # print("\n------------\n")
    # print(f"{i = }")
    new_U = []
    new_U.append(0)
    # print(f"{n - i - 1 = }")
    for j in range(1, n - 1):
        # print(f"{U[n - i - 1][-j] = }")
        U_J_n1 = p[j] * U[n - i - 1][-j - 1] + q[j]
        new_U.append(U_J_n1)
    new_U.append(0)

    U.append(new_U)
    p = [0]
    q = [0]
    for j in range(1, n - 1):
        # print(f"{n - i = }")
        Fj = -U[n - i][-j - 1]
        # print(f"{Fj = }")
        # print(U[n - i])

        pj1 = -Cj / (Aj * p[j - 1] - Bj)
        qj1 = (Fj - Aj * q[j - 1]) / (Aj * p[j - 1] - Bj)
        p.append(pj1)
        q.append(qj1)
    t = t + tau
    i = i - 1


df = pd.DataFrame(U)
print(df)
