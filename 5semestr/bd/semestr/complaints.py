import sys
import db

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
import datetime

head_complaints = ["фамилия", "имя", "отчество","номер телефона","текст"]


class Complaints(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('complaints.ui', self)
        self.tableWidget.setColumnCount(len(head_complaints))
        self.load_data()
        self.add_f = Complaints_add()
        self.add.clicked.connect(self.add_f.show)
        self.add_f.add.clicked.connect(self.add_complaints)
        
    def load_data(self):
        data = db.find_document(db.collection_complaints, {}, True)
        for i in data:
            del i['_id']
            del i['автор']
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(head_complaints)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(head_complaints):
                self.tableWidget.setItem(i, j,
                                           QTableWidgetItem(str(row[elem])))
        self.tableWidget.resizeColumnsToContents()

    def add_complaints(self):
        f = self.add_f.last_name.text()
        n = self.add_f.first_name.text()
        o = self.add_f.patronymic.text()
        t = self.add_f.text.toPlainText()
        author = db.find_document(db.collection_customers,{"фамилия":f,"имя":n,"отчество":o})
        db.insert_document(db.collection_complaints,{
            "автор":author["_id"],
            "фамилия":f,
            "имя":n,
            "отчество":o,
            "номер телефона":author["номер телефона"],
            "текст":t
        })
        self.load_data()

class Complaints_add(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('complaints_add.ui', self)
