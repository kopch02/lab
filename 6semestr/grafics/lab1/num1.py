import tkinter

def circle():
    global canvas,cir
    cir = canvas.create_oval(50,50,150,150)

def circle_del():
    global canvas,cir
    canvas.delete(cir)


def sqare_del():
    global canvas,sq
    canvas.delete(sq)


def triangel_del():
    global canvas,t1,t2,t3
    canvas.delete(t1,t2,t3)


def sqare():
    global canvas, sq
    sq = canvas.create_rectangle(100,100,250,250)
    
def triangel():
    global canvas,t1,t2,t3
    t1 = canvas.create_line(70,70,120,70)
    t2 = canvas.create_line(120,70,95,170)
    t3 = canvas.create_line(95,170,70,70)


t = tkinter.Tk()

canvas = tkinter.Canvas(t,height= 480, width=640)
canvas.pack()

b1 = tkinter.Button(t,text="круг", command= circle)
b2 = tkinter.Button(t,text="квадрат", command=sqare)
b3 = tkinter.Button(t,text="треугольник", command=triangel)
bd1 = tkinter.Button(t,text="удалить круг", command= circle_del)
bd2 = tkinter.Button(t,text="удалить квадрат", command= sqare_del)
bd3 = tkinter.Button(t,text="удалить треугольник", command= triangel_del)

b1.pack()
b2.pack()
b3.pack()

bd1.pack()
bd2.pack()
bd3.pack()

t.mainloop()