import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,  QLineEdit, QGridLayout, QVBoxLayout, QFrame, QTextEdit, QPushButton)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QRect


class GrammarWidget(QFrame):
    def __init__(self):
        super(GrammarWidget, self).__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.layout = QVBoxLayout()
        self.categoryLabel = QLabel("Category")
        self.btnInsert = QPushButton("Accept Suggestion")
        self.txtContext = QTextEdit()
        self.suggestionLabel = QLabel("Suggestion")
        self.txtSuggestion = QTextEdit()
        self.layout.addWidget(self.categoryLabel)
        self.layout.addWidget(self.txtContext)
        self.layout.addWidget(self.suggestionLabel)
        self.layout.addWidget(self.txtSuggestion)
        self.layout.addWidget(self.btnInsert)
        self.setLayout(self.layout)
