from copy import deepcopy
from math import floor, sqrt
class Course:
    # TO ASK

    def __init__(self):
        # 课程基本信息
        self.schedule = []      # 上课时间，用 (day, ti) 来表示 1 - 7, 1 - 12
        self.point = 0          # 课程学分
        self.must = False       # True 表示必须选择这门课
        self.course = ''        # 课程名字
        self.teacher = ''       # 老师名字
        self.chosen = 0         # 已选人数
        self.limit = 0          # 限选人数
        self.selected = False   # 是否选择，默认为不选的状态
        self.index = 0          # 随机的 256bit 编号
        # 用户的情况
        self.intension = 0      # 上这门课的意愿值，用 1 ～ 99 衡量
        # 客户端推荐内容
        self.recommand = 0      # 推荐投点数

    def zao8(self):
        for _, time in self.schedule:
            if time == 1:
                return True
        return False
    
    def calssnum(self, day):
        res = 0
        for _day, _ in self.schedule:
            if _day == day:
                res += 1
        return res
    def cVal(self):
        if self.chosen < self.limit:
            return 0
        else:
            return (self.chosen - self.limit + 1) / self.limit
    def getP(self):
        if self.must == True or self.chosen < self.limit:
            return 1
        else:
            return self.recommand * self.limit / (self.recommand + self.chosen * 10)

class Req:
    def __init__(self, ap = 99, lb = 20, ub = 30):
        self.ap = ap
        self.lb = lb
        self.ub = ub
    def over(self, s):
        return s > self.ub
    def less(self, s):
        return s < self.lb
    
class Res:
    # 选课方案
    def __init__(self):
        self.courses : list[Course] = []
        self.wrong = 0
        self.posb = 0
        self.val = 0
    def fromData(self, courses, wrong, posb, val):
        self.courses = deepcopy(courses)
        self.wrong = wrong
        self.posb = posb
        self.val = val

    def fromAP(self, courses, AP):
        def nearlost(course1 : Course, course2 : Course):
            res = 0
            for day1, time1 in course1.schedule:
                for day2, time2 in course2.schedule:
                    if day1 == day2 and abs(time1 - time2) == 1:
                        res += 1
            return res
        self.courses = deepcopy(courses)
        self.wrong = 0
        self.val = 0
        zao8count = 0
        for course in self.courses:
            zao8count += course.zao8()
            if course.must == False:
                self.val += course.intension * course.point * 6
        self.val -= zao8count ** 2 * 80
        for i in range(len(self.courses)):
            for j in range(i + 1, len(self.courses)):
                self.val -= 50 * nearlost(self.courses[i], self.courses[j])
        for day in range(1, 8):
            classes = 0
            for course in self.courses:
                classes += course.calssnum(day)
            if classes == 0:
                self.val += 1000
            elif classes <=2:
                self.val += 500
            elif classes >= 6:
                self.val -=15 * (classes - 6) ** 3
        total = 0
        for course in self.courses:
            course.recommand = 0
            if course.must == False:
                total += course.cVal()
        sum = 0
        for course in self.courses:
            if course.must == False:
                os = floor(AP * course.cVal() / total)
                course.recommand = os
                sum += os
        for course in self.courses:
            if course.must == False and sum < AP:
                course.recommand += 1
                sum += 1
        for course in self.courses:
            self.posb *= course.getP()
        self.val = self.val * sqrt(self.posb)

def organize(courses : list[Course] = []):
    # 返回二元组，第一个为 True/False 表示是否有合法方案，第二是 list[Course] 通过 selected 来表示选不选
    pass