import sys
import logica
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidgetItem, QMainWindow
from PyQt5 import uic 
import sqlite3

con = sqlite3.connect("sadic.sqlite")
cursor = con.cursor()


class tuir(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self) 
        self.button_mark = True
        self.button_1.clicked.connect(self.swap)
        self.plus.clicked.connect(self.show_add_ch)
        self.summ.clicked.connect(self.suma)
        self.new_ch_form = New_ch_form()
        self.tableWidget.cellClicked.connect(self.cellClick)

    def swap(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        children = cursor.execute('select fio, tarif, lgot from children')
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['фио', 'тариф', 'льгота'])
        for i, row in enumerate(children):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def suma(self):
        current_children = self.tableWidget.item(self.row, 0).text()
        children = cursor.execute(f'''select * from children 
        where fio = "{current_children}"''')
        m = datetime.datetime.now()
        m = int(m.strftime("%m")) - 1
        if m == 0: m = 12
        for i in children:
            logica.sum_cash(cursor, i[1], m)
        logica.save(cursor)

    def cellClick(self, row, col):
        self.row = row
        self.col = col

    def show_add_ch(self):
        self.new_ch_form.fio_add.setPlainText("")
        self.new_ch_form.show()


class New_ch_form(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('new_ch_add.ui', self) 
        self.lgota_add.addItems(['да', 'нет'])
        self.tarif_add.addItems(['почасовой', 'дневной', 'полный', 'старый'])
        self.ch_add_b.clicked.connect(self.new_ch)

    def new_ch(self):
        fio = self.fio_add.toPlainText()
        tarif = self.tarif_add.currentText()
        lgota = self.lgota_add.currentText()
        date = self.cl_add.selectedDate().toString('yyyy-MM-dd')
        print(date)
        logica.insert_children(cursor, fio, tarif, lgota)
        logica.save(cursor)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = tuir()
    ex.show()
    sys.exit(app.exec())
