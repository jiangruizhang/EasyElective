#include "removecourse.h"
#include "ui_removecourse.h"

RemoveCourse::RemoveCourse(const QStringList &items, QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::RemoveCourse)
{
    ui->setupUi(this);
    ui->showList->addItems(items);
    ui->showList->setSelectionMode(QAbstractItemView :: MultiSelection);
    connect(ui->confirmButton, &QPushButton :: clicked, this, &RemoveCourse :: confirmButtonClicked);
}

RemoveCourse::~RemoveCourse()
{
    delete ui;
}

void RemoveCourse :: confirmButtonClicked() {
    QStringList selected;
    for (QListWidgetItem *item : ui->showList->selectedItems()) {
        selected << item->text();
    }
    emit itemsToRemove(selected);
    accept();
}
