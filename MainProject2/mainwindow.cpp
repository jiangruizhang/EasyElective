#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "addcourses.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->courseInfo->clear();
    connect(ui->addCourses, &QPushButton :: clicked, this, &MainWindow :: addCourseWindow);
    connect(ui->unselectedCourses, &QListWidget::itemClicked, [](QListWidgetItem *item){
        qDebug() << "点击了：" << item->text();
    });
    connect(ui->unselectedCourses, &QListWidget::itemClicked, this, [=](QListWidgetItem *item){
        Course c = item->data(Qt::UserRole).value<Course>();
        QString info = QString("课程名称: %1\n学分: %2\n任课教师: %3")
                           .arg(c.getCourseName()).arg(c.getPoints()).arg(c.getTeacherName());
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
