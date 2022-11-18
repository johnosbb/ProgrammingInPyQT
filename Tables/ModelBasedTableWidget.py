from http.client import INSUFFICIENT_STORAGE
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QTableWidget, QTableWidgetItem, QMenu, QAction, QDialog,
                             QInputDialog, QTableView,  QHeaderView, QLineEdit, QLabel, QVBoxLayout)
from PyQt5.QtGui import QIcon, QStandardItemModel

import sys
import beautifulWordsCollection
import beautifulWord
# from PyQt5.QtGui import
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QModelIndex, QRegExp

headers = ["Word", "Meaning", ""]


NUMBER_OF_COLUMNS = 2
NUMBER_OF_ROWS = 4


class TableView(QTableView):
    def __init__(self, wordlist, title, rows, columns):
        QTableView.__init__(self)
        self.wordCollection = wordlist
        # self.proxyModel = QSortFilterProxyModel()
        # self.proxyModel.setDynamicSortFilter(True)
        self.proxyModel = SortFilterProxyModel()
        # This property holds whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change
        self.proxyModel.setDynamicSortFilter(True)
        self.model = QStandardItemModel(
            rows, columns, self)
        self.model.setHeaderData(0, Qt.Horizontal, "Word")
        self.model.setHeaderData(1, Qt.Horizontal, "Meaning")
        # self.setGeometry(300, 300, 700, 450)
        self.setWindowTitle(title)
        # self.setWordData()
        self.setSampleData()

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.verticalHeader().hide()
        self.setSelectionMode(QTableView.SingleSelection)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.clicked.connect(self.getItem)
        self.filterSTring = ""

    def setWordData(self):
        for row, word in enumerate(self.wordCollection.wordList):
            self.model.setData(self.model.index(
                row, 0, QModelIndex()), word.word, Qt.DisplayRole)
            self.model.setData(self.model.index(
                row, 1, QModelIndex()), word.meaning, Qt.DisplayRole)
        self.proxyModel.setSourceModel(self.model)
        self.setModel(self.proxyModel)

    def setSampleData(self):
        self.model.setData(self.model.index(
            0, 0, QModelIndex()), "Abundance", Qt.DisplayRole)
        self.model.setData(self.model.index(
            0, 1, QModelIndex()), "A very large quantity of something", Qt.DisplayRole)
        self.model.setData(self.model.index(
            1, 0, QModelIndex()), "Belonging", Qt.DisplayRole)
        self.model.setData(self.model.index(
            1, 1, QModelIndex()), "An affinity for a place or situation.", Qt.DisplayRole)
        self.model.setData(self.model.index(
            2, 0, QModelIndex()), "Candor", Qt.DisplayRole)
        self.model.setData(self.model.index(
            2, 1, QModelIndex()), "The quality of being open and honest in expression; frankness", Qt.DisplayRole)
        self.proxyModel.setSourceModel(self.model)
        self.setModel(self.proxyModel)

    def setFilterString(self, string):
        self.filterString = "^" + string

    def getItem(self, index):

        mapped_index = self.proxyModel.mapToSource(index)
        item = self.model.itemFromIndex(mapped_index)
        print(item.text() + "  ")
        item = self.model.data(mapped_index)
        row = mapped_index.row()
        column = mapped_index.column()
        data = mapped_index.data()
        item = self.model.itemFromIndex(mapped_index)
        print(item.text() + "  " + str(row) + "  " + str(column) + "  " + data)

    def filterRegExpChanged(self):

        syntax = QRegExp.RegExp  # can be one of QRegExp.RegExp2, QRegExp.WildCard, QRegExp.RegExp2 etc, see https://doc.qt.io/qt-5/qregexp.html#PatternSyntax-enum
        caseSensitivity = Qt.CaseInsensitive
        regExp = QRegExp(self.filterString,
                         caseSensitivity, syntax)
        # This property holds the QRegExp used to filter the contents of the source model
        teststring = "Abundance"
        if regExp.indexIn(teststring) != -1:
            # t = text.replace(value, key)
            print("We found it")
        else:
            print("We did not find it")
        self.proxyModel.setFilterRegExp(regExp)


class SortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        # Do we filter for the date column?
        result = False
        if self.filterKeyColumn() == 0:

            index = self.sourceModel().index(sourceRow, 0, sourceParent)
            data = self.sourceModel().data(index)
            # result = data.startswith("A")
            # Return True if we match a particular condition
            # return (result)
            return True

        # Otherwise ignore
        return super(SortFilterProxyModel, self).filterAcceptsRow(sourceRow, sourceParent)


class WordSelector(QDialog):
    def __init__(self, parent=None):

        QDialog.__init__(self, parent)

        self.parent = parent

        self.lastStart = 0

        self.initUI()

    def initUI(self):
        beautifulWords = beautifulWordsCollection.BeautifulWordsCollection()
        numberOfRows = beautifulWords.load()
        print("Size of word list " + str(len(beautifulWords.wordList)))
        self.table = TableView(beautifulWords, "Beautiful Words",
                               numberOfRows, NUMBER_OF_COLUMNS)
        layout = QVBoxLayout()
        # addWidget(widget, row,column, rowSpan, columnSpan,alignment)
        self.filterLabel = QLabel("  Filter")
        layout.addWidget(self.filterLabel)

        self.filter = QLineEdit(self)
        self.filter.setStyleSheet(
            "background-color: #FFFFFF; padding:1px 1px 1px 1px")
        self.filter.setFixedWidth(120)
        self.filter.returnPressed.connect(self.lookupWord)
        layout.addWidget(self.filter)
        layout.addWidget(self.table)
        self.setGeometry(300, 300, 700, 450)
        # self.setGeometry(300, 300, 360, 250)
        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)

    def lookupWord(self):
        self.table.setFilterString(self.filter.text())
        self.table.filterRegExpChanged()


def main(args):
    app = QApplication(args)

    wordSelector = WordSelector()
    wordSelector.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
