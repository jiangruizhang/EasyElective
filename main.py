import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QListWidgetItem
from PySide6.QtCore import Signal, qDebug, Qt
from ui_mainwindow import Ui_MainWindow 
from ui_addcourse import Ui_AddCourse
import pickle
from pathlib import Path
from course import Course
import secrets

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
        course.limit = getint(self.ui.teacher.toPlainText())
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
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addCourse.clicked.connect(self.openAddCourse)
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
        # item = QListWidgetItem(f'{course.course} - {course.teacher} - {course.point}')
        # item.setData(Qt.ItemDataRole.UserRole, course)
        # self.ui.toselect.addItem(item)

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
                if len(temp[day - 1][time - 1]) > 0:
                    temp[day - 1][time - 1] += '\n'
                temp[day - 1][time - 1] += f'{course.course} - {course.teacher}'
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())