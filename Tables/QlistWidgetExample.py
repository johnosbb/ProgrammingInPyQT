import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem


class ListWidgetDemo(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setStyleSheet('font-size: 35px;')

        jan = 'myword : my meaning'
        feb = 'February'
        mar = 'March'
        apr = 'April'
        may = 'May'
        jun = 'June'

        # add one item at a time
        self.addItem(jan)
        # self.addItem(QListWidgetItem(jan))
        self.addItem(feb)

        # add multiple items
        self.addItems([apr, jun])

        # add item based row position
        self.insertItem(2, mar)
        self.insertItem(4, may)

        self.itemDoubleClicked.connect(self.getItem)

    def getItem(self, lstItem):
        print(self.currentItem().text())
        print(lstItem.text())
        print(self.currentRow())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = ListWidgetDemo()
    demo.show()

    sys.exit(app.exec_())
