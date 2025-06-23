# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1061, 683)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toselect = QListWidget(self.centralwidget)
        self.toselect.setObjectName(u"toselect")
        self.toselect.setGeometry(QRect(20, 20, 241, 191))
        self.selected = QListWidget(self.centralwidget)
        self.selected.setObjectName(u"selected")
        self.selected.setGeometry(QRect(20, 240, 241, 192))
        self.toselectLabel = QLabel(self.centralwidget)
        self.toselectLabel.setObjectName(u"toselectLabel")
        self.toselectLabel.setGeometry(QRect(20, 0, 58, 16))
        self.selectedLabel = QLabel(self.centralwidget)
        self.selectedLabel.setObjectName(u"selectedLabel")
        self.selectedLabel.setGeometry(QRect(20, 220, 58, 16))
        self.courseInfoLable = QLabel(self.centralwidget)
        self.courseInfoLable.setObjectName(u"courseInfoLable")
        self.courseInfoLable.setGeometry(QRect(20, 440, 58, 16))
        self.courseInfo = QTextEdit(self.centralwidget)
        self.courseInfo.setObjectName(u"courseInfo")
        self.courseInfo.setGeometry(QRect(20, 460, 241, 141))
        self.courseInfo.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.courseInfo.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1061, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toselectLabel.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u9009\u8bfe\u7a0b", None))
        self.selectedLabel.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u9009\u8bfe\u7a0b", None))
        self.courseInfoLable.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u4fe1\u606f", None))
    # retranslateUi

