class Course:
    # TO ASK
    # 上课时间 数字 和 星期几/第几节课 怎么对应的
    # 目前认为是 1 - 7, 1 - 12

    def __init__(self):
        # 课程基本信息
        self.schedule = []      # 上课时间，用 (day, ti) 来表示
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
    def __repr__(self):
        return '<course>'
    def __str__(self):
        return f'{self.course} - {self.teacher} - {self.point}'
    # TO THINK : 是否要区分 set 和 get ？