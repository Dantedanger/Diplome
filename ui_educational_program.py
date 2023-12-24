# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'educational_program.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_educational_program(object):
    def setupUi(self, educational_program):
        if not educational_program.objectName():
            educational_program.setObjectName(u"educational_program")
        educational_program.resize(1067, 363)
        self.centralwidget = QWidget(educational_program)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 1061, 351))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 931, 271))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 10, 431, 41))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.statusbar = QStatusBar(educational_program)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 22))
        self.pushButton_2 = QPushButton(educational_program)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(960, 200, 80, 24))
        self.pushButton = QPushButton(educational_program)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(960, 140, 80, 24))
        self.pushButton_3 = QPushButton(educational_program)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(960, 170, 80, 24))

        self.retranslateUi(educational_program)

        QMetaObject.connectSlotsByName(educational_program)
    # setupUi

    def retranslateUi(self, educational_program):
        educational_program.setWindowTitle(QCoreApplication.translate("educational_program", u"Form", None))
        self.label.setText(QCoreApplication.translate("educational_program", u"\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("educational_program", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("educational_program", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("educational_program", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

