import numpy as np
import matplotlib.pyplot as plt
from math import pi,sqrt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def points(count):
    for _ in range(count):
        yield (np.random.rand(), np.random.rand())


ly = 0.01

X, Y = 0, 1
RADIUS_SQRT = 1 / (pi * 2)
hit = lambda X, Y: ((X - 0.5) ** 2) + ((Y - 0.5) ** 2) > RADIUS_SQRT

input_size = 2
hidden_size = 10
out_size = 2
bias = 1
batch_size = 10
sample_count = 100

epochs = 50000
samples = list(points(sample_count))

c = [(1,0) if hit(P[X], P[Y]) else (0,1) for P in samples]
x = [[1, p[X], p[Y]] for p in samples]


np.random.seed(1)
wx = [[(np.random.random()-0.5)/2 for i in range(hidden_size)] for _ in range(input_size + bias)]
wy = [[(np.random.random()-0.5)/2 for i in range(out_size)] for _ in range(hidden_size + bias)]
#тренировка
for epoh in range(epochs + 1):
    if epoh % (epochs//10) == 0:
            print(f"epoch {epoh}")
    z=[]
    E = 0
    for batch in range(sample_count//batch_size):
        c_b = c[batch*batch_size:(batch+1)*batch_size]
        x_b = x[batch*batch_size:(batch+1)*batch_size]
        
        #forward
        y=np.dot(x_b, wx)
        y = sigmoid(y)
        y = np.hstack((np.array([1]*batch_size)[:, np.newaxis], y))

        z_b=np.dot(y, wy)
        z_b = sigmoid(z_b)  #6x2
        #backward
        e = c_b - z_b  #6x2
        delta_out = e * (z_b * (1 - z_b))  #6x2
        wy += ly * np.dot(np.transpose(y),delta_out)  #5x2
        y=np.delete(y, 0, 1)
        delta_hid = y * (1 - y) * np.dot(delta_out, np.transpose(wy[1:]))  #6x4
                                    #3x6    6x4
        wx += ly * np.dot(np.transpose(x_b), delta_hid)  #3x4

        z = np.append(z, z_b)
    z = np.reshape(z, (sample_count, out_size))

    for i in range(sample_count):
        E += 0.5 * ((c[i][X] - z[i][X]) + (c[i][Y] - z[i][Y]))**2
    E /= sample_count
    if epoh % (epochs//10) == 0:
        print(f"E: {E}\n")


# работа на 1000 точках 
np.set_printoptions(suppress=True)
works_points=10000

works = list(points(works_points))
x = [[1, p[X], p[Y]] for p in works]

z=[]

for batch in range(works_points//batch_size):
    x_b = x[batch*batch_size:(batch+1)*batch_size]
    
    #forward
    y = sigmoid(np.dot(x_b, wx))
    y = np.hstack((np.array([1]*batch_size)[:, np.newaxis], y))
    z_b = sigmoid(np.dot(y, wy))  #6x2
    z = np.append(z, z_b)

z = np.reshape(z, (works_points, out_size))

#отрисовка

circle = plt.Circle((0.5, 0.5), sqrt(RADIUS_SQRT), color="red", alpha=0.1)
 
ax = plt.gca()
ax.cla()
 
ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
ax.add_patch(circle)
ax.set_aspect('equal')
 
p_x, p_y = zip(*works)
z_x, z_y = zip(*z)
 
ans_x = list(map(round, z_x))
ans_y = list(map(round, z_y))
 
colors = []


for i in range(len(ans_x)):
    if (ans_x[i]):
        if not hit(x[i][1],x[i][2]):
            colors.append("y")
        else:
            colors.append("r")
    else:
        if hit(x[i][1],x[i][2]):
            colors.append("g")
        else:
            colors.append("b")
 
ax.scatter(p_x, p_y, c=colors,s=11)
 
plt.savefig("4semestr\\neironki\\4lab\\graph.png", dpi=300)