import math as m
import random as ran

x0=1
x1=[0]
c=[]
y=[]
ly=0.01
n=5

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
    
        for x in range(n):
            y[x]=0
            
        for neiron in range(n):
            temp=0
            for i in range(2):
                temp += wx[neiron][i]*x0*x1[sample]
            y[neiron] = 1/(1+m.exp(-temp))
        temp=0
        
        for i in range(n):
            temp += wy[i]*y[i]
        z = 1/(1+m.exp(-temp))
        
        e = c[sample]-z
        
        delta = e*(z*(1-z))
        
        for i in range(n):
            wy[i] += ly*y[i]*delta
        for neiron in range(n):
            for x in range(2):
                e=wy[neiron]*delta*(y[neiron]*(1-y[neiron]))
                wx[neiron][x]+=ly*e*x1[x]
                
    for sample in range(4):
        for x in range(n):
            y[x]=0
        for neiron in range(n):
            temp=0
            for i in range(2):
                temp += wx[neiron][i]*x0*x1[sample]
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
for sample in range(n):
    for x in range(n):
            y[x]=0
    for neiron in range(n):
        temp=0
        for i in range(2):
            temp += wx[neiron][i]*x0*x1[sample]
        y[neiron] = 1/(1+m.exp(-temp))
    temp=0
    for i in range(n):
        temp += wy[i]*y[i]
    z = 1/(1+m.exp(-temp))
    
    print(round(c[sample],4), "   ", round(z,4))
print(x1)