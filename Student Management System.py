from tkinter import *
import sqlite3 as lite
from PIL import *


frame=Tk()
frame.title("Loging Form")
screen_width = frame.winfo_screenwidth()
screen_height = frame.winfo_screenheight()
width=550
height= 450
x = (screen_width/2)-(width/2)
y = (screen_height/2) - (width/2)

frame.geometry("%dx%d+%d+%d" % (width ,height , x , y))
frame.resizable(0,0)
frame.config(bg="#40C8F2")

#DATABASE
def Database():
     global conn,cursor
     conn = lite.connect("sms.db")
     cursor = conn.cursor()
     cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
     cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
     if cursor.fetchone() is NONE:
         cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
         conn.commit()
def Login(event=None):
    Database()

    if USERNAME.get() ==""  or USERPASS.get() == "":
        warningLabel.config(text="Please Filled all field")

    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",(USERNAME.get() ,USERPASS.get()) )
        if cursor.fetchone() is not None:
           MainWindow()
           USERNAME.set("")
           USERPASS.set("")
        else:
            warningLabel.config(text="Invalid username or Password" , fg ="red")
            USERNAME.set("")
            USERPASS.set("")

def MainWindow():
    global Home
    frame.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    frame.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)


image = PhotoImage(file="login.png")
imageLabel= Label(frame,image=image)
imageLabel.place(x=250,y=50 ,height="100",width="100")
usernameLable=Label(frame,text="User name",font=("Algerian",15),bg="#40C8F2")
usernameLable.place(x=95,y=200)


USERNAME= StringVar()
USERPASS = StringVar()


username=Entry(frame,textvariable=USERNAME, width="22" ,font=(18))
username.place(x=250,y=200)
userpassLable=Label(frame,text="Password",font=("Algerian",15),bg="#40C8F2")
userpassLable.place(x=95,y=250)

userpass=Entry(frame,textvariable= USERPASS, show="*", width="22" ,font=(18))
userpass.place(x=250,y=250)
warningLabel=Label(frame,text ="Login please", width="24" , font=("Arial Black",14))
warningLabel.place(x=200,y=385)
def Back():
    frame.destroy()
exitbtn=Button(frame,text="Exit",font=("Courier New", 12),width=19,command=Back)
exitbtn.place(x=250,y=350)

loginbtn=Button(frame,text="Login", font=("Courier New", 12),width=19 ,command=Login)
loginbtn.place(x=250,y=300)
frame.mainloop()