import sys

from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog
from PyQt5 import uic
from PyQt5.Qt import QImage
from PIL import Image, ImageOps, ImageFilter
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QColorDialog

from PyQt5.QtCore import QPoint 

from random import randint


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num4.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Отображение картинки')
        self.s = 2
        self.color = "white"
        self.size_sm = 100
        self.b1.clicked.connect(self.run)
        self.slider.valueChanged.connect(self.skale)
    
    def skale(self, value):
        self.size_sm = abs(value - 100)
        self.update()

    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color.name()     

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(self.color))
        center = QPoint(130,170)
        qp.drawEllipse(center, self.size_sm, self.size_sm)

        qp.setBrush(QColor("black"))
        center = QPoint(abs(self.size_sm - 100)//3 + 90, abs(self.size_sm - 100) + 100)
        qp.drawEllipse(center, self.size_sm // 7, self.size_sm // 7)
        center = QPoint(-(abs(self.size_sm - 100)//3) + 170, abs(self.size_sm - 100) + 100)
        qp.drawEllipse(center, self.size_sm // 7, self.size_sm // 7)

        qp.setBrush(QColor("red"))
        center = QPoint(130,-(abs(self.size_sm - 100)//3) + 210)
        qp.drawEllipse(center, self.size_sm//2, self.size_sm // 7)
        
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())