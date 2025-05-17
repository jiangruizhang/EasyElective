#include "modifyLessons.h"
#include <QPushButton>
#include <QVBoxLayout>

ModifyDialog::ModifyDialog(QWidget *parent)
    : QDialog(parent)
{
    this->setWindowTitle("子窗口");

    QPushButton *btn = new QPushButton("完成");
    connect(btn, &QPushButton::clicked, this, &QDialog::accept); // 关闭对话框

    QVBoxLayout *layout = new QVBoxLayout(this);
    layout->addWidget(btn);
}
