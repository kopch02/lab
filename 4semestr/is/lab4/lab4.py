from math import sqrt


def n1():

    def triangle(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            print("это треугольник")
        else:
            print("это не треугольник")

    a = int(input("первая сторона->"))
    b = int(input("вторая сторона->"))
    c = int(input("третья сторона->"))
    triangle(a, b, c)


def n2():

    def distance(x1, y1, x2, y2):
        res = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        print(res)

    x1 = int(input("x1->"))
    y1 = int(input("y1->"))
    x2 = int(input("x2->"))
    y2 = int(input("y2->"))
    distance(x1, y1, x2, y2)


def n3():

    def number_to_words(n):
        f = {
            1: 'один',
            2: 'два',
            3: 'три',
            4: 'четыре',
            5: 'пять',
            6: 'шесть',
            7: 'семь',
            8: 'восемь',
            9: 'девять'
        }
        o = {
            10: 'десять',
            20: 'двадцать',
            30: 'тридцать',
            40: 'сорок',
            50: 'пятьдесят',
            60: 'шестьдесят',
            70: 'семьдесят',
            80: 'восемьдесят',
            90: 'девяносто'
        }
        s = {
            11: 'одиннадцать',
            12: 'двенадцать',
            13: 'тринадцать',
            14: 'четырнадцать',
            15: 'пятнадцать',
            16: 'шестнадцать',
            17: 'семнадцать',
            18: 'восемнадцать',
            19: 'девятнадцать'
        }
        if n < 10:
            return f[n]
        if n > 10 and n < 20:
            return s[n]
        else:
            return o[(n // 10) * 10] + " " + f[n % 10]

    n = int(input("введите число->"))
    if n < 1 or n > 99:
        print("диапозон от 1 до 99!!!")
        quit()
    else:
        print(number_to_words(n))


def n4():

    def power(a, n):
        for x in range(1, n):
            a *= a
        print(a)

    a = float(input("число а->"))
    n = int(input("в какую степень?->"))
    power(a, n)


def n5():  

    def polindrom(a):
        a=a.replace(" ", "")
        rev = a[::-1]
        r=rev.replace(" ", "")
        if a==r:
            return "палиндром"
        else:
            return "не палиндром"

    a = input("введите строку для проверки на полидром->").lower()
    print(polindrom(a))


def n6():
    def print_without_duplicate(message):
        global list
        if message in list:
            b=0
        else:
            print(message)
            list.append(message)
    global list
    list=[""]
    print_without_duplicate("привет")
    print_without_duplicate("привет")
    print_without_duplicate("как дела?")
    print_without_duplicate("как дела?")
    print_without_duplicate("привет")
    print_without_duplicate("пока")
    
def n7():
    def add_friends(a,b):
        global li
        li[a]=b
    def are_friends(a,b):
        global li
        if b in li[a]:
            return True
        else:
            return False
    def print_friends(a):
        global li
        b=list(li[a])
        b=li[a].sort()
        print(b)
        #for x in range(len(b)):
            #print(list(b)[x],end=" ")
    global li
    li={}
    add_friends("Мария",["Иван","Пётр","Антон"])
    print(are_friends("Мария","Иван"))
    print_friends("Мария")
n7()
