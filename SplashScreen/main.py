import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        pixmap = QPixmap("splash.png")
        self.setPixmap(pixmap)

    def closeSplash(self):
        self.close()

    def delayedClose(self):
        QTimer.singleShot(2000, self.closeSplash)


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.b1 = QPushButton('Display screensaver')
        self.b1.clicked.connect(self.flashSplash)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.b1)

    def flashSplash(self):

        self.splash = SplashScreen()
        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()
        self.splash.delayedClose()
        # Close SplashScreen after 2 seconds (2000 ms)
        #QTimer.singleShot(2000, self.splash.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Dialog()
    main.flashSplash()

    main.show()
    sys.exit(app.exec_())
