import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

a = np.arange(-2, 0.025, 0.025)
print(len(a))
y = np.log10(a**2 + a + 1)
print(len(y))

res = []

for i in range(10,81,10):
    for j in range(10):
        res.append(y[i] + (a[i] - a[j + (i - 10)]) * (y[i-10] - y[i]) / (a[10] - a[0]))

res.append(y[80] + (a[80] - a[80]) * (y[70] - y[80]) / (a[10] - a[0]))


res = np.array(res)
print(res)

r_pract = abs(y - res)

print("x \t\t\t\t res \t\t\t\t r_pract")

for i in range(len(a)):
    print(a[i],"\t\t",res[i],"\t\t",r_pract[i])

figure = plt.figure()

plt.subplot(2, 1, 1)
plt.plot(a,y)
plt.plot(a,res)
plt.legend(["y","linear"])

plt.subplot(2, 1, 2)
plt.plot(r_pract)
plt.legend(["r_pract"])

plt.subplots_adjust(top=0.9, bottom=0.2, wspace=0.25)
plt.show()

