import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QComboBox, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

import mysql.connector as mc

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class DesciplineCompetence(QDialog):
    def __init__(self, mydb):
        super().__init__()
        loader = QUiLoader()
        loader.registerCustomWidget(DesciplineCompetence)
        self.ui = loader.load('desciplinecompetence.ui', self)

        loader = QUiLoader()
        ui_file_path_add = "desciplinecompetenceadd.ui"
        ui_add = QFile(ui_file_path_add)
        if ui_add.open(QFile.ReadOnly):
            self.ui_add = loader.load(ui_add, self)
            ui_add.close()
            self.ui_file_a = ui_add


        loader = QUiLoader()
        ui_file_path_update = "desciplinecompetenceupdate.ui"
        ui_update = QFile(ui_file_path_update)
        if ui_update.open(QFile.ReadOnly):
            self.ui_update = loader.load(ui_update, self)
            ui_update.close()
            self.ui_file_u = ui_update

        self.ui_add.pushButton.clicked.connect(self.insertDatabase)
        self.ui_add.pushButton_2.clicked.connect(self.ui_add.accept)

        self.ui_update.pushButton.clicked.connect(self.updateDatabase)
        self.ui_update.pushButton_2.clicked.connect(self.ui_update.accept)

        self.ui.pushButton.clicked.connect(self.startInsertDatabase)
        self.ui.pushButton_3.clicked.connect(self.startUpdateDatabase)
        self.ui.pushButton_2.clicked.connect(self.deleteDatabase)

        self.table = self.ui.tableWidget
        self.table.setColumnCount(5)
        self.table.setColumnHidden(0, True)
        self.table.setColumnHidden(1, True)
        self.table.setColumnHidden(2, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        column_labels = ["","","", "Название дисциплины", "Компетенции"]
        self.table.setHorizontalHeaderLabels(column_labels)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.mydb = mydb
        self.showDatabase()

    def showDatabase(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM descipline_competence_view")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                 self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        cursor.close()

    def startInsertDatabase(self):
        self.populate_combobox(self.ui_add)
        self.populate_combobox_2(self.ui_add)
        self.ui_add.setWindowTitle("Добавление")
        self.ui_add.exec()

    def populate_combobox(self,x:QWidget):
        x.comboBox.clear()
        cursor = self.mydb.cursor()
        query = "SELECT IDD, Name FROM discipline"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            item_id = row[0]
            item_text = str(row[1])
            x.comboBox.addItem(item_text, userData=item_id)
        if (x==self.ui_update):
            selectedItems = self.table.selectedItems()
            if (selectedItems):
                self.ui_update.comboBox.setCurrentText(selectedItems[0].text())
        cursor.close()

    def populate_combobox_2(self,x:QWidget):
        x.comboBox_2.clear()
        cursor = self.mydb.cursor()
        query = "SELECT IDC, Name FROM competence"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            item_id = row[0]
            item_text = str(row[1])
            x.comboBox_2.addItem(item_text, userData=item_id)
        if (x==self.ui_update):
            selectedItems = self.table.selectedItems()
            if (selectedItems):
                x.comboBox_2.setCurrentText(selectedItems[1].text())
        cursor.close()

    def insertDatabase(self):
        idd = self.ui_add.comboBox.currentData()
        idc = self.ui_add.comboBox_2.currentData()
        self.ui_add.close()
        cursor = self.mydb.cursor()
        query = "INSERT INTO desciplinecompetence (IDD, IDC) VALUES (%s, %s)"
        value = (idd, idc)
        cursor.execute(query, value)
        self.mydb.commit()
        self.showDatabase()
        cursor.close()

    def startUpdateDatabase(self):
        self.populate_combobox(self.ui_update)
        self.populate_combobox_2(self.ui_update)
        self.ui_update.setWindowTitle("Изменение")
        self.ui_update.exec()

    def updateDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            idd = self.ui_update.comboBox.currentData()
            idc = self.ui_update.comboBox_2.currentData()
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "UPDATE desciplinecompetence SET IDD=%s, IDC=%s WHERE ID=%s"
            value = (idd,idc,unique_identifier)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.ui_update.close()
            self.showDatabase()

    def deleteDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "DELETE FROM desciplinecompetence WHERE ID=%s"
            value = (unique_identifier,)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.showDatabase()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DesciplineCompetence()
    widget.show()
    sys.exit(app.exec())
