from copy import deepcopy
from math import floor, sqrt
from PySide6.QtCore import qDebug
class Course:
    '''
    表示一门课程，有若干个参数
    '''
    def __init__(self):
        # 课程基本信息
        self.schedule = []      # 上课时间，用 (day, ti) 来表示 1 - 7, 1 - 12
        self.point = 0          # 课程学分
        self.must = False       # True 表示必须选择这门课
        self.course = ''        # 课程名字
        self.teacher = ''       # 老师名字
        self.chosen = 0         # 已选人数
        self.limit = 1          # 限选人数
        self.selected = False   # 是否选择，默认为不选的状态
        self.index = 0          # 随机的 256bit 编号
        # 用户的情况
        self.intension = 0      # 上这门课的意愿值，用 1 ～ 99 衡量
        # 客户端推荐内容
        self.assignpoint = 0      # 推荐投点数

    def firstclass(self):
        '''
        是否有早八课
        '''
        for _, time in self.schedule:
            if time == 1:
                return True
        return False
    
    def classcount(self, day):
        '''
        查询某一天有几节课
        '''
        res = 0
        for _day, _ in self.schedule:
            if _day == day:
                res += 1
        return res
    def weight(self):
        '''
        用于计算投点分配权重
        '''
        if self.chosen < self.limit:
            return 0
        else:
            return (self.chosen - self.limit + 1) / self.limit
    def posb(self):
        '''
        目前投点状况下，能上这门课的概率，假设别人投了 K 点，默认 K = 10
        '''
        K = 10
        if self.must == True or self.chosen < self.limit:
            return 1
        else:
            return self.assignpoint * self.limit / (self.assignpoint + self.chosen * K)

class Req:
    '''
    表示选课的限制
    '''
    def __init__(self, ap = 99, lb = 0, ub = 25):
        self.ap = ap    # 可投总点数
        self.lb = lb    # 学分下限
        self.ub = ub    # 学分上限
    
class Res:
    '''
    选课方案，同时计算权值 val 用于衡量方案好坏
    '''
    def __init__(self, courses : list[Course] = [], AP : int = 99):
        '''
        courses 选课方案
        AP 可投点数
        '''
        def nearlost(course1 : Course, course2 : Course):
            res = 0
            for day1, time1 in course1.schedule:
                for day2, time2 in course2.schedule:
                    if day1 == day2 and abs(time1 - time2) == 1:
                        res += 1
            return res
        self.courses = deepcopy(courses)
        self.val = 250 * len(courses)
        # 早八课
        firstcount = 0
        for course in self.courses:
            firstcount += course.firstclass()
            if course.must == False:
                self.val += course.intension * course.point * 6
        self.val -= firstcount ** 2 * 80
        # 连堂课
        for i in range(len(self.courses)):
            for j in range(i + 1, len(self.courses)):
                self.val -= 50 * nearlost(self.courses[i], self.courses[j])
        # 一天上课数量
        for day in range(1, 8):
            classes = 0
            for course in self.courses:
                classes += course.classcount(day)
            if classes == 0:
                self.val += 1000 # 放假日奖励
            elif classes <=2:
                self.val += 500 # 少课日奖励
            elif classes >= 6:
                self.val -= 15 * (classes - 6) ** 3 # 多课日惩罚
        # 投点分配
        total = 0
        for course in self.courses:
            course.assignpoint = 0
            if course.must == False:
                total += course.weight()
        if total > 0:
            sum = 0
            for i in range(len(self.courses)):
                if self.courses[i].must == False:
                    os = floor(AP * self.courses[i].weight() / total)
                    self.courses[i].assignpoint = os
                    sum += os
            for i in range(len(self.courses)):
                if self.courses[i].must == False and sum < AP:
                    self.courses[i].assignpoint += 1
                    sum += 1
        else:
            for i in range(len(self.courses)):
                self.courses[i].assignpoint = 0
        # 选上课的概率对权重影响
        posb = 1
        for course in self.courses:
            posb *= course.posb()
        self.val = self.val * sqrt(posb)

def organize(courses : list[Course] = [], constraint : Req = Req()):
    # 返回二元组，第一个为 True/False 表示是否有合法方案，第二是 list[Course] 通过 selected 来表示选不选
    def conflict(courses : list[Course] = []):
        def con(course1 : Course, course2 : Course):
            for d1, t1 in course1.schedule:
                for d2, t2 in course2.schedule:
                    if d1 == d2 and t1 == t2:
                        return True
            return False
        for i  in range(len(courses)):
            for j in range(i + 1, len(courses)):
                if con(courses[i], courses[j]):
                    return True
        return False
    courses1 : list[Course] = []
    for course in courses:
        if course.must == True:
            courses1.append(course)
    if conflict(courses1):
        qDebug('must courses conflict')
        return (False, [])
    points = 0 
    for course in courses1:
        points += course.point
    if points > constraint.ub:
        qDebug('must courses overbound')
        return (False, [])
    courses2 : list[Course] = []
    for course in courses:
        if course.must == False and not conflict(courses1 + [course]):
            courses2.append(course)
    result = None
    def search(toselect : list[Course], selected : list[Course], points):
        nonlocal constraint, result
        if len(toselect) == 0:
            if constraint.lb <= points <= constraint.ub:
                current = Res(selected, constraint.ap)
                qDebug(f'{points} {current.val} {constraint.ap}')
                if result is None:
                    result = current
                else:
                    if current.val > result.val:
                        result = current
            return
        search(toselect[:-1], selected, points)
        if conflict(selected + [toselect[-1]]) == False and points + toselect[-1].point <= constraint.ub:
            search(toselect[:-1], selected + [toselect[-1]], points + toselect[-1].point)
    search(courses2, courses1, points)
    assignpoint = dict()
    for course in result.courses:
        assignpoint.update({course.index : course.assignpoint})
        # index.add(course.index)
    for course in courses:
        if course.index in assignpoint:
            course.selected = True
            course.assignpoint = assignpoint[course.index]
        else:
            course.selected = False
            course.assignpoint = 0
    if result is None:
        qDebug('wrong')
        return (False, None)
    else:
        qDebug('right')
        return (True, courses)