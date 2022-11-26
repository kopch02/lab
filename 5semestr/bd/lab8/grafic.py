import sys
import db

from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import pandas as pd

head = ["title", "autor", "date_of_public"]


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num1.ui', self)
        self.start_btn.clicked.connect(self.start_table)
        self.btn_search_author.clicked.connect(self.load_filter)
        self.btn_search.clicked.connect(self.load_filter)
        self.tableWidget.setColumnCount(3)
        result = db.find_document(db.collection_name, {}, True)
        self.temp_author = set()
        for row in result:
            self.temp_author.add(row["autor"])
        self.temp_author.add(None)

    def load_filter(self):
        t = f'[a-zA-Z0-9]*{self.line_search.text()}[a-zA-Z0-9]*'
        t2 = f'[a-zA-Z0-9]*{self.author_box.currentText()}[a-zA-Z0-9]*'
        result = db.find_document(db.collection_name,
                                  {"title": {f'$regex': t},"autor": {f'$regex': t2}}, 
                                  True)
        for row in result:
            self.load_table(result)

    def start_table(self):
        result = db.find_document(db.collection_name, {}, True)
        self.load_table(result)
        self.author_box.addItems(self.temp_author)
        self.start_btn.hide()

    def load_table(self, result):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(head)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(head):
                self.tableWidget.setItem(i, j,
                                         QTableWidgetItem(str(row[elem])))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())