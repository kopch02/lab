import sys
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('num6.ui', self)
        #вариант с загрузкой всех звуков сразу в надежде убрать задержку перед запуском звука
        #self.name = ["do","re","mi","fa","sol","lja","si"]
        #self.t = dir()
        #for i in self.name:
        #    media = QtCore.QUrl.fromLocalFile(f"sounds/{i}.mp3")
        #    self.t[i] = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        for i in self.b_group.buttons():
            i.clicked.connect(self.play)
    

    def play(self, b):
        media = QtCore.QUrl.fromLocalFile(f"sounds/{self.sender().text()}.mp3")
        self.content = QtMultimedia.QMediaContent(media)
        self.player.setMedia(self.content)
        self.player.play()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())