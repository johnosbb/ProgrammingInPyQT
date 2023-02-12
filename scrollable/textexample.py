from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QTextEdit, QDialog, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys


class Window(QDialog):
    def __init__(self, val):
        super().__init__()
        self.title = "PyQt5 Scroll Bar"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        textEdit = QTextEdit()
        layout = QVBoxLayout(self)
        self.addLayout = layout
        layout.addWidget(textEdit)
        self.show()


App = QApplication(sys.argv)
window = Window(30)
sys.exit(App.exec())
