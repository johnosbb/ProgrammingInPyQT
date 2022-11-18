import random
import sys

from PyQt5 import QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    glay = QtWidgets.QGridLayout(w)
    elements = (
        (0, 0, 1, 1),  # Position: 0x0 1 rowspan 1 colspan
        (1, 0, 1, 1),  # Position: 1x0 1 rowspan 1 colspan
        (0, 1, 2, 1),  # Position: 0x1 2 rowspan 1 colspan
        (2, 0, 1, 2),  # Position: 2x0 1 rowspan 2 colspan
    )
    for i, (row, col, row_span, col_span) in enumerate(elements):
        label = QtWidgets.QLabel("{}".format(i))
        color = QtGui.QColor(*random.sample(range(255), 3))
        label.setStyleSheet("background-color: {}".format(color.name()))
        glay.addWidget(label, row, col, row_span, col_span)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
