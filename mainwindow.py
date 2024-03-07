import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QMainWindow, QWidget, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import mysql.connector as mc
from docx import Document
import re

#     pyside6-uic D:\QtProjects\Diplom\form.ui -o D:\QtProjects\Diplom\ui_form.py
#     pyside6-uic D:\QtProjects\Diplom\discipline.ui -o D:\QtProjects\Diplom\ui_discipline.py
#     pyside6-uic D:\QtProjects\Diplom\competence.ui -o D:\QtProjects\Diplom\ui_competence.py
#     pyside6-uic D:\QtProjects\Diplom\edicational_standart.ui -o D:\QtProjects\Diplom\ui_edicational_standart.py
#     pyside6-uic D:\QtProjects\Diplom\desciplinecompetence.ui -o D:\QtProjects\Diplom\ui_desciplinecompetence.py
#     pyside6-uic D:\QtProjects\Diplom\desciplinecompetenceadd.ui -o D:\QtProjects\Diplom\ui_desciplinecompetenceadd.py
#     pyside6-uic D:\QtProjects\Diplom\educational_program.ui -o D:\QtProjects\Diplom\ui_educational_program.py
#     pyside6-uic D:\QtProjects\Diplom\educational_programadd.ui -o D:\QtProjects\Diplom\ui_educational_programadd.py
#     pyside6-uic D:\QtProjects\Diplom\syllibusdiscipline.ui -o D:\QtProjects\Diplom\ui_syllibusdiscipline.py
#     pyside6-uic D:\QtProjects\Diplom\syllibusdisciplineadd.ui -o D:\QtProjects\Diplom\ui_syllibusdisciplineadd.py
#     pyside6-uic D:\QtProjects\Diplom\result.ui -o D:\QtProjects\Diplom\ui_syllibusresult.py
#     pyside6-uic D:\QtProjects\Diplom\resultadd.ui -o D:\QtProjects\Diplom\ui_syllibusresulteadd.py

from ui_form import Ui_MainWindow
from discipline import Discipline
from competence import Competence
from edicational_standart import Edicational_standart
from desciplinecompetence import DesciplineCompetence
from educational_program import Educational_program
from syllibusdiscipline import SyllibusDiscipline
from result import Result

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.load_files)

        self.ui.action.triggered.connect(self.onActionTriggered)
        self.ui.action_2.triggered.connect(self.onAction_2Triggered)
        self.ui.action_3.triggered.connect(self.onAction_3Triggered)
        self.ui.action_4.triggered.connect(self.onAction_4Triggered)
        self.ui.action_5.triggered.connect(self.onAction_5Triggered)
        self.ui.action_6.triggered.connect(self.onAction_6Triggered)
        self.ui.action_7.triggered.connect(self.onAction_7Triggered)

        self.mydb = self.connect_database()

    def onActionTriggered(self):
        self.discipline_widget = Discipline(self.mydb)
        self.discipline_widget.setWindowTitle("Дисциплины")
        self.discipline_widget.exec()

    def onAction_2Triggered(self):
        self.discipline_widget = SyllibusDiscipline(self.mydb)
        self.discipline_widget.setWindowTitle("Дисциплины учебного плана")
        self.discipline_widget.exec()

    def onAction_3Triggered(self):
        self.competence_widget = Competence(self.mydb)
        self.competence_widget.setWindowTitle("Компетенции")
        self.competence_widget.exec()

    def onAction_4Triggered(self):
        self.competence_widget = DesciplineCompetence(self.mydb)
        self.competence_widget.setWindowTitle("Компетенции и дисциплины")
        self.competence_widget.exec()

    def onAction_5Triggered(self):
        self.edicational_standart_widget = Edicational_standart(self.mydb)
        self.edicational_standart_widget.setWindowTitle("Образовательный стандарт")
        self.edicational_standart_widget.exec()

    def onAction_6Triggered(self):
        self.edicational_standart_widget = Educational_program(self.mydb)
        self.edicational_standart_widget.setWindowTitle("Образовательная программа")
        self.edicational_standart_widget.exec()

    def onAction_7Triggered(self):
        self.edicational_standart_widget = Result(self.mydb)
        self.edicational_standart_widget.setWindowTitle("Связь двух дисциплин")
        self.edicational_standart_widget.exec()

    def connect_database(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "09.03.04.database"
                )
            print(f'Connect')
            return mydb
        except mc.Error as e:
            print(f'NOT Connected')
            return False

    def closeEvent(self, event):
        self.mydb.close()
        print(f'Disconnect')
        event.accept()

    def load_files(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Документы (*.docx)")

        if file_dialog.exec():
            files = file_dialog.selectedFiles()
            for file_name in files:
                print(f"РАБОЧАЯ ПРОГРАММА ДИСЦИПЛИНЫ:", end = ' ')
                self.search_words(file_name, "РАБОЧАЯ ПРОГРАММА ДИСЦИПЛИНЫ")

                print(f"Направление подготовки:", end = ' ')
                self.search_words(file_name, "Направление подготовки")

                print(f"Уровень высшего образования:", end = ' ')
                self.search_words(file_name, "Уровень высшего образования")

                print(f"Направленность (профиль) образовательной программы:", end = ' ')
                self.search_words(file_name, "Направленность (профиль) образовательной программы")

#                print(f"Направленность (профиль) образовательной программы:", end = ' ')
#                self.find_word_after_target(file_name, "")

                print(f"Код компе-тенции:", end = ' ')
                self.find_column_data_below_target(file_name, "Код компе-тенции")

                print(f"Количество часов:", end = ' ')
                self.find_number_before_word(file_name, "час")

    def find_number_before_word(self, doc_name, target_word):
        doc = Document(doc_name)
        for paragraph in doc.paragraphs:
            match = re.search(r'(\d+)\s+' + re.escape(target_word), paragraph.text)
            if match:
                number = match.group(1)
                print(f"{number}")
                return

    def search_words(self, doc_name, target_word):
        doc = Document(doc_name)
        found_target = False

        for paragraph in doc.paragraphs:
            if found_target:
                if paragraph.text.strip():
                    print(paragraph.text.strip())
                    return
            elif target_word in paragraph.text:
                found_target = True

#    def search_words(self, doc_name, target_word):
#        doc = Document(doc_name)
#        found = False

#        for table in doc.tables:
#            for row in table.rows:
#                for cell in row.cells:
#                    # Ищем в первой ячейке
#                    if target_word in cell.text.strip():
#                        # Печатаем текст из второй ячейки
#                        related_cell_text = row.cells[1].text.strip()
#                        print(f"{related_cell_text}")
#                        found = True

#        if not found:
#            print(f"Слово '{target_word}' не найдено в документе.")
    def find_word_after_target(self, doc_name, target_word):
        doc = Document(doc_name)
        found_target = False

        for paragraph in doc.paragraphs:
            if found_target:
                words = paragraph.text.strip().split()
                if words:
                    next_word = words[0]
                    print(f"Найдено слово после строки с ключевым словом: {next_word}")
                    return
            elif target_word in paragraph.text:
                found_target = True

    def find_column_data_below_target(self, doc_name, target_text):
        doc = Document(doc_name)
        found_target = False
        target_row_data = []

        for table in doc.tables:
            for row in table.rows:
                if found_target:
                    first_column_data = row.cells[0].text.strip()
                    second_column_data = row.cells[1].text.strip()
                    target_row_data.append((first_column_data, second_column_data))
                else:
                    for cell in row.cells:
                        if target_text in cell.text.strip():
                            found_target = True
                            break
            if found_target:
                found_target = False
                break
        for row_data in target_row_data:
            print(row_data[0], row_data[1], end = ' ')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
