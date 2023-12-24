# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'discipline.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_discipline(object):
    def setupUi(self, discipline):
        if not discipline.objectName():
            discipline.setObjectName(u"discipline")
        discipline.resize(800, 363)
        self.action = QAction(discipline)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(discipline)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(discipline)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(discipline)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(discipline)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(discipline)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(discipline)
        self.action_7.setObjectName(u"action_7")
        self.centralwidget = QWidget(discipline)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 780, 351))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 621, 271))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(660, 180, 80, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(660, 220, 80, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 221, 41))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.statusbar = QStatusBar(discipline)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 22))

        self.retranslateUi(discipline)

        QMetaObject.connectSlotsByName(discipline)
    # setupUi

    def retranslateUi(self, discipline):
        discipline.setWindowTitle(QCoreApplication.translate("discipline", u"Form", None))
        self.action.setText(QCoreApplication.translate("discipline", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b", None))
        self.action_2.setText(QCoreApplication.translate("discipline", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b \u0443\u0447\u0435\u0431\u043d\u043e\u0433\u043e \u043f\u043b\u0430\u043d\u0430", None))
        self.action_3.setText(QCoreApplication.translate("discipline", u"\u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438", None))
        self.action_4.setText(QCoreApplication.translate("discipline", u"\u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438 \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b", None))
        self.action_5.setText(QCoreApplication.translate("discipline", u"\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442", None))
        self.action_6.setText(QCoreApplication.translate("discipline", u"\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.action_7.setText(QCoreApplication.translate("discipline", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("discipline", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("discipline", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("discipline", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b", None))
    # retranslateUi

