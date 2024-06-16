from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

head_comment = ["name", "text_comment", "raiting"]


class about_form(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('about_form.ui', self)
        self.table_comment.setColumnCount(3)

    def set_data(self, data):
        self.title.setText(data["title"])
        self.author.setText(data["autor"])
        self.date_pub.setText(str(data["date_of_public"]))
        t = ""
        for i in data["tags"]:
            t += str(i) + " "
        self.tegs.setText(t)
        self.text_v.setPlainText(data["text"])

        self.table_comment.clear()
        self.table_comment.setRowCount(0)
        self.table_comment.setHorizontalHeaderLabels(head_comment)
        for i, row in enumerate(data["comments"]):
            self.table_comment.setRowCount(self.table_comment.rowCount() + 1)
            for j, elem in enumerate(head_comment):
                self.table_comment.setItem(i, j,
                                           QTableWidgetItem(str(row[elem])))
        self.table_comment.resizeColumnsToContents()