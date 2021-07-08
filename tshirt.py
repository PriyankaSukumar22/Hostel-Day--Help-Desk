from tkinter import *
import sqlite3
try:
  import Tkinter as tk
except ImportError:
       import tkinter as tk


root=tk.Tk()
root.title("T-Shirt registration Form")

Name=StringVar()
Rollno=StringVar()
Gender=StringVar()
Size=StringVar()
Room_no=StringVar()
No_of_t_shirts=IntVar()

def database():
    name1=Name.get()
    r_no=Rollno.get()
    n_shirts=No_of_t_shirts.get()
    room_no=Room_no.get()
    size1=Size.get()
    gender=Gender.get()
    conn=sqlite3.connect("t_shirt3.db")
    with conn:
          cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS t_shirt3 (Rollno TEXT,Name TEXT,Room_no TEXT,Gender TEXT,Size TEXT,No_of_t_shirts INTEGER)")
    for i in range (0,int(n_shirts)):
     cursor.execute("INSERT INTO t_shirt3 (Rollno,Name,Room_no,Gender,Size,No_of_t_shirts)VALUES(?,?,?,?,?,?)",(r_no,name1,room_no,gender,size1,n_shirts))
    conn.commit()

image1=tk.PhotoImage(file="1.gif")
w=image1.width()
h=image1.height()
root.geometry("%dx%d+0+0"%(w,h))

panel1=tk.Label(root,image=image1)
panel1.pack(side='top',fill='both',expand='yes')


panel1.image=image1


label_0=Label(root,text="T-Shirt registration Form",width=40,font=("bold",40))
label_0.place(x=130,y=10)
label_0.configure(bg="#BA55D3")

label_1=Label(root,text="RollNo :",width=8,font=("bold",15))
label_1.place(x=344,y=120)

entry_1=Entry(root,width=30,font=19,textvar=Rollno)
entry_1.place(x=460,y=120)


label_2=Label(root,text=" Name :",width=8,font=("bold",15))
label_2.place(x=343,y=190)


entry_2=Entry(root,width=30,font=19,textvar=Name)
entry_2.place(x=458,y=192)
entry_2.configure(bg="white")


label_3=Label(root,text="Room No :",width=8,font=("bold",15))
label_3.place(x=343,y=260)

entry_3=Entry(root,width=30,font=12,textvar=Room_no)
entry_3.place(x=460,y=265)
entry_3.configure(bg="white")

label_6=Label(root,text="Gender :",width=8,font=("bold",15))
label_6.place(x=343,y=324)

list0=['FEMALE','MALE']

Gender=StringVar()
droplist=OptionMenu(root,Gender,*list0);
droplist.config(width=15,font=16)
Gender.set('select your Gender')              
droplist.place(x=460,y=324)


label_4=Label(root,text="     Size :",width=8,font=("bold",15))
label_4.place(x=342,y=400)

list1=['S','M','L'];
Size=StringVar()
droplist=OptionMenu(root,Size,*list1);
droplist.config(width=15,font=19)
Size.set('select your size')              
droplist.place(x=460,y=400)

label_5=Label(root,text="      Nos :",width=8,font=("bold",15))
label_5.place(x=342,y=470)

entry_5=Entry(root,width=30,font=12,textvar=No_of_t_shirts)
entry_5.place(x=460,y=476)
entry_5.configure(bg="white")

Button(root,text='Submit',width=15,font=("bold",20),bg='#4B0082',fg='white').place(x=420,y=560)
mainloop()
      




