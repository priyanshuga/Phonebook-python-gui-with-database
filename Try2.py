import sqlite3 as sql
import tkinter as tk
from tkinter import *
import sys

con=sql.connect('qna.db')
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS questions(question TEXT,opt1 TEXT,opt2 TEXT,opt3 TEXT,opt4 TEXT,answer INT)")
    cur.execute("DELETE FROM questions")
    cur.execute("INSERT INTO questions VALUES(?,?,?,?,?,?)",["What is the capital of india?","MUMBAI","NEW DELHI","CHENNAI","KOLKATA",int(2)])
    cur.execute("INSERT INTO questions VALUES(?,?,?,?,?,?)",["Which of the following is an indian brand?","Vedantu","HUL","Bata","Parag food",int(3)])
    con.commit()
    
def display():
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM questions")
        rows=cur.fetchall()
        for i in rows:
            row.append(i)
def setting_values():
    display()
    Label(win,text=row[i][0]).grid()
    Radiobutton(win,text=row[i][1],variable=var,value=1).grid(row=1,column=0)
    Radiobutton(win,text=row[i][2],variable=var,value=2).grid(row=1,column=1)
    Radiobutton(win,text=row[i][3],variable=var,value=3).grid(row=1,column=2)
    Radiobutton(win,text=row[i][4],variable=var,value=4).grid(row=1,column=3)
    Button(win,text='Submit',command=selection).grid(row=2,column=1)
def correct(i):
    new_win=tk.Toplevel(win)
    Label(new_win,text=row[i][0]).grid()
    Radiobutton(new_win,text=row[i][1],variable=var1,value=1).grid(row=1,column=0)
    Radiobutton(new_win,text=row[i][2],variable=var1,value=2).grid(row=1,column=1)
    Radiobutton(new_win,text=row[i][3],variable=var1,value=3).grid(row=1,column=2)
    Radiobutton(new_win,text=row[i][4],variable=var1,value=4).grid(row=1,column=3)
    Button(new_win,text='Submit',command=check).grid(row=2,column=1)
    new_win.mainloop()
def wrong():
    new_win=tk.Toplevel(win)
    Label(new_win,text="wrong answer").grid(row=0,column=0)
    new_win.mainloop()
def check():
    if(row[i+1][5]==var1.get()):
        correct(i+1)
    else:
        wrong()
def selection():
    if(row[i][5]==var.get()):
        correct(i+1)
    else:
        wrong()

win=tk.Tk()
row=[]
var=IntVar()
var1=IntVar()
i=int(0)
setting_values()
win.mainloop()
