import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic  # Импортируем uic


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


strs = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
        'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
low = set(''.join(strs))
up = set(''.join(strs).upper())
num = set('1234567890')
 

def upp(psw):
    return set(psw) & up


def lo(psw):
    return set(psw) & low


def numb(psw):
    return set(psw) & num


def le(psw):
    return len(set(psw)) >8


def pass_is_valid(psw):
    for i in range(len(psw) - 2):
        psw_ = psw[i:i + 3].lower()
        for i in strs:
            if psw_ in i:
                return False
    return True


class num3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('num2.ui', self)
        self.ok.clicked.connect(self.btn)

    def btn(self):
        t=self.data.text()
        if not le(t) : raise LengthError("short")
        if not numb(t) : raise DigitError("no numbers")
        if not upp(t) : raise LetterError("no uppercase letters")
        if not lo(t) : raise LetterError("no lowercase letters")
        if not pass_is_valid(t) : raise SequenceError("simple")
        self.out.setText("OK")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num3()
    ex.show()
    sys.exit(app.exec_())