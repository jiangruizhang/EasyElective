#include "course.h"

Course :: Course() {}
Course :: Course(vector<classtime> p,int pts,bool if_m,int Your_inten,int have_cho,int quo,
    string Cou="Null Course Name",string Tea="Null Teacher's Name"){
        q=p;
        points=pts;
        if_must=if_m;
        Your_intension=Your_inten;
        have_chosen=have_cho;
        quota=quo;
        CourseName=Cou;
        TeacherName=Tea;
}
Requirement::Requirement(){Assignable_Points=99;}
Requirement::Requirement(int z1){Assignable_Points=z1;}
vector<Course> Course :: Organize(vector<Course> kx_Course,Requirement need=Requirement()){

}
void Course::setPoints(int p = 0){points=p;}
void Course::setIfMust(bool must = 0){if_must=must;}
void Course::setCourseName(string name = ""){CourseName=name;}
void Course::setTeacherName(string name = ""){TeacherName=name;}
void Course::setItension(int intension = 0){Your_intension=intension;}

string Course :: getCourseName() const { return CourseName;}
