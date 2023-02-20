from cgitb import text
from curses import window
from dataclasses import field
from fileinput import filename
from importlib.metadata import files
from os import close
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfile
from tkinter import filedialog as fd
from turtle import color
from xml.dom.pulldom import END_DOCUMENT

root=Tk()
root.title("Hello Alex")

#-----------------command-----------------------

def close_win():
    value=messagebox.askquestion("Close window", "Do you want to close the window?")
    #value=messagebox.askokcancel("Close window", "Do you want to close the window?") - true o false
    if value=="yes":
        root.destroy()
  
def saveFile():
    files=[("All files", "*.*")]
    file=asksaveasfile(filetypes=files, defaultextension=files)

def openFile():
    filename=askopenfilename(parent=root)
    f=open(filename)
    f.read

def newFile():
    try:   
        myConection=sqlite3.connect("DDBB new")
        myCursor=myConection.cursor()
        myCursor.execute('''
            CREATE TABLE USERS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR (50),
                Surname VARCHAR (50),
                Password VARCHAR (50),
                DoB VARCHAR (10),
                Comment VARCHAR (100))
        ''')
        myConection.commit()
        myConection.close()
        messagebox.showinfo("BBDD", "The data base is created")
    except:
        messagebox.showwarning("BBDD", "The data base already exists")
    
def create():
    myConection=sqlite3.connect("DDBB new")
    myCursor=myConection.cursor()
    datas=myName.get(),mySurname.get(),myPass.get(),myDoB.get(),screenComment.get("1.0", END)
    myCursor.execute("INSERT INTO USERS VALUES(NULL,?,?,?,?,?)",(datas))
    """myCursor.execute("INSERT INTO USERS VALUES(NULL, '" + myName.get() +
        "', '" + mySurname.get() +
        "', '" + myPass.get() + 
        "', '" + myDoB.get() + 
        "', '" + screenComment.get("1.0", END) + "')")"""
    myConection.commit()
    messagebox.showinfo("BBDD", "The user is created!")

def read():
    screenComment.delete(1.0, END)
    myConection=sqlite3.connect("DDBB new")
    myCursor=myConection.cursor()
    myCursor.execute("SELECT * FROM USERS WHERE ID=" + myID.get())
    theUser=myCursor.fetchall()
    for user in theUser:
        myID.set(user[0])
        myName.set(user[1])
        mySurname.set(user[2])
        myPass.set(user[3])
        myDoB.set(user[4])
        screenComment.insert(1.0, user[5])
    myConection.commit()

def update():
    myConection=sqlite3.connect("DDBB new")
    myCursor=myConection.cursor()
    datas=myName.get(),mySurname.get(),myPass.get(),myDoB.get(),screenComment.get("1.0", END)
    myCursor.execute("UPDATE USERS SET Name=?, Surname=?, Password=?,DoB=?,Comment=? " +
        "WHERE ID=" +myID.get(),(datas)) 
    """myCursor.execute("UPDATE USERS SET Name='" + myName.get() + 
                                "', Surname='" + mySurname.get() +
                                "', Password='" + myPass.get() +
                                "', DoB='" + myDoB.get() +
                                "', Comment='" + screenComment.get("1.0", END)+ 
                                "' WHERE ID=" +myID.get())"""

    myConection.commit()
    messagebox.showinfo("BBDD", "The DDBB is updated")

def deleteUser():
    myConection=sqlite3.connect("DDBB new")
    myCursor=myConection.cursor()
    myCursor.execute("DELETE FROM USERS WHERE ID=" + myID.get())
    myConection.commit()
    messagebox.showinfo("BBDD", "The user is deleted")

def del_text():
    myID.set("")
    myName.set("")
    mySurname.set("")
    myPass.set("")
    myDoB.set("")
    screenComment.delete(1.0, END)

def infoAditional():
    messagebox.showinfo("DDBB", "Created: June 2022, by Alex")

def warnLicencia():
    messagebox.showwarning("Licence", "The product is under HFGD licence")

#-----------------------------menu--------------------------

barraMenu=Menu(root)

root.config(menu=barraMenu, width=300, height=300)

fileMenu=Menu(barraMenu, tearoff=0)
editMenu=Menu(barraMenu, tearoff=0)
clearMenu=Menu(barraMenu, tearoff=0)
aboutMenu=Menu(barraMenu, tearoff=0)


barraMenu.add_cascade(label="Menu", menu=fileMenu)
barraMenu.add_cascade(label="Edit", menu=editMenu)
barraMenu.add_cascade(label="Clear", menu=clearMenu)
barraMenu.add_cascade(label="About", menu=aboutMenu)


fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Close", command=close_win)

editMenu.add_command(label="Create", command=create)
editMenu.add_command(label="Read", command=read)
editMenu.add_command(label="Update", command=update)
editMenu.add_command(label="Delete", command=deleteUser)

clearMenu.add_command(label="Clear", command=del_text)

aboutMenu.add_command(label="Licencies", command=warnLicencia)
aboutMenu.add_command(label="About", command=infoAditional)

#-----------------------pantalla------------------

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

myID=StringVar()
myName=StringVar()
mySurname=StringVar()
myPass=StringVar()
myDoB=StringVar()

screenID=Entry(miFrame, textvariable=myID)
screenID.grid(row=0, column=1, padx=10, pady=10)
screenID.config(fg="black", justify="right")

screenName=Entry(miFrame, textvariable=myName)
screenName.grid(row=1, column=1, padx=10, pady=10)
screenName.config(fg="black", justify="right")

screenSurname=Entry(miFrame, textvariable=mySurname)
screenSurname.grid(row=2, column=1, padx=10, pady=10)
screenSurname.config(fg="black", justify="right")

screenPass=Entry(miFrame, textvariable=myPass)
screenPass.grid(row=3, column=1, padx=10, pady=10)
screenPass.config(fg="black", justify="right", show="*")

screenDoB=Entry(miFrame, textvariable=myDoB)
screenDoB.grid(row=4, column=1, padx=10, pady=10)
screenDoB.config(fg="black", justify="right")

#screenComment=Entry(miFrame)
#screenComment.grid(row=5, column=1, padx=10, pady=10)
#screenComment.config(fg="black", justify="right")

screenComment=Text(miFrame, width=22, height=5)
screenComment.grid(row=5, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=screenComment.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")        #el scroll se mueve depende de la posicion del textos

screenComment.config(yscrollcommand=scrollVert.set)     #sticky="nset"-tenerlo del tamaño de la ventana

IDLabel=Label(miFrame, text="ID: ")
IDLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

NameLabel=Label(miFrame, text="Name: ")
NameLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

SurnameLabel=Label(miFrame, text="Surname: ")
SurnameLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

PassLabel=Label(miFrame, text="Password: ")
PassLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

DoBLabel=Label(miFrame, text="DoB: ")
DoBLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

CommentLabel=Label(miFrame, text="Comment: ")
CommentLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#----------------Buttons-------------------------------------
myFrame=Frame(root)
myFrame.pack()

buttonCreate=Button(myFrame, text="Create", command=create)
buttonCreate.grid(row=1, column=0, padx=5, pady=5)

buttonRead=Button(myFrame, text="Read", command=read)
buttonRead.grid(row=1, column=1, padx=5, pady=5)

buttonUpdate=Button(myFrame, text="Update", command=update)
buttonUpdate.grid(row=1, column=2, padx=5, pady=5)

buttonDelete=Button(myFrame, text="Delete", command=deleteUser)
buttonDelete.grid(row=1, column=3, padx=5, pady=5)
    
root.mainloop()