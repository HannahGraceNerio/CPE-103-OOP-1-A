import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Account Registration'
        self.x = 200
        self.y = 200
        self.width = 400
        self.height = 520
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('python_logo_icon_168886.ico'))
        self.show()

    def initUI (self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('python_logo_icon_168886.ico'))

        self.textbox = QLineEdit(self)
        self.textboxbl1 = QLabel("First Name: ", self)
        self.textboxbl1.move(35, 73)
        self.textbox.move(95, 60)
        self.textbox.resize(250, 40)

        self.textbox = QLineEdit(self)
        self.textboxbl1 = QLabel("Last Name: ", self)
        self.textboxbl1.move(35, 120)
        self.textbox.move(95, 106)
        self.textbox.resize(250, 40)

        self.textbox = QLineEdit(self)
        self.textboxbl1 = QLabel("Username: ", self)
        self.textboxbl1.move(35, 170)
        self.textbox.move(95, 155)
        self.textbox.resize(250, 40)

        self.textbox = QLineEdit(self)
        self.textboxbl1 = QLabel("Password: ", self)
        self.textboxbl1.move(35, 217)
        self.textbox.move(95, 200)
        self.textbox.resize(250, 40)

        self.textbox = QLineEdit(self)
        self.textboxbl1 = QLabel("Email Address: ", self)
        self.textboxbl1.move(35, 260)
        self.textbox.move(110, 245)
        self.textbox.resize(235, 40)

        self.textbox = QLineEdit(self)
        self.textboxbl1 = QLabel("Contact Number: ", self)
        self.textboxbl1.move(35, 307)
        self.textbox.move(120, 290)
        self.textbox.resize(225, 40)

        self.button = QPushButton('Submit', self)
        self.button.setToolTip('')
        self.button.move(20, 355)
        self.button = QPushButton('clear', self)
        self.button.setToolTip('')
        self.button.move(100, 355)

        self.textboxbl = QLabel("Account Regitration", self)
        self.textboxbl.move(100, 20)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())