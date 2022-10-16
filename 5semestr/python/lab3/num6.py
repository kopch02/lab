from csv import list_dialects
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


class NumberError(Exception):
    pass


class FormatError(NumberError):
    pass


class LenghtError(NumberError):
    pass


class CountryError(NumberError):
    pass


class OperatorError(NumberError):
    pass


MTS = str(list(range(910, 920)) + list(range(980, 990)))
MEGAFON = str(list(range(920, 940)))
BILAIN = str(list(range(902, 907)) + list(range(960, 970)))


def Format(number):
    return number.count("(") == number.count(")") or "--" in number


def Lenght(number):
    return len(number) == 11


def Country(psw):
    t = False
    if psw[0] == "8":
        t = True
    elif psw[0] == "7":
        t = True
    return t


def Operator(psw):
    return (psw[1:4] in MTS) or (psw[1:4] in MEGAFON) or (psw[1:4] in BILAIN)


strs = [
    'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю', 'qwertyuiop', 'asdfghjkl',
    'zxcvbnm'
]
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
    return len(list(psw)) > 8


def check_phone(n):
    if not Format(n): raise FormatError("неверный формат")
    chars = ['-', '+', '(', ')', ' ']
    for i in chars:
        n = n.replace(i, "")
    if not Lenght(n): raise LenghtError("неверное количество цифр")
    if not Country(n): raise CountryError("неверный код страны")
    if not Operator(n):
        raise OperatorError("не определяется оператор сотовой связи")

    res = f"+7{n[1:]}"

    return True


def pass_is_valid(psw):
    for i in range(len(psw) - 2):
        psw_ = psw[i:i + 3].lower()
        for i in strs:
            if psw_ in i:
                return False
    return True


def passworld_check(t):
    if not le(t): raise LengthError("пароль слишком короткий")
    if not numb(t): raise DigitError("в пароле нет числе")
    if not upp(t): raise LetterError("в пароле нет загланыйх букв")
    if not lo(t): raise LetterError("в пароле нет маленьких букв")
    if not pass_is_valid(t): raise SequenceError("пароль слишком простой")
    return True


class num6(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num6.ui', self)
        self.ok.clicked.connect(self.btn)

    def btn(self):
        passworld = self.passworld.text()
        login = self.login.text()
        number = self.number.text()
        try:
            passworld_check(passworld)
            check_phone(number)
            self.res.setText("Успешно")
            self.res.setStyleSheet("background-color:Green;")
        except (PasswordError) as e:
            self.res.setText(str(e))
            self.res.setStyleSheet("background-color:Red;")
        except (NumberError) as e:
            self.res.setText(str(e))
            self.res.setStyleSheet("background-color:Red;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num6()
    ex.show()
    sys.exit(app.exec_())