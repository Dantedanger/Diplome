import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import mysql.connector as mc

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from discipline import Discipline
from competence import Competence

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action.triggered.connect(self.onActionTriggered)
        self.ui.action_3.triggered.connect(self.onAction_3Triggered)

    def onActionTriggered(self):
        self.discipline_widget = Discipline()
        self.discipline_widget.show()

    def onAction_3Triggered(self):
        self.discipline_widget = Competence()
        self.discipline_widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
