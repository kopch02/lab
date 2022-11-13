import csv
import sys

from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import pandas as pd
second = 0
third = 0


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('num1.ui', self)
        self.shcool_box.addItems([None])
        self.klass_box.addItems([None])
        self.df = pd.read_csv("rez.csv")
        del self.df["1(Система счисления)"],self.df["2(Количество символов)"],self.df["3(Минимальное число)"],self.df["4(Трамвай)"]
        self.loadTable()
        self.shcool_box.addItems(self.temp_shcool)
        self.klass_box.addItems(self.temp_klass)
        self.kl = ""
        self.sh = ""
        self.klass_box.activated[str].connect(self.klass_sort)
        self.shcool_box.activated[str].connect(self.shcool_sort)

    def klass_sort(self,text):
        self.kl = text
        self.load_filter()
        
    def shcool_sort(self,text):
        self.sh = text
        self.load_filter()
    
    def load_filter(self):
        if self.kl == "" and self.sh == "":
            self.loadTable()
        else:
            t = 0
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(self.df.columns)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(self.df.values):
                if self.kl == "" and self.sh == "":
                    temp = False
                elif (self.sh != "") and (self.kl != ""):
                    temp = not ((row[2][12:14] == self.sh) and (row[2][15:17] == self.kl))
                else:
                    temp = (row[2][12:14] != self.sh) and (row[2][15:17] != self.kl)
                if temp:
                    continue   
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)  
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        t, j, QTableWidgetItem(str(elem)))
                t += 1
        self.tableWidget.resizeColumnsToContents()   
        self.first_place()

    def first_place(self,n = 0):
        global second, third
        if self.tableWidget.item(n,3) == None:
            return True
        else:
            if int(self.tableWidget.item(n,3).text()) == int(self.tableWidget.item(0,3).text()):
                if self.tableWidget.item(n + 1,3) == None:
                    second = -1
                    third = -1
                else:
                    if int(self.tableWidget.item(n + 1,3).text()) < int(self.tableWidget.item(0,3).text()):
                        second = int(self.tableWidget.item(n + 1,3).text())
                self.tableWidget.item(n,1).setBackground(QtGui.QColor(255,215,0))
                n += 1
                self.first_place(n)

            elif int(self.tableWidget.item(n,3).text()) == second:
                if self.tableWidget.item(n + 1,3) == None:
                    third = -1
                else:
                    if int(self.tableWidget.item(n + 1,3).text()) < int(self.tableWidget.item(n,3).text()):
                        third = int(self.tableWidget.item(n + 1,3).text())
                self.tableWidget.item(n,1).setBackground(QtGui.QColor(192,192,192))
                n += 1
                self.first_place(n)

            elif int(self.tableWidget.item(n,3).text()) == third:
                self.tableWidget.item(n,1).setBackground(QtGui.QColor(205,127,50))
                n += 1
                self.first_place(n)
            else:
                return True
                   
    def loadTable(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(self.df.columns))
        self.tableWidget.setHorizontalHeaderLabels(self.df.columns)
        self.temp_shcool = set()
        self.temp_klass = set()
        for i, row in enumerate(self.df.values):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            self.temp_shcool.add(row[2][12:14])
            self.temp_klass.add(row[2][15:17])
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())