from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.resize(506, 312)
        self.centralwidget = QWidget(MainWindow)

        # adding pushbutton
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(200, 150, 93, 28))

        self.createButton = QPushButton(self.centralwidget)
        self.createButton.setText("Hello there!")
        self.createButton.setGeometry(QRect(300, 170, 93, 28))
        self.createButton.setStyleSheet("QPushButton { background-color: blue }"
                                        "QPushButton:pressed { background-color: red }")

        self.frame = QFrame(MainWindow)  # Create QFrame object
        size_policy = QSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Preferred)
        self.frame.setSizePolicy(size_policy)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setStyleSheet("background-color: #223232;")
        # self.frame.setLineWidth(3)
        # self.frame.setMidLineWidth(5)
        self.buttonPanelLayout = QHBoxLayout(self.frame)

        self.buttonPanelLayout.addWidget(self.createButton)
        # self.createButton.setStyleSheet("QPushButton{color:black}"
        #                                 "QPushButton:hover{color:#E6E9CC}"
        #                                 "QPushButton{background-color:#223232}"
        #                                 "QPushButton{border:2px}"
        #                                 "QPushButton{border-color:#000000}"
        #                                 "QPushButton{border-radius:10px}"
        #                                 "QPushButton{padding:2px 4px}")

        # adding signal and slot
        self.pushButton.clicked.connect(self.changelabeltext)

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(140, 90, 221, 20))

        # keeping the text of label empty before button get clicked
        self.label.setText("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Push Button"))

    def changelabeltext(self):

        # changing the text of label after button get clicked
        self.label.setText("You clicked PushButton")

        # Hiding pushbutton from the main window
        # after button get clicked.
        self.pushButton.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
