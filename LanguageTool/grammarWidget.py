import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,  QLineEdit, QGridLayout, QVBoxLayout, QFrame, QTextEdit, QPushButton)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QRect
from highlighter import Highlighter
from grammarCheck import GrammarCheck


class GrammarWidget(QFrame):
    def __init__(self, rule, showContext=False):
        super(GrammarWidget, self).__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.layout = QVBoxLayout()
        self.rule = rule
        self.showContext = showContext
        self.text = ""  # the complete text we wish to correct
        self.txtContext = QTextEdit()
        self.txtContext.highlighter = Highlighter(self.txtContext.document())
        self.txtContext.highlighter.setGrammarRule(self.rule)
        self.layout.addWidget(self.txtContext)
        self.setLayout(self.layout)

    def setContext(self, context):
        self.txtContext.setText(context)

    def setText(self, text):
        self.text = text
