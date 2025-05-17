/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.9.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListView>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QListView *selectedLessons;
    QTableView *calendar;
    QLabel *allLessonsLabel;
    QLabel *selectedLessonsLabel;
    QLabel *calendarLabel;
    QListWidget *allLessons;
    QPushButton *openDialogButton;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(800, 600);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        selectedLessons = new QListView(centralwidget);
        selectedLessons->setObjectName("selectedLessons");
        selectedLessons->setGeometry(QRect(50, 311, 151, 211));
        calendar = new QTableView(centralwidget);
        calendar->setObjectName("calendar");
        calendar->setGeometry(QRect(220, 40, 531, 481));
        allLessonsLabel = new QLabel(centralwidget);
        allLessonsLabel->setObjectName("allLessonsLabel");
        allLessonsLabel->setGeometry(QRect(50, 20, 151, 16));
        selectedLessonsLabel = new QLabel(centralwidget);
        selectedLessonsLabel->setObjectName("selectedLessonsLabel");
        selectedLessonsLabel->setGeometry(QRect(50, 290, 151, 16));
        calendarLabel = new QLabel(centralwidget);
        calendarLabel->setObjectName("calendarLabel");
        calendarLabel->setGeometry(QRect(220, 20, 151, 16));
        allLessons = new QListWidget(centralwidget);
        allLessons->setObjectName("allLessons");
        allLessons->setGeometry(QRect(50, 40, 151, 241));
        openDialogButton = new QPushButton(centralwidget);
        openDialogButton->setObjectName("openDialogButton");
        openDialogButton->setGeometry(QRect(380, 0, 101, 32));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 800, 24));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        allLessonsLabel->setText(QCoreApplication::translate("MainWindow", "All lessons", nullptr));
        selectedLessonsLabel->setText(QCoreApplication::translate("MainWindow", "Selected lessons", nullptr));
        calendarLabel->setText(QCoreApplication::translate("MainWindow", "Calendar", nullptr));
        openDialogButton->setText(QCoreApplication::translate("MainWindow", "PushButton", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
