import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        w = QLabel(self)
        w.setPixmap(QPixmap("Download.jpg"))
        w.move(50, 50)


        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("my first gui")
        self.setWindowIcon(QIcon("Download.jpg"))  # Place an icon and import QIcon
        self.show()


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec())