#include "MainWindow.h"
#include "InputDialog.h"
// #include "ui_mainwindow.h"
#include <QListWidget>
#include <QPushButton>
#include <QVBoxLayout>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    QWidget *central = new QWidget(this);
    QVBoxLayout *layout = new QVBoxLayout(central);

    QListWidget *mylist = new QListWidget(this); // 如果你已经在.ui文件里设置了，可以忽略
    QPushButton *button = new QPushButton("添加项目", this);

    layout->addWidget(mylist);
    layout->addWidget(button);

    setCentralWidget(central);

    connect(button, &QPushButton::clicked, this, [=]() {
        InputDialog *dialog = new InputDialog(this);
        connect(dialog, &InputDialog::stringEntered, this, [=](const QString &text){
            mylist->addItem(text);
        });
        dialog->exec(); // 以模态方式显示对话框
    });
}

MainWindow::~MainWindow()
{
    // delete ui;
}
