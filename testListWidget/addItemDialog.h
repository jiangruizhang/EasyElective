#ifndef ADDITEMDIALOG_H
#define ADDITEMDIALOG_H


#include <QDialog>

class QPushButton;


class AddItemDialog : public QDialog {
    Q_OBJECT
public:
    explicit AddItemDialog(QWidget *parent = nullptr);
};


#endif // ADDITEMDIALOG_H
