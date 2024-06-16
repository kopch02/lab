from typing import Sequence
import math
from decimal import *
import copy
import statistics
import random
from scipy import stats
import numpy as np
from prettytable import PrettyTable
import scipy.stats as stats


def checking_hypo(z):
    global theorFrequnces

    h = (max(z) - min(z)) / (1.0 + 3.3231 * math.log10(100))

    ranges = []
    ranges.append([min(z), min(z) + h])
    i = 0.0
    while min(z) + i * h <= max(z) - h:
        i += 1.0
        ranges.append([min(z) + i * h, min(z) + (i + 1.0) * h])

    print(f"{np.array(ranges) = }")

    phi = lambda u: math.e**((-u**2) / 2) / math.sqrt(2 * math.pi)
    theorFrequences = []
    for i in range(len(ranges)):
        ui = ((ranges[i][0] + ranges[i][1]) / 2 - x_) / sigma
        theorFrequences.append((n * h * phi(ui)) / sigma)

    print(f"{theorFrequences = }")  #теоретические частоты

    frequences = []
    for i in ranges:
        count = 0
        for j in range(len(z)):
            if z[j] >= i[0] and z[j] <= i[1]:
                count += 1
        frequences.append(count)

    print(f"{frequences = }")  # частоты

    frequencesCopy = copy.copy(frequences)
    #theorFrequncesCopy = copy.copy(theorFrequnces)

    frequncesUnion(theorFrequences, frequences)

    print(f"{theorFrequences = }")  #теоретические частоты после объединения
    print(f"{frequences = }")  #Частоты(после объединения)

    hiSqrLook = 0

    for i in range(len(frequences)):
        hiSqrLook += (frequences[i] - theorFrequences[i])**2 / theorFrequences[i]

    # alpha = 0.05 к=3
    hiSqrLook_krit = stats.chi2.ppf(1 - .05, df=len(theorFrequences) )
    print("Хи квадрат: ", hiSqrLook)
    print("Хи кр квадрат: ", hiSqrLook_krit)

    if hiSqrLook < hiSqrLook_krit:
        print("Гипотеза принимается")
    else:
        print("Гипотеза отвергается")

    # Для 6 элементов значение таблицы = 3,182; для 7 = 2,776; для 8 = 2,571; для 5 = 4,303

    ##### 4.

    xmiddles = []

    for i in range(len(ranges)):
        xmiddles.append((ranges[i][0] + ranges[i][1]) / 2)

    stashedFrequences = []
    stashedFrequences.append(frequencesCopy[0])
    i = 1

    while i < len(frequencesCopy):
        stashedFrequences.append(stashedFrequences[i - 1] + frequencesCopy[i])
        i += 1

    #print(stashedFrequences)

    fn = list(np.array(stashedFrequences) / n)

    f = list(stats.norm.cdf((np.array(xmiddles) - x_) / sigma))

    print('f(x)', f)

    d = []
    for i in range(len(f)):
        d.append(math.fabs(f[i] - fn[i]))

    dMax = max(d)
    lambd = dMax * math.sqrt(n)

    print(f"{lambd = }")

    my_table = PrettyTable()

    my_table.add_column("xi", xmiddles)
    my_table.add_column("ni", frequencesCopy)
    my_table.add_column("nНак", stashedFrequences)
    my_table.add_column("Fn(x)= nнак/n", fn)
    my_table.add_column("F(x)", f)
    my_table.add_column("| Fn(x) - F(x) |", d)

    print(my_table)


def frequncesUnion(theorFrequences, frequences):
    i = len(theorFrequences) - 1
    mega_i = len(theorFrequences) - 1

    while i >= 0:
        if i == mega_i:
            if theorFrequences[0] < 5 or frequences[0] < 5:
                i -= 1
                theorFrequences[1] += theorFrequences[0]
                frequences[1] += frequences[0]
                del theorFrequences[0]
                del frequences[0]
                continue

        if theorFrequences[i] < 5.0:
            if i != len(theorFrequences) - 1:
                left = theorFrequences[i - 1]
                right = theorFrequences[i + 1]
                if left < right:
                    theorFrequences[i - 1] += theorFrequences[i]
                    frequences[i - 1] += frequences[i]
                    theorFrequences.pop(i)
                    frequences.pop(i)
                else:
                    theorFrequences[i + 1] += theorFrequences[i]
                    frequences[i + 1] += frequences[i]
                    theorFrequences.pop(i)
                    frequences.pop(i)
            else:
                theorFrequences[len(theorFrequences) -
                                2] += theorFrequences[len(theorFrequences) - 1]
                frequences[len(frequences) - 2] += frequences[len(frequences) -
                                                              1]
                frequences.pop(len(frequences) - 1)
                theorFrequences.pop(len(theorFrequences) - 1)
        i -= 1


#np.random.seed(0)

lambd = 0.1

xi = np.array(np.random.rand(1, 100)[0])

xi = -(1 / lambd) * np.log(xi)

#print("values: ", xi)
M = 1 / lambd  #10
D = 1 / lambd**2  #100

x_ = np.sum(xi) / len(xi)
disper = statistics.stdev(xi)**2

print(f"Мат.ожидание: {x_}")
print(f"{disper = }")

print(f"Ошибки мат.ож.: {abs(x_ - M)}")
print(f"Ошибки дисперсии: {abs(disper - D)}")

h = (Decimal(max(xi)) - Decimal(min(xi))) / (
    Decimal(1.0) + Decimal(3.3231) * Decimal(math.log10(100)))
h = float(h)

print(f"{h = }")

ranges = []  #отрезки
ranges.append([min(xi), min(xi) + h])
i = 0.0
while min(xi) + i * h <= max(xi) - h:
    i += 1.0
    ranges.append([min(xi) + i * h, min(xi) + (i + 1.0) * h])

print(f"{np.array(ranges) = }")

frequences = []  #частоты
for r in ranges:
    count = 0
    for j in range(len(xi)):
        if xi[j] >= r[0] and xi[j] <= r[1]:
            count += 1
    frequences.append(count)

print(f"{frequences = }")

middles = []  #середины отрезков
for r in ranges:
    middles.append((r[0] + r[1]) / 2)

print(f"{middles = }")

x_line = (1 / 100) * sum(
    np.array(middles) * np.array(frequences))  #выборочное среднее
print(f"{x_line = }")
lambd = 1 / x_line
print(f"{lambd = }")

frequencesExp = []
for i in range(len(ranges)):
    frequencesExp.append(math.e**(-lambd * ranges[i][0]) -
                         math.e**(-lambd * ranges[i][1]))

print(f"{frequencesExp = }")  #вероятности попадания в интервалы

theorFrequences = list(100 * np.array(frequencesExp))

print(f"{theorFrequences = }")  #теоретические частоты

frequncesUnion(theorFrequences, frequences)

print(f"{theorFrequences = }")  #теоретические частоты после объединения
print(f"{frequences = }")  #Частоты(после объединения)

pirson = 0
for i in range(len(theorFrequences) ):
    pirson += ((frequences[i] - theorFrequences[i])**2) / theorFrequences[i]

pirson_krit = stats.chi2.ppf(1 - .05, df=len(theorFrequences) )

print(f"{pirson = }")
print(f"{pirson_krit = }")

if pirson < pirson_krit:
    print("Гипотеза принимается")
else:
    print("Гипотеза отвергается")

# alpha = 0.05
# k = s - 2
#

# ##### Моделирование нормально распределенных СВ

# ##### 1.

n = 100

r = []
for i in range(n):
    r.append([])
    for j in range(12):
        r[i].append(random.random())

z = []

for i in r:
    summa = 0
    for j in i:
        summa += j
    z.append(summa - 6)

for i in range(len(z)):
    z[i] = z[i] * 0.25 + 3

#print(z)
x_ = np.sum(z) / len(z)
sigma = statistics.stdev(z)  #сдреднее квадратическое отклонение -- sigmaCH

print('Мат.ожидание: ', x_)
print(f"{sigma = }")

print('Ошибки оценивания мат.ож.: ', math.fabs(x_ - 3.0))
print('Ошибки оценивания ср.кв.откл.: ', math.fabs(sigma - 0.25))
##### 2.

r1 = [random.random() for _ in range(n)]
r2 = [random.random() for _ in range(n)]

zMuller = []

for i in range(n):
    zMuller.append(
        math.sqrt(-2.0 * math.log(r1[i])) * math.cos(2 * math.pi * r2[i]) *
        0.25 + 3)

math_waiting_muller = np.sum(zMuller) / len(zMuller)
sigma_muller = statistics.stdev(zMuller)

print(f"{math_waiting_muller = }")
print(f"{sigma_muller = }")

print('Ошибки оценивания мат.ож.(Мюллер): ',
      math.fabs(math_waiting_muller - 3.0))
print('Ошибки оценивания ср.кв.откл.(Мюллер): ',
      math.fabs(sigma_muller - 0.25))

##### 3.

checking_hypo(z)

print('\n')
checking_hypo(zMuller)