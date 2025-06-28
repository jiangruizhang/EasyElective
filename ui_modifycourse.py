# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifycourse.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDialog,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_ModifyCourse(object):
    def setupUi(self, ModifyCourse):
        if not ModifyCourse.objectName():
            ModifyCourse.setObjectName(u"ModifyCourse")
        ModifyCourse.resize(1160, 370)
        self.toselect = QListWidget(ModifyCourse)
        self.toselect.setObjectName(u"toselect")
        self.toselect.setGeometry(QRect(30, 20, 211, 331))
        self.must = QCheckBox(ModifyCourse)
        self.must.setObjectName(u"must")
        self.must.setGeometry(QRect(330, 148, 85, 20))
        self.label_2 = QLabel(ModifyCourse)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 70, 58, 16))
        self.label_4 = QLabel(ModifyCourse)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 190, 58, 16))
        self.intension = QTextEdit(ModifyCourse)
        self.intension.setObjectName(u"intension")
        self.intension.setGeometry(QRect(330, 260, 241, 31))
        self.limit = QTextEdit(ModifyCourse)
        self.limit.setObjectName(u"limit")
        self.limit.setGeometry(QRect(330, 180, 241, 31))
        self.label = QLabel(ModifyCourse)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 30, 58, 16))
        self.course = QTextEdit(ModifyCourse)
        self.course.setObjectName(u"course")
        self.course.setGeometry(QRect(330, 20, 241, 31))
        self.teacher = QTextEdit(ModifyCourse)
        self.teacher.setObjectName(u"teacher")
        self.teacher.setGeometry(QRect(330, 100, 241, 31))
        self.label_6 = QLabel(ModifyCourse)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 150, 58, 16))
        self.chosen = QTextEdit(ModifyCourse)
        self.chosen.setObjectName(u"chosen")
        self.chosen.setGeometry(QRect(330, 220, 241, 31))
        self.label_5 = QLabel(ModifyCourse)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 230, 58, 16))
        self.label_7 = QLabel(ModifyCourse)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 270, 58, 16))
        self.point = QTextEdit(ModifyCourse)
        self.point.setObjectName(u"point")
        self.point.setGeometry(QRect(330, 60, 241, 31))
        self.label_3 = QLabel(ModifyCourse)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 110, 58, 16))
        self.schedule = QTableWidget(ModifyCourse)
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
        self.schedule.setGeometry(QRect(590, 20, 561, 331))
        self.schedule.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.schedule.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.schedule.horizontalHeader().setMinimumSectionSize(19)
        self.schedule.horizontalHeader().setDefaultSectionSize(60)
        self.schedule.verticalHeader().setDefaultSectionSize(25)
        self.confirm = QPushButton(ModifyCourse)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(260, 310, 100, 32))
        self.remove = QPushButton(ModifyCourse)
        self.remove.setObjectName(u"remove")
        self.remove.setGeometry(QRect(370, 310, 100, 32))
        self.close = QPushButton(ModifyCourse)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(480, 310, 100, 32))

        self.retranslateUi(ModifyCourse)

        QMetaObject.connectSlotsByName(ModifyCourse)
    # setupUi

    def retranslateUi(self, ModifyCourse):
        ModifyCourse.setWindowTitle(QCoreApplication.translate("ModifyCourse", u"\u4fee\u6539\u8bfe\u7a0b", None))
        self.must.setText(QCoreApplication.translate("ModifyCourse", u"\u5fc5\u9009\u8bfe\u7a0b", None))
        self.label_2.setText(QCoreApplication.translate("ModifyCourse", u"\u8bfe\u7a0b\u5b66\u5206", None))
        self.label_4.setText(QCoreApplication.translate("ModifyCourse", u"\u9650\u9009\u4eba\u6570", None))
        self.label.setText(QCoreApplication.translate("ModifyCourse", u"\u8bfe\u7a0b\u540d\u79f0", None))
        self.label_6.setText(QCoreApplication.translate("ModifyCourse", u"\u5fc5\u4fee\u8bfe", None))
        self.label_5.setText(QCoreApplication.translate("ModifyCourse", u"\u5df2\u9009\u4eba\u6570", None))
        self.label_7.setText(QCoreApplication.translate("ModifyCourse", u"\u610f\u613f\u503c", None))
        self.label_3.setText(QCoreApplication.translate("ModifyCourse", u"\u6559\u5e08\u59d3\u540d", None))
        ___qtablewidgetitem = self.schedule.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ModifyCourse", u"\u661f\u671f\u4e00", None));
        ___qtablewidgetitem1 = self.schedule.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ModifyCourse", u"\u661f\u671f\u4e8c", None));
        ___qtablewidgetitem2 = self.schedule.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ModifyCourse", u"\u661f\u671f\u4e09", None));
        ___qtablewidgetitem3 = self.schedule.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ModifyCourse", u"\u661f\u671f\u56db", None));
        ___qtablewidgetitem4 = self.schedule.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ModifyCourse", u"\u661f\u671f\u4e94", None));
        ___qtablewidgetitem5 = self.schedule.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ModifyCourse", u"\u661f\u671f\u516d", None));
        ___qtablewidgetitem6 = self.schedule.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ModifyCourse", u"\u661f\u671f\u5929", None));
        ___qtablewidgetitem7 = self.schedule.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u4e00\u82828:00-8:50", None));
        ___qtablewidgetitem8 = self.schedule.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u4e8c\u82829:00-9:50", None));
        ___qtablewidgetitem9 = self.schedule.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u4e09\u828210:10-11:00", None));
        ___qtablewidgetitem10 = self.schedule.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u56db\u828211:10-12:00", None));
        ___qtablewidgetitem11 = self.schedule.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u4e94\u828213:00-13:50", None));
        ___qtablewidgetitem12 = self.schedule.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u516d\u828214:00-14:50", None));
        ___qtablewidgetitem13 = self.schedule.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u4e03\u828215:10-16:00", None));
        ___qtablewidgetitem14 = self.schedule.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u516b\u828216:10-17:00", None));
        ___qtablewidgetitem15 = self.schedule.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u4e5d\u828217:10-18:00", None));
        ___qtablewidgetitem16 = self.schedule.verticalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u5341\u828218:40-19:30", None));
        ___qtablewidgetitem17 = self.schedule.verticalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u5341\u4e00\u828219:40-20:30", None));
        ___qtablewidgetitem18 = self.schedule.verticalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("ModifyCourse", u"\u7b2c\u5341\u4e8c\u828220:40-21:30", None));
        self.confirm.setText(QCoreApplication.translate("ModifyCourse", u"\u4fdd\u5b58\u8bfe\u7a0b", None))
        self.remove.setText(QCoreApplication.translate("ModifyCourse", u"\u5220\u9664\u8bfe\u7a0b", None))
        self.close.setText(QCoreApplication.translate("ModifyCourse", u"\u5b8c\u6210", None))
    # retranslateUi

