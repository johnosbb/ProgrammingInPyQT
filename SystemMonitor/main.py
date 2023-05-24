import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout


class LabelWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Label Window')
        self.setGeometry(200, 200, 200, 200)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def update_label_text(self, label_text):
        self.label.setText(label_text)


class LabelGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Label Grid')
        self.setGeometry(100, 100, 300, 300)
        layout = QGridLayout()
        labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4',
                  'Label 5', 'Label 6', 'Label 7', 'Label 8', 'Label 9']
        for i, label_text in enumerate(labels):
            label = QLabel(label_text)
            label.setAlignment(Qt.AlignCenter)
            label.mousePressEvent = lambda event, label_text=label_text: self.open_label_window(
                label_text)
            layout.addWidget(label, i // 3, i % 3)
        self.setLayout(layout)
        self.show()
        self.label_window = LabelWindow()

    def open_label_window(self, label_text):
        self.label_window.update_label_text(label_text)
        self.label_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    label_grid = LabelGrid()
    sys.exit(app.exec_())
