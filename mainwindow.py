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

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action.triggered.connect(self.onActionTriggered)

        self.ui.tableWidget.itemChanged.connect(self.updateDatabase)

        self.ui.pushButton.clicked.connect(self.insertDatabase)
        self.ui.pushButton_2.clicked.connect(self.deleteDatabase)

        self.table = self.ui.tableWidget
        self.table.setColumnCount(4)

        self.mydb = self.connect_database()
        self.showDatabase()

    def onActionTriggered(self):
        print(f'onActionTriggered')

    def connect_database(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "09.03.04.database"
                )
            print(f'Connected')
            return mydb
        except mc.Error as e:
            print(f'NOT Connected')

    def showDatabase(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM discipline")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                 self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        cursor.close()


    def insertDatabase(self):
        cursor = self.mydb.cursor()
        query = "INSERT INTO discipline (Name, QuantityAcademicHour, Description) VALUES ('', 0, '')"
        cursor.execute(query)
        self.mydb.commit()
        self.showDatabase()
        cursor.close()

    def updateDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "UPDATE discipline SET Name=%s, QuantityAcademicHour=%s, Description=%s WHERE IDD=%s"
            value = (self.table.item(selectedRow, 1).text(),
                    int(self.table.item(selectedRow, 2).text()),
                    self.table.item(selectedRow, 3).text(),
                    unique_identifier)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.showDatabase()

    def deleteDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "DELETE FROM discipline WHERE IDD=%s"
            value = (unique_identifier,)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.showDatabase()


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
