#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "addItemDialog.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->addItemButton, &QPushButton :: clicked, this, [=](){
        AddItemDialog dialog(this);
        dialog.exec();
    });
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow :: addItem(int number) {
    ui->mylist->addItem(QString :: number(number));
}
