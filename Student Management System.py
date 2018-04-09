from tkinter import *
import sqlite3
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
image = PhotoImage(file="login.png")
imageLabel= Label(frame,image=image)
imageLabel.place(x=250,y=50 ,height="100",width="100")
usernameLable=Label(frame,text="User name",font=("Algerian",15),bg="#40C8F2")
usernameLable.place(x=95,y=200)
username=Entry(frame,textvariable="USERNAME", width="22" ,font=(18))
username.place(x=250,y=200)
userpassLable=Label(frame,text="Password",font=("Algerian",15),bg="#40C8F2")
userpassLable.place(x=95,y=250)
userpass=Entry(frame,textvariable="PASSWORD", show="*", width="22" ,font=(18))
userpass.place(x=250,y=250)

loginbtn=Button(frame,text="Login", font=("Courier New", 12),width=19)
loginbtn.place(x=250,y=300)
def Back():
    frame.destroy()
exitbtn=Button(frame,text="Exit",font=("Courier New", 12),width=19,command=Back)
exitbtn.place(x=250,y=350)


frame.mainloop()