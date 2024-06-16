import numpy as np
import pandas as pd

def U_x(x):
  return x + 1

def U_2_t(t):
  return 1

def U_2_t(t):
  return 2 + (t ** 2)

def mega_round(num, val=4):
  return float(str(num)[:val])

print("Неявная схема")
n = 11
h = 0.1
r = 0.5 * h ** 2
T = 1
x = []
t = []
u_x_0 = []
n_t = []
U = []

for i in range(n):
  x.append(round(i * h, 5))

for i in range(n):
  u_x_0.append(round(U_x(x[i]), 5))

U = [u_x_0]

Aj = (r / h) - (r / (2 * h))
Bj = ((2 * r) / (h ** 2)) + 1
Cj = (r / (h ** 2)) + (r / (2 * h))
p = [0]
q = [1]

t = 0
for j in range(n - 1):
  Fj = -U[0][-j - 1] - r * x[j] * (t + 1)
  pj = -Cj / (Aj * p[j - 1] - Bj)
  qj = (Fj - Aj * q[j - 1]) / (Aj * p[j - 1] - Bj)
  p.append(mega_round(pj))
  q.append(mega_round(qj))

t += r
i = n - 1

while t < T:
  temp = []
  temp.append(U_2_t(t))
  for j in range(1, n - 1):
    temp.append(p[j] * U[n - i - 1][-j - 1] + q[j])
  temp.append(U_2_t(t))
  U.append(temp)
  p = [0]
  q = [0]
  for j in range(n - 1):
    Fj = -U[0][-j - 1] - r * x[j] * (t + 1)
    pj = -Cj / (Aj * p[j - 1] - Bj)
    qj = (Fj - Aj * q[j - 1]) / (Aj * p[j - 1] - Bj)
    p.append(mega_round(pj))
    q.append(mega_round(qj))
  t += r
  i -= 1

df = pd.DataFrame(U)
print(df)
#print(pd.DataFrame(U, columns=[z * 0.1 for z in range(n)])[0.5].to_string())