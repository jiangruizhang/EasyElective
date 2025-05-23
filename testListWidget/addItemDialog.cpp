#include "addItemDialog.h"
#include <QPushButton>
#include <QVBoxLayout>


AddItemDialog :: AddItemDialog(QWidget *parent) : QDialog(parent) {
    this -> setWindowTitle("添加内容");
    QPushButton *button  = new QPushButton("完成");
    connect(button, &QPushButton :: clicked, this, &QDialog :: accept);

    QVBoxLayout *layout = new QVBoxLayout(this);
    layout -> addWidget(button);
}
