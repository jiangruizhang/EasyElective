#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "addcourses.h"
#include "removecourse.h"

const string __daytime[7] = {"一", "二", "三", "四", "五", "六", "日"};

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->courseInfo->clear();
    connect(ui->addCourses, &QPushButton :: clicked, this, &MainWindow :: addCourseWindow);
    connect(ui->removeCourse, &QPushButton :: clicked, this, &MainWindow :: removeCourseWindow);
    // connect(ui->unselectedCourses, &QListWidget::itemClicked, [](QListWidgetItem *item){
    //     qDebug() << "点击了：" << item->text();
    // });
    connect(ui->unselectedCourses, &QListWidget::itemClicked, this, [=](QListWidgetItem *item){
        Course c = item->data(Qt::UserRole).value<Course>();/*
        QString info = QString("课程名称: %1\n学分: %2\n任课教师: %3\n是否必修: %4\n限选: %5\n已选: %6\n")
                           .arg(c.getCourseName()).arg(c.getPoints()).arg(c.getTeacherName()).arg(c.getIfMust() ? "是" : "否").arg(c.getQuota()).arg(c.getHaveChosen());*/
        QString info;
        info += QString("课程名称: %1\n").arg(c.getCourseName());
        info += QString("学分: %1\n").arg(c.getPoints());
        info += QString("任课教师: %1\n").arg(c.getTeacherName());
        info += QString("是否必修: %1\n").arg(c.getIfMust() ? "是" : "否");
        info += QString("限选: %1\n").arg(c.getQuota());
        info += QString("已选: %1\n").arg(c.getHaveChosen());
        info += QString("上课时间:\n");
        for (classtime lesson : c.getClasstime()) {
            info += QString("星期%1 第 %2 节\n").arg(__daytime[lesson.getday() - 1]).arg(lesson.getti());
        }
        ui->courseInfo->setText(info);  // 假设你有一个 QLabel
    });
}

MainWindow::~MainWindow()
{
    delete ui;
}

QString toQString(string str) { return QString::fromUtf8(str.c_str());}

void MainWindow::addCourseWindow() {
    addCourses *addDialog = new addCourses(this);
    connect(addDialog, &addCourses :: receiveInfo, this, [&](const Course &course) {
        QListWidgetItem *item = new QListWidgetItem(toQString(course.getCourseName() + "; " + course.getTeacherName() + "; " + to_string(course.getPoints()) + " 学分"));
        item->setData(Qt :: UserRole, QVariant::fromValue(course));
        ui->unselectedCourses->addItem(item);
    });
    addDialog->exec();
}

void MainWindow::removeCourseWindow() {
    QStringList items;
    for (int i = 0; i < ui->unselectedCourses->count(); ++i) {
        items << ui->unselectedCourses->item(i)->text();
    }
    RemoveCourse *removeDialog = new RemoveCourse(items, this);
    connect(removeDialog, &RemoveCourse :: itemsToRemove, this, [&](const QStringList &itemsToRemove) {
        for (int i = ui->unselectedCourses->count() - 1; i >=0; --i) {
            QListWidgetItem *item = ui->unselectedCourses->item(i);
            if (itemsToRemove.contains(item->text())) {
                delete ui->unselectedCourses->takeItem(i);
            }
        }
    });
    removeDialog->exec();
}
