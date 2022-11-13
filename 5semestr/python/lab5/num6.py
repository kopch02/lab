import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import pandas as pd

class PasswordError(Exception):
    pass

class LoginError(Exception):
    pass

class not_found(LoginError):
    pass

class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass

class CopyError(PasswordError):
    pass

class invalid_password(PasswordError):
    pass


strs = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
        'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
low = set(''.join(strs))
up = set(''.join(strs).upper())
num = set('1234567890')


def pass_is_valid(psw):
    for i in range(len(psw) - 2):
        psw_ = psw[i:i + 3].lower()
        for i in strs:
            if psw_ in i:
                return False
    return True


def passworld_check(t):
        if not len(set(t)) >8: raise LengthError("пароль слишком короткий")
        if not (set(t) & num): raise DigitError("в пароле нет числе")
        if not (set(t) & up): raise LetterError("в пароле нет загланыйх букв")
        if not (set(t) & low): raise LetterError("в пароле нет маленьких букв")
        if not pass_is_valid(t): raise SequenceError("пароль слишком простой")
        return True


class enter_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('num6_enter.ui', self)
        self.error.setStyleSheet("color:Red;")
        self.enter_btn.clicked.connect(self.enter)
        self.registration_btn.clicked.connect(self.registration)
        self.reg = registration_window()
        self.m = main_window()

        self.connection = sqlite3.connect("password.sqlite")

    def enter(self):
        try:
            self.error.setText("")
            login = self.login.text()
            passwor = self.password.text()
            chec = "select * from users"
            chec = self.connection.cursor().execute(chec).fetchall()
            for i in chec:
                if login in i:
                    if passwor in i:
                        break
                    else:raise invalid_password("неверный пароль")
                else:raise not_found("логин не найден")
            self.close()
            self.m.show()
        except (PasswordError, LoginError) as e:
            self.error.setText(str(e))
        
        
    def registration(self):
        self.close()
        self.reg.show()


class registration_window(QMainWindow):    
    def __init__(self):
        super().__init__()
        uic.loadUi('num6_registration.ui', self)
        self.error.setStyleSheet("color:Red;")
        self.registration_btn.clicked.connect(self.registration)
        self.m = main_window()

        self.connection = sqlite3.connect("password.sqlite")

    def registration(self):
        try:
            chec_login = "select login from users"
            chec_login = self.connection.cursor().execute(chec_login).fetchall()
            my_login = self.login.text()
            print(chec_login)
            for i in chec_login:
                if my_login in i: raise LoginError("этот логин уже занят")
            password = self.password.text()
            passworld_check(password)
            passord_re = self.password_re.text()
            if password != passord_re: raise CopyError("пароли не совпадают")
            self.error.setText("")
            reg = f'''insert into users (login , password)
                            values ('{my_login}' , '{password}')'''
            self.connection.cursor().execute(reg)
            self.connection.cursor().execute('commit')
            self.close()
            self.m.show()
        except (PasswordError, LoginError) as e:
            self.error.setText(str(e))

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = enter_window()
    ex.show()
    sys.exit(app.exec())