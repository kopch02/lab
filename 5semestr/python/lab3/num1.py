import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic  # Импортируем uic


strs = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
        'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
low = set(''.join(strs))
up = set(''.join(strs).upper())
num = set('1234567890')
 
 
def pass_is_valid(psw):
    p = set(psw)
    if not (p & low and p & up and p & num and len(psw) > 8):
        return False
    for i in range(len(psw) - 2):
        psw_ = psw[i:i + 3].lower()
        for i in strs:
            if psw_ in i:
                return False
    return True


class num1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('num1.ui', self)
        self.ok.clicked.connect(self.btn)

    def btn(self):
        t=self.data.text()
        if pass_is_valid(t):
            self.out.setText("OK")
        else:
            self.out.setText("error")

                            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = num1()
    ex.show()
    sys.exit(app.exec_())