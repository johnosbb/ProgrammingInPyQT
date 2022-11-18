#!/usr/bin/python3

import sys

from PyQt5.QtCore import Qt, pyqtSignal, QIdentityProxyModel, QModelIndex, QSortFilterProxyModel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlRelationalDelegate
from PyQt5.QtWidgets import QTableView, QTabWidget, QGridLayout, QWidget, QApplication

db_file = "test.db"


# ========================================
# handle database:

def create_connection(db_file):
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_file)
    if not db.open():
        print("Cannot establish a database connection to {}!".format(db_file))
        return False
    return db


def fill_tables():
    q = QSqlQuery()
    q.exec_("DROP TABLE IF EXISTS Manufacturers;")
    q.exec_("CREATE TABLE Manufacturers (Name TEXT, Country TEXT);")
    q.exec_("INSERT INTO Manufacturers VALUES ('VW', 'Germany');")
    q.exec_("INSERT INTO Manufacturers VALUES ('Honda' , 'Japan');")

    q.exec_("DROP TABLE IF EXISTS Cars;")
    q.exec_("CREATE TABLE Cars (Company TEXT, Model TEXT, Year INT);")
    q.exec_("INSERT INTO Cars VALUES ('Honda', 'Civic', 2009);")
    q.exec_("INSERT INTO Cars VALUES ('VW', 'Golf', 2013);")
    q.exec_("INSERT INTO Cars VALUES ('VW', 'Polo', 1999);")


# ========================================
# general classes:

class FlippedProxyModel(QIdentityProxyModel):
    """a proxy model where all columns and rows are inverted
     (compared to the source model);
    source: http://www.howtobuildsoftware.com/index.php/how-do/bgJv/pyqt-pyside-qsqltablemodel-qsqldatabase-qsqlrelationaltablemodel-with-qsqlrelationaldelegate-not-working-behind-qabstractproxymodel
    """

    def mapFromSource(self, index):
        return self.index(index.column(), index.row())

    def mapToSource(self, index):
        return self.sourceModel().index(index.column(), index.row())

    def columnCount(self, parent=QModelIndex()):
        return self.sourceModel().rowCount(parent)

    def rowCount(self, parent=QModelIndex()):
        return self.sourceModel().columnCount(parent)

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column)

    def parent(self, index):
        return QModelIndex()

    def data(self, index, role):
        return self.sourceModel().data(self.mapToSource(index), role)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal:
            return self.sourceModel().headerData(section, Qt.Vertical, role)
        if orientation == Qt.Vertical:
            return self.sourceModel().headerData(section, Qt.Horizontal, role)


class FlippedProxyDelegate(QSqlRelationalDelegate):
    """a delegate for handling data displayed through a FlippedProxyModel;
    source: http://www.howtobuildsoftware.com/index.php/how-do/bgJv/pyqt-pyside-qsqltablemodel-qsqldatabase-qsqlrelationaltablemodel-with-qsqlrelationaldelegate-not-working-behind-qabstractproxymodel
    """

    def createEditor(self, parent, option, index):
        proxy = index.model()
        base_index = proxy.mapToSource(index)
        return super(FlippedProxyDelegate, self).createEditor(parent, option, base_index)

    def setEditorData(self, editor, index):
        proxy = index.model()
        base_index = proxy.mapToSource(index)
        return super(FlippedProxyDelegate, self).setEditorData(editor, base_index)

    def setModelData(self, editor, model, index):
        base_model = model.sourceModel()
        base_index = model.mapToSource(index)
        return super(FlippedProxyDelegate, self).setModelData(editor, base_model, base_index)


class SQLTable(QWidget):
    def __init__(self, query):
        super().__init__()
        self.create_model(query)
        self.init_UI()

    def create_model(self, query):
        self.model = QSortFilterProxyModel()
        querymodel = QSqlQueryModel()
        querymodel.setQuery(query)
        self.model.setSourceModel(querymodel)

    def init_UI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.table = QTableView()
        self.grid.addWidget(self.table, 1, 0)
        self.table.setModel(self.model)


class InvertedTable(SQLTable):
    """a Widget that displays content of an SQLite query inverted
    (= with rows and columns flipped);
    """

    def __init__(self, query=""):
        super().__init__(query)

        self.flipped_model = FlippedProxyModel()
        self.flipped_model.setSourceModel(self.model)
        self.table.setModel(self.flipped_model)
        self.table.setItemDelegate(FlippedProxyDelegate(
            self.table))  # use flipped proxy delegate
        h_header = self.table.horizontalHeader()
        h_header.hide()
        v_header = self.table.verticalHeader()
        v_header.setFixedWidth(70)
        self.table.resizeColumnsToContents()


# ========================================
# application classes:

class MainWidget(QWidget):
    def __init__(self, company):
        super().__init__()
        self.init_UI()
        self.filter(company)

        self.overview.company_changed.connect(self.details.filter)

    def init_UI(self):
        self.resize(400, 400)
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.overview = Overview()
        self.grid.addWidget(self.overview, 0, 0)

        self.details = DetailedView()
        self.grid.addWidget(self.details, 1, 0)

    def filter(self, company):
        self.details.filter(company)


class Overview(SQLTable):
    company_changed = pyqtSignal(str)

    def __init__(self):
        query = "select * from Manufacturers"
        super().__init__(query)
        self.table.clicked.connect(self.on_clicked)

    def on_clicked(self, index):
        company_index = self.model.index(index.row(), 0)
        company = self.model.data(company_index)
        self.company_changed.emit(company)


class DetailedView(QTabWidget):
    def __init__(self):
        super().__init__()
        self.add_tab1()
        self.add_tab2()

    def add_tab1(self):
        query = "select * from cars"
        self.tab1 = InvertedTable(query)
        self.addTab(self.tab1, "Cars")

    def add_tab2(self):
        query = "SELECT company, count(*) as nr_cars from cars group by company"
        self.tab2 = InvertedTable(query)
        self.addTab(self.tab2, "Numbers")

    def filter(self, company):
        for mytab in [self.tab1, self.tab2]:
            mytab.model.layoutAboutToBeChanged.emit()
            mytab.model.setFilterFixedString(company)
            mytab.model.layoutChanged.emit()


# ========================================
# execution:

def main():
    mydb = create_connection(db_file)
    if not mydb:
        sys.exit(-1)
    fill_tables()
    app = QApplication(sys.argv)
    ex = MainWidget('VW')
    ex.show()
    result = app.exec_()

    if (mydb.open()):
        mydb.close()

    sys.exit(result)


if __name__ == '__main__':
    main()

"""
See https://gitpress.io/u/1155/pyqt-example-basicsortfiltermodel

# Work around the fact that QSortFilterProxyModel always filters datetime
# values in QtCore.Qt.ISODate format, but the tree views display using
# QtCore.Qt.DefaultLocaleShortDate format.
class SortFilterProxyModel(QSortFilterProxyModel):
    def filterAcceptsRow(self, sourceRow, sourceParent):
        # Do we filter for the date column?
        if self.filterKeyColumn() == DATE:
            # Fetch datetime value.
            index = self.sourceModel().index(sourceRow, DATE, sourceParent)
            data = self.sourceModel().data(index)

            # Return, if regExp match in displayed format.
            return (self.filterRegExp().indexIn(data.toString(Qt.DefaultLocaleShortDate)) >= 0)

        # Not our business.
        return super(SortFilterProxyModel, self).filterAcceptsRow(sourceRow, sourceParent)
"""
