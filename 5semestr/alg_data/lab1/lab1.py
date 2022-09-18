"вариант 5"

import matplotlib.pyplot as plt
import timeit
import random


def num1():

    def foo(nums):  # nums - список
        for x in nums:
            if x % 2 == 0:
                print("!!")
                return True
        else:
            return False

    li = []
    time = timeit.Timer("foo(li)", globals=locals())

    plt_x = []
    plt_y = []

    for i in range(1000, 100001, 1000):
        li = list(range(1, i, 2))
        plt_x.append(i)
        plt_y.append(
            timeit.timeit(f"foo({list(range(1,i,2))})",
                          number=100,
                          globals=locals()))

    print('''функция возвращает True если в списке встречается чётное число 
    и False если не одного чётного нет''')
    print("вычислительная сложность O(2n)")

    plt.plot(plt_x, plt_y)
    plt.show()


def num2():

    def first(st):
        a = set(st)
        ar = {}
        for i in a:
            ar[i] = st.count(i)
        #print(ar)

    "o(n)"

    def second(st):
        ar = {}
        for i in st:
            ar[i] = ar.get(i, 0) + 1
        #print(max(ar.values()))

    "o(2n)"

    plt_x = []
    plt_y1 = []
    plt_y2 = []

    s = 'asd'

    for i in range(10):
        plt_x.append(i)
        plt_y1.append(
            timeit.timeit(f"first('{s}')", number=100, globals=locals()))
        plt_y2.append(
            timeit.timeit(f"second('{s}')", number=100, globals=locals()))
        s += "a" * 1000

    plt.plot(plt_x, plt_y1)
    plt.plot(plt_x, plt_y2)
    plt.show()


def num3():

    def first_t(n):
        return (n**2 - n - 10)

    def second_t(n):
        return (4 * n + 40)

    n = 0
    plt_lst1 = [first_t(n)]
    plt_lst2 = [second_t(n)]
    plt_x = [n]
    while True:
        n += 1
        plt_x.append(n)
        plt_lst1.append(first_t(n))
        plt_lst2.append(second_t(n))
        if first_t(n) == second_t(n):
            break

    print("N =", n)

    plt.plot(plt_x, plt_lst1, plt_lst2)
    plt.show()


def num4():

    def del_test(collection):
        del collection[random.randrange(len(collection))]

    plt_x = []
    plt_list = []
    plt_dict = []
    for i in range(1000, 1000001, 100000):
        plt_x.append(i)

        test_collection = list(range(i))
        plt_list.append(
            timeit.timeit(f"del_test(test_collection)",
                          number=100,
                          globals=locals()))

        test_collection = dict.fromkeys(range(i))

        plt_dict.append(
            timeit.timeit(f"del_test(test_collection)",
                          number=1,
                          globals=locals()))

    plt.plot(plt_x, plt_list, plt_x, plt_dict)
    plt.legend(["list", "dict"])

    plt.show()


def num5():

    plt_x = []
    plt_list = []
    plt_set = []

    def test_in(numbers):
        "test" in numbers

    for i in range(10000, 100001, 10000):
        plt_x.append(i)

        test_list = list(range(i))
        plt_list.append(
            timeit.timeit(f"test_in(test_list)", number=100, globals=locals()))

        test_set = set(range(i))
        plt_set.append(
            timeit.timeit(f"test_in(test_set)", number=100, globals=locals()))

    plt.plot(plt_x, plt_list, plt_x, plt_set)
    plt.legend(["list", "set"])

    plt.show()


num3()