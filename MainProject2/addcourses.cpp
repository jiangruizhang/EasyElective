#include "addcourses.h"
#include "ui_addcourses.h"

addCourses::addCourses(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::addCourses)
{
    ui->setupUi(this);
    connect(ui->confirmButton, &QPushButton :: clicked, this, &addCourses :: transCourseInfo);
}

addCourses::~addCourses()
{
    delete ui;
}

string toString(QString str) { return str.toUtf8().constData();}

void addCourses :: transCourseInfo() {
    Course course;
    course.setCourseName(toString(ui->courseName->text()));
    course.setTeacherName(toString(ui->teacherName->text()));
    course.setPoints(ui->coursePoint->text().toInt());
    course.setIntension(ui->intension->text().toInt());
    course.setIfMust(ui->ifMust->isChecked());
    emit receiveInfo(course);
    accept();
}
