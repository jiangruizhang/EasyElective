#include "modifyLessons.h"
#include <QPushButton>
#include <QVBoxLayout>
#include "mainwindow.h"

ModifyDialog::ModifyDialog(QWidget *parent)
    : QDialog(parent)
{
    this->setWindowTitle("子窗口");

    QPushButton *btn = new QPushButton("完成");
    connect(btn, &QPushButton::clicked, this, &ModifyDialog :: onConfirmClicked); // 关闭对话框

    QVBoxLayout *layout = new QVBoxLayout(this);
    layout->addWidget(btn);
}

void ModifyDialog :: onConfirmClicked() {
    MainWindow *parent = qobject_cast<MainWindow *>(this->parent());
    if (parent) {
        parent->test_addLessons(); // 调用父窗口的函数
    }
    accept();
}
