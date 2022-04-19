import numpy as np

def sigmoid(x):
    return x * (1 - np.exp(x))

ly=0.1

x0=1
x1=[]
x2=[]

c1=np.array([1,0])
c2=np.array([0,1])

wx = (-0.5-0.5)*np.random.random( size=(4, 2))+0.5
wy=np.random.sample(3)-0.5

y=[0,0,0,0]
for epoh in range(100000+1):
    for sample in range(2):
        for neiron in range(4):
            y[neiron]=sigmoid(np.dot(x0,x1[neiron],x2[neiron],wx[neiron]))
                        
        z=sigmoid(np.dot(y,wx))
        
        e1=c1[sample]-z
        e2=c2[sample]-z
        
        delta1=e1*(z*(1-z))
        delta2=e2*(z*(1-z))
        
        
        
        