import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
import mysql.connector as mc

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class Edicational_standart(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        loader.registerCustomWidget(Edicational_standart)
        self.ui = loader.load('edicational_standart.ui', self)

        self.ui.tableWidget.itemChanged.connect(self.updateDatabase)

        self.ui.pushButton.clicked.connect(self.insertDatabase)
        self.ui.pushButton_2.clicked.connect(self.deleteDatabase)

        self.table = self.ui.tableWidget
        self.table.setColumnCount(4)
        self.table.setColumnHidden(0, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        column_labels = ["","Код направления подготовки", "Название", "Сроки получения образования"]
        self.table.setHorizontalHeaderLabels(column_labels)

        self.mydb = self.connect_database()
        self.showDatabase()

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
        cursor.execute("SELECT * FROM edicational_standart")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                 self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        cursor.close()


    def insertDatabase(self):
        cursor = self.mydb.cursor()
        query = "INSERT INTO edicational_standart (Specialization_code, Name, Time) VALUES ('', '', '')"
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
            query = "UPDATE edicational_standart SET Specialization_code=%s, Name=%s, Time=%s WHERE IDEdSt=%s"
            value = (self.table.item(selectedRow, 1).text(),
                    self.table.item(selectedRow, 2).text(),
                    self.table.item(selectedRow, 3).text(),
                    unique_identifier)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()

    def deleteDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "DELETE FROM edicational_standart WHERE IDEdSt=%s"
            value = (unique_identifier,)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.showDatabase()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Edicational_standart()
    widget.show()
    sys.exit(app.exec())
