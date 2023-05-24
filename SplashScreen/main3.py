import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import logging


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


class MainWindow(QMainWindow):

    def __init__(self, appContext, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("Splash Screen")
    # When the Internet domain is set, it is used on macOS and iOS instead of the organization name, since macOS and iOS applications conventionally use Internet domains to identify themselves.
    QCoreApplication.setOrganizationDomain("splashscreen-editor.com")
    QCoreApplication.setApplicationName("SplashTest")
    logging.basicConfig(level=logging.DEBUG, filename="splash.log", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s", force=True)
    logging.info("lyrical: Starting Lyrical Editor")

    app.setStyle("fusion")
    splash = SplashScreen()
    # By default, SplashScreen will be in the center of the screen.
    # You can move it to a specific location if you want:
    # self.splash.move(10,10)

    splash.show()
    main = MainWindow(app)
    splash.delayedClose()
    app.exec_()
