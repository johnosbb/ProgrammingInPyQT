from PyQt5.uic import loadUi
from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt, QSize
from PyQt5.QtWidgets import (
    QApplication,
    QStyledItemDelegate,
    QWidget,
    QMainWindow,
)


class Editor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("step.ui", self)


class MyListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._data_list = list()

        self._size_hints = dict()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._data_list)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data_list[index.row()]
        elif role == Qt.SizeHintRole:
            return self._size_hints.get(index.row(), QSize(100, 30))

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.SizeHintRole:
            self._size_hints[index.row()] = value
            self.dataChanged.emit(index, index, (role,))
            return True
        return False

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        self.beginResetModel()
        self._data_list = data_list.copy()
        self.endResetModel()


class StyledItemDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = Editor(parent)
        model = index.model()
        model.setData(index, editor.sizeHint(), Qt.SizeHintRole)
        return editor

    def setEditorData(self, editor, index):
        value = index.data()
        editor.label.setText(value)


data = ["Apple", "Strawberry", "Cherry"]


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        """
        Init main window
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.show()


class MyCtrl:
    def __init__(self, view):
        self.view = view

    def load_datalist(self):
        self.model = MyListModel()
        self.model.data_list = data
        self.view.listView.setModel(self.model)
        delegate = StyledItemDelegate(self.view.listView)
        self.view.listView.setItemDelegate(delegate)

        for i in range(self.model.rowCount()):
            index = self.model.index(i, 0)
            self.view.listView.openPersistentEditor(index)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main = MainWindow()
    main.showMaximized()

    controller = MyCtrl(main)
    controller.load_datalist()

    sys.exit(app.exec_())
