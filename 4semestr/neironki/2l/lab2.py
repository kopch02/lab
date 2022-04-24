import math as m

x0 = [1, 1, 1, 1]
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
x = [x0, x1, x2]

wx1 = [0.1, -0.05, 0.05]
wx2 = [0.03, -0.1, 0.01]
wy = [-0.05, -0.01, -0.05]
w = [wx1, wx2, wy]

y0 = [1, 1, 1, 1]
y1 = [0, 0, 0, 0]
y2 = [0, 0, 0, 0]
y = [y0, y1, y2]

c = [0, 1, 1, 0]

e1 = 0
e2 = 0

q = 0
r = 0
t = 0

ly = 1

for epoh in range(100000):
    E = 0
    for sample in range(4):
        z = 0
        q = 0
        r = 0
        t = 0

        y1[sample] = 0
        y2[sample] = 0

        for i in range(3):
            q += w[0][i] * x[i][sample]
        y1[sample] = 1 / (1 + pow(m.e, -q))

        for i in range(3):
            r += w[1][i] * x[i][sample]
        y2[sample] = 1 / (1 + pow(m.e, -r))

        for i in range(3):
            t += w[2][i] * y[i][sample]
        z = 1 / (1 + pow(m.e, -t))

        # z=w[1][0]*y[0][sample]+w[1][1]*y[1][sample]+w[1][2]*y[2][sample]

        e = c[sample] - z

        delta = e * (z * (1 - z))

        for i in range(3):
            w[2][i] += ly * y[i][sample] * delta

        e1 = w[2][1] * (y1[sample] * (1 - y1[sample])) * delta
        e2 = w[2][2] * (y2[sample] * (1 - y2[sample])) * delta

        for i in range(3):
            w[0][i] += ly * x[i][sample] * e1
            w[1][i] += ly * x[i][sample] * e2

    for sample in range(4):
        q = 0
        r = 0
        t = 0

        for i in range(3):
            q += w[0][i] * x[i][sample]
        y1[sample] = 1 / (1 + pow(m.e, -q))

        for i in range(3):
            r += w[1][i] * x[i][sample]
        y2[sample] = 1 / (1 + pow(m.e, -r))

        for i in range(3):
            t += w[2][i] * y[i][sample]
        z = 1 / (1 + pow(m.e, -t))

        e = 0.5 * pow(c[sample] - z, 2)
        E += e

    if epoh % 1000 == 0:
        print(E / 4)

for sample in range(4):
    z = 0

    y1[sample] = 0
    y2[sample] = 0

    q = 0
    r = 0
    t = 0

    for i in range(3):
        q += w[0][i] * x[i][sample]
    y1[sample] = 1 / (1 + pow(m.e, -q))
    for i in range(3):
        r += w[1][i] * x[i][sample]
    y2[sample] = 1 / (1 + pow(m.e, -r))

    for i in range(3):
        t += w[2][i] * y[i][sample]
    z = 1 / (1 + pow(m.e, -t))

    print(c[sample], "   ", z)
