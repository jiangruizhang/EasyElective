import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from ui_mainwindow import Ui_MainWindow 
from ui_addcourse import Ui_AddCourse

class AddCourse(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_AddCourse()
        self.ui.setupUi(self)
        self.ui.finish.clicked.connect(self.accept)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addCourse.clicked.connect(self.openAddCourse)
    
    def openAddCourse(self):
        self.addcourse = AddCourse(self)
        self.addcourse.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())