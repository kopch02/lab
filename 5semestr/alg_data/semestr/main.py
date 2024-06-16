from merge import merge_sort
from timeit import Timer
import random
import matplotlib.pyplot as plt


def num1():
    some_list = [7, 3, 9, 4, 2, 5, 6, 1, 8]
    print(some_list)
    merge_sort(some_list)
    print(some_list)


num1()

def almost(r):
    a = list(range(r))
    x, y = r//2, r//4
    a[x], a[x + y] = a[x + y], a[x]
    return a

def almost_reverse(r):
    a = list(range(r))
    a.reverse()
    x, y = r//2, r//4
    a[x], a[x + y] = a[x + y], a[x]
    return a

def list_95(r):
    a = list(range(r))
    idx = int(r * 0.95)
    a[idx:] = [random.random() for _ in range(r - idx)]
    return a

def var10(r):
    a = list(range(r))
    chunks = [10 * x for x in range(r//10)]
    for chunk in chunks:
        aa = a[chunk:chunk+10]
        random.shuffle(aa)
        a[chunk:chunk+10] = aa
    return a