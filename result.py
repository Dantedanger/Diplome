import sys

from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QLineEdit, QComboBox, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

import mysql.connector as mc

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class Result(QDialog):
    def __init__(self, mydb):
        super().__init__()
        loader = QUiLoader()
        loader.registerCustomWidget(Result)
        self.ui = loader.load('result.ui', self)

        loader = QUiLoader()
        ui_file_path_add = "resultadd.ui"
        ui_add = QFile(ui_file_path_add)
        if ui_add.open(QFile.ReadOnly):
            self.ui_add = loader.load(ui_add, self)
            ui_add.close()
            self.ui_file_a = ui_add

        self.ui_add.pushButton.clicked.connect(self.insertDatabase)
        self.ui_add.pushButton_2.clicked.connect(self.ui_add.accept)

        self.ui.pushButton.clicked.connect(self.startInsertDatabase)
        self.ui.pushButton_3.clicked.connect(self.startUpdateDatabase)
        self.ui.pushButton_2.clicked.connect(self.deleteDatabase)
        self.ui.pushButton_4.clicked.connect(self.getResult)
        self.ui.pushButton_5.clicked.connect(self.getAllResult)
        self.ui.pushButton_6.clicked.connect(self.loadAll)

        self.table = self.ui.tableWidget
        self.table.setColumnCount(9)
        self.table.setColumnHidden(0, True)
        self.table.setColumnHidden(1, True)
        self.table.setColumnHidden(2, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        column_labels = ["","","", "Название дисциплины 1", "Предметная область", "Название дисциплины 2", "Предметная область","Связь","Описание"]
        self.table.setHorizontalHeaderLabels(column_labels)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.mydb = mydb
        self.showDatabase()

    def showDatabase(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM result_view")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                 self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        cursor.close()

    def startInsertDatabase(self):
        self.type = True
        self.populate_combobox()
        self.populate_combobox_2()
        self.ui_add.setWindowTitle("Добавление")
        self.ui_add.label_3.setText("Добавление результата:")
        self.ui_add.exec()

    def populate_combobox(self):
        self.ui_add.comboBox.clear()
        cursor = self.mydb.cursor()
        query = "SELECT IDD, Name FROM discipline"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            item_id = row[0]
            item_text = str(row[1])
            self.ui_add.comboBox.addItem(item_text, userData=item_id)
        if not(self.type):
            selectedItems = self.table.selectedItems()
            self.ui_add.comboBox.setCurrentText(selectedItems[0].text())
        cursor.close()

    def populate_combobox_2(self):
        self.ui_add.comboBox_2.clear()
        cursor = self.mydb.cursor()
        query = "SELECT IDD, Name FROM discipline"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            item_id = row[0]
            item_text = str(row[1])
            self.ui_add.comboBox_2.addItem(item_text, userData=item_id)
        if not (self.type):
            selectedItems = self.table.selectedItems()
            self.ui_add.comboBox_2.setCurrentText(selectedItems[2].text())
        cursor.close()

    def insertDatabase(self):
        idd1 = self.ui_add.comboBox.currentData()
        idd2 = self.ui_add.comboBox_2.currentData()
        self.ui_add.close()
        cursor = self.mydb.cursor()
        if (self.type):
            query = "INSERT INTO result (IDD1, IDD2) VALUES (%s, %s)"
            value = (idd1, idd2)
        else:
            selectedItems = self.table.selectedItems()
            selectedRow = selectedItems[0].row()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "UPDATE result SET IDD1=%s, IDD2=%s, Object1='', Object2='', Relations=0, DescriptionR='' WHERE IDResult=%s"
            value = (idd1,idd2,unique_identifier)
        cursor.execute(query, value)
        self.mydb.commit()
        cursor.close()
        self.showDatabase()

    def startUpdateDatabase(self):
        selectedItems = self.table.selectedItems()
        if not selectedItems:
            QMessageBox.warning(None, 'Ошибка', 'Не выделена строка для обновления')
        else:
            self.type = False
            self.populate_combobox()
            self.populate_combobox_2()
            self.ui_add.setWindowTitle("Изменение")
            self.ui_add.label_3.setText("Изменение результата:")
            self.ui_add.exec()

    def deleteDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "DELETE FROM result WHERE IDResult=%s"
            value = (unique_identifier,)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.showDatabase()

    def getResult(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            text = "Checked"
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "UPDATE result SET Object1=%s, Object2=%s, Relations=0, DescriptionR=%s WHERE IDResult=%s"
            value = (text,text,text,unique_identifier)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.ui_add.close()
            self.showDatabase()

    def getAllResult(self):
        print("getall")

    def loadAll(self):
        print("loadall")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Result()
    widget.show()
    sys.exit(app.exec())
