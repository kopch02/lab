import math


def Func(x):
    return x**3 - 6 * x - 8

def Proiz(x):
    return 3 * (x ** 2) - 6 


def Proiz2(x):
    return 6 * x


A = 2.5
a = 2.5
b = 3.5
eps = 10 ** -12
count = 0
while True:
    c = a
    a = a - (Func(a)/Proiz(a))-(Proiz2(a)*Func(a)*Func(a))/(2*Proiz(a)*Proiz(a)*Proiz(a))
    count = count + 1
    if (a - c) < eps:
        break

print("func = x ** 3 - 6 * x - 8")
print(f'{A = }')
print(f'{b = }')
print('Eps = ' + str(eps))
print('Метод Чебышева')
print('x = ' + str(a))
print(f'{count = }')
print('F(' + str(a) + ') = ' + str(Func(a)))