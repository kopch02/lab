import math as m
import random as ran
import matplotlib.pyplot as plt
import numpy as np


x0=1
x1=[0]
c=[]
y=[]
ly=0.01
n=10

for x in range(n):
    y.append(0)

wx=[]
for x in range(n):
    wx.append([round(ran.random()*-0.5,2) for x in range(2)])
wy=[round(ran.random()*-0.5,2) for x in range(n)]
s=g=1/(n-1)

for x in range(n-2):
    x1.append(g)
    g+=s
x1.append(1)
for x in range(n):
    c.append(m.sin(x1[x]))

for epoh in range(100000+1):
    E=0
    for sample in range(n):
        for neiron in range(n):
            temp=0
            
            temp += wx[neiron][0]*x0+wx[neiron][1]*x1[sample]

            y[neiron] = 1/(1+m.exp(-temp))
        temp=0
        
        for i in range(n):
            temp += wy[i]*y[i]
        z = 1/(1+m.exp(-temp))
        
        e = c[sample]-z
        
        delta = e*(z*(1-z))
        
        for i in range(n):
            wy[i] += ly*y[i]*delta
            for x in range(2):
                e=wy[i]*delta*(y[i]*(1-y[i]))
                wx[i][x]+=ly*e*x1[x]
                
    for sample in range(4):
        
        for neiron in range(n):
            temp=0
            
            temp += wx[neiron][0]*x0+wx[neiron][1]*x1[sample]
            y[neiron] = 1/(1+m.exp(-temp))
        temp=0
        for i in range(n):
            temp += wy[i]*y[i]
        z = 1/(1+m.exp(-temp))
        
        e = 0.5*pow(c[sample]-z, 2)
        E += e
        
    if epoh % 5000 == 0:
        print(E/4)
        print("z=",z)
zg=[]
for sample in range(n):
    for x in range(n):
            y[x]=0
    for neiron in range(n):
        temp=0
        temp += wx[neiron][0]*x0+wx[neiron][1]*x1[sample]
        
        y[neiron] = 1/(1+m.exp(-temp))
    temp=0
    for i in range(n):
        temp += wy[i]*y[i]
    z = 1/(1+m.exp(-temp))
    
    print(round(c[sample],4), "   ", round(z,4))
    zg.append(z)
print(x1)

xgraf_title=np.linspace(0,7,15)
ygraf_title=np.linspace(-1,1,11)

xgraf=np.linspace(0,2.0*np.pi,101)
ygraf=np.sin(xgraf)


plt.plot(xgraf,ygraf,color="r",label="sin")
plt.plot(x1,zg,color="blue",label="sin_neyro")
plt.xticks(xgraf_title)
plt.yticks(ygraf_title)
plt.legend()
plt.grid()
plt.axis([0,6.5,-1.1,1.1])
plt.show()