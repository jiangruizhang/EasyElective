import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PySide6.QtCore import Signal, qDebug
from ui_mainwindow import Ui_MainWindow 
from ui_addcourse import Ui_AddCourse
import pickle
from pathlib import Path
from course import Course
import secrets

class AddCourse(QDialog):
    sendcourse = Signal(Course)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_AddCourse()
        self.ui.setupUi(self)
        for row in range(self.ui.schedule.rowCount()):
            for col in range(self.ui.schedule.columnCount()):
                if self.ui.schedule.item(row, col) is None:
                    self.ui.schedule.setItem(row, col, QTableWidgetItem(""))
        self.ui.finish.clicked.connect(self.newcourse)
        self.ui.cancel.clicked.connect(self.close)
    
    def newcourse(self):
        def getint(text, default = 0):
            try:
                return int(text)
            except:
                # QMessageBox.warning(None, "输入错误", "请输入有效整数")
                return default
        course = Course()
        course.course = self.ui.course.toPlainText()
        course.teacher = self.ui.teacher.toPlainText()
        course.limit = getint(self.ui.teacher.toPlainText())
        course.chosen = getint(self.ui.chosen.toPlainText())
        course.intension = getint(self.ui.intension.toPlainText())
        course.point = getint(self.ui.point.toPlainText())
        course.must = self.ui.must.isChecked()
        # qDebug(f'{len(self.ui.schedule.selectedItems())}')
        for item in self.ui.schedule.selectedItems():
            course.schedule.append((item.column() + 1, item.row() + 1))
            # qDebug(f'{item.column() + 1} {item.row() + 1}')
        self.sendcourse.emit(course)
        self.close()
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load()
        self.ui.addCourse.clicked.connect(self.openAddCourse)
    
    def openAddCourse(self):
        self.addcourse = AddCourse(self)
        self.addcourse.sendcourse.connect(self.newcourse)
        self.addcourse.exec()
    def newcourse(self, course : Course):
        self.save(course)
        self.ui.toselect.addItem(course.course)

    def load(self):
        # 从文件读取所有课程信息
        self.courseindex = set()
        data = Path('data')
        data.mkdir(exist_ok = True)  # 如果目录已存在不会报错
        courses = [item for item in data.iterdir() if item.is_file()]
        for item in courses:
            self.courseindex.add(item.name)
            with open(item, 'rb') as f:
                course = pickle.load(f)
            if course.selected == False:
                self.ui.toselect.addItem(course.course)
            else:
                self.ui.selected.addItem(course.course)
    def save(self, course):
        # 保存课程信息到文件
        index = secrets.token_bytes(32).hex()
        while index in self.courseindex:
            index = secrets.token_bytes(32).hex()
        data = Path('data')
        data.mkdir(exist_ok = True)
        data = data / index
        with open(data, 'wb') as f:
            pickle.dump(course, f)
        self.courseindex.add(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())