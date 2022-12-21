
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import logging
import re
from specialAction import SpecialAction
from highlighter import Highlighter
# from spellCheck import SpellCheck
import collections
from pprint import pprint


class CorrectorTextEdit(QTextEdit):

    wordReplaced = pyqtSignal(object, object)

    def __init__(self, *args):
        super().__init__(*args[3:])
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.createContextMenu()
        self.customContextMenuRequested.connect(self.createContextMenu)
        self.rule = None
        self.rules = None

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            cursor = self.cursorForPosition(event.pos())
            # self.contextMenu = self.createStandardContextMenu(event.pos())

            position = cursor.position()
            textCursor = self.textCursor()
            textCursor.setPosition(position)
            rule = self.findAssociatedRule(position)
            if rule:
                self.addHelperContexts(rule)
            else:
                print("No rules found for this word")
            self.contextMenu.exec_(event.globalPos())

    def createContextMenu(self):
        self.contextMenu = QMenu(self)
        action1 = QAction("First option")
        action1.triggered.connect(lambda: print(
            "You have clicked the first option"))

        action2 = QAction("Second option")
        action2.triggered.connect(lambda: print(
            "You have clicked the second option"))

        self.contextMenu.addAction(action1)
        self.contextMenu.addAction(action2)

        # self.contextMenu.exec_(QCursor.pos())

    # def contextMenuEvent(self, event: QContextMenuEvent) -> None:
    #     self.contextMenu = self.createStandardContextMenu(event.pos())
    #     print(event.pos())

    #     # we only want to check single isolated words.
    #     rule = self.findAssociatedRule()
    #     if rule:
    #         self.addHelperContexts(rule)
    #     else:
    #         print("No rules found for this word")
    #     self.contextMenu.exec_(event.globalPos())

    def addHelperContexts(self, rule):
        suggestions = rule.replacements
        if len(suggestions) > 0:
            self.contextMenu.addSeparator()
            self.contextMenu.addMenu(self.createSuggestionsMenu(suggestions))

    def setRule(self, rule):
        self.rule = rule

    def setRules(self, rules):
        self.rules = rules

    def replaceSelectedWord(self, word, rule):

        textCursor = self.textCursor()
        textCursor.beginEditBlock()
        textCursor.clearSelection()
        textCursor.setPosition(rule.offset)
        originalLength = len(rule.matchedText)
        modifiedLength = len(word)
        changeInOffset = modifiedLength - originalLength
        print("Change in offset {}".format(changeInOffset))
        textCursor.setPosition(
            rule.offset + rule.errorLength, QTextCursor.KeepAnchor)
        self.setTextCursor(textCursor)
        textCursor.removeSelectedText()
        textCursor.insertText(word)
        textCursor.endEditBlock()
        self.ensureCursorVisible()
        self.wordReplaced.emit(rule, changeInOffset)

    @ pyqtSlot(str)
    def correctWord(self, word: str):
        self.replaceSelectedWord(word, self.rule)

    def createSuggestionsMenu(self, suggestions: list[str]):
        suggestionsMenu = QMenu("Change to", self)
        for word in suggestions:
            action = SpecialAction(word, self.contextMenu)
            action.actionTriggered.connect(self.correctWord)
            suggestionsMenu.addAction(action)
        return suggestionsMenu

    def findAssociatedRule(self, currentPosition):
        # we only want to check single isolated words.
        print("Finding rules for position {}\n".format(
            currentPosition))
        for rule in self.rules:
            ruleStart = (rule.offset)
            ruleEnd = (rule.errorLength+rule.offset)
            # if((start >= ruleStart) and (end <= ruleEnd)):
            if((currentPosition >= ruleStart) and (currentPosition <= ruleEnd)):
                print(" Position: {} - RS {} - RE {} ".format(
                    currentPosition, ruleStart,  ruleEnd))
                self.rule = rule
                return rule
        return None