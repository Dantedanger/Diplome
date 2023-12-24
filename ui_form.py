# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 326)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 471, 51))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 731, 51))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 731, 51))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 731, 51))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 190, 731, 51))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 220, 761, 51))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 130, 731, 51))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 250, 731, 51))
        self.label_8.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_7)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b \u0443\u0447\u0435\u0431\u043d\u043e\u0433\u043e \u043f\u043b\u0430\u043d\u0430", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438 \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0443\u0436\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0432 \u043c\u0435\u043d\u044e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b, \u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b \u0443\u0447\u0435\u0431\u043d\u043e\u0433\u043e \u043f\u043b\u0430\u043d\u0430 \u0438 \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043c\u043e\u0436\u043d\u043e \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043d\u0443\u044e \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d \u0438 \u0441\u0432\u044f\u0437\u044c \u043c\u0435\u0436\u0434\u0443 \u043d\u0438\u043c\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e \u043a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438, \u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438 \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442 \u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043a\u0430\u0436\u0434\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u043c\u043e\u0436\u043d\u043e \u0443\u0434\u0430\u043b\u044f\u0442\u044c, \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c \u0438 \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0438 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043a\u043d\u043e\u043f\u043e\u043a \u0438\u043b\u0438 \u043f\u0440\u044f\u043c\u043e \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e\u0431\u044b \u0443\u0437\u043d\u0430\u0442\u044c \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u0440\u043e\u043a\u0443 \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c\"", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0430\u0441\u0438\u0431\u043e \u0437\u0430 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u043e\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0446\u0438\u0438", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u044b", None))
    # retranslateUi

