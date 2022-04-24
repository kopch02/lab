import numpy as np

def sigmoid(x):
    return x * (1 - np.exp(x))

ly=0.1

x0=1
x1=[1,2,3,4]
x2=[2,3,4,5]

c1=np.array([1,0])
c2=np.array([0,1])

wx=(-0.5-0.5)*np.random.random( size=(4, 2))+0.5
wy=(-0.5-0.5)*np.random.random( size=(4, 2))+0.5

y=[0,0,0,0]
for epoh in range(100000+1):
    for sample in range(2):
        for neiron in range(4):#доделать
            y[neiron]=sigmoid(x1[neiron]*x2[neiron]*wx[neiron])
                        
        z=sigmoid(np.dot(y,wy))
        e1=c1[sample]-z
        e2=c2[sample]-z
        
        delta1=e1*(z*(1-z))
        delta2=e2*(z*(1-z))
        
        for i in range(4):
            wy[0][i] += ly*y[i]*delta1
            for x in range(2):
                e=wy[0][i]*delta1*(y[i]*(1-y[i]))
                wx[i][x]+=ly*e*x1[x]
        
        for i in range(4):
            wy[1][i] += ly*y[i]*delta2
            for x in range(2):
                e=wy[1][i]*delta2*(y[i]*(1-y[i]))
                wx[i][x]+=ly*e*x1[x]
        
        
        

        
        