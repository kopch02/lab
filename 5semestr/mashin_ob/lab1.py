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

figure=plt.figure()

plt.title('название')
plt.ylabel('y - axis')
plt.xlabel('x - axis ')


def num1_1():
    plt.title('№1.1')
    plt.plot((0, 1), (0, 1)) #num1


def num1_2():
    plt.title('№1.2')
    plt.plot((10, 20,30), (20, 40,10),linewidth=3)
    plt.plot((10, 20,30), (40, 10,30),color="red",linewidth=5)
    plt.legend(['line1-width-3','line2-width-5'])


def num1_3():
    plt.title('№1.3')
    plt.plot((10, 20,30), (20, 40,10),linestyle="dotted")
    plt.plot((10, 20,30), (40, 10,30),color="red",linestyle="dashed")
    plt.legend(['line1-dotter','line2-dashed'])


def num1_4():
    plt.title('№1.4')
    plt.plot((1, 4,5,6,7), (2,6,3,6,3),color="red",linestyle="dashdot")
    plt.scatter((1, 4,5,6,7), (2,6,3,6,3),color="blue")


def num1_5():
    plt.title('№1.5')
    plt.xlim(0,10)
    plt.ylim(0,30)
    plt.scatter((2,3,5,6,8), (1,5,10,17,20),color="blue",marker="*")
    plt.scatter((3,4,6,7,9), (2,6,11,20,21),color="red")


def num1_6():
    plt.ylabel('Closing Value')
    plt.xlabel('Date ') 
    plt.title('№1.6')
    now = dt.datetime.now()
    then = now + dt.timedelta(days=5)
    days = mdates.drange(now,then,dt.timedelta(days=1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.xlim(0,4)
    plt.ylim(772.5,777.0)
    plt.plot((0,1,2,3,4), (772.5,776.4,776.5,776.9,775.1),color="red")
    plt.scatter((0,1,2,3,4), (772.5,776.4,776.5,776.9,775.1),color="red")
    plt.minorticks_on() 
    plt.gcf().autofmt_xdate()
    plt.grid(True,color="red",which="major")# сетка
    plt.grid(True,linestyle="--",which="minor")# сетка


def num2():
    plt.title('№2')
    plt.ylabel('y - подпись')
    plt.xlabel('x - подпись')
    plt.plot((10, 20,30), (20, 40,10),linestyle="dotted")
    plt.plot((10, 20,30), (40, 10,30),color="red",linestyle="dashed")
    plt.scatter((18,22,27), (12,17,20),color="blue",marker="*")
    plt.legend(['line1-dotter','line2-dashed','markers'])
    plt.minorticks_on() 
    ax = figure.gca()
    ax.yaxis.set_minor_formatter(FormatStrFormatter("%.3f"))
    plt.grid(True)


def num3():
    plt.title('№3')
    x=1
    y=x*x-x-6
    

plt.show()