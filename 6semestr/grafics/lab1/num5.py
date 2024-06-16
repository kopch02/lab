import tkinter
import numpy as np

def draw_point(x,y):
    #canvas.create_line(x,y,x+1,y)
    canvas.create_rectangle(x,y,x+1,y+1,fill='black')


def draw_line(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    k = dy / dx
    x = x1
    y = y1
    while x <= x2:
        draw_point(x,y)
        y += int(k)
        x += 1


def func(x,y, R):
    return x ** 2 + y ** 2 - R ** 2


def draw_circle_18(x,y, x_c,y_c):
    draw_point(x_c + x, y_c + y)
    draw_point(x_c - x, y_c + y)
    draw_point(x_c + x, y_c - y)
    draw_point(x_c - x, y_c - y)

    draw_point(x_c + y, y_c + x)
    draw_point(x_c - y, y_c + x)
    draw_point(x_c + y, y_c - x)
    draw_point(x_c - y, y_c - x)
    


def draw_circle(R,x_c=200,y_c=200):
    x = 0
    y = R
    draw_point(x,y)
    while x <= y :
        if func(x + 1, y - 0.5, R) > 0:
            y -= 1
        x = x + 1
        draw_circle_18(x,y, x_c,y_c)


tk = tkinter.Tk()
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()
draw_line(100,100,200,200)
draw_circle(200)
tk.mainloop()
