import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import mysql.connector as mc

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

        self.ui.pushButton.clicked.connect(self.loadPrograms)

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

    def loadPrograms(self):
        print("load")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
