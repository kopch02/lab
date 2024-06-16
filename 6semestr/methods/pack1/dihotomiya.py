import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x**3 - 6 * x - 8

#def func(x):
#    return x**2 + 4 * np.sin(x)

ab = [2.5,3.5]



print("func = x ** 3 - 6 * x - 8")
print(f"{ab = }")
print("\n--------\n")


for i in [-3,-5,-7]:
    n = 0
    a = 2.5
    b = 3.5
    eps = 10**i

    while True:
        n += 1
        c = (a + b) / 2
        x = func(c) * func(a) 
        if x < 0:
            b = c
        else:
            a = c

        if abs(b - a) <= eps:
            break

    print(f"{eps = }")
    print(f"res = {c}")
    print(f"{n = }")
    print(f"func(x) = {func(c)}")
    print("\n--------\n")

x = np.array(list(range(int(ab[0] * 10),int(ab[1] * 10)))) /10
y = func(x)

plt.plot(x,y)
plt.plot([2,4],[0,0])
plt.show()
