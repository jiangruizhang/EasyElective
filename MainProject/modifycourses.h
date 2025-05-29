#ifndef MODIFYCOURSES_H
#define MODIFYCOURSES_H

#include <QDialog>
#include "course.h"

namespace Ui {
class ModifyCourses;
}

class ModifyCourses : public QDialog
{
    Q_OBJECT

public:
    explicit ModifyCourses(QWidget *parent = nullptr);
    ~ModifyCourses();
signals:
    void courseInformation(const Course &course);
private slots:
    void confirmButtonClicked();

private:
    Ui::ModifyCourses *ui;
};

#endif // MODIFYCOURSES_H
