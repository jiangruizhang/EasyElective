#ifndef REMOVECOURSE_H
#define REMOVECOURSE_H

#include <QDialog>
#include <QListWidget>

namespace Ui {
class RemoveCourse;
}

class RemoveCourse : public QDialog
{
    Q_OBJECT

public:
    explicit RemoveCourse(const QStringList &items, QWidget *parent = nullptr);
    ~RemoveCourse();
signals:
    void itemsToRemove(const QStringList &selectedItems);
private slots:
    void confirmButtonClicked();

private:
    Ui::RemoveCourse *ui;
};

#endif // REMOVECOURSE_H
