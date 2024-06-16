   y=float(w[0])*float(x0[sample])+float(w[1])*float(x1[sample])+float(w[2])*float(x2[sample])
        w[0]+=ly*x0[sample]*(c[sample]-y)
        w[1]+=ly*x1[sample]*(c[sample]-y)
        w[2]+=ly*x2[sample]*(c[sample]-y)

    for i in range(4):
        y=float(w[0])*float(x0[i])+float(w[1])*float(x1[i])+float(w[2])*float(x2[i])
        e=0.5*pow(c[i]-y,2)
        se+=e

    print(se/4)
