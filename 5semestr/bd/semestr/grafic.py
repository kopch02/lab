import sys
import db

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
import datetime
import complaints


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num1.ui', self)
        self.complaints_view = complaints.Complaints()
        self.complaints.clicked.connect(self.complaints_view.show)
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())