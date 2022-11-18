import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import json
# read in JSON family structure


def readJsonData(fileName):
    with open(fileName) as json_data:
        treeData = json.load(json_data)
    return treeData


fileName = 'family.json'

d = readJsonData(fileName)

myList = []


def myprint(d, myList):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v, myList)
            myList.append(k)
        else:
            myList.append(k)
    return myList


a = myprint(d, myList)


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.tree = QTreeWidget(self)

        self.tree.setSelectionMode(QAbstractItemView.SingleSelection)

        editKey = QShortcut(QKeySequence(Qt.Key_Return), self.tree)
        self.setCentralWidget(self.tree)
        self.tree.setHeaderLabel('Tree')
        i = QTreeWidgetItem(self.tree, [a[len(a)-1]])
        a.pop()
        self.tree.addTopLevelItem(i)
        for x in a:
            QTreeWidgetItem(i, ['{}'.format(x)])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec_())
