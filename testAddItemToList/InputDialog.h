#ifndef INPUTDIALOG_H
#define INPUTDIALOG_H

#include <QDialog>
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>

class InputDialog : public QDialog {
    Q_OBJECT

public:
    InputDialog(QWidget *parent = nullptr) : QDialog(parent) {
        setWindowTitle("输入项目");

        QVBoxLayout *layout = new QVBoxLayout(this);
        lineEdit = new QLineEdit(this);
        QPushButton *okButton = new QPushButton("确定", this);

        layout->addWidget(lineEdit);
        layout->addWidget(okButton);

        connect(okButton, &QPushButton::clicked, this, &InputDialog::onOkClicked);
    }

signals:
    void stringEntered(const QString &text);

private slots:
    void onOkClicked() {
        emit stringEntered(lineEdit->text());
        accept(); // 关闭窗口
    }

private:
    QLineEdit *lineEdit;
};

#endif // INPUTDIALOG_H
