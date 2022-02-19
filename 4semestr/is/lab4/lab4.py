def n1():
    def triangle(a,b,c):
        if a+b>c and a+c>b and b+c>a:
            print("это треугольник")
        else:
            print("это не треугольник")
    a=int(input("первая сторона->"))
    b=int(input("вторая сторона->"))
    c=int(input("третья сторона->"))
    triangle(a,b,c)



