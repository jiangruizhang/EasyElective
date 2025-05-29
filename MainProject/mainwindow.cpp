#include "mainwindow.h"
#include "modifycourses.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
    , allCourses(0)
{
    ui->setupUi(this);
    connect(ui->modifyCoursesButton, &QPushButton :: clicked, this, [=]() {
        ModifyCourses *modifyCoursesDialog = new ModifyCourses(this);
        connect(modifyCoursesDialog, &ModifyCourses :: courseInformation, this, [&](const Course &item) {
            // allCourses.emplace_back(item);
            // ui->allCourses->addItem(QString::fromUtf8(item.getCourseName().c_str()));
            addCourse(item);
            flush();
        });
        modifyCoursesDialog -> exec();
    });
}

void MainWindow :: flush() {
    ui->allCourses->clear();
    for (Course item : allCourses) {
        ui->allCourses->addItem(QString::fromUtf8(item.getCourseName().c_str()));
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}
