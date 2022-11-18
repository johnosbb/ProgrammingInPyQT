import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Template(QWidget):

    def __init__(self):
        super().__init__()
        self.textbox = QPlainTextEdit()
        btn = QPushButton('Highlight')
        btn.clicked.connect(self.highlight_word)
        btn2 = QPushButton('Get Selection')
        btn2.clicked.connect(self.get_selections)
        grid = QGridLayout(self)
        grid.addWidget(btn, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(self.textbox, 1, 0, 1, 2)

    def highlight_word(self):
        selection = QTextEdit.ExtraSelection()
        color = QColor(Qt.yellow).lighter()
        selection.format.setBackground(color)
        selection.cursor = self.textbox.textCursor()
        self.textbox.setExtraSelections([selection])
        print(selection.format.background().color().getRgb())

    def get_selections(self):
        selection = self.textbox.extraSelections()[0]
        print(selection.cursor.selectedText(), selection.format.background().color().getRgb())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Template()
    gui.show()
    sys.exit(app.exec_())