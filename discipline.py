import sys

from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView,QDialog, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
import mysql.connector as mc

import re
from pymorphy2 import MorphAnalyzer
import nltk
from nltk.corpus import stopwords

import os
import numpy as np
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import joblib

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
        self.ui.pushButton_3.clicked.connect(self.objectOne)
        self.ui.pushButton_4.clicked.connect(self.objectAll)

        self.table = self.ui.tableWidget
        self.table.setColumnCount(5)
        self.table.setColumnHidden(0, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        column_labels = ["","Название", "Кол-во часов", "Описание", "Предметная область"]
        self.table.setHorizontalHeaderLabels(column_labels)

        self.morph = MorphAnalyzer()
        self.model_vec = Word2Vec.load("updated_model")
        self.kmeans = joblib.load('kmeans_model.pkl')
        nltk.download('stopwords')

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
        query = "INSERT INTO discipline (Name, QuantityAcademicHour, Description, Object) VALUES ('', 0, '', '')"
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
            query = "UPDATE discipline SET Name=%s, QuantityAcademicHour=%s, Description=%s, Object=%s WHERE IDD=%s"
            value = (self.table.item(selectedRow, 1).text(),
                    int(self.table.item(selectedRow, 2).text()),
                    self.table.item(selectedRow, 3).text(),
                    '',
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

    def get_word_vectors(self, text, model):
        vectors = []
        for word in text:
            if word in model.wv:
                vectors.append(model.wv[word])
        return vectors

    def kMeansDoing(self, description):
        description = self.lemmatize(description)
        text = description

        self.model_vec.build_vocab(text, update=True)
        self.model_vec.train(text, total_examples=self.model_vec.corpus_count, epochs=self.model_vec.epochs)

        word = [[self.model_vec.wv[token][0] for token in doc] for doc in text]

        text_word_vectors = [self.get_word_vectors(text, self.model_vec)]

        # Сбор всех векторов слов в один массив
        all_word_vectors = [vector for vectors in text_word_vectors for vector in vectors]
        # Кластеризация всех векторов слов
        text_cluster_counts = [np.bincount(self.kmeans.predict(vectors), minlength=2) for vectors in text_word_vectors]
        classification_labels = ["Гуманитарная" if counts[0] > counts[1] else "Техническая" for counts in text_cluster_counts]
                # Вывод результата классификации
        for label in classification_labels:
            print("Text:", text)
            print("Classification label:", label)
            return label

    def lemmatize(self,doc):
        patterns = "[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\\]^_`{|}~—\"\\-]+«»"
        stopwords_ru = stopwords.words("russian")
        filters='!-"—#$%&amp;,()*+,-./:;<=>?@[\\]^_`{|}~\t\n\r«»'
        for znak in filters:
            if znak in doc:
                doc = doc.replace(znak, "")
        doc = doc.lower()
        doc = re.sub(patterns, ' ', doc)
        tokens = []
        for token in doc.split():
            if token and token not in stopwords_ru and token != 'с':
                token = token.strip()
                if token == 'ии':
                    token = 'искусственый'
                    tokens.append(token)
                    token = 'интеллект'
                    tokens.append(token)
                else:
                    token = self.morph.normal_forms(token)[0]
                    tokens.append(token)
        return tokens


    def objectOne(self):
        selectedItems = self.table.selectedItems()
        description = ''
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "SELECT Description FROM discipline WHERE IDD = %s LIMIT 1"
            value = (unique_identifier,)
            cursor.execute(query, value)  # Исправлено
            row = cursor.fetchone()  # Получение первой строки результата запроса
            if row:
                description = str(row[0])
                print(description)
            cursor.close()

            object = self.kMeansDoing(description)

            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "UPDATE discipline SET Object=%s WHERE IDD=%s"
            value = (object,
                    unique_identifier)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.showDatabase()

    def objectAll(self):
        description = ''
        cursor = self.mydb.cursor()
        query = "SELECT IDD, Description FROM discipline"
        cursor.execute(query)  # Исправлено
        rows = cursor.fetchall()
        cursor.close()

        for row in rows:
            id = row[0]
            description = str(row[1])

            print(description)
            object = self.kMeansDoing(description)

            cursor = self.mydb.cursor()
            query = "UPDATE discipline SET Object=%s WHERE IDD=%s"
            value = (object,
                    id)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
        self.showDatabase()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Discipline()
    widget.show()
    sys.exit(app.exec())
