#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.setWindowTitle("EasyElective");
    w.test_addLessons();
    w.show();
    return a.exec();
}
