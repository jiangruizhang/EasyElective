#ifndef COURSE_H
#define COURSE_H

#include <vector>
#include <string>
#include <QString>
using namespace std;
class classtime{
public:
    int day,ti;
    classtime(){day=0,ti=0;}
    classtime(int x,int y){day=x,ti=y;}
};
class Requirement{
private:
    int Assignable_Points;
public:
    Requirement();
    Requirement(int z1);
};
class Course {
private:
    vector<classtime>q; //上课时间
    int points; //学分
    bool if_must; //是否必修
    string CourseName,TeacherName;
    //int Teachers_points; //教师得分
    int Your_intension; //意愿值
    int have_chosen,quota;
public:
    Course();
    Course(vector<classtime> p,int pts,bool if_m,int Your_inten,int have_chosen,int quo,
        string Cou,string Tea);
    vector<Course> Organize(vector<Course> kx_Course,Requirement need);

    void setPoints(int p);
    void setIfMust(bool must);
    void setCourseName(string name);
    void setTeacherName(string name);
    void setItension(int intension);

    // int getPoints() const;
    // bool getIfMust() const;
    string getCourseName() const;
    // string getTeacherName() const;
    // int getItension() const;


};

#endif // COURSE_H
