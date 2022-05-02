import sqlite3
import global_var as GV


def upload_equipment_details(date , Tblinfo):
    conn = sqlite3.connect("loginDB.db")
    db = conn.cursor()
    print("upload equipment details")
    for i in range(len(Tblinfo)):
        db.execute("insert into tblequipment_details(SrNo,Date,Utilitydetails,Downtimeinnumbers,DowntimeinMinute,"
                   "DowntimeForm,Remark)values(?,?,?,?,?,?,?)" , (
                       Tblinfo[i][0] , date , Tblinfo[i][1] , Tblinfo[i][2] , Tblinfo[i][3] , Tblinfo[i][4] ,
                       Tblinfo[i][5]))
    conn.commit()


def upload_shift_info(date , Shift , Shift_incharge , Handoverby , Takeoverby):
    print("shift info")
    conn = sqlite3.connect("loginDB.db")
    db = conn.cursor()
    db.execute('insert into tblShift_info(Date,Shift,Shift_incharge,Handoverby,Takeoverby)values(?,?,?,?,?)' ,
               (date , Shift , Shift_incharge , Handoverby , Takeoverby))
    conn.commit()


def upload_shift_activity(date, Read_data):
    conn = sqlite3.connect("loginDB.db")
    db = conn.cursor()
    for i in range(len(Read_data)):

        if (Read_data[i][1] == None or Read_data[i][2] == None):
            # print("data empty")
            pass
        else:
            db.execute('insert into tblShift_major(Date,Time,Plan,Action)values(?,?,?,?)' ,
                       (date , Read_data[i][0] , Read_data[i][1] , Read_data[i][2]))
    conn.commit()


def upload_user_data(name , key):
    conn = sqlite3.connect("loginDB.db")
    db = conn.cursor()
    db.execute('insert into user_details(name,key)values(?,?)' , (name , key))
    conn.commit()


def download_user_data(id):
    conn = sqlite3.connect('loginDB.db')
    db = conn.cursor()
    db.execute('SELECT name,key from user_details ')
    x = db.fetchall()
    # print(x[0][0])
    return x
# name='Admin'
# key='123'
# upload_user_data(name,key)
# download_user_data(1)
