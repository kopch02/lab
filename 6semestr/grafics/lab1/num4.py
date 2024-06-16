import tkinter
import math
import numpy as np

class Rect:
    def __init__(self):
        pass

class Myline:
    def __init__(self):
        pass

names = ["T1_left","T1_right","T1_up","T1_down",
         "T2_left","T2_right","T2_up","T2_down",
         "T3_left","T3_right","T3_up","T3_down",]

def triangel_del():
    canvas.delete(t)


def triangel(T1,T2,T3,size = False, x_raz = 0, y_raz = 0):
    global canvas, t1,t2,t3, h, a, T_true_1, T_true_2, T_true_3
    canvas.delete(t1,t2,t3)
    
    t1 = canvas.create_line(T1.x1,T1.y1,T1.x2,T1.y2) #верх
    t2 = canvas.create_line(T2.x1,T2.y1,T2.x2,T2.y2) #право
    t3 = canvas.create_line(T3.x1,T3.y1,T3.x2,T3.y2) #лево

    
    
    

def left(e):
    global canvas,t1,t2,t3, T_true_1, T_true_2, T_true_3
    T1.x1 -= 10
    T1.x2 -= 10
    T2.x1 -= 10
    T2.x2 -= 10
    T3.x1 -= 10
    T3.x2 -= 10

    T_true_1.x1 -= 10
    T_true_1.x2 -= 10
    T_true_2.x1 -= 10
    T_true_2.x2 -= 10
    T_true_3.x1 -= 10
    T_true_3.x2 -= 10
    check()



def right(e):
    global canvas, t1,t2,t3, T_true_1, T_true_2, T_true_3
    T1.x1 += 10
    T1.x2 += 10
    T2.x1 += 10
    T2.x2 += 10
    T3.x1 += 10
    T3.x2 += 10

    T_true_1.x1 += 10
    T_true_1.x2 += 10
    T_true_2.x1 += 10
    T_true_2.x2 += 10
    T_true_3.x1 += 10
    T_true_3.x2 += 10
    check()



def up(e):
    global canvas, t1,t2,t3, T_true_1, T_true_2, T_true_3
    T1.y1 -= 10
    T1.y2 -= 10
    T2.y1 -= 10
    T2.y2 -= 10
    T3.y1 -= 10
    T3.y2 -= 10

    T_true_1.y1 -= 10
    T_true_1.y2 -= 10
    T_true_2.y1 -= 10
    T_true_2.y2 -= 10
    T_true_3.y1 -= 10
    T_true_3.y2 -= 10
    check()



def down(e):
    global canvas, t1,t2,t3, T_true_1, T_true_2, T_true_3
    T1.y1 += 10
    T1.y2 += 10
    T2.y1 += 10
    T2.y2 += 10
    T3.y1 += 10
    T3.y2 += 10

    T_true_1.y1 += 10
    T_true_1.y2 += 10
    T_true_2.y1 += 10
    T_true_2.y2 += 10
    T_true_3.y1 += 10
    T_true_3.y2 += 10
    check()


def turn(e, alf):
    global canvas, T_true_1, T_true_2, T_true_3

    y_c = (T1.y1 + T3.y2 + T1.y2) / 3
    x_c = (T1.x1 + T1.x2 + T2.x2) / 3

    center = [x_c,y_c]

    x = T1.x1
    y = T1.y1

    new_x1 = center[0] + (x - center[0]) * np.cos(alf) - (
        y - center[1]) * np.sin(alf)
    new_y1 = center[1] + (x - center[0]) * np.sin(alf) + (
        y - center[1]) * np.cos(alf)
    

    x = T1.x2
    y = T1.y2

    new_x2 = center[0] + (x - center[0]) * np.cos(alf) - (
        y - center[1]) * np.sin(alf)
    new_y2 = center[1] + (x - center[0]) * np.sin(alf) + (
        y - center[1]) * np.cos(alf)
    

    x = T3.x2
    y = T3.y2

    new_x3 = center[0] + (x - center[0]) * np.cos(alf) - (
        y - center[1]) * np.sin(alf)
    new_y3 = center[1] + (x - center[0]) * np.sin(alf) + (
        y - center[1]) * np.cos(alf)


    T_true_1.y1 = new_y1
    T_true_1.y2 = new_y2
    T_true_2.y1 = new_y2
    T_true_2.y2 = new_y3
    T_true_3.y1 = new_y1
    T_true_3.y2 = new_y3

    T_true_1.x1 = new_x1
    T_true_1.x2 = new_x2
    T_true_2.x1 = new_x2
    T_true_2.x2 = new_x3
    T_true_3.x1 = new_x1
    T_true_3.x2 = new_x3

    check()


def size(e, si):
    y_c = (T1.y1 + T3.y2 + T1.y2) / 3
    x_c = (T1.x1 + T1.x2 + T2.x2) / 3
    center = [x_c,y_c]
    vek1 = np.array([x_c,y_c,T1.x1,T1.y1])
    vek2 = np.array([x_c,y_c,T1.x2,T1.y2])
    vek3 = np.array([x_c,y_c,T2.x2,T2.y2])
    vek1 *= si
    vek2 *= si
    vek3 *= si

    new_x_c = (vek1[2] + vek2[2] + vek3[2]) / 3
    new_y_c = (vek1[3] + vek2[3] + vek3[3]) / 3
    new_center = [new_x_c,new_y_c]

    x_raz = new_x_c - x_c
    y_raz = new_y_c - y_c

    T_true_1.y1 = vek1[3]
    T_true_1.y2 = vek2[3]
    T_true_2.y1 = vek2[3]
    T_true_2.y2 = vek3[3]
    T_true_3.y1 = vek1[3]
    T_true_3.y2 = vek3[3]

    T_true_1.x1 = vek1[2]
    T_true_1.x2 = vek2[2]
    T_true_2.x1 = vek2[2]
    T_true_2.x2 = vek3[2]
    T_true_3.x1 = vek1[2]
    T_true_3.x2 = vek3[2]

    canvas.move(T1,x_raz, y_raz)
    canvas.move(T2,x_raz, y_raz)
    canvas.move(T3,x_raz, y_raz)

    check(size = True, x_raz= -x_raz, y_raz= -y_raz)


def check(size = False, x_raz = 0, y_raz = 0):
    global rect_coords, canvas, t1,t2,t3, T_true_1, T_true_2, T_true_3
    T1.x1 = T_true_1.x1
    T1.y1 = T_true_1.y1
    T1.x2 = T_true_1.x2
    T1.y2 = T_true_1.y2

    T2.x1 = T_true_2.x1
    T2.y1 = T_true_2.y1
    T2.x2 = T_true_2.x2
    T2.y2 = T_true_2.y2

    T3.x1 = T_true_3.x1
    T3.y1 = T_true_3.y1
    T3.x2 = T_true_3.x2
    T3.y2 = T_true_3.y2
    
    triangel(T1,T2,T3)
    if size:
        canvas.move(t1,x_raz, y_raz)
        canvas.move(t2,x_raz, y_raz)
        canvas.move(t3,x_raz, y_raz)
        pos1 = canvas.coords(t1)
        pos2 = canvas.coords(t2)
        pos3 = canvas.coords(t3)
        print(pos1)
        print(pos2)
        print(pos3)
        T1.x1 = pos1[0]
        T1.y1 = pos1[1]
        T1.x2 = pos1[2]
        T1.y2 = pos1[3]

        T2.x1 = pos2[0]
        T2.y1 = pos2[1]
        T2.x2 = pos2[2]
        T2.y2 = pos2[3]

        T3.x1 = pos3[0]
        T3.y1 = pos3[1]
        T3.x2 = pos3[2]
        T3.y2 = pos3[3]
    

    left_rec = [rect_coords.x1,rect_coords.y1,rect_coords.x1,rect_coords.y2]
    right_rec = [rect_coords.x2,rect_coords.y1,rect_coords.x2,rect_coords.y2]
    up_rec = [rect_coords.x1,rect_coords.y1,rect_coords.x2,rect_coords.y1]
    down_rec = [rect_coords.x1,rect_coords.y2,rect_coords.x2,rect_coords.y2]

    mega_rec_coords = [left_rec,right_rec,up_rec,down_rec]

    coords_t1 = [T1.x1,T1.y1,T1.x2,T1.y2]
    coords_t2 = [T2.x1,T2.y1,T2.x2,T2.y2]
    coords_t3 = [T3.x1,T3.y1,T3.x2,T3.y2]

    mega_coords = [coords_t1,coords_t2,coords_t3]
    
    dots = {}
    n = 0
    if T1.x1 <= rect_coords.x1 or T1.x2 >= rect_coords.x2 or T1.y1 < rect_coords.y1 or T3.y2 >= rect_coords.y2:
        for i in mega_coords:
            for j in mega_rec_coords:
                dots[names[n]] = cross(i[0],i[1],i[2],i[3],j[0],j[1],j[2],j[3])
                n+=1
    if T1.x1 <= rect_coords.x1:
        T1.x1 = dots["T1_left"][0]
        T1.y1 = dots["T1_left"][1]
        T3.x1 = dots["T3_left"][0]
        T3.y1 = dots["T3_left"][1]
    
    if T2.x2 <= rect_coords.x1:
        T2.x2 = dots["T2_left"][0]
        T2.y2 = dots["T2_left"][1]
        T3.x2 = rect_coords.x1
        T3.y1 = rect_coords.y1
        T3.y2 = rect_coords.y1
        if T2.y2 >= rect_coords.y2:
            T2.y2 = rect_coords.y2
            T2.x2 = dots["T2_down"][0]
            T3.x1 = rect_coords.x1
            T3.x2 = rect_coords.x1
            T3.y1 = rect_coords.y2
            T3.y2 = rect_coords.y2

    if T1.x2 >= rect_coords.x2:
        T1.x2 = dots["T1_right"][0]
        T1.y2 = dots["T1_right"][1]
        T2.x1 = dots["T2_right"][0]
        T2.y1 = dots["T2_right"][1]

    if T3.x2 >= rect_coords.x2:
        T3.x2 = dots["T3_right"][0]
        T3.y2 = dots["T3_right"][1]
        T2.x2 = rect_coords.x2

    if T1.y1 < rect_coords.y1:
        T1.y1 = rect_coords.y1
        T1.y2 = rect_coords.y1
        T2.x1 = dots["T2_up"][0]
        T2.y1 = dots["T2_up"][1]
        if T1.x1 <= rect_coords.x1:
            pass
        else:
            T3.x1 = dots["T3_up"][0]
            T3.y1 = dots["T3_up"][1]
        
        if T2.x1 >= rect_coords.x2:
            T2.x1 = dots["T2_right"][0]
            T2.y1 = dots["T2_right"][1]
        
    
    if T3.y2 >= rect_coords.y2:
        T2.x2 = dots["T2_down"][0]
        T2.y2 = dots["T2_down"][1]
        T3.x2 = dots["T3_down"][0]
        T3.y2 = dots["T3_down"][1]
        if T3.x2 <= rect_coords.x1:
            T3.x2 = rect_coords.x1
            T3.y1 = rect_coords.y2
        if T2.y1 >= rect_coords.y2:
            T2.y1 = rect_coords.y2
            T2.x2 = rect_coords.x2
    
    yy = [T1.y1,T1.y2,T2.y1,T2.y2,T3.y1,T3.y2]
    xx = [T1.x1,T1.x2,T2.x1,T2.x2,T3.x1,T3.x2]
    if T1.x1<=rect_coords.x1:
        T1.x1 = rect_coords.x1
        if T1.x2 <= rect_coords.x1:
            T1.x2 = rect_coords.x1
    
    if T1.x2>=rect_coords.x2:
        T1.x2 = rect_coords.x2
        if T1.x1 >= rect_coords.x2:
            T1.x1 = rect_coords.x2

    if T2.x1<=rect_coords.x1:
        T2.x1 = rect_coords.x1
        if T2.x2 <= rect_coords.x1:
            T2.x2 = rect_coords.x1
    
    if T2.x2>=rect_coords.x2:
        T2.x2 = rect_coords.x2
        if T2.x1 >= rect_coords.x2:
            T2.x1 = rect_coords.x2
    
    if T3.x1<=rect_coords.x1:
        T3.x1 = rect_coords.x1
        if T3.x2 <= rect_coords.x1:
            T3.x2 = rect_coords.x1
    
    if T3.x2>=rect_coords.x2:
        T3.x2 = rect_coords.x2
        if T3.x1 >= rect_coords.x2:
            T3.x1 = rect_coords.x2

    if T1.y1<=rect_coords.y1:
        T1.y1 = rect_coords.y1
        if T1.y2 <= rect_coords.y1:
            T1.y2 = rect_coords.y1

    if T2.y1<=rect_coords.y1:
        T2.y1 = rect_coords.y1
        if T2.y2 <= rect_coords.y1:
            T2.y2 = rect_coords.y1
    
    if T3.y1<=rect_coords.y1:
        T3.y1 = rect_coords.y1
        if T3.y2 <= rect_coords.y1:
            T3.y2 = rect_coords.y1

    if T1.y2>=rect_coords.y2:
        T1.y2 = rect_coords.y2
        if T1.y1 >= rect_coords.y2:
            T1.y1 = rect_coords.y2

    if T2.y2>=rect_coords.y2:
        T2.y2 = rect_coords.y2
        if T2.y1 >= rect_coords.y2:
            T2.y1 = rect_coords.y2
    
    if T3.y2>=rect_coords.y2:
        T3.y2 = rect_coords.y2
        if T3.y1 >= rect_coords.y2:
            T3.y1 = rect_coords.y2

    if T2.y2 <= 50 :
        T2.y2 = rect_coords.y1
    if T3.y2 <= 50 :
        T3.y2 = rect_coords.y1
    if T2.y1 >= 300 :
        T2.y1 = rect_coords.y2

    
    triangel(T1,T2,T3)
    


def f():
    global t
    if t in canvas.find_overlapping(100, 50, 400, 300):
        print('see on rect1')
    triangel()


def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    n = 0
    dot = [None, None]
    if (y2 - y1 != 0):  #a(y)
        q = (x2 - x1) / (y1 - y2)
        sn = (x3 - x4) + (y3 - y4) * q
        if not (sn):
            return  # c(x) + c(y)*q
        fn = (x3 - x1) + (y3 - y1) * q  # b(x) + b(y)*q
        n = fn / sn
    else:
        if not (y3 - y4):
            return  # b(y)
        n = (y3 - y1) / (y3 - y4)
        # c(y)/b(y)

    dot[0] = x3 + (x4 - x3) * n
    # x3 + (-b(x))*n
    dot[1] = y3 + (y4 - y3) * n
    # y3 +(-b(y))*n
    return dot


a = 100
h = int(a / 2 * math.sqrt(3))


T1 = Myline()
T1.x1 = 200
T1.y1 = 100
T1.x2 = 200 + a
T1.y2 = 100

T2 = Myline()
T2.x1 = 200 + a
T2.y1 = 100
T2.x2 = 200 + a / 2
T2.y2 = h + 100

T3 = Myline()
T3.x1 = 200
T3.y1 = 100
T3.x2 = 200 + a / 2
T3.y2 = h + 100


T_true_1 = Myline()
T_true_1.x1 = 200
T_true_1.y1 = 100
T_true_1.x2 = 200 + a
T_true_1.y2 = 100

T_true_2 = Myline()
T_true_2.x1 = 200 + a
T_true_2.y1 = 100
T_true_2.x2 = 200 + a / 2
T_true_2.y2 = h + 100

T_true_3 = Myline()
T_true_3.x1 = 200
T_true_3.y1 = 100
T_true_3.x2 = 200 + a / 2
T_true_3.y2 = h + 100


tk = tkinter.Tk()
tk.geometry("500x400")

canvas = tkinter.Canvas(tk, height=480, width=640)
canvas.pack()

#rect_coords = [[100, 50], [400, 300]]
rect_coords = Rect
rect_coords.x1 = 100
rect_coords.y1 = 50
rect_coords.x2 = 400
rect_coords.y2 = 300

canvas.create_rectangle(rect_coords.x1, rect_coords.y1,
                        rect_coords.x2, rect_coords.y2)

canvas.bind_all("<Left>", left)
canvas.bind_all("<Right>", right)
canvas.bind_all("<Up>", up)
canvas.bind_all("<Down>", down)
canvas.bind_all("<q>", lambda e, alf=-np.pi / 4: turn(e, alf))
canvas.bind_all("<e>", lambda e, alf=np.pi / 4: turn(e, alf))
canvas.bind_all("<a>", lambda e, si = 1.1: size(e, si))
canvas.bind_all("<s>", lambda e, si = 0.9: size(e, si))

t1 = canvas.create_line(T1.x1,T1.y1,T1.x2,T1.y2)
t2 = canvas.create_line(T2.x1,T2.y1,T2.x2,T2.y2)
t3 = canvas.create_line(T3.x1,T3.y1,T3.x2,T3.y2)

tk.mainloop()