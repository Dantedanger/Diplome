import sys

from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QLineEdit, QComboBox, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

import mysql.connector as mc

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class Educational_program(QDialog):
    def __init__(self, mydb):
        super().__init__()
        loader = QUiLoader()
        loader.registerCustomWidget(Educational_program)
        self.ui = loader.load('educational_program.ui', self)

        loader = QUiLoader()
        ui_file_path_add = "educational_programadd.ui"
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

        self.table = self.ui.tableWidget
        self.table.setColumnCount(5)
        self.table.setColumnHidden(0, True)
        self.table.setColumnHidden(1, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        column_labels = ["","","Название образовательного стандарта","Профиль","Год плана"]
        self.table.setHorizontalHeaderLabels(column_labels)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.mydb = mydb
        self.showDatabase()

    def showDatabase(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM edicational_program_view")
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
        self.ui_add.setWindowTitle("Добавление")
        self.ui_add.label_3.setText("Добавление образовательной программы:")
        self.ui_add.lineEdit_2.setText("")
        self.ui_add.lineEdit_3.setText("")
        self.ui_add.exec()

    def populate_combobox(self):
        self.ui_add.comboBox.clear()
        cursor = self.mydb.cursor()
        query = "SELECT IDEdSt, Name FROM edicational_standart"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            item_id = row[0]
            item_text = str(row[1])
            self.ui_add.comboBox.addItem(item_text, userData=item_id)
        if not(self.type):
            selectedItems = self.table.selectedItems()
            if (selectedItems):
                self.ui_add.comboBox.setCurrentText(selectedItems[0].text())
                self.ui_add.lineEdit_2.setText(selectedItems[1].text())
                self.ui_add.lineEdit_3.setText(selectedItems[2].text())
        cursor.close()

    def insertDatabase(self):
        idedst = self.ui_add.comboBox.currentData()
        profile = self.ui_add.lineEdit_2.text()
        year = self.ui_add.lineEdit_3.text()
        cursor = self.mydb.cursor()
        self.ui_add.close()
        if (self.type):
            query = "INSERT INTO edicational_program (IDEdSt, Profile, Year) VALUES (%s, %s, %s)"
            value = (idedst, profile, year)
        else:
            selectedItems = self.table.selectedItems()
            selectedRow = selectedItems[0].row()
            unique_identifier = int(self.table.item(selectedRow, 1).text())
            query = "UPDATE edicational_program SET IDEdSt=%s, Profile=%s, Year=%s WHERE IDEdPr=%s"
            value = (idedst, profile, year, unique_identifier)
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
            self.ui_add.setWindowTitle("Изменение")
            self.ui_add.label_3.setText("Изменение образовательной программы:")
            self.ui_add.exec()

    def deleteDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 1).text())
            try:
                query = "DELETE FROM edicational_program WHERE IDEdPr=%s"
                value = (unique_identifier,)
                cursor.execute(query, value)
                self.mydb.commit()
            except mc.errors.IntegrityError as e:
                QMessageBox.warning(None, 'Ошибка', 'Невозможно удалить запись. Она используется в другой таблице.')
            cursor.close()
            self.showDatabase()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Educational_program()
    widget.show()
    sys.exit(app.exec())
