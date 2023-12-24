import sys

from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView,QDialog, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
import mysql.connector as mc

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class Discipline(QDialog):
    def __init__(self, mydb):
        super().__init__()
        loader = QUiLoader()
        loader.registerCustomWidget(Discipline)
        self.ui = loader.load('discipline.ui', self)

        self.ui.tableWidget.itemChanged.connect(self.updateDatabase)

        self.ui.pushButton.clicked.connect(self.insertDatabase)
        self.ui.pushButton_2.clicked.connect(self.deleteDatabase)

        self.table = self.ui.tableWidget
        self.table.setColumnCount(4)
        self.table.setColumnHidden(0, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        column_labels = ["","Название", "Кол-во часов", "Описание"]
        self.table.setHorizontalHeaderLabels(column_labels)

        self.mydb = mydb
        self.showDatabase()

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

    def deleteDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            try:
                query = "DELETE FROM discipline WHERE IDD=%s"
                value = (unique_identifier,)
                cursor.execute(query, value)
                self.mydb.commit()
            except mc.errors.IntegrityError as e:
                QMessageBox.warning(None, 'Ошибка', 'Невозможно удалить запись. Она используется в другой таблице.')
            cursor.close()
            self.showDatabase()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Discipline()
    widget.show()
    sys.exit(app.exec())
