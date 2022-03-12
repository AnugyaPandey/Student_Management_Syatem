import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['studname'])
    e2.insert(0,select['email_id'])
    e3.insert(0,select['college'])
    e4.insert(0,select['contact'])


def Add():
    studname = e1.get()
    email_id = e2.get()
    college = e3.get()
    contact = e4.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="student_management")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  student (studname,email_id,college,contact) VALUES (%s, %s, %s, %s)"
       val = (studname,email_id,college,contact)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Student information inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e4.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


def update():
    studname = e1.get()
    email_id = e2.get()
    college = e3.get()
    contact = e4.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="student_management")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  student set studname= %s,email_id= %s,college= %s where contact= %s"
       val = (studname,email_id,college,contact)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e4.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    studname = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="student_management")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from student where studname = %s"
       val = (studname,email_id,college,contact)
       mycursor.execute(sql, val)
       mysqldb.commit()
       laststudname = mycursor.lastrowstudname
       messagebox.showinfo("information", "Record Deleted successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e4.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="student_management")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT studname,email_id,college,contact FROM student")
        records = mycursor.fetchall()
        print(records)

        for i, (studname,email_id,college,contact) in enumerate(records  , start=1):
            listBox.insert("", "end", values=(studname,email_id,college,contact))
            mysqldb.close()

root = tk.Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root, text="Student Mangement System", fg="blue", font=("Arial",25,"bold")).place(x=300, y=10)


tk.Label(root, text="Name").place(x=10, y=10)
Label(root, text="Email-id").place(x=10, y=40)
Label(root, text="College").place(x=10, y=70)
Label(root, text="Contact").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)

cols = ('studname','email_id','college','contact')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()
