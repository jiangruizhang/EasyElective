import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QFontDatabase, QFont

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. 加载字体文件
        font_id = QFontDatabase.addApplicationFont("fonts/cool black.ttf")
        if font_id == -1:
            print("字体加载失败！")
            return

        # 2. 获取字体家族名称
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        # 3. 创建字体对象
        custom_font = QFont(font_family, 12)  # 字体大小12

        # 4. 应用到整个应用
        QApplication.setFont(custom_font)

        # 5. 创建控件
        label = QLabel("这是站酷酷黑体", self)
        label.setFont(custom_font)
        button = QPushButton("按钮", self)

        # 6. 布局
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())