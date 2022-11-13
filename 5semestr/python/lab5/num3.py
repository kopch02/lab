import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtCore import Qt, QPointF
from random import randint
import math


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.drow = None
        self.setStyleSheet("background-color:black;")

    def initUI(self):
        self.setGeometry(300, 300, randint(300,800), randint(300,800))
        self.setMouseTracking(True)


    def mouseMoveEvent(self, event):
        self.x_ = event.x()
        self.y_ = event.y()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.drow = self.drow_circle
        elif (event.button() == Qt.RightButton):
            self.drow = self.drow_rectangle
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.drow = self.draw_triangle
            self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.drow == None:
            pass
        else:
            self.drow(qp)
        qp.end()

    def getRandomColor(self):
        return QColor(randint(0, 255), randint(0, 255), randint(0, 255))

    def drow_circle(self, qp):
        qp.setBrush(self.getRandomColor())
        center = QPointF(self.x_,self.y_)
        circle_size = randint(10,80)
        qp.drawEllipse(center, circle_size, circle_size)
    
    def drow_rectangle(self, qp):
        qp.setBrush(self.getRandomColor())
        rect_size = randint(10,80)
        qp.drawRect(self.x_ - rect_size // 2,self.y_ - rect_size // 2, rect_size, rect_size)
    
    def draw_triangle(self, qp):
        a = randint(10,80)
        d = a * math.tan(math.radians(30))

        pos_top = QPointF(self.x_,self.y_)
        pos_left = QPointF(self.x_ - d, self.y_ + a)
        pos_right = QPointF(self.x_ + d, self.y_ + a) 
        
        qp.setBrush(self.getRandomColor())
        path = QPainterPath()
        path.moveTo(pos_top)
        path.lineTo(pos_right)
        path.lineTo(pos_left)

        qp.drawPath(path)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())