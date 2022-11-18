from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox, QGridLayout, QLabel, QSpacerItem, \
    QSizePolicy
from PyQt5.QtCore import QSize, QCoreApplication, QSettings

# When creating a QSettings object, you must pass the name of your company or organization as well as the name of your application.
ORGANIZATION_NAME = 'Example App'
ORGANIZATION_DOMAIN = 'example.com'
APPLICATION_NAME = 'QSettings program'
SETTINGS_TRAY = 'settings/tray'


class MainWindow(QMainWindow):
    """
         Checkbox.
         Will initialize in the constructor.
    """
    check_box = None

    # Override the class constructor
    def __init__(self):
        # Be sure to call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(480, 240))  # Set sizes
        self.setWindowTitle("Settings Application")  # Set a title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Set the central widget

        grid_layout = QGridLayout()  # Create a QGridLayout
        # Set the layout into the central widget
        central_widget.setLayout(grid_layout)
        grid_layout.addWidget(
            QLabel("Application, which can minimize to Tray", self), 0, 0)

        # Add a checkbox, which will depend on the behavior of the program when the window is closed
        self.check_box = QCheckBox('Settings CheckBox for minimizing to tray')
        grid_layout.addWidget(self.check_box, 1, 0)
        grid_layout.addItem(QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding), 2, 0)

        # https://doc.qt.io/qtforpython-5/PySide2/QtCore/QSettings.html

        # Get settings
        settings = QSettings()
        # Get checkbox state with speciying type of checkbox:
        # type=bool is a replacement of toBool() in PyQt5
        check_state = settings.value(SETTINGS_TRAY, False, type=bool)
        # Set state
        self.check_box.setChecked(check_state)
        # connect the slot to the signal by clicking the checkbox to save the state settings
        self.check_box.clicked.connect(self.save_check_box_settings)

    # Slot checkbox to save the settings
    def save_check_box_settings(self):
        settings = QSettings()
        # QSettings stores settings. Each setting consists of a QString that specifies the setting’s name (the key ) and a QVariant that stores the data associated with the key. To write a setting, use setValue()
        settings.setValue(SETTINGS_TRAY, self.check_box.isChecked())
        settings.sync()


if __name__ == "__main__":
    import sys

    # When creating a QSettings object, you must pass the name of your company or organization as well as the name of your application.
    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    # When the Internet domain is set, it is used on macOS and iOS instead of the organization name, since macOS and iOS applications conventionally use Internet domains to identify themselves.
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
