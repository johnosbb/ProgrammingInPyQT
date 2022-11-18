from PyQt5.QtCore import (QSize, QRegExp)
from PyQt5.QtGui import QIcon, QKeySequence, QTextCursor, QTextCharFormat
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow,
                             QTextEdit, QLineEdit)
from sys import argv, exit
import re


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(50, 50, 800, 600)
        self.windowList = []
        self.myeditor = QTextEdit(""" Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.""")
        self.myeditor.setAcceptRichText(False)
        self.myeditor.setUndoRedoEnabled(True)

        self.createActions()
        self.createToolBars()

        self.setWindowIcon(QIcon.fromTheme("accessories-text-editor"))

        self.setCentralWidget(self.myeditor)
        self.findfield.setFocus()

    def createToolBars(self):
        self.findToolBar = self.addToolBar("Suchen")
        self.findToolBar.setIconSize(QSize(16, 16))
        self.findfield = QLineEdit()
        self.findfield.addAction(QIcon.fromTheme("edit-find"), 0)
        self.findfield.setClearButtonEnabled(True)
        self.findfield.setFixedWidth(200)
        self.findfield.setPlaceholderText("search")
        self.findfield.setStatusTip("press RETURN")
        self.findfield.setText("ipsum")
        self.findfield.returnPressed.connect(self.findText)

        self.findUnderlinedField = QLineEdit()
        self.findUnderlinedField.addAction(QIcon.fromTheme("edit-find"), 0)
        self.findUnderlinedField.setClearButtonEnabled(True)
        self.findUnderlinedField.setFixedWidth(200)
        self.findUnderlinedField.setPlaceholderText("search")
        self.findUnderlinedField.setStatusTip("press RETURN")
        self.findUnderlinedField.setText("Find Underlined Text")
        self.findUnderlinedField.returnPressed.connect(
            self.setFindUnderlinedText)

        self.findToolBar.addWidget(self.findfield)
        self.findToolBar.addWidget(self.findUnderlinedField)

    def createActions(self):
        self.findAct = QAction(QIcon.fromTheme('edit-find'), "find", self,
                               shortcut=QKeySequence.Find, statusTip="find",
                               triggered=self.setFindText)
        self.findAct = QAction(QIcon.fromTheme('edit-find'), "find underlined", self,
                               shortcut=QKeySequence.FindNext, statusTip="find underlined text",
                               triggered=self.setFindUnderlinedText)

    def setFindText(self):
        self.findfield.setText(self.myeditor.textCursor().selectedText())
        self.findText()

    def setFindUnderlinedText(self):
        self.findUnderlinedField.setText(
            self.myeditor.textCursor().selectedText())
        self.findUnderLinedText()

    def findText(self):
        fmt = QTextCharFormat()
        fmt.setFontUnderline(False)
        self.myeditor.selectAll()
        self.myeditor.textCursor().mergeCharFormat(fmt)
        self.myeditor.moveCursor(QTextCursor.Start)
        fmt.setFontUnderline(True)
        word = self.findfield.text()
        while self.myeditor.find(word):
            textcursor = self.myeditor.textCursor()
            pos = textcursor.position()
            print('pos {}'.format(pos))
            textcursor.select(QTextCursor.WordUnderCursor)
            textcursor.mergeCharFormat(fmt)
            self.myeditor.setTextCursor(textcursor)

    def findUnderLinedText(self):
        self.myeditor.moveCursor(QTextCursor.Start)
        reg = QRegExp(r"\b([A-Za-z]{2,})\b")
        while self.myeditor.find(reg):
            textcursor = self.myeditor.textCursor()
            textCursorAttribute = self.myeditor.textCursor()
            pos = textcursor.position()
            textcursor.select(QTextCursor.WordUnderCursor)
            wordToCheck = textcursor.selectedText()
            rangeStart = textCursorAttribute.selectionStart()
            if textcursor.hasSelection():
                rangeEnd = textcursor.selectionEnd() + 1
            else:
                rangeEnd = textcursor.selectionStart() + 1
            wordToCheck = textcursor.selectedText()
            for pos in range(rangeStart, rangeEnd):
                textCursorAttribute.setPosition(pos)
                fmt = textCursorAttribute.charFormat()
                underline = fmt.fontUnderline()
                colour = fmt.underlineColor()
                print('word to check {}, cursor position {}, underline {},  colour {}'.format(
                    wordToCheck, str(pos), str(underline), str(colour.name())))

            self.myeditor.setTextCursor(textcursor)


if __name__ == '__main__':
    app = QApplication(argv)
    mainWin = MainWindow()
    mainWin.show()
    exit(app.exec_())
