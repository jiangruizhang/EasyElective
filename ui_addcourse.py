# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addcourse.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_AddCourse(object):
    def setupUi(self, AddCourse):
        if not AddCourse.objectName():
            AddCourse.setObjectName(u"AddCourse")
        AddCourse.resize(740, 410)
        self.finish = QPushButton(AddCourse)
        self.finish.setObjectName(u"finish")
        self.finish.setGeometry(QRect(330, 320, 100, 32))

        self.retranslateUi(AddCourse)

        QMetaObject.connectSlotsByName(AddCourse)
    # setupUi

    def retranslateUi(self, AddCourse):
        AddCourse.setWindowTitle(QCoreApplication.translate("AddCourse", u"Dialog", None))
        self.finish.setText(QCoreApplication.translate("AddCourse", u"\u6dfb\u52a0\u8bfe\u7a0b", None))
    # retranslateUi

