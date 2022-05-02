# import keyboard
import main as mymain
from loginpage import *
from Report_main import *
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(QtWidgets.QMainWindow , mymain.Ui_MainWindow):
    def __init__(self , p1 , p2):
        super(Ui_MainWindow , self).__init__()
        self.setupUi(self)
        self.p1 = p1
        self.p2 = p2

    @pyqtSlot()
    def Page_change(self):

        if (GV.state_machine == 0):
            self.dockWidget.setWidget(self.p1)
        elif (GV.state_machine == 1):
            self.dockWidget.setWidget(self.p2)
            self.p2.lineEdit_3.setText(str(GV.username))


def main():
    app = QtWidgets.QApplication(sys.argv)
    p1 = loginpage()
    p2 = Report()
    GUI = Ui_MainWindow(p1 , p2)
    GUI.show()
    GUI.showMaximized()
    timer = QtCore.QTimer()
    timer.timeout.connect(GUI.Page_change)
    timer.start(100)
    app.exec_()


if __name__ == '__main__':
    main()
