import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Fenster(QMainWindow):         # Erbt from Qmain...
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.statusBar().showMessage('hallöchen')       # Statusbar down left in the window
        exitMe = QAction(QIcon('Download.jpg'), '&Exit', self)  # shows Icon if in File
        exitMe.setShortcut('Ctrl+E')                            # shows and does a shortcut
        exitMe.setStatusTip('Exit')                             # tooltip
        exitMe.triggered.connect(self.close)
        menubar = self.menuBar()

        file = menubar.addMenu('File')                  # creates a menubar
        file.addAction(exitMe)

        toolBar = self.addToolBar('Exit')       # create a Toolbar
        toolBar.addAction(exitMe)

        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("my first gui")
        self.setWindowIcon(QIcon("Download.jpg"))  # Place an icon and import QIcon
        self.show()



app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec())