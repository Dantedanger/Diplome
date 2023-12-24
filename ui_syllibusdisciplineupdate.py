# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'syllibusdisciplineupdate.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 250, 80, 24))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 250, 80, 24))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 40, 351, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 190, 161, 24))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 90, 161, 24))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 140, 131, 21))
        self.label_2.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 90, 131, 21))
        self.label.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 190, 131, 21))
        self.label_4.setFont(font)
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(200, 140, 161, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b \u0432 \u0443\u0447\u0435\u0431\u043d\u043e\u043c \u043f\u043b\u0430\u043d\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0430:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0423\u0447\u0435\u0431\u043d\u044b\u0439 \u043f\u043b\u0430\u043d:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440:", None))
    # retranslateUi

