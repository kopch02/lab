x0=[1,1,1,1]
x1=[0,0,1,1]
x2=[0,1,0,1]
x=[x0,x1,x2]

wx=[0.1,-0.05,0.05]
wx2=[0.1,-0.1,0.01]
wy=[-0.05,-0.01,-0.05]
w=[wx,wy,wx2]

y0=[1,1,1,1]
y1=[0,0,0,0]
y2=[0,0,0,0]
y=[y0,y1,y2]

c=[0,1,1,0]

e1=0
e2=0

ly=0.001

for epoh in range(10000):
    E=0
    z=0
    for sample in range(4):
        for i in range(3):
            y1[sample]+=w[0][i]*x[i][sample]
        for i in range(3):
            y2[sample]+=w[2][i]*x[i][sample]
        for i in range(3):
            z+=w[1][i]*y[i][sample]
        
        #z=w[1][0]*y[0][sample]+w[1][1]*y[1][sample]+w[1][2]*y[2][sample]
        for i in range(4):
            e=0.5*pow(c[i]-z,2)
            E+=e

        e1=E*w[1][1]
        e2=E*w[1][2]
        for i in range(3):
            w[0][i]+=ly*x0[i]*(e1)
            w[2][i]+=ly*x0[i]*(e2)
        for i in range(3):
            w[1][i]+=ly*y[i][sample]*(c[sample]-z)
    E=0
    for i in range(4):
        e=0.5*pow(c[i]-z,2)
        E+=e
    print(E/4)
        
for sample in range(4):
    z=w[1][0]*y0[sample]+w[1][1]*y1[sample]+w[1][2]*y2[sample]
    print(c[sample],"   ",z)