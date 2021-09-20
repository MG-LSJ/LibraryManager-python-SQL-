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

def add_check():
    file = open(r"counters\addbook.txt","r")
    a = file.read()
    file.close()
    if a == "1":
        return True
    else:
        return False
    
def add_open():
    file = open(r"counters\addbook.txt","a")
    file.write("1")
    file.close()

def add_close():
    file = open(r"counters\addbook.txt","w")
    file.write("")
    file.close()

def issue():
    
    global root
    bid = bookInfo1.get()
    issuedto = bookInfo5.get()
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issuedto+"')"
    
    try:
        cur.execute(issueSql)
        con.commit()
        messagebox.showinfo('Success',"Book Issued Successfully to "+issuedto)
 
    except:
        messagebox.showinfo("Error","Failed to Issue Book/nPlease Issue Manually")
        allBid.clear()
        root.destroy()
        
        
    
    print(bid)
    print(issuedto)
    
def bookRegister():
    
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    if bid == "" and title == "" and author == "" and status == "":
        messagebox.showinfo("Caution","All fields must be filled")
        root.destroy()
        addBook()
        return
    
    else:
        if status in ["avail","issued"]:
            insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
            try:
                cur.execute(insertBooks)
                con.commit()
                messagebox.showinfo('Success',"Book named "+title+" added successfully")
                
                if status == "issued":
                    issue()
                
                root.destroy()
                add_close()
                    
            except:
                messagebox.showinfo("Error","Can't add data into Database")
                root.destroy()
                addBook()


        else:
            messagebox.showinfo("Caution","Unknown Status")
            root.destroy()
            addBook()
            
    
def addBook():
    
    if add_check() == True:

        global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,Canvas1,root
    
        root = Tk()
        root.title("Add Book AVBIL LM")
        root.iconbitmap("media\logo.ico")
        root.minsize(width=400,height=400)
        root.geometry("600x500")


        Canvas1 = Canvas(root)
        
        Canvas1.config(bg="#161616")
        Canvas1.pack(expand=True,fill=BOTH)
        
        headingFrame1 = Frame(root,bg="#ff6e40",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

        headingLabel = Label(headingFrame1, text="Add Book", bg='#121212', fg='white', font=('Segoe UI',20))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


        labelFrame = Frame(root,bg='#121212')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
        # Book ID
        lb1 = Label(labelFrame,text="Book ID : ", bg='#121212', fg='white', font=('Segoe UI',))
        lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
        bookInfo1 = Entry(labelFrame)
        bookInfo1.place(relx=0.4,rely=0.2, relwidth=0.52, relheight=0.08)
        
        # Title
        lb2 = Label(labelFrame,text="Title : ", bg='#121212', fg='white', font=('Segoe UI',))
        lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
        bookInfo2 = Entry(labelFrame)
        bookInfo2.place(relx=0.4,rely=0.35, relwidth=0.52, relheight=0.08)
        
        # Book Author
        lb3 = Label(labelFrame,text="Author : ", bg='#121212', fg='white', font=('Segoe UI',))
        lb3.place(relx=0.05,rely=0.50, relheight=0.08)
            
        bookInfo3 = Entry(labelFrame)
        bookInfo3.place(relx=0.4,rely=0.50, relwidth=0.52, relheight=0.08)
        
        # Book Status
        lb4 = Label(labelFrame,text="Status(Avail/Issued) : ", bg='#121212', fg='white', font=('Segoe UI',))
        lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
        bookInfo4 = Entry(labelFrame)
        bookInfo4.place(relx=0.4,rely=0.65, relwidth=0.52, relheight=0.08)
    
        lb5 = Label(labelFrame,text="(If) Issued to : ", bg='#121212', fg='white', font=('Segoe UI',))
        lb5.place(relx=0.05,rely=0.8, relheight=0.08)
        
        bookInfo5 = Entry(labelFrame)
        bookInfo5.place(relx=0.4,rely=0.8, relwidth=0.52, relheight=0.08)
        
        # Add Button
        SubmitBtn = Button(root,text="ADD",bg='#121212', fg='white', font=('Segoe UI',12),command = lambda:[click(),bookRegister()])
        SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
        def SubmitBtn_hoverin(event):
            SubmitBtn["bg"] = "#222222"
            SubmitBtn["font"]= 'Segoe UI',15
    
        def SubmitBtn_hoverout(event):
            SubmitBtn["bg"] = "#121212"
            SubmitBtn["font"]= 'Segoe UI',12
    
        SubmitBtn.bind("<Enter>", SubmitBtn_hoverin)
        SubmitBtn.bind("<Leave>", SubmitBtn_hoverout)
    
        #Back Button
        backBtn = Button(root,text="CANCEL",bg='#121212', fg='white', font=('Segoe UI',12), command = lambda:[click(),add_close(),root.destroy()])
        backBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

        def backBtn_hoverin(event):
            backBtn["bg"] = "#222222"
            backBtn["font"]= 'Segoe UI',15
    
        def backBtn_hoverout(event):
            backBtn["bg"] = "#121212"
            backBtn["font"]= 'Segoe UI',12
    
        backBtn.bind("<Enter>", backBtn_hoverin)
        backBtn.bind("<Leave>", backBtn_hoverout) 
    
        root.mainloop()