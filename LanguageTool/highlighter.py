import re

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QTextDocument


class Highlighter(QSyntaxHighlighter):

    def __init__(self, parent: QTextDocument) -> None:
        super().__init__(parent)
        self.echoDictionary = {}
        self.blockNumber = -1
        self.selectionEnd = -1
        self.selectionStart = -1
        self.typeOfCheck = "Spelling"
        self.rule = None
        self.rules = None

    wordRegEx = re.compile(r"\b([A-Za-z]{2,})\b")  # find words
    # This gets called with each paragraph of a document open in the QTextDocument

    def highlightBlock(self, text: str) -> None:
        if text == '':
            return

        # The character format of text in a document specifies the visual properties of the text, as well as information about its role in a hypertext document.
        self.misspelledFormat = QTextCharFormat()
        self.misspelledFormat.setUnderlineStyle(
            QTextCharFormat.SpellCheckUnderline)  # we can set its visual style
        self.misspelledFormat.setUnderlineColor(Qt.red)  # red and underlined

        self.echoFormat = QTextCharFormat()
        self.echoFormat.setUnderlineStyle(
            QTextCharFormat.WaveUnderline)  # we can set its visual style
        self.echoFormat.setUnderlineColor(Qt.blue)  # red and underlined
        if self.rules:
            for rule in self.rules:
                startPosition = rule.offset
                count = rule.errorLength
                self.setFormat(    # if it is not we underline it using the style shown above
                    startPosition,  # index of first letter of match
                    # index of last letter - index of first letter= length
                    count,
                    self.misspelledFormat,
                )

    def setTargetBlockNumber(self, blockNumber, start, end):
        self.blockNumber = blockNumber
        self.selectionStart = start
        self.selectionEnd = end

    def setGrammarRule(self, rule):
        self.rule = rule

    def setGrammarRules(self, rules):
        self.rules = rules

    def setTypeOfCheck(self, checkType):
        self.typeOfCheck = checkType

    def resetTypeOfCheck(self):
        self.typeOfCheck = "spelling"

    # def check(self, rule, word):
    #     if(rule):
    #         print(word)
    #         # if the word appears in the ; then we highlight it
    #         if word in rule.context:
    #             return True
    #         else:
    #             return False
    #     else:
    #         print("No rule has been set")
