#include "addcourses.h"
#include "ui_addcourses.h"


void addCourses :: fortest() {
    QList<QTableWidgetItem*> selectedItems = ui->courseSchedule->selectedItems();
    qDebug() << selectedItems.count();
    for (QTableWidgetItem *item : selectedItems) {
        int row = item->row();
        int col = item->column();
        qDebug() << "选中单元格：" << row + 1 << "   " << col + 1;
    }
}


addCourses::addCourses(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui :: addCourses)
{
    ui->setupUi(this);
    connect(ui->confirmButton, &QPushButton :: clicked, this, &addCourses :: transCourseInfo);
    connect(ui->cancel, &QPushButton :: clicked, this, &addCourses :: accept);
    connect(ui->test, &QPushButton :: clicked, this, &addCourses :: fortest);
    ui->courseSchedule->setSelectionMode(QAbstractItemView :: MultiSelection);
    for (int row = 0; row < ui->courseSchedule->rowCount(); ++row) {
        for (int col = 0; col < ui->courseSchedule->columnCount(); ++col) {
            if (!ui->courseSchedule->item(row, col)) {
                ui->courseSchedule->setItem(row, col, new QTableWidgetItem(""));
            }
            QTableWidgetItem *item = ui->courseSchedule->item(row, col);
            item->setFlags(item->flags() & ~Qt::ItemIsEditable); // 禁止编辑
        }
    }
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
    course.setQuota(ui->limit->text().toInt());
    course.setHaveChosen(ui->nowSelected->text().toInt());
    QList<QTableWidgetItem*> selectedItems = ui->courseSchedule->selectedItems();
    for (QTableWidgetItem *item : selectedItems) {
        int row = item->row();
        int col = item->column();
        course.addClasstime(col + 1, row + 1);
        qDebug() << "选中单元格：" << row << col;
    }

    emit receiveInfo(course);
    accept();
}
