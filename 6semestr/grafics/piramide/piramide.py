import numpy as np
import tkinter as tk


class Point2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3d:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get2D(self):
        x = (self.x - self.z) / np.sqrt(2)
        y = (self.x + 2 * self.y + self.z) / np.sqrt(6)
        return Point2d(x + 250, y + 250)

    def rotate(self, roll_, pitch_, yaw_):
        roll = (roll_ / 180) * np.pi
        pitch = (pitch_ / 180) * np.pi
        yaw = (yaw_ / 180) * np.pi
        X = self.x
        Y = self.y
        Z = self.z
        self.x = np.cos(yaw) * np.cos(pitch) * X + (
            np.cos(yaw) * np.sin(pitch) * np.sin(roll) - np.sin(yaw) *
            np.cos(roll)) * Y + (np.cos(yaw) * np.sin(pitch) * np.cos(roll) +
                                 np.sin(yaw) * np.sin(roll)) * Z
        self.y = np.sin(yaw) * np.cos(pitch) * X + (
            np.sin(yaw) * np.sin(pitch) * np.sin(roll) + np.cos(yaw) *
            np.cos(roll)) * Y + (np.sin(yaw) * np.sin(pitch) * np.cos(roll) -
                                 np.cos(yaw) * np.sin(roll)) * Z
        self.z = -np.sin(pitch) * X + np.cos(pitch) * np.sin(
            roll) * Y + np.cos(pitch) * np.cos(roll) * Z

    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz


class Line2d:

    def __init__(self, pointA: Point2d, pointB: Point2d):
        self.A = pointA
        self.B = pointB


class Line3d:

    def __init__(self, pointA: Point3d, pointB: Point3d, collor = "black"):
        self.A = pointA
        self.B = pointB
        self.collor = collor

    def draw(self, canvas: tk.Canvas):
        A2 = self.A.get2D()
        B2 = self.B.get2D()

        canvas.create_line(A2.x, A2.y, B2.x, B2.y, fill = self.collor)


class Pyramid3d:

    def __init__(self, pointA: Point3d, pointB: Point3d, pointC: Point3d,
                 pointD: Point3d):
        self.A = pointA
        self.B = pointB
        self.C = pointC
        self.D = pointD
        self.AB = Line3d(self.A, self.B, collor = "red")
        self.AC = Line3d(self.A, self.C, collor = "red")
        self.BC = Line3d(self.B, self.C, collor = "blue")
        self.AD = Line3d(self.A, self.D, collor = "red")
        self.BD = Line3d(self.B, self.D, collor = "blue")
        self.CD = Line3d(self.C, self.D, collor = "blue")
        self.get_center()
        self.get_top()

    def get_center(self):
        centerX = (self.A.x + self.B.x + self.C.x + self.D.x) / 4
        centerY = (self.A.y + self.B.y + self.C.y + self.D.y) / 4
        centerZ = (self.A.z + self.B.z + self.C.z + self.D.z) / 4
        self.center = Point3d(centerX, centerY, centerZ)

    def get_top(self):
        centerX = (self.A.x + self.B.x + self.C.x + self.D.x) / 4
        centerY = (self.A.y + self.B.y + self.C.y + self.D.y) / 4
        centerZ = (self.A.z + self.B.z + self.C.z + self.D.z) / 4

        base = np.sqrt((self.B.x - self.A.x)**2 + (self.B.y - self.A.y)**2 +
                       (self.B.z - self.A.z)**2)

        length = base / np.sqrt(2)
        height = np.sqrt(length**2 - (base / 2)**2)
        self.hhh = Point3d(centerX, height, centerZ)

    def draw(self, canvas: tk.Canvas):
        canvas.delete("all")
        self.AB.draw(canvas)
        self.AC.draw(canvas)
        self.BC.draw(canvas)
        self.AD.draw(canvas)
        self.BD.draw(canvas)
        self.CD.draw(canvas)
        center = self.center.get2D()

    def rotate(self, a, b, y):
        self.A.rotate(a, b, y)
        self.B.rotate(a, b, y)
        self.C.rotate(a, b, y)
        self.D.rotate(a, b, y)
        self.get_center()
        self.get_top()

    def move(self, dx, dy, dz):
        self.A.move(dx, dy, dz)
        self.B.move(dx, dy, dz)
        self.C.move(dx, dy, dz)
        self.D.move(dx, dy, dz)
        self.get_center()
        self.get_top()


def rotateX():
    pyramid.rotate(10, 0, 0)
    pyramid.draw(canvas)


def rotateY():
    pyramid.rotate(0, 10, 0)
    pyramid.draw(canvas)


def rotateZ():
    pyramid.rotate(0, 0, -10)
    pyramid.draw(canvas)


width = 600
height = 600
t = tk.Tk()
canvas = tk.Canvas(t, width=width, height=height)
canvas.pack()

pyramid = Pyramid3d(
    Point3d(0, 0, 0),
    Point3d(100, 0, 0),
    Point3d(0, 100, 0),
    Point3d(0, 0, 100),
)
pyramid.draw(canvas)

b1 = tk.Button(t, text="x", command=rotateX)
b2 = tk.Button(t, text="z", command=rotateY)  #лево право
b3 = tk.Button(t, text="y", command=rotateZ)

b1.pack()
b2.pack()
b3.pack()

t.mainloop()