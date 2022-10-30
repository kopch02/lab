import sys

from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog
from PyQt5 import uic
from PyQt5.Qt import QImage
from PIL import Image, ImageOps, ImageFilter
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QInputDialog

from random import randint


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num3.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Отображение картинки')
        self.s = 0
        self.b1.clicked.connect(self.run)
        
    
    def run(self):
        count, ok_pressed = QInputDialog.getInt(
            self, "Введите количество", "сколько линий будет на флаге??",
            3, 1, 10, 1)
        if ok_pressed:
            self.s = count
            self.a = []
            for i in range(self.s):
                self.a.append(randint(0, 255))
                self.a.append(randint(0, 255))
                self.a.append(randint(0, 255))
                

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        for i in range(self.s):
            c = []
            for j in range(3):
                c.append(self.a[i*j])
            qp.setBrush(QColor(c[0], c[1], c[2]))
            qp.drawRect(30, 150 // self.s * i, 200, 150 // self.s)
        
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())