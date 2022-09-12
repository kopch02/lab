import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QSpinBox
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont


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
        self.button_mark = True

        self.input_1 = QLineEdit(self)
        self.input_1.move(10, 40)

        self.input_2 = QLineEdit(self)
        self.input_2.move(160, 40)

        self.show()

    def swap(self):
        if self.button_mark:
            self.button_mark = False
            self.button_1.setText("<-")
            temp = self.input_2.text()
            self.input_2.setText(self.input_1.text())
            self.input_1.setText(temp)

        else:
            self.button_mark = True
            self.button_1.setText("->")
            temp2 = self.input_1.text()
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
        self.button_mark = True

        self.input_1 = QLineEdit(self)
        self.input_1.move(10, 30)

        self.res_label = QLabel(self)
        self.res_label.setGeometry(20, 120, 100, 10)
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
        funk = {self.box1, self.box2, self.box3}
        self.labels = []

        y = 0
        n = 1

        for i in funk:
            self.check = QCheckBox(str(n), self)
            self.check.move(10, y)
            self.check.stateChanged.connect(i)

            label = QLabel(self)
            label.setText("")
            label.setGeometry(40, y, 150, 15)
            self.labels.append(label)

            y += 30
            n += 1

        self.show()

    def box1(self, state):
        if state == Qt.Checked:
            self.labels[0].setText("Первая строка ")
        else:
            self.labels[0].setText("")

    def box2(self, state):
        if state == Qt.Checked:
            self.labels[1].setText("Вторая строка ")
        else:
            self.labels[1].setText("")

    def box3(self, state):
        if state == Qt.Checked:
            self.labels[2].setText("Третья строка ")
        else:
            self.labels[2].setText("")


MORSE_CODE_DICT = {
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}


class num4(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 0
        y = 100
        for i in MORSE_CODE_DICT:
            self.button = QPushButton(self)
            self.button.setGeometry(x, y, 40, 40)
            self.button.setText(i)
            self.button.clicked.connect(self.res)
            x += 40
            if x >= 400:
                x = 0
                y += 40

        self.label = QLabel(self)
        self.label.setText("")
        self.label.setGeometry(0, 0, 400, 100)

        self.show()

    def res(self):
        self.label.setText(self.label.text() + " " +
                           MORSE_CODE_DICT[self.sender().text()])


class num5(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle("меню")

        paths = [
            '5semestr\python\lab1\\img\\burger.jpeg',
            '5semestr\python\lab1\\img\\napitok.jpg',
            '5semestr\python\lab1\\img\\sup.jpg'
        ]
        y = 20
        for i in paths:
            photo_label = QLabel(self)
            photo = QPixmap(i)
            photo = photo.scaled(135, 90)
            photo_label.setPixmap(photo)
            photo_label.move(10, y)
            y += 110

        y = 65
        phrase = ("добавить бургер", "добавить напиток", "добавить суп")
        price = ("390₽", "90₽", "190₽")
        self.price2 = (390, 90, 190)
        self.labels = []
        self.spins = []
        self.sums = [0, 0, 0]
        self.sum = 0

        for i in range(3):
            self.check = QCheckBox(phrase[i], self)
            self.check.move(160, y)
            self.check.id = i
            self.check.stateChanged.connect(self.box)
            self.check.setStyleSheet('''
                QCheckBox::indicator:unchecked {
                    image: url(5semestr/python/lab1/img/off.png);
                }
                QCheckBox::indicator:checked {
                    image: url(5semestr/python/lab1/img/on.png);
                }
            ''')

            label = QLabel(self)
            label.setText(price[i])
            label.setGeometry(160, y - 30, 50, 15)
            self.labels.append(label)

            self.spin = QSpinBox(self)
            self.spin.setMinimum(0)
            self.spin.setSingleStep(1)
            self.spin.move(330, y)
            self.spin.hide()
            self.spin.valueChanged.connect(self.spin_update)
            self.spin.id = i
            self.spins.append(self.spin)

            y += 110

        self.button = QPushButton(self)
        self.button.move(410, 300)
        self.button.setText("Сделать заказ")
        self.button.clicked.connect(self.summ)

        self.label = QLabel(self)
        self.label.setText("0₽")
        self.label.setGeometry(410, 250, 90, 20)

        self.show()

    def box(self, state):
        if state == Qt.Checked:
            self.spins[self.sender().id].show()
            self.spins[self.sender().id].setValue(1)

        else:
            self.spins[self.sender().id].hide()
            self.spins[self.sender().id].setValue(0)
            self.update()

    def spin_update(self, value):
        self.sums[self.sender().id] = value * self.price2[self.sender().id]
        self.update()

    def update(self):
        for i in self.sums:
            self.sum += i
        self.label.setText(str(self.sum) + "₽")
        self.sum = 0

    def summ(self):
        self.check = check(price=self.sums)
        self.check.show()


class check(QWidget):

    def __init__(self, price, *args):
        super().__init__()
        self.initUI(args, price=price)

    def initUI(self, args, price):
        self.setGeometry(400, 330, 180, 200)
        self.setWindowTitle('чек')
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 200, 70)
        self.final_text = ""
        if int(price[0] / 390) != 0:
            self.burger = f"Бургер x{int(price[0]/390)}\t\t{price[0]}\n"
            self.final_text += self.burger
        if int(price[1] / 90) != 0:
            self.napitok = f"Напиток x{int(price[1]/90)}\t\t{price[1]}\n"
            self.final_text += self.napitok
        if int(price[2] / 190) != 0:
            self.sup = f"Суп x{int(price[2]/190)}\t\t\t{price[2]}\n"
            self.final_text += self.sup
        self.final_text += f"\n\tсумма:\t\t{str(price[0]+price[1]+price[2])}"
        self.label.setText(self.final_text)

        self.btn = QPushButton(self)
        self.btn.setText("OK")
        self.btn.setGeometry(75, 170, 30, 30)
        self.btn.clicked.connect(self.hide)


class num6(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 485, 550)
        self.setWindowTitle("калькулятор")
        self.btns = [
            "C", "DEL", "*", "=", "1", "2", "3", "/", "4", "5", "6", "+", "7",
            "8", "9", "-", "+/-", "0", "%", "X^2"
        ]
        x = 10
        y = 140
        for bt in self.btns:
            self.b = QPushButton(self)
            self.b.setText(bt)
            self.b.setGeometry(x, y, 115, 79)
            self.b.clicked.connect(self.logicalc)
            x += 117
            if x > 400:
                x = 10
                y += 81
        self.formula = "0"
        self.lbl = QLabel(self,text=self.formula)
        self.lbl.setGeometry(11,50,480,100)
        self.lbl.setFont(QFont("Times", 16, QFont.Bold))

    def summ(self):
        print(self.sender.text())

    def logicalc(self):
        if self.sender().text() == "C":
            self.formula = ""
        elif self.sender().text() == "DEL":
            self.formula = self.formula[0:-1]
        elif self.sender().text() == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif self.sender().text() == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += self.sender().text()
        self.lbl.setText(self.formula)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num6()
    ex.show()
    sys.exit(app.exec())