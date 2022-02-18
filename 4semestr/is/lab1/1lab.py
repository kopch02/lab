from logging import handlers


def n1():
    a = input("какой кинотеатр?\n-")
    b = input("какой фильм?\n-")
    c = input("какое время?\n-")
    print('''билет на "%s" в "%s", забронирован на "%s"''' % (b, a, c))


def n2():
    a = input("первое слово:")
    b = input("второе слово:")
    if (a == "да" and b == "нет") or (a == "да" and b == "да") or (a == "нет" and b == "нет") or (a == "нет" and b == "да"):
        print("верно")
    else:
        print("не верно")


def n3():
    a = input("логин:")
    b = input("пароль:")
    if "@" in a:
        print("неправильно")
    if "@" in b:
        print("неправильно")


def n4():
    print(input("ввод:"))


def n5():
    a = input("ввод:")
    if a == "":
        print("ДА")
    else:
        print("нет")


def n6():
    a = int(input("введите число:"))
    b = a % 10
    c = a // 100
    d = (b + c) / 2
    f = (a // 10) % 10
    if d == f:
        print("красивое число")
    else:
        print("число не красиове((((")


def n7():
    a = int(input("введите число:"))
    b1 = a // 1000
    b2 = (a // 100) % 10
    b3 = (a % 100) // 10
    b4 = a % 10
    g1 = 10
    g2 = 10
    g3 = 10
    g4 = 10
    #g1
    if b1 < g1:
        g1 = b1
    if b2 < g1:
        g1 = b2
    if b3 < g1:
        g1 = b3
    if b4 < g1:
        g1 = b4
    #g2
    if b1 < g2 and b1 != g1:
        g2 = b1
    if b2 < g2 and b2 != g1:
        g2 = b2
    if b3 < g2 and b3 != g1:
        g2 = b3
    if b4 < g2 and b4 != g1:
        g2 = b4
    #g3
    if b2 < g3 and b2 != g1 and b2 != g2:
        g3 = b2
    if b3 < g3 and b3 != g1 and b3 != g2:
        g3 = b3
    if b1 < g3 and b1 != g1 and b1 != g2:
        g3 = b1
    if b4 < g3 and b4 != g1 and b4 != g2:
        g3 = b4
    #g4

    if b2 < g4 and b2 != g1 and b2 != g2 and b2 != g3:
        g4 = b2
    if b3 < g4 and b3 != g1 and b3 != g2 and b3 != g3:
        g4 = b3
    if b4 < g4 and b4 != g1 and b4 != g2 and b4 != g3:
        g4 = b4
    if b1 < g4 and b1 != g1 and b1 != g2 and b1 != g3:
        g4 = b1
    a = g1 * 10
    a += g2
    a *= 10
    a += g3
    a *= 10
    a += g4
    print(a)


def n8():
    max = 0
    min = 10000000
    good = 0
    while True:
        rost = input("введите рост-")
        if rost == "!":
            break
        if int(rost) / 1 == int(rost):
            rost = int(rost)
            if rost > 150 and rost < 190:
                good += 1
                if rost > max:
                    max = rost
                if rost < min:
                    min = rost
    print(good, "\n", max, "  ", min)


def n9():
    while True:
        a = input("введите пароль:")
        if len(a) < 8:
            print("короткий")
        elif "123" in a:
            print("простой")
        else:
            b = input("повторите парль:")
            if a == b:
                print("OK")
                break


def n10():
    while True:
        a = int(input("1е:"))
        c = input("что делать:")
        if c == "+":
            b = int(input("2e:"))
            t = a + b
            print(t)
        if c == "-":
            b = int(input("2e:"))
            t = a - b
            print(t)
        if c == "*":
            b = int(input("2e:"))
            t = a * b
            print(t)
        if c == "/":
            b = int(input("2e:"))
            t = a // b
            print(t)
        if c == "%":
            b = int(input("2e:"))
            t = a % b
            print(t)
        if c == "!":
            t = 1
            for x in range(a):
                t *= (x + 1)
            print(t)
        if c == "x":
            print(a)
            break


def n11():
    h = int(input("введите высоту:"))
    n = h
    g = 1
    for i in range(h):
        n -= 1
        print(" " * n, "*" * g, " " * n)
        g += 2


def n12():
    n = int(input("введите число:"))
    if n <= 0:
        print("число должно быть положительным!!!")
        quit
    a = 1
    b = 1
    t = 0
    while (b + t) < n + 1:
        for x in range(1, a + 1):
            print(str(b + t) * b, " ", end="")
            if (b + t) == n:
                quit()
            t += 1
        print("\n")
        a += 1


def n13():
    a = int(input("Длинна:"))
    b = int(input("Ширина:"))
    c = input("из чего:")
    print(str(c) * b, sep=" ")
    for x in range(a - 2):
        print(c, " " * (b - 2), c, sep='')
    print(str(c) * b, sep=" ")
n7()