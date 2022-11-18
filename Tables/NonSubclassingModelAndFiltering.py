

from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QTableWidget, QTableWidgetItem, QMenu, QAction, QDialog,
                             QInputDialog, QTableView,  QHeaderView, QLineEdit, QLabel, QVBoxLayout)
from PyQt5.QtGui import QIcon, QStandardItemModel

import sys
import beautifulWordsCollection
import beautifulWord
import re

from PyQt5.QtCore import Qt, QSortFilterProxyModel, QModelIndex, QRegExp
from typing import Callable

headers = ["Word", "Meaning", ""]


NUMBER_OF_COLUMNS = 2
NUMBER_OF_ROWS = 3
COLUMN_TO_FILTER = 1

# see also https://stackoverflow.com/questions/47201539/how-to-filter-multiple-column-in-qtableview


class SortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent):
        self.parentReference = parent
        super().__init__()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        result = False
        if self.filterKeyColumn() == COLUMN_TO_FILTER:
            index = self.sourceModel().index(sourceRow, COLUMN_TO_FILTER, sourceParent)
            data = self.sourceModel().data(index).lstrip()
            # Note that the result raw string has the quote at the beginning and end of the string. To remove them, you can use slices: [1:-1]
            pattern = repr(self.parentReference.filterString)[1:-1]
            # print(data)
            if(re.search(pattern, data)):
                return True
        # Otherwise ignore
        return super(SortFilterProxyModel, self).filterAcceptsRow(sourceRow, sourceParent)

# Reference: https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/qtjambi-customfilter.html


class WordSelector(QDialog):
    def __init__(self,  title,  parent=None):
        QDialog.__init__(self,  parent)
        self.parent = parent
        self.lastStart = 0

        self.proxyModel = SortFilterProxyModel(self)
        # This property holds whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change
        self.proxyModel.setDynamicSortFilter(True)

        self.sourceView = QTableView()  # where we store the unfiltered list

        self.proxyView = QTableView()
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)

        self.setWindowTitle(title)
        self.proxyView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.proxyView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setSortingEnabled(True)
        self.proxyView.verticalHeader().hide()
        self.proxyView.setSelectionMode(QTableView.SingleSelection)
        self.proxyView.setSelectionBehavior(QTableView.SelectRows)
        self.proxyView.clicked.connect(self.getItem)
        self.filterString = ""
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        self.filterLabel = QLabel("  Filter")
        layout.addWidget(self.filterLabel)
        self.wordFilter = QLineEdit(self)
        self.wordFilter.setStyleSheet(
            "background-color: #FFFFFF; padding:1px 1px 1px 1px")
        self.wordFilter.setFixedWidth(120)
        self.wordFilter.returnPressed.connect(self.setWordFilter)

        layout.addWidget(self.wordFilter)

        self.meaningFilter = QLineEdit(self)
        self.meaningFilter.setStyleSheet(
            "background-color: #FFFFFF; padding:1px 1px 1px 1px")
        self.meaningFilter.setFixedWidth(120)
        self.meaningFilter.returnPressed.connect(self.setMeaningFilter)

        layout.addWidget(self.meaningFilter)

        layout.addWidget(self.proxyView)
        self.setGeometry(300, 300, 500, 300)

        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)

    def setWordFilterString(self, string):
        self.filterString = "^" + string

    def setMeaningFilterString(self, string):
        self.filterString = string

    def getItem(self, index):

        mapped_index = self.proxyModel.mapToSource(index)
        row = mapped_index.row()
        column = mapped_index.column()
        data = mapped_index.data()
        print("Row:  " + str(row) + ",Column:  " + str(column) + "  " + data)

    def setWordFilter(self):
        self.setWordFilterString(self.wordFilter.text())
        self.filterRegExpChanged()

    def setMeaningFilter(self):
        self.setMeaningFilterString(self.meaningFilter.text())
        self.filterRegExpChanged()

    def setSourceModel(self, model):
        self.proxyModel.setSourceModel(model)
        self.sourceView.setModel(model)

    def filterRegExpChanged(self):

        syntax = QRegExp.RegExp  # can be one of QRegExp.RegExp2, QRegExp.WildCard, QRegExp.RegExp2 etc, see https://doc.qt.io/qt-5/qregexp.html#PatternSyntax-enum
        caseSensitivity = Qt.CaseInsensitive
        regExp = QRegExp(self.filterString,
                         caseSensitivity, syntax)
        self.proxyModel.setFilterKeyColumn(COLUMN_TO_FILTER)
        # This property holds the QRegExp used to filter the contents of the source model
        self.proxyModel.setFilterRegExp(regExp)


def createModel(parent):

    beautifulWords = beautifulWordsCollection.BeautifulWordsCollection()
    numberOfRows = beautifulWords.load()
    model = QStandardItemModel(
        numberOfRows, NUMBER_OF_COLUMNS, parent)  # rows columns
    model.setHeaderData(0, Qt.Horizontal, "Word")
    model.setHeaderData(1, Qt.Horizontal, "Meaning")
    for row, word in enumerate(beautifulWords.wordList):
        model.setData(model.index(
            row, 0, QModelIndex()), word.word, Qt.DisplayRole)
        model.setData(model.index(
            row, 1, QModelIndex()), word.meaning, Qt.DisplayRole)
    return model


def main(args):
    app = QApplication(args)
    wordSelector = WordSelector("words")
    wordSelector.setSourceModel(createModel(wordSelector))
    wordSelector.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
