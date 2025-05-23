#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    /*
    w.addItem(123);
    w.addItem(145);
    */
    return a.exec();
}
