from PyQt5.QtWidgets import QMessageBox

import Report
import sys
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import QDate
from Sql_db import *
import global_var as GV
from XL_to_pdf import *

class Report(QtWidgets.QMainWindow , Report.Ui_MainWindow):  # class of login page

    def __init__(self):
        super(Report , self).__init__()
        self.setupUi(self)
        print(GV.username)
        now = QDate.currentDate()
        self.dateEdit.setDate(now)
        self.pushButton.clicked.connect(self.Read_Shiftactivity)
        self.pushButton_3.clicked.connect(self.logout)

    def popupmeassage(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(self.quit_msg)
        msgBox.setWindowTitle("Message")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            msgBox.close()
        if returnValue == QMessageBox.Cancel:
            msgBox.close()

    def logout(self):
        print("logout")
        GV.state_machine = 0

    def Read_Shiftactivity(self):
        GV.date = self.dateEdit.text()
        GV.Shift = self.lineEdit_4.text()
        GV.Shift_incharge = self.lineEdit_3.text()
        GV.Handoverby = self.lineEdit_5.text()
        GV.Takeoverby = self.lineEdit_6.text()
        # -------------------------------------Read shift major activity data------------------------#
        row = self.tableWidget.rowCount()
        col = self.tableWidget.columnCount()
        data_list = [[] for i in range(100)]
        for i in range(row):
            for j in range(col):
                try:
                    item = self.tableWidget.item(i , j).text()
                    try:
                        data_list[i].append(item)
                        # row += 1
                    except ValueError as e:
                        print('value error' , e)
                except AttributeError:
                    row += 1
                    data_list[i].append(None)

        for i in range(len(data_list)):
            if (len(data_list[i]) > 0):
                GV.readcheck.append(data_list[i])
        # ---------------------------------------Equipment table-----------------------------------------------------------------------#
        row_1 = self.tableWidget_2.rowCount()
        col_1 = self.tableWidget_2.columnCount()
        Table_data = [[] for i in range(100)]
        for i in range(row_1):
            for j in range(col_1):
                try:
                    item = self.tableWidget_2.item(i , j).text()
                    try:
                        Table_data[i].append(item)
                        # row += 1
                    except ValueError as e:
                        print('value error' , e)
                except AttributeError:
                    row_1 += 1
                    Table_data[i].append(None)


        for i in range(len(Table_data)):
            if (len(Table_data[i]) > 0):
                GV.Tblcheck.append(Table_data[i])
        # -------------------------------------------------------------------------------------------------------#
        upload_equipment_details(GV.date , GV.Tblcheck)
        upload_shift_activity(GV.date , GV.readcheck)
        upload_shift_info(GV.date , GV.Shift , GV.Shift_incharge , GV.Handoverby , GV.Takeoverby)
        print(GV.date , row , col)
        print("shift ")
        Report_Generation()
        self.quit_msg = "Data save successfully"
        self.popupmeassage()


def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Report()
    GUI.show()
    app.exec_()


if __name__ == '__main__':
    main()
