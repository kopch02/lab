def n1():
    print('различных символов = ', len(set([1, 2, 3, 4, 4, 4, 1, 5])))


def n2():
    print(
        'одинаковых символов = ',
        len(set([1, 2, 3, 4, 4, 4, 1, 5]).intersection(set([1, 7, 7, 8, 5]))))


def n3():
    print(
        'одинаковые числа = ',
        set([1, 2, 3, 4, 4, 4, 1, 5, 2]).intersection(set([1, 7, 7, 8, 5, 2])))


def n4():#множества
    a = input("введите строку")
    b = list(a)
    c = []
    for x in range(0, len(b), 2):
        if b[x] in c:
            print(b[x], "YES")
        else:
            print(b[x], "NO")
            c.append(b[x])


def n5():# множества
    a = int(input("строки:"))
    g = 0
    for x in range(a):
        b = input("текст->")
        w = b.split()
        g += len(w)
    print(g)

