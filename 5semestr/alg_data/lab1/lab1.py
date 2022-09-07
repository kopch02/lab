"вариант 5"

import matplotlib as plt
import timeit


def num1():
    def foo(nums): # nums - список
        for x in nums:
            if x % 2 == 0:
                return True
        else:
            return False


    plt_x = []
    plt_y=[]

    for i in range(1000,10001,1000):
        plt_x.append(i)
        plt_y.append(timeit.timeit(f"foo({i})", number=100, globals=locals()))

    print("функция возвращает True если в списке встречается чётное число и False если не одного чётного нет")
    print("вычислительная сложность O(2n)")

    plt.plot(plt_x, plt_y)
    plt.show()

num1()