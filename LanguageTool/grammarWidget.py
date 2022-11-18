import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,  QLineEdit, QGridLayout, QVBoxLayout, QFrame, QTextEdit, QPushButton)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QRect
from highlighter import Highlighter
from grammarCheck import GrammarCheck


class GrammarWidget(QFrame):
    def __init__(self, grammarCheck):
        super(GrammarWidget, self).__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.layout = QVBoxLayout()
        self.categoryLabel = QLabel("Category")
        self.btnInsert = QPushButton("Accept Suggestion")
        self.txtContext = QTextEdit()
        self.txtContext.highlighter = Highlighter(self.txtContext.document())
        self.txtContext.highlighter.setSpeller(grammarCheck.check)
        self.suggestionLabel = QLabel("Suggestion")
        self.txtSuggestion = QTextEdit()
        self.layout.addWidget(self.categoryLabel)
        self.layout.addWidget(self.txtContext)
        self.layout.addWidget(self.suggestionLabel)
        self.layout.addWidget(self.txtSuggestion)
        self.layout.addWidget(self.btnInsert)
        self.setLayout(self.layout)

    def setContext(self, context):
        self.txtContext.setText(context)

    def setSuggestions(self, suggestions):
        if(len(suggestions) > 1):
            for suggestion in suggestions:
                self.txtSuggestion.setText(
                    self.txtSuggestion.toPlainText() + "," + suggestion)
        elif(len(suggestions) == 1):
            self.txtSuggestion.setText(suggestions[0])
        else:
            self.txtSuggestion.setText("")

    def setCategoryDetails(self, details):
        self.categoryLabel.setText(details)
