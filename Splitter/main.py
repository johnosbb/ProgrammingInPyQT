import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import json


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.tree = QTreeWidget(self)

        self.load_project_structure("./", self.tree)

    def load_project_structure(self, startpath, tree):
        """
        Load Project structure tree
        :param startpath: 
        :param tree: 
        :return: 
        """
        import os
        from PyQt5.QtWidgets import QTreeWidgetItem
        from PyQt5.QtGui import QIcon
        for element in os.listdir(startpath):
            path_info = startpath + "/" + element
            parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
            if os.path.isdir(path_info):
                self.load_project_structure(path_info, parent_itm)
                parent_itm.setIcon(0, QIcon('assets/folder.ico'))
            else:
                parent_itm.setIcon(0, QIcon('assets/file.ico'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec_())


tree = QTreeWidget()
