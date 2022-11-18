# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MyLabel(QLabel):
    """
    Define a signal change_style that takes no arguments.
    """
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 800, 600)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # creating label
        label = MyLabel(self)
        label.setText("My new label Label")
        label.move(205, 15)
        label.adjustSize()

        label2 = QLabel("Hello Geeks Label2", self)
        # setting geometry of the label
        label.setGeometry(200, 150, 100, 40)
        label2.setGeometry(300, 250, 100, 40)

        text = MyLabel(self)
        text.setText("Hello There Beep Beep Text")
        text.move(105, 150)

        # setting background color to label when mouse hover over it
        label2.setStyleSheet("QLabel::hover"
                             "{"
                             "background-color : lightgreen; border: 4px solid #d0d0d0;"
                             "}")

        createButton = QPushButton("Create .......")
        createButton.setStyleSheet("QPushButton { background-color: blue }"
                                   "QPushButton:pressed { background-color: red }")
        createButton.setGeometry(300, 250, 100, 40)
        createButton.move(300, 300)
        # self.v_box = QVBoxLayout()
        # # self.v_box.addWidget(label)
        # self.v_box.addWidget(label2)
        # self.setLayout(self.v_box)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
