import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtCore import Slot
import TestTool_UI
import autoinstall


class Backtool(QWidget, TestTool_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.choose_roll_back.connet(self.get_umd(15))




if __name__ == '__main__':
    app = QApplication([])
    window = Backtool()
    window.show()
    app.exit()
