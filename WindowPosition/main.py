import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QTextEdit, QPushButton)


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(400, 200)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.textEdit = QTextEdit()
        self.btn = QPushButton("get the screen position of `QMainWindow`")
        self.btn.clicked.connect(self.btnClicked)

        layoutV = QVBoxLayout(centralWidget)
        layoutV.addWidget(self.textEdit)
        layoutV.addWidget(self.btn)

        self.textEdit.append("Start:")
        self.textEdit.append("pos.x=`{}`, pos.y=`{}`"
                             "".format(self.pos().x(), self.pos().y()))
        self.textEdit.append("geometry.x=`{}`, geometry.y=`{}`"
                             "".format(self.geometry().x(), self.geometry().y()))
        self.textEdit.append("--------------------------------------")

    def btnClicked(self):
        self.textEdit.append("pos.x=`{}`, pos.y=`{}`"
                             "".format(self.pos().x(), self.pos().y()))
        self.textEdit.append("geometry.x=`{}`, geometry.y=`{}`"
                             "".format(self.geometry().x(), self.geometry().y()))

    def moveEvent(self, event):    # QMoveEvent
        print("x=`{}`, y=`{}`".format(event.pos().x(), event.pos().y()))
        super(MainWindow, self).moveEvent(event)

    def resizeEvent(self, event):  # QResizeEvent
        print("w=`{}`, h=`{}`".format(
            event.size().width(), event.size().height()))
        super(MainWindow, self).resizeEvent(event)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
