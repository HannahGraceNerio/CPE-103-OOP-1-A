import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt Line Edit'
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('python_logo_icon_168886.ico'))

        self.textboxbl = QLabel("Hello World!", self)
        self.textboxbl.move(120,120)
        self.textboxbl = QLabel("This program is written in Pycharm", self)
        self.textboxbl.move (70,150)
        self.show()


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())