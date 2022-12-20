import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class EigenerEvent(QObject):
    schliesmichEvent = pyqtSignal()
class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.sig = EigenerEvent()
        self.sig.schliesmichEvent.connect(self.close)
        QToolTip.setFont(QFont('Arial', 14))    # create a ToolTip
        button = QPushButton("drücken", self)   # setzt den Button auf das Fenster
        button.move(50, 50)
        button.setToolTip('this is my')         # set a ToolTip to the button
        button.clicked.connect(self.gedruckt)   # instead of clicked there is also pressed and released
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("my first gui")
        self.setWindowIcon(QIcon("Download.jpg"))  # Place an icon and import QIcon
        self.show()

    def gedruckt(self):
        sender = self.sender()
        sender.move(100, 100)
        print(sender.text() + "button gedruckt")

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QT.Key_Escape:
            self.sig.schliesmichEvent.emit()


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec())