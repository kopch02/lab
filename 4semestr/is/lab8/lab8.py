import numpy as np
from PIL import Image


def num1():
    # a
    arr_1 = np.zeros((3, 4))+3
    print(arr_1)
    # b
    arr_2 = np.random.randint(0, 9, size=(2, 4))
    print(arr_2)
    # c
    print("arr1 size: ", arr_1.size, "\narr2 size: ", arr_2.size)
    # d
    c = np.concatenate((arr_1, arr_2), axis=0)
    print(c)
    # e
    arr_3 = np.array((1, 8, 6, 5, 8, 3))
    print(arr_3)
    # f
    arr_4 = (arr_3*3)+1
    print(arr_4)
    # g
    arr_5 = arr_3.reshape(2, 3)
    print(arr_5)
    # h
    print(np.amin(arr_5, axis=1))
    # i
    print(np.mean(arr_5))
    # j
    arr_6 = np.linspace(0, 10, 11)**2
    print(arr_6)
    # k
    print(arr_6[1::2])
    # l
    print(arr_6[::-1])
    # m
    arr_6[1::2] = 2
    print(arr_6)
    # n
    print(49 in arr_6)
    # o
    a = (-10-10)*np.random.random(10)+10
    b = a[a < 0]
    print(a)
    print(b)


def num2():
    def make_field(size):
        array = np.zeros((size, size), dtype=np.int8)
        array[(size+1) % 2::2, 1::2] = 1
        array[size % 2::2, ::2] = 1
        return array
    print(make_field(10))


def num3():
    def super_sort(rows, cols):
        a =np.random.randint(0,100,(rows,cols))
        b=a.copy()
        b[1::2].sort()#чётные по возростанию
        b[::2,::-1].sort()#не чётные по убыванию
        return (a,b)
        
    print(*super_sort(10,10))


def num4():
    def bw_convert(image):
        r,g,b=(Image.open(image)).split()
        c=0.2989*r+0.5870*g+0.1140*b
        Image.fromarray(np.uint8(c)).save('r2.png')
    bw_convert("4semestr\is\lab8\kek_dimas.png")