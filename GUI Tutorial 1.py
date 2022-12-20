import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont

class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        QToolTip.setFont(QFont('Arial', 14))    # create a ToolTip
        button = QPushButton("drücken", self)   # setzt den Button auf das Fenster
        button.move(50, 50)
        button.setToolTip('this is my')         # set a ToolTip to the button
        button.clicked.connect(self.gedruckt)
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("my first gui")
        self.setWindowIcon(QIcon("Download.jpg"))  # Place an icon and import QIcon
        self.show()
    def_gedruckt:





app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec())