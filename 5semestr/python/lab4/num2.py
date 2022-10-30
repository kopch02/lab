import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic
from PyQt5 import QtCore, QtGui

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num2.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Отображение картинки')
        self.set_frame()
        self.slider_alpha.valueChanged.connect(self.onValueChanged)
    
    def onValueChanged(self, value):
        new_pix = QtGui.QPixmap(self.pixmap.size())
        new_pix.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(new_pix)
        painter.setOpacity(abs(value - 100) * 0.01)
        painter.drawPixmap(QtCore.QPoint(), self.pixmap)
        painter.end()
        self.image.setPixmap(new_pix)
        

    def set_frame(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        self.pixmap = QPixmap(fname[0])
        self.pixmap = self.pixmap.scaled(self.pixmap.width() // 5,
                                         self.pixmap.height() // 5)
        self.image.resize(self.pixmap.width(), self.pixmap.height())
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())