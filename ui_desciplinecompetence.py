# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desciplinecompetence.ui'
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

class Ui_desciplinecompetence(object):
    def setupUi(self, desciplinecompetence):
        if not desciplinecompetence.objectName():
            desciplinecompetence.setObjectName(u"desciplinecompetence")
        desciplinecompetence.resize(800, 363)
        self.centralwidget = QWidget(desciplinecompetence)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 780, 351))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 621, 271))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(660, 160, 80, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(660, 220, 80, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 10, 431, 41))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(660, 190, 80, 24))
        self.statusbar = QStatusBar(desciplinecompetence)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 22))

        self.retranslateUi(desciplinecompetence)

        QMetaObject.connectSlotsByName(desciplinecompetence)
    # setupUi

    def retranslateUi(self, desciplinecompetence):
        desciplinecompetence.setWindowTitle(QCoreApplication.translate("desciplinecompetence", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("desciplinecompetence", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("desciplinecompetence", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("desciplinecompetence", u"\u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438 \u0438 \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b", None))
        self.pushButton_3.setText(QCoreApplication.translate("desciplinecompetence", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

