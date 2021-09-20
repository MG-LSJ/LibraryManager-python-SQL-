from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from modules.Sounds import click

with open("Credentials.txt", "r") as file:
        
    mysql_host = file.readline()
    mysql_host = mysql_host.strip("\n")
        
    mysql_user = file.readline()
    mysql_user = mysql_user.strip("\n")
        
    mysql_pass = file.readline()
    mysql_pass = mysql_pass.strip("\n")
        
    mysql_db = file.readline()
    
    file.close()

con = pymysql.connect(host = mysql_host, user = mysql_user, password = mysql_pass, database = mysql_db)
cur = con.cursor()

bookTable = "books"
issueTable = "books_issued"

def view_check():
    file = open(r"counters\viewbook.txt","r")
    a = file.read()
    file.close()
    if a == "1":
        return True
    else:
        return False
    
def view_open():
    file = open(r"counters\viewbook.txt","a")
    file.write("1")
    file.close()

def view_close():
    file = open(r"counters\viewbook.txt","w")
    file.write("")
    file.close()
    
def View(): 
    
    if view_check() == True:
    
        root = Tk()
        root.title("View Books AVBIL LM")
        root.iconbitmap("media\logo.ico")
        root.minsize(width=500,height=400)
        root.geometry("600x500")
    
    
        Canvas1 = Canvas(root) 
        Canvas1.config(bg="#161616")
        Canvas1.pack(expand=True,fill=BOTH)
            
            
        headingFrame1 = Frame(root,bg="#12a4d9",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            
        headingLabel = Label(headingFrame1, text="View Books", bg='#121212', fg='white', font=('Segoe UI',20))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        
        labelFrame = Frame(root,bg='#121212')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
        y = 0.25
        
        Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),bg='#121212',fg='white').place(relx=0.07,rely=0.1)
        Label(labelFrame, text="----------------------------------------------------------------------------",bg='#121212',fg='white').place(relx=0.05,rely=0.2)
        getBooks = "select * from "+bookTable
        try:
            cur.execute(getBooks)
            con.commit()
            for i in cur:
                Label(labelFrame, text="%-10s%-40s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='#121212',fg='white').place(relx=0.07,rely=y)
                y += 0.1
        except:
            messagebox.showinfo("Failed to fetch files from database")
        
    
    
        #Back Button
        backBtn = Button(root,text="BACK",bg='#121212', fg='white', font=('Segoe UI',12), command = lambda:[click(),view_close(),root.destroy()])
        backBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
        def backBtn_hoverin(event):
            backBtn["bg"] = "#222222"
            backBtn["font"]= 'Segoe UI',15
        
        def backBtn_hoverout(event):
            backBtn["bg"] = "#121212"
            backBtn["font"]= 'Segoe UI',12
        
        backBtn.bind("<Enter>", backBtn_hoverin)
        backBtn.bind("<Leave>", backBtn_hoverout) 
        
        root.mainloop()