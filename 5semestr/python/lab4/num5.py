import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('num5.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.x_start.valueChanged.connect(self.run)
        self.x_end.valueChanged.connect(self.run)

    def run(self):
        try:
            self.graphicsView.clear()
            self.error_label.clear()
            self.graphicsView.plot([i for i in range(int(self.x_start.text()),int(self.x_end.text()))], [eval(self.formula.text()) for x in range(int(self.x_start.text()),int(self.x_end.text()))], pen='r')
        except(Exception) as e:
            self.error_label.setText("ERROR\n"+str(e))
            self.error_label.setStyleSheet("color:Red;")


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())