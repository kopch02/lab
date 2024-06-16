from math import sqrt
from tkinter import N


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
        res = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
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
        a = a.replace(" ", "")
        rev = a[::-1]
        if a == rev:
            return "палиндром"
        else:
            return "не палиндром"

    a = input("введите строку для проверки на полидром->").lower()
    print(polindrom(a))


def n6():
    def print_without_duplicate(message):
        global list
        if message in list:
            b = 0
        else:
            print(message)
            list.append(message)
    global list
    list = [""]
    print_without_duplicate("привет")
    print_without_duplicate("привет")
    print_without_duplicate("как дела?")
    print_without_duplicate("как дела?")
    print_without_duplicate("привет")
    print_without_duplicate("пока")


def n7():
    def add_friends(a, b):
        global li
        li[a] = b

    def are_friends(a, b):
        global li
        if b in li[a]:
            return True
        else:
            return False

    def print_friends(a):
        global li
        b = list(li[a])
        b.sort()
        for x in b:
            print(x, end=" ")
    global li
    li = {}
    add_friends("Мария", ["Иван", "Пётр", "Антон"])
    print(are_friends("Мария", "Иван"))
    print_friends("Мария")


def n8():
    def mirror(arr):
        temp = []
        for x in arr:
            temp.append(x)
        temp.reverse()
        for i in temp:
            arr.append(i)
    arr = [1, 2, 3]
    mirror(arr)
    print(arr)


def n9():
    def from_string_to_list(string, conteiner):
        temp = list(string)
        for x in range(0, len(string), 2):
            a.append(int(string[x]))
    a = [1, 2, 3]
    st = input("что добавить?->")
    from_string_to_list(st, a)
    print(a)


def n10():
    import copy

    def transpose(matrix):
        temp = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrix[y][i] = temp[i][y]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    for x in matrix:
        print(x)


def n11():
    def matrix(n=1, m=0, a=0):
        if m == 0:
            if n != 1:
                m = n
        matrix = []
        for x in range(n):
            matrix.append([a])
            for y in range(m-1):
                matrix[x].append(a)
        return matrix
    s = matrix(3)
    for q in s:
        print(q)
    print()
    s = matrix(3, 5)
    for q in s:
        print(q)
    print()
    s = matrix(3, 5, 9)
    for q in s:
        print(q)


def n12():
    def patrial_sums(*n):
        a = [0]
        temp = []
        for x in n:
            temp.append(x)
        a.append(temp[0])
        for s in range(1, len(temp)):
            a.append(a[s]+temp[s])
        return a
    print(patrial_sums(1, 4, 5, 6, 7))


def n13():
    def power(a, n):
        if n == 1:
            return a
        else:
            n -= 1
            return a * power(a, n)
    print(power(2, 4))

n13()
def n14():
    def recursive_len(lis):
        if not lis:
            return 0
        return 1 + recursive_len(lis[1:])
    print(recursive_len([1, 2, 3, 4, 5, 6]))


def n15():
    pass


