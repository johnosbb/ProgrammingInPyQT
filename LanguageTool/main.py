# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,  QLineEdit,
                             QVBoxLayout, QMainWindow, QScrollArea, QTextEdit)
from PyQt5.QtCore import Qt
from grammarHighlighter import GrammarHighlighter
from grammarCheck import GrammarCheck
from correctorTextEdit import CorrectorTextEdit


class GrammarCorrectionWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.txtMain = CorrectorTextEdit()
        self.checkGrammar('At lunchtime, we went to Mangan’s Cafe. It was a nice sunny afternoon and we noticed that the staff had put one or two seating areas out on the sidewalk. These were small green cast iron tables with two ruleing chairs; a navy and white table cloth gave the area a novel continental look that, while a little out of place for the town, was pleasant and refreshing. In the centre of the table was a small glass jar with some lavender and soft peach garden roses arranged in an attractive display. We took our seats there and each ordered a sandwich and an coffee. The town looked very pretty in the warm sunshine; the houses seemed a shade more vibrant and the hills in the background, which were usually softened and obscured by mist, were unusually clear and vivid against a cloudless blue sky.')
        self.initializeUI()

    def checkGrammar(self, text):
        self.text = text
        self.gc = GrammarCheck()
        self.gc.setText(self.text)
        self.rules = self.gc.checkSection()

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
        self.SetupControls()
        self.show()

    def wordReplaced(self, rule, offsetAdjustment):
        print("A word was replaced rule offset: {} offset adjustment {} ".format(
            rule.offset, offsetAdjustment))
        self.text = self.txtMain.toPlainText()
        self.updateRuleOffsets(rule, offsetAdjustment)
        self.txtMain.grammarHighlighter.rehighlight()

    def updateRuleOffsets(self, activeRule, offsetAdjustment):
        for rule in self.rules:
            if(rule.offset > activeRule.offset):
                print("Adjusting rule offset at {}, new offset is {}".format(
                    rule.offset, rule.offset + offsetAdjustment))
                rule.offset = rule.offset + offsetAdjustment
        self.rules.remove(activeRule)
        print("Removing active rule, rules remaining {}".format(len(self.rules)))

    def SetupControls(self):
        self.txtMain.setMinimumHeight(200)
        self.txtMain.setText(self.text)
        self.txtMain.setRule(self.rules[0])
        self.txtMain.setRules(self.rules)
        self.txtMain.wordReplaced.connect(
            self.wordReplaced)
        self.txtMain.grammarHighlighter = GrammarHighlighter(
            self.txtMain.document())
        self.txtMain.grammarHighlighter.setGrammarRules(self.rules)
        self.vboxLayout.addWidget(self.txtMain)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GrammarCorrectionWindow()
    sys.exit(app.exec_())
