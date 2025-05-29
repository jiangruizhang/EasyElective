#include "modifycourses.h"
#include "ui_modifycourses.h"

ModifyCourses::ModifyCourses(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::ModifyCourses)
{
    ui->setupUi(this);
    connect(ui->confirmButton, &QPushButton :: clicked, this, &ModifyCourses :: confirmButtonClicked);
}

ModifyCourses::~ModifyCourses()
{
    delete ui;
}

void ModifyCourses :: confirmButtonClicked() {
    Course t;
    t.setCourseName(ui->courseName->text().toUtf8().constData());
    t.setTeacherName(ui->teacherName->text().toUtf8().constData());
    t.setIfMust(ui->ifMust->text().toInt() == 1);
    t.setItension(ui->intensionPoint->text().toInt());
    t.setPoints(ui->courseCredit->text().toInt());
    emit courseInformation(t);
    accept();
}



// Course(vector<classtime> p,int pts,bool if_m,int Your_inten,int have_chosen,int quo,
//        string Cou="Null Course Name",string Tea="Null Teacher's Name");
