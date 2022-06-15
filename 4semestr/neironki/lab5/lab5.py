import numpy as np
import matplotlib.pyplot as plt
from math import pi,sqrt
import gzip
import sys

np.set_printoptions(threshold=sys.maxsize)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


c = np.zeros((10000,10))

i=0
with gzip.open('4semestr\\neironki\lab5\mnist\\t10k-labels-idx1-ubyte.gz', 'rb') as f:
    f.read(8)
    for lab in f:
        for l in lab:
            c[i][l]=1
            i+=1


x=[]
with gzip.open('4semestr\\neironki\lab5\mnist\\t10k-images-idx3-ubyte.gz', 'rb') as f:
    f.read(16)
    for lab in f:
        for l in lab:
            x.append(l)
x=np.array(x)
x=x.reshape((10000,784))

x = np.hstack((np.array([1]*10000)[:, np.newaxis], x))

ly = 0.01

input_size = 784
hidden_size = 200
out_size = 10
bias = 1
batch_size = 50
sample_count = 10000

epochs = 50

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
        z_b = sigmoid(z_b)  
        #backward
        e = c_b - z_b 
        delta_out = e * (z_b * (1 - z_b)) 
        wy += ly * np.dot(np.transpose(y),delta_out) 
        y=np.delete(y, 0, 1)
        delta_hid = y * (1 - y) * np.dot(delta_out, np.transpose(wy[1:]))  
        wx += ly * np.dot(np.transpose(x_b), delta_hid)  

        z = np.append(z, z_b)
    z = np.reshape(z, (sample_count, out_size))


    temp=0
    for i in range(sample_count):
        for k in range(10):
            temp+=c[i][k] - z[i][k]
        E += 0.5 * (temp/10)**2
        E /= sample_count
    if epoh % (epochs//10) == 0:
        print(f"E: {E}\n")


# работа на 1000 точках 
works_points=60000

x=[]

with gzip.open('4semestr\\neironki\lab5\mnist\\train-images-idx3-ubyte.gz', 'rb') as f:
    f.read(16)
    for lab in f:
        for l in lab:
            x.append(l)
x=np.array(x)
x=x.reshape((60000,784))
x = np.hstack((np.array([1]*60000)[:, np.newaxis], x))


z=[]

for batch in range(works_points//batch_size):
    x_b = x[batch*batch_size:(batch+1)*batch_size]
    
    #forward
    y = sigmoid(np.dot(x_b, wx))
    y = np.hstack((np.array([1]*batch_size)[:, np.newaxis], y))
    z_b = sigmoid(np.dot(y, wy)) 
    z = np.append(z, z_b.round())

z = np.reshape(z, (works_points, out_size))



c = np.zeros((60000,10))

i=0
with gzip.open('4semestr\\neironki\lab5\mnist\\train-labels-idx1-ubyte.gz', 'rb') as f:
    f.read(8)
    for lab in f:
        for l in lab:
            c[i][l]=1
            i+=1

print("labels:\n")
print(c[:20])
print("z:\n")
print(z[:20])
