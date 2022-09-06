import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt


class num1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)

        self.button_1 = QPushButton(self)
        self.button_1.move(110, 80)
        self.button_1.setText("->")
        self.button_1.clicked.connect(self.swap)
        self.button_mark=True

        self.input_1 = QLineEdit(self)
        self.input_1.move(10, 40)

        self.input_2 = QLineEdit(self)
        self.input_2.move(160, 40)

        self.show()


    def swap(self):
        if self.button_mark:
            self.button_mark=False
            self.button_1.setText("<-")
            temp=self.input_2.text()
            self.input_2.setText(self.input_1.text())
            self.input_1.setText(temp)

        else:
            self.button_mark=True
            self.button_1.setText("->")
            temp2=self.input_1.text()
            self.input_1.setText(self.input_2.text())
            self.input_2.setText(temp2)


class num2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)

        self.button_1 = QPushButton(self)
        self.button_1.move(210, 60)
        self.button_1.setText("Вычислить")
        self.button_1.clicked.connect(self.res)
        self.button_mark=True

        self.input_1 = QLineEdit(self)
        self.input_1.move(10, 30)

        self.res_label = QLabel(self)
        self.res_label.setGeometry(20,120,100,10)
        self.res_label.setText("Результат: ")

        self.show()


    def res(self):
        self.res_label.setText(f"Результат: {eval(self.input_1.text())}")
        self.input_1.setText("")


class num3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.label_1 = QLabel(self)
        self.label_1.setText("")
        self.label_1.setGeometry(40,0,150,15)

        self.label_2 = QLabel(self)
        self.label_2.setText("")
        self.label_2.setGeometry(40,30,150,15)

        self.label_3 = QLabel(self)
        self.label_3.setText("")
        self.label_3.setGeometry(40,60,150,15)

        self.check_1 = QCheckBox('1', self)
        self.check_1.move(10, 0)
        self.check_1.stateChanged.connect(self.box1)

        self.check_2 = QCheckBox('2', self)
        self.check_2.move(10, 30)
        self.check_2.stateChanged.connect(self.box2)

        self.check_3 = QCheckBox('3', self)
        self.check_3.move(10, 60)
        self.check_3.stateChanged.connect(self.box3)

        self.show()


    def box1(self, state):
        if state == Qt.Checked:
            self.label_1.setText("Первая строка ")
        else:
            self.label_1.setText("")
    
    def box2(self, state):

        print(self.sender().text())


        if state == Qt.Checked:
            self.label_2.setText("Вторая строка ")
        else:
            self.label_2.setText("")

    def box3(self, state):
        if state == Qt.Checked:
            self.label_3.setText("Третья строка ")
        else:
            self.label_3.setText("")


MORSE_CODE_DICT = { '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----',
                    'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'
                    }


class num4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x=0
        y=100
        for i in MORSE_CODE_DICT:
            self.button = QPushButton(self)
            self.button.setGeometry(x, y,40,40)
            self.button.setText(i)
            self.button.clicked.connect(self.res)
            x+=40
            if x>=400:
                x=0
                y+=40

        self.label = QLabel(self)
        self.label.setText("")
        self.label.setGeometry(0,0,400,100)

        self.show()
    def res(self):
        self.label.setText(self.label.text()+" "+MORSE_CODE_DICT[self.sender().text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num1()
    ex.show()
    sys.exit(app.exec())