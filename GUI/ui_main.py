# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 595)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 20, 741, 521))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.comboBox_user = QComboBox(self.page)
        self.comboBox_user.setObjectName(u"comboBox_user")
        self.comboBox_user.setGeometry(QRect(110, 100, 531, 22))
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 70, 261, 16))
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 30, 501, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.pushButton_call_start = QPushButton(self.page)
        self.pushButton_call_start.setObjectName(u"pushButton_call_start")
        self.pushButton_call_start.setGeometry(QRect(280, 140, 181, 24))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 181, 16))
        self.lineEdit_time_start = QLineEdit(self.page_2)
        self.lineEdit_time_start.setObjectName(u"lineEdit_time_start")
        self.lineEdit_time_start.setGeometry(QRect(20, 40, 201, 22))
        self.pushButton_call_end = QPushButton(self.page_2)
        self.pushButton_call_end.setObjectName(u"pushButton_call_end")
        self.pushButton_call_end.setGeometry(QRect(240, 480, 261, 24))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u043e\u0442\u0432\u0435\u0447\u0430\u044e\u0449\u0435\u0433\u043e \u043d\u0430 \u0437\u0432\u043e\u043d\u043e\u043a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438 \u0437\u0432\u043e\u043d\u043a\u043e\u0432 \u0432 \u0426\u0435\u043d\u0442\u0440 \u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.pushButton_call_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442 \u043e \u0437\u0432\u043e\u043d\u043a\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0437\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.pushButton_call_end.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442 \u043e \u0437\u0432\u043e\u043d\u043a\u0435", None))
    # retranslateUi

