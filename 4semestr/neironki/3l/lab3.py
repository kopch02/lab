import math as m

x0=1
x1=[0]
c=[]
y=[]

n=4
s=1/(n-1)
g=s

for x in range(n):
    x1.append(g)
    g+=s
x1.append(1)
for x in range(n):
    c.append(m.sin(x1[x]))

print(c)

for epoh in range(10000):
        
        for sample in range(n):
        