from tkinter import *
from tkinter import messagebox
from subprocess import call
 
root = Tk()
root.title("Main")
root.geometry("500x500")
global e1
global e2
 
def Ok():
    call(["python", "AddStudent.py"])
 
Label(root, text="Welcome").place(x=10, y=10)
Button(root, text="Add Student", command=Ok, height= 3, width= 12).place(x=10,y=100)
 
 
root.mainloop()
