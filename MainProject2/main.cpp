#include "mainwindow.h"
#include "course.h"

#include <QApplication>
#include <QVariant>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    qRegisterMetaType<Course>("Course");
    // qRegisterMetaTypeStreamOperators<Course>("Course");
    MainWindow w;
    w.show();
    return a.exec();
}
