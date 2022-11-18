# import necessary modules
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QLabel,  QLineEdit, QGridLayout, QVBoxLayout, QScrollArea)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QRect
from grammarWidget import GrammarWidget


class GrammarCorrectionWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):

        self.setMinimumSize(800, 600)
        self.setWindowTitle('Custom Widget')
        self.scroll = QScrollArea()
        # Widget that contains the collection of Vertical Box
        self.vboxLayoutContainingWidget = QWidget()
        # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.vboxLayout = QVBoxLayout()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.vboxLayoutContainingWidget)
        self.vboxLayoutContainingWidget.setLayout(self.vboxLayout)
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.vboxLayout.addWidget(GrammarWidget())
        self.setCentralWidget(self.scroll)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    check = GrammarCorrectionWindow()
    sys.exit(app.exec_())
