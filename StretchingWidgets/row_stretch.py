import random
import sys

from PyQt5 import QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    glay = QtWidgets.QGridLayout(w)
    for i in range(3):
        for j in range(3):
            label = QtWidgets.QLabel("{}x{}".format(i, j))
            color = QtGui.QColor(*random.sample(range(255), 3))
            label.setStyleSheet("background-color: {}".format(color.name()))
            glay.addWidget(label, i, j)
    glay.setRowStretch(0, 1)
    glay.setRowStretch(1, 2)
    glay.setRowStretch(2, 3)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
