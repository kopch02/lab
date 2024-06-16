from operator import delitem
import numpy as np
from PIL import Image


def num1():
    # a
    arr_1 = np.zeros((3, 4)) + 3
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
    arr_4 = (arr_3 * 3) + 1
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
    a = (-10 - 10) * np.random.random(10) + 10
    b = a[a < 0]
    print(a)
    print(b)




def num2():

    def make_field(size):
        array = np.zeros((size, size), dtype=np.int8)
        array[(size + 1) % 2::2, 1::2] = 1
        array[size % 2::2, ::2] = 1
        return array

    print(make_field(10))


def num3():

    def super_sort(rows, cols):
        a = np.random.randint(0, 100, (rows, cols))
        b = a.copy()
        b[1::2].sort()  #чётные по возростанию
        b[::2, ::-1].sort()  #не чётные по убыванию
        return (a, b)

    print(*super_sort(10, 10))


def num4():

    def bw_convert(image):
        open_image = Image.open(image)
        print(open_image.mode)
        bw = np.array(open_image)
        c = np.array((0.2989, 0.587, 0.114))
        resul = np.round(bw.dot(c))
        Image.fromarray(resul).convert("RGB").save(
            "4semestr\is\lab8\\result.png", "png")
        open_image.close()

    bw_convert("4semestr\is\lab8\mem.jpg")


def num5():
    table = np.genfromtxt("4semestr\is\lab8\ABBREV.csv",
                          delimiter=";",
                          dtype=None,
                          names=True,
                          encoding="utf8")
    name = table["Shrt_Desc"]
    cal = table["Energ_Kcal"]
    sugar = table["Sugar_Tot"]
    protein = table["Protein"]
    vit_c = table["Vit_C"]
    print("Most calories:", name[len(table) - np.argmax(cal[::-1])])
    print("Least sugar:", name[len(table) - np.argmin(sugar)])
    print("Most protein:", name[len(table) - np.argmax(protein)])
    print("Most vitamin C:", name[len(table) - np.argmax(vit_c)])




def num6():
    from random import randint
    file = open("4semestr\is\lab8\\file_num6.txt", "r+")
    lines = []
    try:
        for line in file:
            lines.append(line)
        print(lines[randint(0, len(lines) - 1)])
    except:
        print("errors")
    file.close()
num6()

def num8():

    def revers(in_file):
        data = in_file.read()
        out = open("4semestr\is\lab8\\num8_files\output.dat", "bw")
        out.write(data[::-1])

    in_file = open("4semestr\is\lab8\\num8_files\input.dat", "br")
    revers(in_file)


def num9():
    file = open("4semestr\is\lab8\\num9_files\input.txt")
    zeros = 0
    negativ = 0
    positiv = 0
    for line in file:
        temp = line.split()
        for token in temp:
            token = int(token)
            if type(token) == int or type(token) == float:
                if token > 0:
                    positiv += 1
                elif token < 0:
                    negativ += 1
                else:
                    zeros += 1
    file.close()

    
    file2 = open("4semestr\is\lab8\\num9_files\output.txt", "r+")
    sum = positiv + negativ + zeros
    file2.write(str(sum) + "\n")
    file2.write("1 - " + str(positiv) + "\n")
    file2.write("-1 - " + str(negativ) + "\n")
    file2.write("0 - " + str(zeros) + "\n")
    file2.close()
