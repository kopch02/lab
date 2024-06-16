import numpy as np
import pandas as pd

def U_x(x):
  return x + 1

def U_0_t(t):
  return 1

def U_1_t(t):
  return 2 + (t ** 2)

print("Явная схема")
n = 11
h = 0.1
r = 0.5 * h ** 2
T = 1
x = []
u_x_0 = []
U = []

for i in range(n):
  x.append(round(i * h, 5))

for i in range(n):
  u_x_0.append(round(U_x(x[i]), 5))

U = [u_x_0]

t = r
i = 0
coef = r / (h ** 2)

while t < T:
    temp = []
    temp.append(U_0_t(t))  
    
    for j in range(1, n - 1):
        term1 = U[i][j + 1] * (coef + r / (2 * h))
        term2 = U[i][j] * (1 - 2 * r / (h ** 2))
        term3 = U[i][j - 1]
        term4 = coef - r / (2 * h)
        term5 = r * x[j] * (t + 1)
        
        result = round((term1 + term2 + term3) * term4 + term5, 5)
        temp.append(result)
    
    temp.append(U_1_t(t))  
    U.append(temp)  
    
    t += r  
    i += 1  

df = pd.DataFrame(U, columns=[z * 0.1 for z in range(n)])
print(df)
#print(pd.DataFrame(U, columns=[z * 0.1 for z in range(n)])[0.5].to_string())



