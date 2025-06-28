import sys
import os
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QApplication,\
QMainWindow, QDialog, QTableWidgetItem,QListWidgetItem, \
QTableWidget,QAbstractScrollArea, QVBoxLayout,QGridLayout
from PySide6.QtCore import Signal, qDebug, Qt
from PySide6.QtGui import QFontDatabase, QFont
from ui_mainwindow import Ui_MainWindow 
from ui_addcourse import Ui_AddCourse
from ui_modifycourse import Ui_ModifyCourse
import pickle
from pathlib import Path
from course import Course, organize
from PySide6.QtGui import QPixmap
import secrets

#app = QApplication(sys.argv)

class AddCourse(QDialog):
    sendcourse = Signal(Course)
    def __init__(self, parent = None, courseindex = None):
        super().__init__(parent)
        self.ui = Ui_AddCourse()
        self.ui.setupUi(self)
        for row in range(self.ui.schedule.rowCount()):
            for col in range(self.ui.schedule.columnCount()):
                if self.ui.schedule.item(row, col) is None:
                    self.ui.schedule.setItem(row, col, QTableWidgetItem(''))
        self.ui.finish.clicked.connect(self.newcourse)
        self.ui.cancel.clicked.connect(self.close)
        self.courseindex = courseindex
    
    def newcourse(self):
        def getint(text, default = 0):
            try:
                return int(text)
            except:
                return default
        course = Course()
        course.course = self.ui.course.toPlainText()
        course.teacher = self.ui.teacher.toPlainText()
        course.limit = getint(self.ui.limit.toPlainText())
        course.chosen = getint(self.ui.chosen.toPlainText())
        course.intension = getint(self.ui.intension.toPlainText())
        course.point = getint(self.ui.point.toPlainText())
        course.must = self.ui.must.isChecked()
        for item in self.ui.schedule.selectedItems():
            course.schedule.append((item.column() + 1, item.row() + 1))
        index = secrets.token_bytes(32).hex()
        while index in self.courseindex:
            index = secrets.token_bytes(32).hex()
        course.index = index
        self.sendcourse.emit(course)
        self.close()

class ModifyCourse(QDialog):
    currentindex = None
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_ModifyCourse()
        self.ui.setupUi(self)
        self.ui.toselect.itemClicked.connect(self.displaycourse)
        self.ui.confirm.clicked.connect(self.savecourse)
        self.ui.remove.clicked.connect(self.removecourse)
        self.ui.close.clicked.connect(self.close)
        for i in range(self.ui.schedule.rowCount()):
            for j in range(self.ui.schedule.columnCount()):
                self.ui.schedule.setItem(i, j, QTableWidgetItem(''))
                self.ui.schedule.item(i, j).setSelected(False)
        self.load()
        # for i in range(toselect.count()):
        #     item = QListWidgetItem(toselect.item(i).text())
        #     item.setData(Qt.ItemDataRole.UserRole, toselect.item(i).data(Qt.ItemDataRole.UserRole))
        #     self.ui.toselect.addItem(item)

    def savecourse(self):
        self.save()
        self.load()
        self.parent().load()

    def removecourse(self):
        self.remove()
        self.load()
        self.parent().load()

    def displaycourse(self, item):
        course : Course = item.data(Qt.ItemDataRole.UserRole)
        self.currentindex = course.index
        self.ui.course.setPlainText(course.course)
        self.ui.teacher.setPlainText(course.teacher)
        self.ui.point.setPlainText(str(course.point))
        self.ui.chosen.setPlainText(str(course.chosen))
        self.ui.limit.setPlainText(str(course.limit))
        self.ui.intension.setPlainText(str(course.intension))
        self.ui.must.setChecked(course.must)
        for i in range(self.ui.schedule.rowCount()):
            for j in range(self.ui.schedule.columnCount()):
                self.ui.schedule.item(i, j).setSelected(False)
        for (day, time) in course.schedule:
            # qDebug(f'{day} {time}')
            self.ui.schedule.item(time - 1, day - 1).setSelected(True)

    def load(self):
        # 从文件读取课程
        self.ui.toselect.clear()

        data = Path('data')
        data.mkdir(exist_ok = True)  # 如果目录已存在不会报错
        courses = [item for item in data.iterdir() if item.is_file()]
        for item in courses:
            with open(item, 'rb') as f:
                course = pickle.load(f)
            item = QListWidgetItem(f'{course.course} - {course.teacher} - {course.point}')
            item.setData(Qt.ItemDataRole.UserRole, course)
            if course.selected == False:
                self.ui.toselect.addItem(item)
    
    def save(self):
        # 保存当前修改的课程
        if self.currentindex is None:
            qDebug('no selection')
            return
        # qDebug(str(self.currentindex))
        def getint(text, default = 0):
            try:
                return int(text)
            except:
                return default
        
        # qDebug(f' ** debuginfo ** : limit  = {self.ui.limit.toPlainText()}')

        course = Course()
        course.course = self.ui.course.toPlainText()
        course.teacher = self.ui.teacher.toPlainText()
        course.limit = getint(self.ui.limit.toPlainText())
        course.chosen = getint(self.ui.chosen.toPlainText())
        course.intension = getint(self.ui.intension.toPlainText())
        course.point = getint(self.ui.point.toPlainText())
        course.must = self.ui.must.isChecked()
        for item in self.ui.schedule.selectedItems():
            course.schedule.append((item.column() + 1, item.row() + 1))
        course.index = self.currentindex


        # displayinfo = [f'课程名称：{course.course}\n',
        #                f'教师名称：{course.teacher}\n',
        #                f'课程学分：{course.point}\n',
        #                f'选课情况：{course.chosen} / {course.limit}\n',
        #                f'课程类型：{'必修' if course.must else '非必修'}']
        # qDebug(''.join(displayinfo))

        
        data = Path('data')
        data.mkdir(exist_ok = True)
        data = data / course.index
        with open(data, 'wb') as f:
            pickle.dump(course, f)
    
    def remove(self):
        # 删除当前修改的课程
        if self.currentindex is None:
            qDebug('no selection')
            return
        data = Path('data')
        data.mkdir(exist_ok = True)
        data = data / self.currentindex
        if data.exists():
            data.unlink()

class CurrentArrangement(QDialog):
    def __init__(self, parent = None, courses : list[Course] = None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle('投点建议')
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['课程', '投点'])
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        data = []
        for course in courses:
            data.append((f'{course.course} - {course.teacher}', course.assignpoint))
        with open('points.txt', 'w', encoding = 'utf-8') as f:
            for name, point in data:
                f.write(f'{name} : {point}')
        

        self.table.setRowCount(len(data))
        for row, (name, score) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(score)))

        # 自动调整尺寸
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

        # 根据布局自动调整窗口尺寸
        self.adjustSize()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("EasyElective")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.initUI()
        self.ui.addCourse.clicked.connect(self.openAddCourse)
        self.ui.modifyCourse.clicked.connect(self.openModifyCourse)
        self.ui.finish.clicked.connect(self.close)
        self.ui.organize.clicked.connect(self.autoarrange)
        self.ui.toselect.itemClicked.connect(self.displaycourse)
        self.ui.selected.itemClicked.connect(self.displaycourse)
        self.ui.toselect.itemDoubleClicked.connect(self.to2ed)
        self.ui.selected.itemDoubleClicked.connect(self.ed2to)
        for row in range(self.ui.schedule.rowCount()):
            for col in range(self.ui.schedule.columnCount()):
                if self.ui.schedule.item(row, col) is None:
                    self.ui.schedule.setItem(row, col, QTableWidgetItem(''))
        self.load()
            
    def openAddCourse(self):
        self.addcourse = AddCourse(self, self.courseindex)
        self.addcourse.sendcourse.connect(self.newcourse)
        self.addcourse.exec()

    def to2ed(self, item):
        course = item.data(Qt.ItemDataRole.UserRole)
        course.selected = True
        self.save(course)
        self.load()

    def ed2to(self, item):
        course = item.data(Qt.ItemDataRole.UserRole)
        course.selected = False
        self.save(course)
        self.load()

    def newcourse(self, course : Course):
        self.save(course)
        self.load()

    def displaycourse(self, item):
        course = item.data(Qt.ItemDataRole.UserRole)
        self.ui.courseInfo.clear()
        displayinfo = [f'课程名称：{course.course}\n',
                       f'教师名称：{course.teacher}\n',
                       f'课程学分：{course.point}\n',
                       f'选课情况：{course.chosen} / {course.limit}\n',
                       f'课程类型：{'必修' if course.must else '非必修'}']
        self.ui.courseInfo.setPlainText(''.join(displayinfo))

    def flushschedule(self):
        temp = [['' for j in range(self.ui.schedule.columnCount())] for i in range(self.ui.schedule.rowCount())]
        for i in range(self.ui.selected.count()):
            item = self.ui.selected.item(i)
            course = item.data(Qt.ItemDataRole.UserRole)
            for (day, time) in course.schedule:
                if len(temp[time - 1][day - 1]) > 0:
                    temp[time - 1][day - 1] += '\n'
                temp[time - 1][day - 1] += f'{course.course} - {course.teacher}'
        for i in range(self.ui.schedule.rowCount()):
            for j in range(self.ui.schedule.columnCount()):
                self.ui.schedule.setItem(i, j, QTableWidgetItem(temp[i][j]))

    def load(self):
        # 从文件读取所有课程信息
        self.ui.toselect.clear()
        self.ui.selected.clear()
        self.ui.courseInfo.clear()
        self.courseindex = set()

        data = Path('data')
        data.mkdir(exist_ok = True)  # 如果目录已存在不会报错
        courses = [item for item in data.iterdir() if item.is_file()]
        for item in courses:
            self.courseindex.add(item.name)
            with open(item, 'rb') as f:
                course = pickle.load(f)
            item = QListWidgetItem(f'{course.course} - {course.teacher} - {course.point}')
            item.setData(Qt.ItemDataRole.UserRole, course)
            if course.selected == False:
                self.ui.toselect.addItem(item)
            else:
                self.ui.selected.addItem(item)
        self.flushschedule()

    def save(self, course):
        # 保存课程信息到文件
        self.courseindex.add(course.index)
        data = Path('data')
        data.mkdir(exist_ok = True)
        data = data / course.index
        with open(data, 'wb') as f:
            pickle.dump(course, f)

    def openModifyCourse(self):
        self.modifycourse = ModifyCourse(self)
        # self.addcourse.sendcourse.connect(self.newcourse)
        self.modifycourse.exec()
    
    def autoarrange(self):
        courses = []
        for i in range(self.ui.selected.count()):
            item = self.ui.selected.item(i)
            courses.append(item.data(Qt.ItemDataRole.UserRole))
        p, courses = organize(courses)
        if p == True:
            for course in courses:
                self.save(course)
            self.load()
            display = []
            for course in courses:
                if course.must == False and course.selected == True:
                    display.append(course)
            displaywindow = CurrentArrangement(self, display)
            displaywindow.exec()
        else:
            qDebug('Something wrong')

class CoverPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # 保存主窗口的引用
        self.setup_ui()

    def setup_ui(self):
    # 基本设置保持不变
        self.setWindowTitle("EasyElective")
        self.setFixedSize(1064, 723)

        # 创建图片标签
        self.cover_label = QLabel(self)
        pixmap = QPixmap("cover_page.png").scaled(1064, 723, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.cover_label.setPixmap(pixmap)
        self.cover_label.setAlignment(Qt.AlignCenter)

        # 创建按钮（注意设置为self的子组件）
        self.start_button = QPushButton("开始选课", self)
        self.start_button.clicked.connect(self.open_main_window)
    
        # 使用网格布局实现叠加效果
        layout = QGridLayout(self)
        layout.addWidget(self.cover_label, 0, 0)
        layout.addWidget(self.start_button, 0, 0, alignment=Qt.AlignCenter | Qt.AlignBottom)
    
        # 设置边距使按钮上移
        layout.setContentsMargins(0, 0, 0, 50)  # 下边距50像素

    def open_main_window(self):
        self.main_window.show()  # 显示主窗口
        self.close()  # 关闭封面页
        
if __name__ == "__main__":
    # 先加载样式表
    app = QApplication(sys.argv)
    try:
        with open("style.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("警告: 未找到样式表文件 style.qss")
    # 创建主窗口但不显示
    window = MainWindow()
    window.setWindowTitle("EasyElective")
    # 显示封面页
    cover_page = CoverPage(window)
    cover_page.show()
    sys.exit(app.exec())  # 注意是 exec() 不是 exec()