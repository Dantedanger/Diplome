import sys

from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QLineEdit, QComboBox, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

import mysql.connector as mc

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class SyllibusDiscipline(QDialog):
    def __init__(self, mydb):
        super().__init__()
        loader = QUiLoader()
        loader.registerCustomWidget(SyllibusDiscipline)
        self.ui = loader.load('syllibusdiscipline.ui', self)

        loader = QUiLoader()
        ui_file_path_add = "syllibusdisciplineadd.ui"
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
        self.ui.comboBox.currentIndexChanged.connect(self.filterData)

        self.table = self.ui.tableWidget
        self.table.setColumnCount(7)
        self.table.setColumnHidden(0, True)
        self.table.setColumnHidden(1, True)
        self.table.setColumnHidden(2, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        column_labels = ["","","", "Профиль", "Год учебного плана", "Название дисциплины", "Семестр"]
        self.table.setHorizontalHeaderLabels(column_labels)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.mydb = mydb
        self.filter_combobox()

    def startInsertDatabase(self):
        self.type = True
        self.populate_combobox()
        self.populate_combobox_2()
        self.ui_add.setWindowTitle("Добавление")
        self.ui_add.label_3.setText("Добавление дисциплины в учебный план:")
        self.ui_add.exec()

    def populate_combobox(self):
        self.ui_add.comboBox.clear()
        self.ui_add.lineEdit.setText("")
        cursor = self.mydb.cursor()
        query = "SELECT IDEdPr, Profile, Year FROM edicational_program"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            item_id = row[0]
            item_text = str(row[1])
            item_text2 = str(row[2])
            self.ui_add.comboBox.addItem(item_text+' '+item_text2, userData=item_id)
        if not (self.type):
            selectedItems = self.table.selectedItems()
            self.ui_add.comboBox.setCurrentText(selectedItems[0].text()+' '+ selectedItems[1].text())
            self.ui_add.lineEdit.setText(selectedItems[3].text())
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
        idd = self.ui_add.comboBox.currentData()
        idc = self.ui_add.comboBox_2.currentData()
        semester = self.ui_add.lineEdit.text()
        self.ui_add.close()
        cursor = self.mydb.cursor()
        if (self.type):
            query = "INSERT INTO syllibusdiscipline (IDEdPr, IDD, Semesters) VALUES (%s, %s, %s)"
            value = (idd, idc, semester)
        else:
            selectedItems = self.table.selectedItems()
            selectedRow = selectedItems[0].row()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "UPDATE syllibusdiscipline SET IDEdPr=%s, IDD=%s, Semesters=%s WHERE ID=%s"
            value = (idd,idc,semester,unique_identifier)
        cursor.execute(query, value)
        self.mydb.commit()
        cursor.close()
        self.filterData()

    def startUpdateDatabase(self):
        selectedItems = self.table.selectedItems()
        if not selectedItems:
            QMessageBox.warning(None, 'Ошибка', 'Не выделена строка для обновления')
        else:
            self.type = False
            self.populate_combobox()
            self.populate_combobox_2()
            self.ui_add.setWindowTitle("Изменение")
            self.ui_add.label_3.setText("Изменение дисциплины в учебном плане:")
            self.ui_add.exec()

    def deleteDatabase(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "DELETE FROM syllibusdiscipline WHERE ID=%s"
            value = (unique_identifier,)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.filterData()

    def filter_combobox(self):
        self.ui.comboBox.clear()
        cursor = self.mydb.cursor()
        query = "SELECT IDEdPr, Profile, Year FROM edicational_program"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            item_id = row[0]
            item_text = str(row[1])
            item_text2 = str(row[2])
            self.ui.comboBox.addItem(item_text+' '+item_text2, userData=item_id)
        cursor.close()

    def filterData(self):
        prof_year = self.ui.comboBox.currentText()
        prof = prof_year[:-5]  # Получить все символы до последних 4
        year = prof_year[-4:]  # Получить последние 4 символа
        cursor = self.mydb.cursor()
        query = "SELECT * FROM syllibusdiscipline_view WHERE Profile = %s AND Year= %s"
        cursor.execute(query, (prof, year))
        filtered_data = cursor.fetchall()

        self.table.setRowCount(len(filtered_data))
        self.table.setColumnCount(len(filtered_data[0]))

        for i, row in enumerate(filtered_data):
            for j, cell in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(cell)))
        cursor.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = SyllibusDiscipline()
    widget.show()
    sys.exit(app.exec())
