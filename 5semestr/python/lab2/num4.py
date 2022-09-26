import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic  # Импортируем uic
from random import randint
from time import sleep


class num4(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num4.ui', self)
        self.b1.clicked.connect(self.start)

    def start(self):
        self.rocks = self.spinBox.text()
        uic.loadUi('num4_2.ui', self)
        self.bGroup.buttonClicked.connect(self.buttons)
        self.update()

    def update(self):
        if int(self.rocks) <= 0:
            self.label2.setText("игра закончилась!")
            for b in self.bGroup.buttons():
                b.setEnabled(False)
        else:
            self.label2.setText("Количество камней: " + self.rocks)

    def buttons(self, b):
        self.rocks = str(int(self.rocks) - int(b.text()))
        self.update()
        self.comp()

    def comp(self):
        sleep(0.2)
        if int(self.rocks) % 4 == 0:
            self.rocks = str(int(self.rocks) - randint(1, 3))
        else:
            self.rocks = str(int(self.rocks) - int(self.rocks) % 4)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num4()
    ex.show()
    sys.exit(app.exec_())