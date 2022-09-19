import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic  # Импортируем uic


class num1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('num1.ui', self)  # Загружаем дизайн
        self.groups=[self.first,self.mid,self.last]
        self.labels=[self.label,self.label_3,self.label_2]
        e=0
        for i in self.groups:
            i.buttonClicked.connect(self.a)
            i.id=e
            e+=1
    def a(self):
        self.labels[self.sender().id].setText('<h1 style="color: black">'+self.sender().checkedButton().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num1()
    ex.show()
    sys.exit(app.exec_())