import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return x * (1 - np.exp(x))


ly = 0.1

x = np.array([[1, 0], 
            [1, 0.2], 
            [1, 0.4], 
            [1, 0.6], 
            [1, 0.8], 
            [1, 1]])

c = np.array([[np.sin(0)], 
                [np.sin(0.2)], 
                [np.sin(0.4)], 
                [np.sin(0.6)],
                [np.sin(0.8)], 
                [np.sin(1)]])
wx = (-0.5 - 0.5) * np.random.random(size=(2, 4)) + 0.5
wy = (-0.5 - 0.5) * np.random.random(size=(5, 1)) + 0.5
y0 = np.zeros((4, 5)) + 1

for epoh in range(100000 + 1):
    E = 0
    y = sigmoid(np.dot(x, wx))
    y_ = np.dot(y, y0)  #6x5
    z = sigmoid(np.dot(y_, wy))  #6x1
    e = c - z  #6x1
    delta_out = e * (z * (1 - z))  #6x1
    wy += np.transpose(ly * np.dot(np.transpose(delta_out), y_))  #5x1
    delta_hid = y * (1 - y) * np.dot(delta_out, np.transpose(wy[1:]))  #6x4

    wx += ly * np.dot(np.transpose(x), delta_hid)  #2x4

    E += e
    if epoh % 5000 == 0:
        print(E / 4)
        print("z=", z)
print()
for i in range(6):
    print(c[i][0], "   ", z[i][0])
