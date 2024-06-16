import sys
import db

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
import about
import insert
import datetime

head = ["title", "autor", "date_of_public"]
h = head.copy()
h.append("count")


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('num1.ui', self)
        self.start_btn.clicked.connect(self.start_table)
        self.btn_search_author.clicked.connect(self.load_filter)
        self.btn_search.clicked.connect(self.load_filter)
        result = db.find_document(db.collection_name, {}, True)
        self.temp_author = set()
        for row in result:
            self.temp_author.add(row["autor"])
        self.temp_author.add(None)

        self.btn_about.clicked.connect(self.about_btn)
        self.btn_insert.clicked.connect(self.insert_btn)
        self.about_f = about.about_form()
        self.insert_f = insert.insert_form()

        self.btn_delete.clicked.connect(self.delete_btn)
        self.btn_top.clicked.connect(self.top_artical)
        self.insert_f.btn_insert.clicked.connect(self.insert_new)

    def load_filter(self):
        t = f'[a-zA-Z0-9]*{self.line_search.text()}[a-zA-Z0-9]*'
        t2 = f'[a-zA-Z0-9]*{self.author_box.currentText()}[a-zA-Z0-9]*'
        result = db.find_document(db.collection_name, {
            "title": {
                f'$regex': t
            },
            "autor": {
                f'$regex': t2
            }
        }, True)
        self.load_table(result)

    def start_table(self):
        result = db.find_document(db.collection_name, {}, True)
        res = db.top_artical()
        self.load_table(result)
        self.author_box.addItems(self.temp_author)
        self.author_box.setCurrentText(None)
        self.tableWidget.cellClicked.connect(self.cellClick)
        self.start_btn.hide()
        self.btn_insert.setEnabled(True)
        self.btn_top.setEnabled(True)

    def load_table(self, result, head=head):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(head))
        self.tableWidget.setHorizontalHeaderLabels(head)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(head):
                self.tableWidget.setItem(i, j,
                                         QTableWidgetItem(str(row[elem])))
        self.tableWidget.resizeColumnsToContents()

    def cellClick(self, row, col):
        self.row = row
        self.col = col
        self.btn_about.setEnabled(True)
        self.btn_delete.setEnabled(True)

    def about_btn(self):
        t = self.tableWidget.item(self.row, 0)
        a = self.tableWidget.item(self.row, 1)
        result = db.find_document(db.collection_name, {
            "title": t.text(),
            "autor": a.text()
        }, True)
        self.about_f.set_data(result[0])
        self.about_f.show()

    def insert_btn(self):
        self.insert_f.clear()
        self.insert_f.show()

    def insert_new(self):
        new_data = self.insert_f.getter()
        #h = new_data[4][-5:-3].replace(" ","0")
        #date = f"{new_data[4][:10]}T{h}:{new_data[4][-2:]}:00.000Z"
        #d = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.000Z")

        db.insert_document(
            db.collection_name, {
                "title": new_data[0],
                "autor": new_data[1],
                "date_of_public": new_data[4],
                "text": new_data[3],
                "tags": new_data[2],
                "comments": []
            })

        self.load_filter()

    def delete_btn(self):

        ret = QMessageBox.question(self, 'deleted',
                                   "Вы правда хотите удалить запись?",
                                   QMessageBox.Yes | QMessageBox.Cancel,
                                   QMessageBox.Cancel)

        if ret == QMessageBox.Yes:
            t = self.tableWidget.item(self.row, 0)
            a = self.tableWidget.item(self.row, 1)
            db.delete_document(db.collection_name, {
                "title": t.text(),
                "autor": a.text()
            })
            self.load_filter()

    def top_artical(self):
        result = db.top_artical()
        self.load_table(result, head=h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())