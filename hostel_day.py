
from tkinter import *
import sqlite3
root=Tk()
root.title("Registration for Hostel Day")

Name=StringVar()
Rollno=StringVar()
var=StringVar()
No_of_tokens=StringVar()
No_of_veg_tokens=StringVar()
No_of_Non_veg_tokens=StringVar()
def database():
    name1=Name.get()
    r_no=Rollno.get()
    gender=var.get()
    n_tokens=No_of_tokens.get()
    v_tokens=No_of_veg_tokens.get()
    n_veg_tokens=No_of_Non_veg_tokens.get()
    amount=10000
    veg_cost=600
    non_veg_cost=650
    if int(n_tokens)==(int(v_tokens)+int(n_veg_tokens)):
        c=(int(v_tokens)*veg_cost)+(int(n_veg_tokens)*non_veg_cost)
    else:
        print("YOUR REQUEST IS INVALID")
    if c<amount:
        r=amount-c
        s=str(r)
    else:
        print("YOU ARE NOT HAVING SUGGICIENT AMOUNT")
    conn=sqlite3.connect("Hostel_day_9.db")
    with conn:
        cursor=conn.cursor()
       
    cursor.execute('CREATE TABLE IF NOT EXISTS hostel_day (Name TEXT,Rollno TEXT,Gender Text,Initial_amt TEXT,No_of_tokens TEXT,No_of_veg_tokens TEXT,No_of_Non_veg_tokens TEXT, Remaining_cost TEXT,Token_id TEXT)')
    for i in range(0,int(n_tokens)):
        cursor.execute('INSERT INTO hostel_day (Name,Rollno,Gender,Initial_amt,No_of_tokens,No_of_veg_tokens,No_of_Non_veg_tokens,Remaining_cost,Token_id)VALUES (?,?,?,?,?,?,?,?,?)',(name1,r_no,gender,amount,n_tokens,v_tokens,n_veg_tokens,s,r_no))
        conn.commit()
                     
label_0 =Label(root,text="Registration for Hostel Day",width=20,font=("bold",20))
label_0.place(x=90,y=53)

label_1 =Label(root,text="Name",width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1=Entry(root,textvar=Name)
entry_1.place(x=240,y=130)

label_2=Label(root,text="Rollno",width=20,font=("bold",10))
label_2.place(x=80,y=180)

entry_2=Entry(root,textvar=Rollno)
entry_2.place(x=240,y=180)


label_3=Label(root,text="Gender",width=20,font=("bold",10))
label_3.place(x=80,y=230)

list0=['Female','Male']

droplist=OptionMenu(root,var,*list0)
droplist.config(width=25)
var.set('select your gender')
droplist.place(x=240,y=230)


label_4=Label(root,text="No_of_tokens",width=20,font=("bold",10))
label_4.place(x=70,y=290)

entry_4=Entry(root,textvar=No_of_tokens)
entry_4.place(x=240,y=290)


label_5=Label(root,text="No_of_veg_tokens",width=20,font=("bold",10))
label_5.place(x=70,y=360)

entry_5=Entry(root,textvar=No_of_veg_tokens)
entry_5.place(x=240,y=360)

label_6=Label(root,text="No_of_Non_veg_tokens",width=20,font=("bold",10))
label_6.place(x=70,y=430)

entry_6=Entry(root,textvar=No_of_Non_veg_tokens)

entry_6.place(x=240,y=430)


Button(root,text='Submit',width=20,bg='brown',fg='white',command=database).place(x=170,y=500)
root=Tk()
Rollno1=StringVar()
def gettoken():
    ro_no=Rollno1.get()
    conn=sqlite3.connect("Hostel_day_9.db")
    with conn:
        cursor=conn.cursor()
    cursor.execute("SELECT Name,Rollno,Gender,Token_id FROM hostel_day WHERE Rollno='$ro_no' ")
    rows=cursor.fetchall()
    for row in rows:
        print(row)


label_0 =Label(root,text="Rollno1",width=20,font=("bold",10))
label_0.place(x=80,y=130)

entry_0=Entry(root,textvar=Rollno1)
entry_0.place(x=240,y=130)

Button(root,text='Submit',width=20,bg='brown',fg='white',command=gettoken).place(x=160,y=200)                   
root.mainloop()                   
                   








