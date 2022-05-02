import login_scr
import sys
from PyQt5 import QtCore , QtGui , QtWidgets
from Sql_db import *
import global_var as GV


class loginpage(QtWidgets.QMainWindow , login_scr.Ui_MainWindow):  # class of login page

    def __init__(self):
        super(loginpage , self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Login_btn)

    def Login_btn(self , event):
        username = str(self.lineEdit.text())
        password = self.lineEdit_2.text()
        x = download_user_data(1)
        for i in range(len(x)):
            if (username in x[i][0]):
                print(x)
                GV.username = x[i][0]
                GV.password = x[i][1]
        if (username == GV.username) and (password == GV.password):
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            GV.state_machine = 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI = loginpage()
    GUI.show()
    app.exec_()

# if __name__ == '__main__':
#     main()
