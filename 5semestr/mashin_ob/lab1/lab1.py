import numpy as np
import matplotlib.font_manager as fm
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

from matplotlib import rc, rcParams
from matplotlib.ticker import FormatStrFormatter, NullFormatter
from matplotlib.ticker import AutoMinorLocator, FixedLocator, MultipleLocator
from random import randint, choice
from numpy import pi
import datetime as dt
import math

figure = plt.figure()

plt.title('название')
plt.ylabel('y - axis')
plt.xlabel('x - axis ')


def num1_1():
    plt.title('№1.1')
    plt.plot((0, 1), (0, 1))  #num1


def num1_2():
    plt.title('№1.2')
    plt.plot((10, 20, 30), (20, 40, 10), linewidth=3)
    plt.plot((10, 20, 30), (40, 10, 30), color="red", linewidth=5)
    plt.legend(['line1-width-3', 'line2-width-5'])


def num1_3():
    plt.title('№1.3')
    plt.plot((10, 20, 30), (20, 40, 10), linestyle="dotted")
    plt.plot((10, 20, 30), (40, 10, 30), color="red", linestyle="dashed")
    plt.legend(['line1-dotter', 'line2-dashed'])


def num1_4():
    plt.title('№1.4')
    plt.plot((1, 4, 5, 6, 7), (2, 6, 3, 6, 3),
             color="red",
             linestyle="dashdot")
    plt.scatter((1, 4, 5, 6, 7), (2, 6, 3, 6, 3), color="blue")


def num1_5():
    plt.title('№1.5')
    plt.xlim(0, 10)
    plt.ylim(0, 30)
    plt.scatter((2, 3, 5, 6, 8), (1, 5, 10, 17, 20), color="blue", marker="*")
    plt.scatter((3, 4, 6, 7, 9), (2, 6, 11, 20, 21), color="red")


def num1_6():
    plt.ylabel('Closing Value')
    plt.xlabel('Date ')
    plt.title('№1.6')
    now = dt.datetime.now()
    then = now + dt.timedelta(days=5)
    days = mdates.drange(now, then, dt.timedelta(days=1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.xlim(0, 4)
    plt.ylim(772.5, 777.0)
    plt.plot((0, 1, 2, 3, 4), (772.5, 776.4, 776.5, 776.9, 775.1), color="red")
    plt.scatter((0, 1, 2, 3, 4), (772.5, 776.4, 776.5, 776.9, 775.1),
                color="red")
    plt.minorticks_on()
    plt.gcf().autofmt_xdate()
    plt.grid(True, color="red", which="major")  # сетка
    plt.grid(True, linestyle="--", which="minor")  # сетка


def num2():
    plt.title('№2')
    plt.ylabel('y - подпись')
    plt.xlabel('x - подпись')
    plt.plot((10, 20, 30), (20, 40, 10), linestyle="dotted")
    plt.plot((10, 20, 30), (40, 10, 30), color="red", linestyle="dashed")
    plt.scatter((18, 22, 27), (12, 17, 20), color="blue", marker="*")
    plt.legend(['line1-dotter', 'line2-dashed', 'markers'])
    plt.minorticks_on()
    ax = figure.gca()
    ax.yaxis.set_minor_formatter(FormatStrFormatter("%.3f"))
    plt.grid(True)


def num3():
    plt.title('№3')
    x = range(0, 11)
    y = list(map(lambda x: x * x - x - 6, x))
    plt.plot(x, y)
    print(y)


def num4():
    plt.title('№4')

    def func(x):
        return (math.log((x**2 + 1),
                         (1. + math.tan(1. / (1. + math.sin(x)**2)))) *
                math.exp(-abs(x) / 10.))

    plt_x = []
    plt_res = []

    for i in np.arange(-8, 8, 0.1):
        plt_x.append(i)

        plt_res.append(func(i))

    plt.plot(plt_x, plt_res)


def num5_1():
    plt.title(
        'popularity of programming language\n worldwide, oct 2017 compared to a yaer ago'
    )
    plt.xlabel('languages')
    plt.ylabel('popularity')
    plt.minorticks_on()
    plt.xlim(0, 6)
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    y = [23, 18.5, 9.8, 8, 7.8, 6.9]
    plt.bar(x, y, align='edge')
    plt.grid(True, color="red", which="major")  # сетка
    plt.grid(True, linestyle="--", which="minor")  # сетка


def num5_2():
    plt.title(
        'popularity of programming language\n worldwide, oct 2017 compared to a yaer ago'
    )
    plt.xlabel('languages')
    plt.ylabel('popularity')
    plt.minorticks_on()
    y = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    x = [23, 18.5, 9.8, 8, 7.8, 6.9]
    plt.barh(y, x, align='edge', color='green')
    plt.grid(True, color="red", which="major")  # сетка
    plt.grid(True, linestyle="--", which="minor")  # сетка


def num5_3():
    plt.title(
        'popularity of programming language\n worldwide, oct 2017 compared to a yaer ago'
    )
    plt.xlabel('languages')
    plt.ylabel('popularity')
    plt.minorticks_on()
    plt.xlim(0, 6)
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    y = [23, 18.5, 9.8, 8, 7.8, 6.9]
    my_color = ['red', 'black', 'green', 'blue', 'yellow', 'lightblue']
    plt.bar(x, y, align='edge', color=my_color)
    plt.grid(True, color="red", which="major")  # сетка
    plt.grid(True, linestyle="--", which="minor", color='black')  # сетка


def num5_4():

    def addlabels(x, y):
        for i in range(len(x)):
            plt.text(i, y[i] + 0.5, y[i])

    plt.title(
        'popularity of programming language\n worldwide, oct 2017 compared to a yaer ago'
    )
    plt.xlabel('languages')
    plt.ylabel('popularity')
    plt.minorticks_on()
    plt.xlim(0, 6)
    plt.ylim(0, 25)
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    plt.bar(x, y, align='edge')
    addlabels(x, y)
    plt.grid(True, color="red", which="major")  # сетка
    plt.grid(True, linestyle="--", which="minor")  # сетка


def num5_5():
    plt.title(
        'popularity of programming language\n worldwide, oct 2017 compared to a yaer ago'
    )
    plt.xlabel('languages')
    plt.ylabel('popularity')
    plt.minorticks_on()
    plt.xlim(0, 6)
    my_width = [0.1, 0.2, 0.5, 0.8, 0.2, 0.3]
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    y = [23, 18.5, 9.8, 8, 7.8, 6.9]
    plt.bar(x, y, align='edge', width=my_width)
    plt.grid(True, color="red", which="major")  # сетка
    plt.grid(True, linestyle="--", which="minor")  # сетка


def num5_6():
    plt.title('scores by person')
    y1 = [22, 30, 33, 30, 26]
    y2 = [25, 32, 30, 35, 27]
    x1 = np.array([1, 2, 3, 4, 5]) - 0.2
    x2 = np.array([1, 2, 3, 4, 5]) + 0.2
    plt.ylim(0, 35)

    plt.bar(x1, y1, align='center', width=0.4, color="green")
    plt.bar(x2, y2, align='center', width=0.4, color="red")
    plt.legend(['men', 'women'])


def num5_7():
    plt.title('№5_7')
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    y = [23, 18.5, 9.8, 8, 7.8, 6.9]
    explode = [0.3, 0, 0, 0, 0, 0]
    plt.pie(y, labels=x, shadow=True, explode=explode, autopct='%1.2f%%')


def num5_8():
    plt.title('№5_7')
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    y = [23, 18.5, 9.8, 8, 7.8, 6.9]
    explode = [0.3, 0, 0, 0, 0, 0.2]
    plt.pie(y, labels=x, shadow=True, explode=explode, autopct='%1.2f%%')


def num6_2():
    plt.plot((0.0, 100.0), (0.0, 200.0))
    plt.xlabel("x")
    plt.ylabel("y")
    figure.add_axes([0.6, 0.5, 0.17, 0.15])
    plt.plot([0.0, 100.0], [0.0, 200.0])
    plt.xlabel("x")
    plt.ylabel("y")


def num6_3():
    plt.subplot(1, 2, 1)
    plt.plot([0.0, 100.0], [0.0, 200.0], color="blue", linewidth=5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.subplot(1, 2, 2)
    x = np.linspace(0, 100, 100)
    y = x**2
    plt.plot(x, y, color="red", linestyle="--", linewidth=3)
    plt.xlabel("x")
    plt.ylabel("z")
    plt.subplots_adjust(top=1, bottom=0.3, wspace=0.25)


num6_3()
plt.show()