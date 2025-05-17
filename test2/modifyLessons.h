#ifndef MODIFYLESSONS_H
#define MODIFYLESSONS_H

#include <QDialog>

class QPushButton;

class ModifyDialog : public QDialog
{
    Q_OBJECT

public:
    explicit ModifyDialog(QWidget *parent = nullptr);
};

#endif // MODIFYLESSONS_H
