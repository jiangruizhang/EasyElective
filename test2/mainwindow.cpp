#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "modifyLessons.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->openDialogButton, &QPushButton::clicked, this, [=]() {
        ModifyDialog dialog(this);  // 创建子窗口
        dialog.exec();              // 模态方式显示（会阻塞，直到关闭）
    });
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow :: test_addLessons() {
    // ui->allLessons->addItem("1");
    for (int i = 0; i < 100; ++i)
        ui->allLessons->addItem(QString::number(i));
}
