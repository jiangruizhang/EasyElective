#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "addcourses.h"
#include "removecourse.h"

const string __daytime[7] = {"一", "二", "三", "四", "五", "六", "日"};
void MainWindow :: displayBasicInfo(const Course &course) {
    QString info;
    info += QString("课程名称: %1\n").arg(course.getCourseName());
    info += QString("学分: %1\n").arg(course.getPoints());
    info += QString("任课教师: %1\n").arg(course.getTeacherName());
    info += QString("是否必修: %1\n").arg(course.getIfMust() ? "是" : "否");
    info += QString("限选: %1\n").arg(course.getQuota());
    info += QString("已选: %1\n").arg(course.getHaveChosen());
    info += QString("上课时间:\n");
    for (classtime lesson : course.getClasstime()) {
        info += QString("星期%1 第 %2 节\n").arg(__daytime[lesson.getday() - 1]).arg(lesson.getti());
    }
    ui->courseInfo->setText(info);  // 假设你有一个 QLabel
}


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->courseInfo->clear();
    connect(ui->addCourses, &QPushButton :: clicked, this, &MainWindow :: addCourseWindow);
    connect(ui->removeCourse, &QPushButton :: clicked, this, &MainWindow :: removeCourseWindow);
    // connect(ui->unselectedCourses, &QListWidget::itemClicked, [](QListWidgetItem *item){
    //     qDebug() << "点击了：" << item->text();
    // });
    connect(ui->unselectedCourses, &QListWidget::itemClicked, this, [=](QListWidgetItem *item){
        Course c = item->data(Qt::UserRole).value<Course>();
        displayBasicInfo(c);
    });
    connect(ui->selectedCourses, &QListWidget::itemClicked, this, [=](QListWidgetItem *item){
        Course c = item->data(Qt::UserRole).value<Course>();
        displayBasicInfo(c);
    });
    connect(ui->unselectedCourses, &QListWidget :: itemDoubleClicked, this, &MainWindow :: unselectedToSeleted);
    connect(ui->selectedCourses, &QListWidget :: itemDoubleClicked, this, &MainWindow :: selectedToUnselected);
    ui->schedule->setSelectionMode(QAbstractItemView :: NoSelection);
    for (int row = 0; row < ui->schedule->rowCount(); ++row) {
        for (int col = 0; col < ui->schedule->columnCount(); ++col) {
            ui->schedule->setCellWidget(row, col, new QTextBrowser());
        }
    }
    displaySchedule();
}

MainWindow::~MainWindow()
{
    delete ui;
}

QString toQString(string str) { return QString::fromUtf8(str.c_str());}

void MainWindow::addCourseWindow() {
    addCourses *addDialog = new addCourses(this);
    connect(addDialog, &addCourses :: receiveInfo, this, [&](const Course &course) {
        QListWidgetItem *item = new QListWidgetItem(toQString(course.getCourseName() + "; " + course.getTeacherName() + "; " + to_string(course.getPoints()) + " 学分"));
        item->setData(Qt :: UserRole, QVariant::fromValue(course));
        ui->unselectedCourses->addItem(item);
    });
    addDialog->exec();
}

void MainWindow::removeCourseWindow() {
    QStringList items;
    for (int i = 0; i < ui->unselectedCourses->count(); ++i) {
        items << ui->unselectedCourses->item(i)->text();
    }
    RemoveCourse *removeDialog = new RemoveCourse(items, this);
    connect(removeDialog, &RemoveCourse :: itemsToRemove, this, [&](const QStringList &itemsToRemove) {
        for (int i = ui->unselectedCourses->count() - 1; i >=0; --i) {
            QListWidgetItem *item = ui->unselectedCourses->item(i);
            if (itemsToRemove.contains(item->text())) {
                delete ui->unselectedCourses->takeItem(i);
            }
        }
    });
    removeDialog->exec();
}

void MainWindow :: unselectedToSeleted(QListWidgetItem *item) {
    QListWidgetItem *newItem = new QListWidgetItem(item->text());
    newItem->setData(Qt::UserRole, item->data(Qt::UserRole));
    ui->selectedCourses->addItem(newItem);

    int row = ui->unselectedCourses->row(item);
    delete ui->unselectedCourses->takeItem(row);

    displaySchedule();
}
void MainWindow :: selectedToUnselected(QListWidgetItem *item) {
    QListWidgetItem *newItem = new QListWidgetItem(item->text());
    newItem->setData(Qt::UserRole, item->data(Qt::UserRole));
    ui->unselectedCourses->addItem(newItem);

    int row = ui->selectedCourses->row(item);
    delete ui->selectedCourses->takeItem(row);

    displaySchedule();
}
void MainWindow :: displaySchedule() {
    for (int row = 0; row < ui->schedule->rowCount(); ++row) {
        for (int col = 0; col < ui->schedule->columnCount(); ++col) {
            QTextBrowser* browser = qobject_cast<QTextBrowser*>(ui->schedule->cellWidget(row, col));
            browser->clear();
        }
    }
    for (int i = 0; i < ui->selectedCourses->count(); ++i) {
        Course c = ui->selectedCourses->item(i)->data(Qt::UserRole).value<Course>();
        for (classtime lesson : c.getClasstime()) {
            int col = lesson.getday() - 1, row = lesson.getti() - 1;
            QTextBrowser* browser = qobject_cast<QTextBrowser*>(ui->schedule->cellWidget(row, col));
            browser->append(toQString(c.getCourseName() + "-" + c.getTeacherName()));
        }
    }
}
