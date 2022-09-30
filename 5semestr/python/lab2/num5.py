import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QSpinBox, QRadioButton, QListWidgetItem,QStatusBar
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import uic  # Импортируем uic
from random import randint
from time import sleep


class num5(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('num5.ui', self)
        self.label=QLabel("",self)
        self.statusbar.addWidget(self.label)
        self.b1.clicked.connect(self.anti_plag)
    def anti_plag(self):
        text1 = list(set(self.textEdit.toPlainText().lower().split()))
        text2 = list(set(self.textEdit_2.toPlainText().lower().split()))
        t=0
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    t += 1
        try:
            value = t/len(text1)*100
        
            if value <= float(self.doubleSpinBox.text()[:-1].replace(",",".")):
                self.statusbar.setStyleSheet("background-color:Green;")
            else:
                self.statusbar.setStyleSheet("background-color:Red;")
            self.label.setText(f"количество совпадений: {value}%")
        except:
            pass
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num5()
    ex.show()
    sys.exit(app.exec_())