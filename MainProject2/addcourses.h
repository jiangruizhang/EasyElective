#ifndef ADDCOURSES_H
#define ADDCOURSES_H

#include <QDialog>
#include "course.h"

namespace Ui {
class addCourses;
}

class addCourses : public QDialog
{
    Q_OBJECT

public:
    explicit addCourses(QWidget *parent = nullptr);
    ~addCourses();
signals:
    void receiveInfo(const Course &course);

private:
    Ui::addCourses *ui;
private slots:
    void transCourseInfo();
    void fortest();
};

#endif // ADDCOURSES_H
