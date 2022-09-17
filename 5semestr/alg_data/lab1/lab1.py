"вариант 5"

import matplotlib.pyplot as plt
import timeit


def num1():
    def foo(nums): # nums - список
        for x in nums:
            if x % 2 == 0:
                print("!!")
                return True
        else:
            return False

    li=[]
    time = timeit.Timer("foo(li)", globals=locals())

    #timeit.timeit(f"foo({list(range(1,i,2))})", number=100, globals=locals())
    plt_x = []
    plt_y=[]


    for i in range(1000,100001,100):
        li=list(range(1,i,2))
        plt_x.append(i)
        t=time.timeit(number=1000)
        plt_y.append(t)

    print("функция возвращает True если в списке встречается чётное число и False если не одного чётного нет")
    print("вычислительная сложность O(2n)")

    plt.plot(plt_x, plt_y)
    plt.show()


num1()
