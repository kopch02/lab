import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

a = np.arange(-3, 2.1, 0.1)
y = np.log10(a**2 + a + 1)

res=y[0] * (a - a[10]) * (a - a[20]) * (a - a[30]) * (a - a[40]) * (a - a[50])/ ((a[0] - a[10]) * (a[0] - a[20]) * (a[0] - a[30]) * (a[0] - a[40]) * (a[0] - a[50])) +\
y[10] * (a - a[0]) * (a - a[20]) * (a - a[30]) * (a - a[40]) * (a - a[50]) / ((a[10] - a[0]) * (a[10] - a[20]) * (a[10] - a[30]) * (a[10] - a[40]) * (a[10] - a[50])) +\
y[20] * (a - a[10]) * (a - a[0]) * (a - a[30]) * (a - a[40]) * (a - a[50]) / ((a[20] - a[10]) * (a[20] - a[0]) * (a[20] - a[30]) * (a[20] - a[40]) * (a[20] - a[50])) +\
y[30] * (a - a[10]) * (a - a[20]) * (a - a[0]) * (a - a[40]) * (a - a[50]) / ((a[30] - a[10]) * (a[30] - a[20]) * (a[30] - a[0]) * (a[30] - a[40]) * (a[30] - a[50])) +\
y[40] * (a - a[10]) * (a - a[20]) * (a - a[30]) * (a - a[0]) * (a - a[50]) / ((a[40] - a[10]) * (a[40] - a[20]) * (a[40] - a[30]) * (a[40] - a[0]) * (a[40] - a[50])) +\
y[50] * (a - a[10]) * (a - a[20]) * (a - a[30]) * (a - a[40]) * (a - a[0]) / ((a[50] - a[10]) * (a[50] - a[20]) * (a[50] - a[30]) * (a[50] - a[40]) * (a[50] - a[0])) 

print(res)

r_pract = abs(y - res)
print(r_pract)



print("x \t\t\t res \t\t\t r_pract")

for i in range(len(a)):
    print(a[i],"\t",res[i],"\t",r_pract[i])

figure = plt.figure()

plt.subplot(1, 2, 1)
plt.plot(a,y)
plt.plot(a,res)
plt.legend(["y","L5"])

plt.subplot(1, 2, 2)
plt.plot(r_pract)
plt.legend(["r_pract"])

plt.subplots_adjust(top=0.9, bottom=0.2, wspace=0.25)
plt.show()

