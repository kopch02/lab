import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QSpinBox, QRadioButton,QListWidgetItem
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import uic  # Импортируем uic


class num1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('num3.ui', self)  # Загружаем дизайн
        self.b1.clicked.connect(self.a)
    def a(self):
        item = QListWidgetItem(self.lineEdit.text()+self.lineEdit_2.text())
        self.listWidget.addItem(item)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num1()
    ex.show()
    sys.exit(app.exec_())