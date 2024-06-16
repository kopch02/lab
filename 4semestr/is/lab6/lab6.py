def num1_1():
    print(*[x for x in range(10) if x < 5])


def num1_2():
    spisok = [x for x in range(10)]
    print(list(filter(lambda x: x < 5, spisok)))


def num2_1():
    print([x/2 for x in range(10)])


def num2_2():
    spisok = [x for x in range(10)]
    print(list(map(lambda x: x / 2, spisok)))


def num3():
    print(sum(map(lambda x: x ** 2, filter(lambda x: x %9 == 0, [x for x in range(10, 100)]))))


def num4_1():
    print(
        *list(map(lambda x: x/2, filter(lambda x: x > 17, [x for x in range(30)]))))


def num4_2():
    print(*[x/2 for x in range(30) if x > 17])

def num5():
    def factorials(n):
        s = 1
        for x in range(1, n+1):
            yield s*x
            s *= x
    while True:
        try:
            b = int(input("до какого числа?->"))
            a = factorials(7)
            for i in a:
                print(i)

        except ValueError:
            print("вы ввели слово, а не число")
        except:
            print("что-то не так, попробуйте сново")
        else:
            quit()


def num6():
    def square_fibonacci(n):
        i = 0
        fib1 = 1
        fib2 = 1
        n += 1
        while i < n - 2:
            yield fib2**2
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            i = i + 1
    while True:
        try:
            b = int(input("до какого числа?->"))
            a = square_fibonacci(b)
            for x in a:
                print(x)
        except ValueError:
            print("вы ввели слово, а не число")
        except:
            print("что-то не так, попробуйте сново")
        else:
            quit()


def num7():
    def alfavit():
        for x in range(1072, 1104):
            yield chr(x)
    a = alfavit()
    for x in a:
        print(x)


def num8():
    a = (chr(x) for x in range(1072, 1104))
    for x in a:
        print(x)


def num9():
    def arithmetic_operation(o):
        if o == "+":
            return lambda x, y: x + y
        if o == "-":
            return lambda x, y: x - y
        if o == "/":
            return lambda x, y: x / y
        if o == "*":
            return lambda x, y: x * y

    operation = arithmetic_operation("+")
    print(operation(1, 4))
    operation = arithmetic_operation("-")
    print(operation(1, 4))
    operation = arithmetic_operation("/")
    print(operation(1, 4))
    operation = arithmetic_operation("*")
    print(operation(1, 4))


def num10():  # через all
    def same_by(characteristic, object):
        n = len(values)
        n -= 1
        while characteristic(object[n]):
            if n == -1:
                break
            n -= 1
        if n == -1:
            return True
        else:
            return False
    values = [8, 4, 10, 4]
    print(values)
    if same_by(lambda x: x % 2 == 0, values):
        print("same")
    else:
        print("different")


def num11():
    def print_operation_table(operation, num_rows=9, num_columns=9):
        for x in range(1, num_columns+1):
            print("%3d" % (x), end="  ")
        print()
        for i in range(2, num_rows+1):
            print("%3d" % (i), end="  ")
            for x in range(2, num_columns+1):
                print("%3d" % (operation(x, i)), end="  ")
            print()

    print_operation_table(lambda x, y: x+y)


def num12():
    stroka = input("->")
    print(*sorted(stroka.split(), key=str.lower))


def num13():
    a = [3, 6, -8, -78, 1, 23, -45, 9]
    print(sorted(a, key=lambda x: -abs(x)))


def num14():
    pass


def num15():
    print(not all([1, 2, 3, 4, 5, 6, 7, 0]))


def num16():
    pass


def num17():
    from copy import deepcopy
    m1 = []
    m2 = []
    m3 = []
    matrix = [m1, m2, m3]
    for x in range(3):
        temp = list(input(f"{x+1}строка->").replace(" ", ""))
        for i in temp:
            matrix[x].append(int(i))
    s = sum(p for p in m1)
    temp = deepcopy(matrix)
    for q in range(3):
        matrix[q].clear()
        for j in range(3):
            matrix[q].append(temp[j][q])
    matrix += temp
    for x in matrix:
        if s == sum(x):
            continue
        else:
            print("квадрат не магический")
            quit()
    print("квадрат магический")


def num18():
    def check_password(func):
        password = "qwer"

        def wrapped(n):
            nonlocal password_ent
            if not password_ent:
                password_in = input("Пароль:")
                password_ent = True
                if password_in == password:
                    return func(n)
                else:
                    print("В доступе отказано")
                    return
            else:
                return func(n)
        return wrapped

    password_ent = False

    @check_password
    def fibo_numbers(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fibo_numbers(n - 1) + fibo_numbers(n - 2)

    print(fibo_numbers(int(input("Число Фибоначчи №:"))))
