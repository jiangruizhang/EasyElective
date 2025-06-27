#include "course.h"

bool classtime::near(const classtime &x){
    if(day==x.day&&abs(ti-x.ti)==1)return true;
    return false;
}
int classtime::getti(){return ti;}
int classtime::getday(){return day;}
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
Requirement::Requirement(int z1,int lb,int ub){
    Assignable_Points=z1;
    LowerBound=lb;
    UpperBound=ub;
}
bool Requirement::OverUpperBound(int s){return s>UpperBound;}
bool Requirement::LessLowerBound(int s){return s<LowerBound;}
int Requirement::getAP(){return Assignable_Points;}
Organize_Result::Organize_Result(vector<Course> Cl,int wn,double pos,double v){
    Course_list=Cl;
    wrong_number=wn;
    possibility=pos;
    val=v;
}
Organize_Result::Organize_Result(vector<Course> Cl,int AP){
    Course_list=Cl; wrong_number=0;
    double oVal=0; int n=Cl.size();
    for(int i=0; i<n; ++i)
     if(!Cl[i].getIfMust())oVal+=Cl[i].getInten()*Cl[i].getPoints()*6; //oval+=选中选修课的意愿值*学分*10
    for(int i=0; i<n; ++i)
     for(int j=i+1; j<n; ++j)
      oVal-=50*Cl[i].near(Cl[j]); //连堂课价值损失
    int s_Zao8=0;
    for(int i=0; i<n; ++i)
     if(!Cl[i].getIfMust())s_Zao8+=Cl[i].Zao8(); 
    oVal-=s_Zao8*s_Zao8*80; //早八课程损失
    for(int oday=1; oday<=7; ++oday){
        int ocs=0;
        for(int i=0; i<n; ++i)
         ocs+=Cl[i].getClassNum(oday);
        if(!ocs)oVal+=1000; //假期奖励
        else if(ocs<=2)oVal+=500; //少课奖励
         else if(ocs>=6)oVal-=15*(ocs-5)*(ocs-5)*(ocs-5); //多课惩罚
    }
    double op=1,s=0;
    for(int i=0; i<n; ++i){
        Course_list[i].oAss_Points=0;
        if(!Cl[i].getIfMust()) s+=Cl[i].Compe_Value();
    }
    int oos=0;
    for(int i=0; i<n; ++i){
        if(!Cl[i].getIfMust()){
            int os=AP*Cl[i].Compe_Value()/s;
            Cl[i].oAss_Points=os; oos+=os;
        }
    }
    for(int i=0; i<n&&oos<AP; ++i)
     if(!Cl[i].getIfMust()){Cl[i].oAss_Points++; oos++;}
    for(int i=0; i<n; ++i)op*=Cl[i].getP();
    possibility=op;
    val=oVal*sqrt(op); //平衡多课and少课/高价值的低概率方案
}
void dfs(vector<Course> oXX,int o,Requirement need,int opts,const vector<Course> &XX,const vector<Course> &BX,Organize_Result &best_ans){
    if(need.OverUpperBound(opts))return;
    if(o==XX.size()){
        if(need.LessLowerBound(opts))return;
        vector<Course>cho;
        for(int i=0; i<oXX.size(); ++i)cho.push_back(oXX[i]);
        for(int i=0; i<BX.size(); ++i)cho.push_back(BX[i]);
        Organize_Result now_ans(cho,need.getAP());
        best_ans.Update(now_ans);
        return;
    }
    dfs(oXX,o+1,need,opts,XX,BX,best_ans);
    oXX.push_back(XX[o]);
    dfs(oXX,o+1,need,opts+XX[o].getPoints(),XX,BX,best_ans);
    oXX.pop_back();
}
void Organize_Result::Update(const Organize_Result &x){
    if(val<x.val){
        Course_list=x.Course_list;
        wrong_number=0;
        possibility=x.possibility;
        val=x.val;
    }
}
Organize_Result Organize(vector<Course> kx_Course,Requirement need=Requirement()){
    vector<Course>BX,null,XX;
    int n1=kx_Course.size();
    for(int i=0; i<n1; ++i){
        if(kx_Course[i].getIfMust()) BX.push_back(kx_Course[i]);
    }
    int n2=BX.size(); bool fl=0;
    for(int i=0; i<n2; ++i){
        for(int j=i+1; j<n2; ++j)
         if(BX[i].Conflict(BX[j])){fl=1; break;}
        if(fl)break;
    }
    if(fl){
        cout<<"There is a conflict between your required courses"<<endl; //报错1
        return Organize_Result(null,1,0,0);
    }
    int s=0;
    for(int i=0; i<n2; ++i)s+=BX[i].getPoints();
    if(need.OverUpperBound(s)){
        cout<<"Your required course credits have exceeded the upper limit"<<endl; //报错2
        return Organize_Result(null,2,0,0);
    }
    for(int i=0; i<n1; ++i){
        if(!kx_Course[i].getIfMust()){
            int ofl=1;
            for(int j=0; j<n2; ++j)
             if(BX[j].Conflict(kx_Course[i])){ofl=0; break;}
            if(ofl)XX.push_back(kx_Course[i]);
        }
    }
    Organize_Result Plan(null,0,0,-1);
    dfs(null,0,need,s,XX,BX,Plan);
    return Plan;
}
void Course::setPoints(int p){points=p;}
void Course::setIfMust(bool must){if_must=must;}
void Course::setCourseName(string name){CourseName=name;}
void Course::setTeacherName(string name = ""){TeacherName=name;}
void Course::setIntension(int intension = 0){Your_intension=intension;}
bool Course::getIfMust(){return if_must;}
int Course::getPoints() const{return points;}
int Course::getInten(){return Your_intension;}
bool Course::Conflict(const Course &x){
    int n1=q.size(),n2=x.q.size();
    for(int i=0; i<n1; ++i)
     for(int j=0; j<n2; ++j)
      if(q[i]==x.q[j])return false;
    return true;
}
int Course::near(const Course &x){
    int n1=q.size(),n2=x.q.size(),s=0;
    for(int i=0; i<n1; ++i)
     for(int j=0; j<n2; ++j)
      if(q[i].near(x.q[j]))s++;
    return s;
}
int Course::Zao8(){
    int n=q.size(),s=0;
    for(int i=0; i<n; ++i)
     if(q[i].getti()==1)s++;
    return s;
}
int Course::getClassNum(int oday){
    int n=q.size(),s=0;
    for(int i=0; i<n; ++i)
     if(q[i].getday()==oday)s++;
    return s;
}
double Course::Compe_Value(){
    if(have_chosen<quota)return 0;
    return 1.0*(have_chosen-quota+1)/quota;
}
double Course::getP(){
    if(if_must||have_chosen<quota)return 1.0;
    return 1.0*oAss_Points*quota/(oAss_Points+have_chosen*10);
    //在这里我们假设如果已选人数大于等于名额数，每人投10个点，否则不投点
}