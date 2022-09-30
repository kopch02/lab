import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QSpinBox, QRadioButton, QListWidgetItem,QStatusBar
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import uic  # Импортируем uic
from random import randint
from time import sleep


class num4(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('num5.ui', self)
        self.label=QLabel("asd",self)
        self.statusbar.addWidget(self.label)
        self.b1.clicked.connect(self.anti_plag)
    def anti_plag(self):
        textEdit
        textEdit_2
        self.statusbar.setStyleSheet("background-color:Green;")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num4()
    ex.show()
    sys.exit(app.exec_())