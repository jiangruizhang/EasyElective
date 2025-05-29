#ifndef COURSE_H
#define COURSE_H


#include <QMetaType>
#include <QString>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
using namespace std;
class classtime{
private:
    int day,ti; //  day 1-7 , ti 1-12
public:
    classtime(){day=0,ti=0;}
    classtime(int x,int y){day=x,ti=y;}
    bool operator == (const classtime &x) const{
        return day==x.day&&ti==x.ti;
    }
    bool near(const classtime &x);
    int getti();
    int getday();
};
class Requirement{
private:
    int LowerBound,UpperBound;
    int Assignable_Points;
public:
    Requirement(int z1=99,int lb=20,int ub=30);
    bool OverUpperBound(int s);
    bool LessLowerBound(int s);
    int getAP();
};
class Course {
private:
    vector<classtime>q; //上课时间
    int points; //学分
    bool if_must; //是否必修
    string CourseName,TeacherName;
    //int Teachers_points; //教师得分
    int Your_intension; //意愿值 1~99
    int have_chosen,quota; // 已选 ，限选
public:
    int oAss_Points; //当前分配的点数，载入时的值无意义，Organize后的值为推荐投点数
    Course();
    Course(vector<classtime> p,int pts,bool if_m,int Your_inten,int have_chosen,int quo,
        string Cou,string Tea);
    void setPoints(int p);
    void setIfMust(bool must);
    void setCourseName(string name);
    void setTeacherName(string name);
    void setIntension(int intension);
    bool getIfMust() const;
    int getPoints() const;
    int getInten() const;
    string getCourseName() const;
    string getTeacherName() const;
    bool Conflict(const Course &x); //判断课程时间是否冲突
    int near(const Course &x); //判断是否连堂课
    int Zao8();// 判断是否早8
    int getClassNum(int oday); // 计算某天有多少节此课
    double Compe_Value();
    double getP();
};

Q_DECLARE_METATYPE(Course)



class Organize_Result{
private:
    vector<Course> Course_list;
    int wrong_number;
    double possibility,val;
public:
    Organize_Result(vector<Course> Cl,int wn,double pos,double v);
    Organize_Result(vector<Course> Cl,int AP);
    void Update(const Organize_Result &x);
};



Organize_Result Organize(vector<Course> kx_Course,Requirement need);


#endif // COURSE_H
