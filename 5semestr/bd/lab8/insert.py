from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

head_comment = ["name", "text_comment", "raiting"]


class insert_form(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('insert_form.ui', self)
        self.btn_insert.clicked.connect(self.insert_btn)

    def clear(self):
        self.title_edit.setText("")
        self.author_edit.setText("")
        self.tegs_edit.setText("")
        self.text_v.setPlainText("")

    def insert_btn(self):
        title = self.title_edit.text()
        author = self.author_edit.text()
        tegs = self.tegs_edit.text().replace(" ", "").split(",")
        text = self.text_v.toPlainText()
        date = self.calendarWidget.selectedDate().toString(
            'yyyy-MM-dd') + " " + self.timeEdit.text()

        self.new_data=[title,author,tegs,text,date]

        self.close()
    
    def getter(self):
        return self.new_data