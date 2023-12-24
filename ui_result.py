# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result.ui'
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

class Ui_result(object):
    def setupUi(self, result):
        if not result.objectName():
            result.setObjectName(u"result")
        result.resize(1275, 363)
        self.centralwidget = QWidget(result)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 1281, 351))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 1131, 271))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 10, 541, 41))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1170, 240, 80, 24))
        self.statusbar = QStatusBar(result)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 22))
        self.pushButton_2 = QPushButton(result)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1170, 210, 80, 24))
        self.pushButton = QPushButton(result)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1170, 150, 80, 24))
        self.pushButton_3 = QPushButton(result)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1170, 180, 80, 24))

        self.retranslateUi(result)

        QMetaObject.connectSlotsByName(result)
    # setupUi

    def retranslateUi(self, result):
        result.setWindowTitle(QCoreApplication.translate("result", u"Form", None))
        self.label.setText(QCoreApplication.translate("result", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0441\u0432\u044f\u0437\u0438 \u0434\u0432\u0443\u0445 \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d", None))
        self.pushButton_4.setText(QCoreApplication.translate("result", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("result", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("result", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("result", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

