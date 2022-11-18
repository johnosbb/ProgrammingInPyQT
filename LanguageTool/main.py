# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,  QLineEdit,
                             QVBoxLayout, QMainWindow, QScrollArea)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from grammarWidget import GrammarWidget

import language_tool_python
from grammarCheck import GrammarCheck


class GrammarCorrectionWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.gc = GrammarCheck()

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
        self.setCentralWidget(self.scroll)
        self.updateControls()
        self.show()

    def updateControls(self):
        text = 'At lunchtime, we went to Mangan’s Cafe. It was a nice sunny afternoon and we noticed that the staff had put one or two seating areas out on the sidewalk. These were small green cast iron tables with two matching chairs; a navy and white table cloth gave the area a novel continental look that, while a little out of place for the town, was pleasant and refreshing. In the centre of the table was a small glass jar with some lavender and soft peach garden roses arranged in an attractive display. We took our seats there and each ordered a sandwich and an coffee. The town looked very pretty in the warm sunshine; the houses seemed a shade more vibrant and the hills in the background, which were usually softened and obscured by mist, were unusually clear and vivid against a cloudless blue sky.'

        self.gc.setText(text)
        matches = self.gc.checkSection()
        for match in matches:
            widget = GrammarWidget(self.gc)
            widget.setContext(match.context)
            widget.setSuggestions(match.replacements)
            self.vboxLayout.addWidget(widget)


# Not currently used
class loadGrammarCheck(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def checkGrammar(self):
        # tool = language_tool_python.LanguageTool('en-GB')  # use a local server (automatically set up), language English
        text = 'At lunchtime, we went to Mangan’s Cafe. It was a nice sunny afternoon and we noticed that the staff had put one or two seating areas out on the sidewalk. These were small green cast iron tables with two matching chairs; a navy and white table cloth gave the area a novel continental look that, while a little out of place for the town, was pleasant and refreshing. In the centre of the table was a small glass jar with some lavender and soft peach garden roses arranged in an attractive display. We took our seats there and each ordered a sandwich and an coffee. The town looked very pretty in the warm sunshine; the houses seemed a shade more vibrant and the hills in the background, which were usually softened and obscured by mist, were unusually clear and vivid against a cloudless blue sky.'
    # matches = tool.check(text)
    # print("Found {} errors".format(len(matches)))
    # # print(matches)
    # print(text)
    # print(tool.correct(text))
    # my_mistakes = []
    # my_corrections = []
    # start_positions = []
    # end_positions = []
    # for rules in matches:
    #     if len(rules.replacements)>0:
    #         start_positions.append(rules.offset)
    #         end_positions.append(rules.errorLength+rules.offset)
    #         my_mistakes.append(text[rules.offset:rules.errorLength+rules.offset])
    #         my_corrections.append(rules.replacements[0])
    # my_new_text = list(text)
    # for m in range(len(start_positions)):
    #     for i in range(len(text)):
    #         my_new_text[start_positions[m]] = my_corrections[m]
    #         if (i>start_positions[m] and i<end_positions[m]):
    #             my_new_text[i]=""

    # my_new_text = "".join(my_new_text)
    # print("Corrected Text {} ".format(my_new_text))
        self.gc = GrammarCheck()
        self.gc.setText(text)

    def initializeUI(self):
        self.setMinimumSize(600, 800)
        self.setWindowTitle('Custom Widget')
        self.checkGrammar()
        matches = self.gc.check()
        v_box = QVBoxLayout()
        for match in matches:
            widget = GrammarWidget()
            widget.setContext(match.context)
            widget.setSuggestions(match.replacements)
            v_box.addWidget(widget)
        self.setLayout(v_box)
        # self.resize(640, 480)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GrammarCorrectionWindow()
    sys.exit(app.exec_())
