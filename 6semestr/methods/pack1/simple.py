import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x**2 - 6 * x - 8

def fi(x):
    #return np.cos(0.387 * x) * np.cos(0.387 * x)
    return (x**2 - 8) / 6

ab = [2.5,3.5]

x = np.array(list(range(int(ab[0] * 10),int(ab[1] * 10)))) /10
y = func(x)

print("func = x**2 - 6 * x - 8")
print(f"{ab=}")
print("\n--------\n")

for i in [-3,-5,-7]:
    n = 0
    ab = [2.5,3.5]
    eps = 10**i
    x = fi(ab[0])
    while abs(x - fi(x)) > eps:
        x = fi(x)
        n += 1

    print(f"{eps = }")
    print(f"{n = }")
    print(f"{x = }")
    print(f"{func(x) = }")
    print("\n--------\n")

#plt.plot(x,y)
#plt.plot([2,4],[0,0])
#plt.show()
