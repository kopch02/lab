import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.x_main = randint(400,700)
        self.y_main = randint(400,700)
        self.setGeometry(300, 300, self.x_main, self.y_main)

        self.btn = QPushButton(self)
        self.l = QLabel(self)
        self.l.setText("")
        self.btn.setText("Нажми")
        self.btn_x = self.x_main // 2
        self.btn_y = self.y_main // 2
        self.btn.setGeometry(self.btn_x, self.btn_y, 50, 30)
        self.btn.setStyleSheet("background-color:violet;")
        self.btn.clicked.connect(self.what)

        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        if (abs(event.x() +  - (self.btn_x + 25)) < 20) or (abs(event.y() - (self.btn_y + 15)) < 20):
            self.btn_x = randint(0,self.x_main - 50)
            self.btn_y = randint(0,self.y_main - 30)
            self.btn.move(self.btn_x, self.btn_y)
    
    def what(self):
        self.l.setText("как ты это сделал???")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())