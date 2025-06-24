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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1064, 723)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toselect = QListWidget(self.centralwidget)
        self.toselect.setObjectName(u"toselect")
        self.toselect.setGeometry(QRect(20, 40, 241, 191))
        self.selected = QListWidget(self.centralwidget)
        self.selected.setObjectName(u"selected")
        self.selected.setGeometry(QRect(20, 260, 241, 192))
        self.toselectLabel = QLabel(self.centralwidget)
        self.toselectLabel.setObjectName(u"toselectLabel")
        self.toselectLabel.setGeometry(QRect(20, 20, 58, 16))
        self.selectedLabel = QLabel(self.centralwidget)
        self.selectedLabel.setObjectName(u"selectedLabel")
        self.selectedLabel.setGeometry(QRect(20, 240, 58, 16))
        self.courseInfoLable = QLabel(self.centralwidget)
        self.courseInfoLable.setObjectName(u"courseInfoLable")
        self.courseInfoLable.setGeometry(QRect(20, 460, 58, 16))
        self.courseInfo = QTextEdit(self.centralwidget)
        self.courseInfo.setObjectName(u"courseInfo")
        self.courseInfo.setGeometry(QRect(20, 480, 241, 141))
        self.courseInfo.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.courseInfo.setReadOnly(True)
        self.addCourse = QPushButton(self.centralwidget)
        self.addCourse.setObjectName(u"addCourse")
        self.addCourse.setGeometry(QRect(20, 630, 100, 32))
        self.schedule = QTableWidget(self.centralwidget)
        if (self.schedule.columnCount() < 7):
            self.schedule.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.schedule.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.schedule.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.schedule.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.schedule.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.schedule.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.schedule.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.schedule.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.schedule.rowCount() < 12):
            self.schedule.setRowCount(12)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.schedule.setVerticalHeaderItem(11, __qtablewidgetitem18)
        self.schedule.setObjectName(u"schedule")
        self.schedule.setGeometry(QRect(280, 40, 701, 581))
        self.schedule.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.schedule.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.schedule.horizontalHeader().setMinimumSectionSize(19)
        self.schedule.horizontalHeader().setDefaultSectionSize(80)
        self.schedule.verticalHeader().setDefaultSectionSize(46)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1064, 37))
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
        self.addCourse.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u8bfe\u7a0b", None))
        ___qtablewidgetitem = self.schedule.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00", None));
        ___qtablewidgetitem1 = self.schedule.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e8c", None));
        ___qtablewidgetitem2 = self.schedule.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e09", None));
        ___qtablewidgetitem3 = self.schedule.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u56db", None));
        ___qtablewidgetitem4 = self.schedule.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e94", None));
        ___qtablewidgetitem5 = self.schedule.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u516d", None));
        ___qtablewidgetitem6 = self.schedule.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f\u5929", None));
        ___qtablewidgetitem7 = self.schedule.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u82828:00-8:50", None));
        ___qtablewidgetitem8 = self.schedule.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u82829:00-9:50", None));
        ___qtablewidgetitem9 = self.schedule.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u828210:10-11:00", None));
        ___qtablewidgetitem10 = self.schedule.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u828211:10-12:00", None));
        ___qtablewidgetitem11 = self.schedule.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e94\u828213:00-13:50", None));
        ___qtablewidgetitem12 = self.schedule.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u516d\u828214:00-14:50", None));
        ___qtablewidgetitem13 = self.schedule.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e03\u828215:10-16:00", None));
        ___qtablewidgetitem14 = self.schedule.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u516b\u828216:10-17:00", None));
        ___qtablewidgetitem15 = self.schedule.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e5d\u828217:10-18:00", None));
        ___qtablewidgetitem16 = self.schedule.verticalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u5341\u828218:40-19:30", None));
        ___qtablewidgetitem17 = self.schedule.verticalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u5341\u4e00\u828219:40-20:30", None));
        ___qtablewidgetitem18 = self.schedule.verticalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u5341\u4e8c\u828220:40-21:30", None));
    # retranslateUi

