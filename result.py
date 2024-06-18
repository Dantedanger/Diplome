import sys

from PySide6.QtWidgets import QApplication, QMessageBox, QScrollArea, QVBoxLayout, QWidget, QLineEdit, QComboBox, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

import mysql.connector as mc


import os
sys.stdout.reconfigure(encoding='utf-8')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
#os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
#os.environ['TF_USE_LEGACY_KERAS'] = '1'

import tensorflow as tf
#tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from gensim.models import Word2Vec
import networkx as nx
#import tf.keras as keras

from tensorflow.keras.models import load_model
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.models import Model
import re
from pymorphy2 import MorphAnalyzer
import nltk
from nltk.corpus import stopwords


QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class Precision(tf.keras.metrics.Metric):
    def __init__(self, name='precision',threshold=0.45,**kwargs):
        super(Precision, self).__init__(name=name,**kwargs)
        self.threshold = threshold
        self.tp = self.add_weight(name='true_positives', initializer='zeros')
        self.fp = self.add_weight(name='false_positives', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.cast(y_pred >= self.threshold, tf.float32)
        y_true = tf.cast(y_true, tf.float32)

        true_positives = tf.reduce_sum(y_true * y_pred)
        false_positives = tf.reduce_sum(y_pred) - true_positives

        self.tp.assign_add(true_positives)
        self.fp.assign_add(false_positives)

    def result(self):
        precision = self.tp / (self.tp + self.fp + tf.keras.backend.epsilon())
        return precision

    def reset_state(self):
        self.tp.assign(0)
        self.fp.assign(0)

class Recall(tf.keras.metrics.Metric):
    def __init__(self, name='recall',threshold=0.45,**kwargs):
        super(Recall, self).__init__(name=name,**kwargs)
        self.threshold = threshold
        self.tp = self.add_weight(name='true_positives', initializer='zeros')
        self.fn = self.add_weight(name='false_negatives', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.cast(y_pred >= self.threshold, tf.float32)
        y_true = tf.cast(y_true, tf.float32)

        true_positives = tf.reduce_sum(y_true * y_pred)
        false_negatives = tf.reduce_sum(y_true) - true_positives

        self.tp.assign_add(true_positives)
        self.fn.assign_add(false_negatives)

    def result(self):
        recall = self.tp / (self.tp + self.fn + tf.keras.backend.epsilon())
        return recall

    def reset_state(self):
        self.tp.assign(0)
        self.fn.assign(0)

class ROCAUC(tf.keras.metrics.Metric):
    def __init__(self, name='roc_auc', **kwargs):
        super(ROCAUC, self).__init__(name=name, **kwargs)
        self.auc_metric = tf.keras.metrics.AUC(name='auc')

    def update_state(self, y_true, y_pred, sample_weight=None):
        self.auc_metric.update_state(y_true, y_pred, sample_weight)

    def result(self):
        return self.auc_metric.result()

    def reset_state(self):
        self.auc_metric.reset_state()

class Tp(tf.keras.metrics.Metric):
    def __init__(self, name: str = 'true_positives', num_classes: int = 2, threshold: float = 0.45, **kwargs):
        super(Tp, self).__init__(name=name, **kwargs)
        self.threshold = threshold
        self.num_classes = num_classes
        self.tp = self.add_weight(name='tp', initializer='zeros')

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: tf.Tensor = None):
        y_pred = tf.cast(y_pred >= self.threshold, tf.float32)
        y_true = tf.cast(y_true, tf.float32)
        true_positives = tf.reduce_sum(y_true * y_pred)
        self.tp.assign_add(true_positives)

    def result(self) -> tf.Tensor:
        return self.tp

    def reset_state(self):
        self.tp.assign(0)


class Fp(tf.keras.metrics.Metric):
    def __init__(self, name: str = 'false_positives', num_classes: int = 2, threshold: float = 0.45, **kwargs):
        super(Fp, self).__init__(name=name, **kwargs)
        self.threshold = threshold
        self.num_classes = num_classes
        self.fp = self.add_weight(name='fp', initializer='zeros')

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: tf.Tensor = None):
        y_pred = tf.cast(y_pred >= self.threshold, tf.float32)
        y_true = tf.cast(y_true, tf.float32)
        false_positives = tf.reduce_sum(y_pred * (1 - y_true))
        self.fp.assign_add(false_positives)

    def result(self) -> tf.Tensor:
        return self.fp

    def reset_state(self):
        self.fp.assign(0)


class Fn(tf.keras.metrics.Metric):
    def __init__(self, name: str = 'false_negatives', num_classes: int = 2, threshold: float = 0.45, **kwargs):
        super(Fn, self).__init__(name=name, **kwargs)
        self.threshold = threshold
        self.num_classes = num_classes
        self.fn = self.add_weight(name='fn', initializer='zeros')

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: tf.Tensor = None):
        y_pred = tf.cast(y_pred >= self.threshold, tf.float32)
        y_true = tf.cast(y_true, tf.float32)
        false_negatives = tf.reduce_sum((1 - y_pred) * y_true)
        self.fn.assign_add(false_negatives)

    def result(self) -> tf.Tensor:
        return self.fn

    def reset_state(self):
        self.fn.assign(0)



class Tn(tf.keras.metrics.Metric):
    def __init__(self, name: str = 'true_negatives', num_classes: int = 2, threshold: float = 0.45, **kwargs):
        super(Tn, self).__init__(name=name, **kwargs)
        self.threshold = threshold
        self.num_classes = num_classes
        self.tn = self.add_weight(name='tn', initializer='zeros')

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: tf.Tensor = None):
        y_pred = tf.cast(y_pred >= self.threshold, tf.float32)
        y_true = tf.cast(y_true, tf.float32)

        true_negatives = tf.reduce_sum((1 - y_true) * (1 - y_pred))
        self.tn.assign_add(true_negatives)

    def result(self) -> tf.Tensor:
        return self.tn

    def reset_state(self):
        self.tn.assign(0)

class F1Score(tf.keras.metrics.Metric):
    def __init__(self, name='f1_score', threshold=0.45, **kwargs):
        super(F1Score, self).__init__(name=name, **kwargs)
        self.threshold = threshold
        self.tp = self.add_weight(name='true_positives', initializer='zeros')
        self.fp = self.add_weight(name='false_positives', initializer='zeros')
        self.fn = self.add_weight(name='false_negatives', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.cast(y_pred >= self.threshold, tf.float32)
        y_true = tf.cast(y_true, tf.float32)

        true_positives = tf.reduce_sum(y_true * y_pred)
        false_positives = tf.reduce_sum(y_pred) - true_positives
        false_negatives = tf.reduce_sum(y_true) - true_positives

        self.tp.assign_add(true_positives)
        self.fp.assign_add(false_positives)
        self.fn.assign_add(false_negatives)

    def result(self):
        precision = self.tp / (self.tp + self.fp + tf.keras.backend.epsilon())
        recall = self.tp / (self.tp + self.fn + tf.keras.backend.epsilon())
        f1 = 2 * (precision * recall) / (precision + recall + tf.keras.backend.epsilon())
        return f1

    def reset_state(self):
        self.tp.assign(0)
        self.fp.assign(0)
        self.fn.assign(0)

class GraphWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('График')

        self.layout = QVBoxLayout()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.canvas)
        scroll_area.setWidgetResizable(True)  # Разрешаем масштабирование холста
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # Включаем горизонтальную прокрутку
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # Включаем вертикальную прокрутку

        self.layout.addWidget(scroll_area)

        self.setLayout(self.layout)

    def showGraph(self,names,rel):
        G = nx.Graph()
        G.add_nodes_from(names)
        G.add_edges_from(rel)

        self.figure.clear()

        pos = nx.spring_layout(G, scale=10)
        ax = self.figure.add_subplot(frameon=False)
        ax.margins(0.2)
        nx.draw(G, ax=ax, pos=pos, with_labels=True, node_color='lightblue', node_size=500, font_size=6, font_weight='bold')  # Измените размер шрифта
        self.canvas.draw()

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
        self.ui.comboBox.currentIndexChanged.connect(self.filterData)

        self.ui.pushButton.clicked.connect(self.startInsertDatabase)
        self.ui.pushButton_3.clicked.connect(self.startUpdateDatabase)
        self.ui.pushButton_2.clicked.connect(self.deleteDatabase)
        self.ui.pushButton_4.clicked.connect(self.getResult)
        self.ui.pushButton_5.clicked.connect(self.getAllResult)
        self.ui.pushButton_6.clicked.connect(self.loadAll)
        self.ui.pushButton_7.clicked.connect(self.openGraph)

        self.table = self.ui.tableWidget
        self.table.setColumnCount(13)
        self.table.setColumnHidden(0, True)
        self.table.setColumnHidden(1, True)
        self.table.setColumnHidden(2, True)
        self.table.setColumnHidden(9, True)
        self.table.setColumnHidden(10, True)
        self.table.setColumnHidden(11, True)
        self.table.setColumnHidden(12, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        column_labels = ["","","", "Название дисциплины 1", "Предметная область", "Название дисциплины 2", "Предметная область","Связь","Описание"]
        self.table.setHorizontalHeaderLabels(column_labels)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.model = Model()
        self.model = load_model('best_model_f1.keras',
        custom_objects={'F1Score': F1Score,'ROCAUC': ROCAUC,'Precision': Precision, 'Recall': Recall,
                        'Tp': Tp,'Fp': Fp,'Tn': Tn, 'Fn': Fn})
#        self.model = tf.keras.models.load_model('saved_model/best_model_f1_main_embedding50')
        self.morph = MorphAnalyzer()
        self.model_vec = Word2Vec.load("updated_model")
#        nltk.download('stopwords')

        self.mydb = mydb
        self.filter_combobox()

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
        query = "SELECT syllibusdiscipline.ID, discipline.Name FROM syllibusdiscipline, discipline WHERE syllibusdiscipline.IDD=discipline.IDD AND syllibusdiscipline.IDEdPr=%s"
        cursor.execute(query,(self.idedpr,))
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
        query = "SELECT syllibusdiscipline.ID, discipline.Name FROM syllibusdiscipline, discipline WHERE syllibusdiscipline.IDD=discipline.IDD AND syllibusdiscipline.IDEdPr=%s"
        cursor.execute(query,(self.idedpr,))
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
            query = "UPDATE result SET IDD1=%s, IDD2=%s, Relations=0, DescriptionR='' WHERE IDResult=%s"
            value = (idd1,idd2,unique_identifier)
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
        self.idedpr = self.ui.comboBox.currentData()
        prof = prof_year[:-5]  # Получить все символы до последних 4
        year = prof_year[-4:]  # Получить последние 4 символа
        cursor = self.mydb.cursor()
        query = "SELECT * FROM result_view WHERE Profile = %s AND Year= %s"
        cursor.execute(query, (prof, year))
        filtered_data = cursor.fetchall()

        self.table.setRowCount(len(filtered_data))
        self.table.setColumnCount(len(filtered_data[0]))

        for i, row in enumerate(filtered_data):
            for j, cell in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(cell)))
        cursor.close()

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

    def semanticRelations(self, desc1, desc2):
        max_text_len = 300

        new_new_main_text = self.lemmatize(desc1)
        new_new_related_text = self.lemmatize(desc2)

        two_texts = [new_new_main_text + new_new_related_text]

        # Добавление новых текстов к существующей модели
        self.model_vec.build_vocab(two_texts, update=True)

        # Переобучение модели на расширенном корпусе данных
        self.model_vec.train(two_texts, total_examples=self.model_vec.corpus_count, epochs=self.model_vec.epochs)

        new_main_sequence = [self.model_vec.wv[token][0] for token in new_new_main_text]
        new_padded_main_sequence = pad_sequences([new_main_sequence], maxlen=max_text_len, dtype='float32')

        new_related_sequence = [self.model_vec.wv[token][0] for token in new_new_related_text]
        new_padded_related_sequence = pad_sequences([new_related_sequence], maxlen=max_text_len, dtype='float32')

        new_X = [new_padded_main_sequence, new_padded_related_sequence]
        prediction = self.model.predict(new_X)

        predicted_label = "1" if prediction[0][0] >= 0.45 else "0"
        return predicted_label, prediction[0][0]
#        print("", desc1, desc2, predicted_label, prediction[0][0])


    def getResult(self):
        selectedItems = self.table.selectedItems()
        if selectedItems:
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "SELECT Desc1, Desc2 FROM result_view WHERE IDResult = %s LIMIT 1"
            value = (unique_identifier,)
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row:
                description1 = str(row[0])
                description2 = str(row[1])
            cursor.close()

            predicted_label, prediction = self.semanticRelations(description1, description2)
            selectedRow = selectedItems[0].row()
            cursor = self.mydb.cursor()
            unique_identifier = int(self.table.item(selectedRow, 0).text())
            query = "UPDATE result SET Relations=%s, DescriptionR=%s WHERE IDResult=%s"
            value = (int(predicted_label), str(prediction), unique_identifier)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
            self.ui_add.close()
            self.filterData()

    def getAllResult(self):       
        desc1, desc2 = '', ''

        prof_year = self.ui.comboBox.currentText()
        prof = prof_year[:-5]  # Получить все символы до последних 4
        year = prof_year[-4:]  # Получить последние 4 символа

        cursor = self.mydb.cursor()
        query = "SELECT IDResult, Desc1, Desc2 FROM result_view WHERE Profile = %s AND Year= %s"
        cursor.execute(query, (prof, year))  # Исправлено
        rows = cursor.fetchall()
        cursor.close()

        for row in rows:
            id = row[0]
            desc1 = str(row[1])
            desc2 = str(row[2])

            predicted_label, prediction = self.semanticRelations(desc1, desc2)
            cursor = self.mydb.cursor()
            query = "UPDATE result SET Relations=%s, DescriptionR=%s WHERE IDResult=%s"
            value = (int(predicted_label), str(prediction), id)
            cursor.execute(query, value)
            self.mydb.commit()
            cursor.close()
        self.filterData()

    def loadAll(self):
        prof_year = self.ui.comboBox.currentText()
        prof = prof_year[:-5]  # Получить все символы до последних 4
        year = prof_year[-4:]  # Получить последние 4 символа

        cursor = self.mydb.cursor()
        query = "SELECT ID FROM syllibusdiscipline_view WHERE Profile = %s AND Year= %s"
        cursor.execute(query, (prof, year))
        rows = cursor.fetchall()
        cursor.close()

        cursor = self.mydb.cursor()
        for i in range(len(rows)):
            idd1 = rows[i][0]
            for j in range(i+1,len(rows)):
                if i!=j:
                    idd2 = rows[j][0]
                    query = "INSERT INTO result (IDD1, IDD2) VALUES (%s, %s)"
                    value = (idd1, idd2)
                    try:
                        cursor.execute(query, value)
                    except mc.Error as err:
                        if err.errno == 1062:  # Ошибка нарушения уникального ключа
                            pass  # Пропускаем эту ошибку
                        else:
                            print("Ошибка MySQL:", err.msg)
                    self.mydb.commit()
        cursor.close()
        self.filterData()

    def openGraph(self):
        names = []
        rel = []

        prof_year = self.ui.comboBox.currentText()
        prof = prof_year[:-5]
        year = prof_year[-4:]

        cursor = self.mydb.cursor()
        query = "SELECT Name1, Name2, Relations FROM result_view WHERE Profile = %s AND Year= %s"
        cursor.execute(query, (prof, year))
        rows = cursor.fetchall()
        cursor.close()

        for row in rows:
            name1 = row[0]
            name2 = row[1]
            if name1 not in names:
                names.append(name1)
            if name2 not in names:
                names.append(name2)
            if row[2] == 1:
                rel.append((name1, name2))

        self.graphWindow = GraphWindow()
        self.graphWindow.showGraph(names, rel)
        self.graphWindow.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Result()
    widget.show()
    sys.exit(app.exec())
