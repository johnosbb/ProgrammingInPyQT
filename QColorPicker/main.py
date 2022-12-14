import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 color dialog - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Open color dialog', self)
        button.setToolTip('Opens color dialog')
        button.move(10, 10)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.openColorDialog()

    def openColorDialog(self):

        color = QColorDialog.getColor()
        myColor = QColor()
        list = myColor.colorNames()
        myColor.setNamedColor("aqua")
        if color.isValid():
            print("Color is " + color.name())
            print("Color is " + myColor.name())
            print(list)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
