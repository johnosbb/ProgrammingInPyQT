from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import beautifulWordsCollection
import beautifulWord


headers = ["Word", "Meaning", ""]


NUMBER_OF_COLUMNS = 2
NUMBER_OF_ROWS = 4


class TableView(QTableWidget):
    def __init__(self, wordlist, title, * args):
        QTableWidget.__init__(self, *args)
        self.wordCollection = wordlist
        self.setGeometry(300, 300, 700, 450)
        self.setWindowTitle(title)
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.verticalHeader().hide()
        self.itemDoubleClicked.connect(self.getItem)

    def setData(self):
        for row, word in enumerate(self.wordCollection.wordList):
            wordItem = QTableWidgetItem(word.word)
            self.setItem(row, 0, wordItem)
            meaningItem = QTableWidgetItem(word.meaning)
            self.setItem(row, 1, meaningItem)
        self.setHorizontalHeaderLabels(headers)

    def getItem(self, lstItem):
        print(self.currentItem().text())
        print(lstItem.text())
        print(self.currentRow())


def main(args):
    app = QApplication(args)
    beautifulWords = beautifulWordsCollection.BeautifulWordsCollection()
    numberOfRows = beautifulWords.load()
    print("Size of word list " + str(len(beautifulWords.wordList)))
    table = TableView(beautifulWords, "Beautiful Words",
                      numberOfRows, NUMBER_OF_COLUMNS)
    table.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
