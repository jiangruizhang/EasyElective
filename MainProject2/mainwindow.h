#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QListWidget>
#include "course.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    void displayBasicInfo(const Course &course);
private slots:
    void addCourseWindow();
    void removeCourseWindow();
    void unselectedToSeleted(QListWidgetItem *item);
    void selectedToUnselected(QListWidgetItem *item);
};
#endif // MAINWINDOW_H
