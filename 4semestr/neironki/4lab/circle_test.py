import numpy as np
import matplotlib.pyplot as plt
import math
 
 
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))
 
def sigmoid_d(x):
    return x * (1 - x)
 
def points(count):
    for _ in range(count):
        yield (np.random.rand(), np.random.rand())
 
def hit_tri(x, y):
    return (y > 0) and (y < (-2*x + 2)) and (y < 2*x)
 
 
X, Y = 0, 1
RADIUS_SQRT = 1 / (math.pi * 2)
hit = lambda X, Y: ((X - 0.5) ** 2) + ((Y - 0.5) ** 2) > RADIUS_SQRT
 
 
sample_count = 100
batch_size = 10
 
bias = 1
input_size = 2
hidden_size = 10
out_size = 2
 
 
np.random.seed(1)
samples = list(points(sample_count))
c = [(1,0) if hit(P[X], P[Y]) else (0,1) for P in samples]
x = [[1, p[X], p[Y]] for p in samples]
 
w_ji = [[(np.random.random()-0.5)/2 for i in range(hidden_size)] for _ in range(input_size + bias)]
w_kj = [[(np.random.random()-0.5)/2 for i in range(out_size)] for _ in range(hidden_size + bias)]
 
 
lbd = 0.01
epochs = 50_000
 
min_E = 1.0
min_epoch = 0
 
    
for epoch in range(epochs):
    if epoch % (epochs//10) == 0:
            print(f"epoch {epoch}")
    
    z = []
    for batch in range(sample_count//batch_size):
        c_b = c[batch*batch_size:(batch+1)*batch_size]
        x_b = x[batch*batch_size:(batch+1)*batch_size]
        
        # forward
        y = np.dot(x_b, w_ji)
        y = sigmoid(y)
        y = np.hstack((np.array([1]*batch_size)[:, np.newaxis], y))
        
        z_b = np.dot(y, w_kj)
        z_b = sigmoid(z_b)
        
        
        # backward
        e_z = np.subtract(c_b, z_b)
        delta_z = np.multiply(sigmoid_d(z_b), e_z)
        w_kj += lbd * np.dot(np.transpose(y), delta_z)
        
        delta_y = np.multiply(sigmoid_d(np.delete(y, 0, 1)), np.dot(delta_z, np.transpose(np.delete(w_kj, 0, 0))))
        w_ji += lbd * np.dot(np.transpose(x_b), delta_y)
        
        z = np.append(z, z_b)
        
    z = np.reshape(z, (sample_count, out_size))
    
    if epoch % (epochs//10) == 0:
        print(z)
    E = 0
    for i in range(sample_count):
        E += 0.5 * ((c[i][X] - z[i][X]) + (c[i][Y] - z[i][Y]))**2
    E /= sample_count
    if epoch % (epochs//10) == 0:
        print(f"E: {E}\n")
    
    if E < min_E:
        min_E = E
        min_epoch = epoch


 
np.set_printoptions(suppress=True)
print(z)
print(f"min E: {min_E} at epoch {min_epoch}")

# работа на 1000 точках 
works_points=10000

works = list(points(works_points))
x = [[1, p[X], p[Y]] for p in works]

z=[]

for batch in range(works_points//batch_size):
    x_b = x[batch*batch_size:(batch+1)*batch_size]
    
    #forward
    y = sigmoid(np.dot(x_b, w_ji))
    y = np.hstack((np.array([1]*batch_size)[:, np.newaxis], y))
    z_b = sigmoid(np.dot(y, w_kj))  #6x2
    z = np.append(z, z_b)

z = np.reshape(z, (works_points, out_size))

#отрисовка

circle = plt.Circle((0.5, 0.5), math.sqrt(RADIUS_SQRT), color="red", alpha=0.1)
 
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
for i in ans_x:
    if (i):
        colors.append("r")
    else:
        colors.append("b")
 
ax.scatter(p_x, p_y, c=colors,s=13)
 
plt.savefig("4semestr\\neironki\\4lab\\graph.png", dpi=300)