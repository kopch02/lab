import sys

from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic
from PyQt5.Qt import QImage
from PIL import Image
from PIL.ImageQt import ImageQt


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num1.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Отображение картинки')
        self.btn_image.clicked.connect(self.set_frame)
        self.left.clicked.connect(self.left_rotate)
        self.right.clicked.connect(self.right_rotate)
        self.groups = [self.red, self.green, self.blue]
        self.chanels = [1, 1, 1]
        e = 0
        for i in self.groups:
            i.clicked.connect(self.a)
            i.id = e
            e += 1

    def a(self):
        if self.red.isChecked():
            self.chanels[0] = 0
        else:
            self.chanels[0] = 1
        if self.green.isChecked():
            self.chanels[1] = 0
        else:
            self.chanels[1] = 1
        if self.blue.isChecked():
            self.chanels[2] = 0
        else:
            self.chanels[2] = 1
        self.set_picture()

    def set_frame(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        self.set_picture()

    def set_picture(self):
        self.img = Image.open(self.fname[0]).convert("RGB")
        r, g, b = self.img.split()
        r = r.point(lambda i: i * self.chanels[0])
        g = g.point(lambda i: i * self.chanels[1])
        b = b.point(lambda i: i * self.chanels[2])
        self.img = Image.merge('RGB', (r, g, b))
        qim = ImageQt(self.img)
        self.pixmap = QPixmap(QImage(qim))
        self.pixmap = self.pixmap.scaled(self.pixmap.width() // 5,
                                         self.pixmap.height() // 5)
        self.image.resize(self.pixmap.width(), self.pixmap.height())
        self.image.setPixmap(self.pixmap)

    def left_rotate(self):
        t = QTransform().rotate(-90)
        self.pixmap = QPixmap(self.pixmap.transformed(t))
        self.image.setPixmap(self.pixmap)

    def right_rotate(self):
        t = QTransform().rotate(+90)
        self.pixmap = QPixmap(self.pixmap.transformed(t))
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())