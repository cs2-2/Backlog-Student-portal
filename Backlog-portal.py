import sqlite3
import sys
import os
import re

conn = sqlite3.connect('backlog.db')
c = conn.cursor()
#c.execute("CREATE TABLE learner(NAME text,YEAR text,DEPARTMENT text ,EMAIL text,PHONE integer,  COURSE text)")
#c.execute("CREATE TABLE tutor(NAME TEXT,EMAIL TEXT,PHONE INTEGER,  COURSE TEXT,TEACHER TEXT)")
class toption:

    def t_insert(self):

        t_name = input("enter the name of tutor")
        t_email = input("enter the email")
        t_cell = input("enter the cell phone no")
        t_course = input("enter the course you wnat to teach")
        t_trainer = input('enter the teacher name fram whom you studied')
        c.execute(
            "INSERT INTO tutor(NAME,EMAIL,PHONE,COURSE,TEACHER) VALUES(?,?,?,?,?)",
            (t_name,t_email,t_cell,t_course,t_trainer))
        conn.commit()
        print("data entered")
        c.close()
        conn.close()

    def t_display(self):
            c.execute("SELECT * FROM tutor")
            print(c.fetchall())
            conn.commit()
            c.close()
            conn.close()

class tutor:


    def __init__(self):
        self.tput = toption()
        self.tsee = toption()
        self.tlook = toption()

    def teacher(self):
        print('''TUTOR INFORMATION
        1-INSERT TUTOR
        2-DISPLAY TUTOR
        3-SEARCH STUDENT BY course NAME''')
        another=input("enter your choice")
        if(another == '1'):
            self.tput.t_insert()
        elif(another == '2'):
            self.tsee.t_display()
        elif(another == '3'):
            self.tlook.t_search()
        else:
            print("invalid selection")

class soption:

    def insert(self):

        print("Enter the name of student")
        name=(input())
        year=input("Enter the class of student")
        department=input("Enter the name of department")
        email=input("enter your email")
        cell=input("enter your cell number")
        course=input("enter the you want to pick in backlog")
        c.execute("INSERT INTO learner(NAME,YEAR,DEPARTMENT,EMAIL,PHONE,COURSE) VALUES(?,?,?,?,?,?)",
                  (name,year,department,email,cell,course))
        conn.commit()
        print("data entered")
        c.close()
        conn.close()

    def display(self):
        c.execute("SELECT * FROM learner")
        print(c.fetchall())
        conn.commit()
        c.close()
        conn.close()
    def search(self):
        print("enter the course name through which you find a relevant tutors")
        ssubj=input()
        c.execute("SELECT * from tutor WHERE COURSE=?",(ssubj,))
        print(c.fetchall())
        conn.commit()
        c.close()
        conn.close()




class Learner:
    c = conn.cursor()

    def __init__(self):

        self.put = soption()
        self.see = soption()
        self.look = soption()


    def student(self):
            print('''STUDENT INFORMATION 
                1-INSERT STUDENT
                2-DISPLAY STUDENT
                3-SEARCH FOR TUTOR BY COURSE NAME''')
            ch=input("ENTER YOUR SELECTION")
            if(ch=='1'):
                self.put.insert()
            elif(ch=='2'):
                print("display")
                self.see.display()
            elif(ch=='3'):
                print("search")
                self.look.search()
            elif(ch=='4'):
                print("menu")
                self.menul.menu()
            else:
                print("invalidselection")

class Admin:

    def __init__(self):
        self.sa = Learner()
        self.ta = tutor()

    def menu(self):

        print('''BACKLOG STUDENT PORTAL
                1-student
                2=tutor
                3-menu
                4-exit''')
        choice = input("enter the choice")
        if(choice=='1'):
            self.sa.student()
        elif(choice=='2'):
            self.ta.teacher()


aa= Admin()
aa.menu()










