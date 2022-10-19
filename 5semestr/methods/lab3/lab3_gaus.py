import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

a = np.arange(-2, 0.1, 0.1)
y = np.log10(a**2 + a + 1)

del_y = [y[10] - y[0], y[20] - y[10]]
del2_y = del_y[1] - del_y[0]

t=(a-a[0])/(a[10]-a[0])

print(del_y)
print(del2_y)
print(t)

res = y[0] + del_y[0] * t + del2_y * t * (t - 1)/2

r_pract = abs(y - res)

print("x \t\t\t\t res \t\t\t\t r_pract")

for i in range(len(a)):
    print(a[i],"\t\t",res[i],"\t\t",r_pract[i])

figure = plt.figure()

plt.subplot(1, 2, 1)
plt.plot(a,y)
plt.plot(a,res)
plt.legend(["y","gauss2"])

plt.subplot(1, 2, 2)
plt.plot(r_pract)
plt.legend(["r_pract"])

plt.subplots_adjust(top=0.9, bottom=0.2, wspace=0.25)
plt.show()

