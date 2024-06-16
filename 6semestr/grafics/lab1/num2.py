import tkinter
import math
import numpy as np

a = 260
h = int(a / 2 * math.sqrt(3))

R = 150
R2 = 75

center = [130, 75]

tria_point = [[0, 0], [a, 0], [a / 2, h]]


def triangel_del():
    canvas.delete(t)


def triangel():
    global canvas, t, h, a
    canvas.delete(t)
    t = canvas.create_polygon(tria_point[0][0],
                              tria_point[0][1],
                              tria_point[1][0],
                              tria_point[1][1],
                              tria_point[2][0],
                              tria_point[2][1],
                              fill="white",
                              outline='black')
    canvas.move(t, 100, 100)
    canvas.create_oval(center[0] + 98,
                       center[1] + 98,
                       center[0] + 102,
                       center[1] + 102,
                       fill="green")


def left():
    global canvas, t, h, a, tria_point

    alf = -np.pi / 4

    canvas.delete(t)
    for i in range(3):

        x = tria_point[i][0]
        y = tria_point[i][1]

        tria_point[i][0] = center[0] + (x - center[0]) * np.cos(alf) - (
            y - center[1]) * np.sin(alf)
        tria_point[i][1] = center[1] + (x - center[0]) * np.sin(alf) + (
            y - center[1]) * np.cos(alf)

    triangel()


def right():
    global canvas, t, h, a, tria_point

    alf = np.pi / 4

    canvas.delete(t)
    for i in range(3):

        x = tria_point[i][0]
        y = tria_point[i][1]

        tria_point[i][0] = center[0] + (x - center[0]) * np.cos(alf) - (
            y - center[1]) * np.sin(alf)
        tria_point[i][1] = center[1] + (x - center[0]) * np.sin(alf) + (
            y - center[1]) * np.cos(alf)

    triangel()


t = tkinter.Tk()

canvas = tkinter.Canvas(t, height=480, width=640)
canvas.pack()

b1 = tkinter.Button(t, text="треугольник", command=triangel)
bd1 = tkinter.Button(t, text="удалить треугольник", command=triangel_del)

b_left = tkinter.Button(t, text="<-", command=left)
b_right = tkinter.Button(t, text="->", command=right)

b_left.place(x=50, y=490)
b_right.place(x=80, y=490)

b1.pack()
bd1.pack()

t.mainloop()