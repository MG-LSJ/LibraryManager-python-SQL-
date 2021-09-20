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

def del_check():
    file = open(r"counters\deletebook.txt","r")
    a = file.read()
    file.close()
    if a == "1":
        return True
    else:
        return False
    
def del_open():
    file = open(r"counters\deletebook.txt","a")
    file.write("1")
    file.close()

def del_close():
    file = open(r"counters\deletebook.txt","w")
    file.write("")
    file.close()

def deleteBook():
    
    bid = bookInfo1.get()
    
    if bid == "":
        messagebox.showinfo('Caution',"Book ID can't be empty")
        root.destroy()
        delete()
        return
    else:
        
        deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
        deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
        try:
            cur.execute(deleteSql)
            con.commit()
            cur.execute(deleteIssue)
            con.commit()
            messagebox.showinfo('Success',"Book Record Deleted Successfully")
            
            bookInfo1.delete(0, END)
            root.destroy()
            del_close()
        
        except:
            messagebox.showinfo("Please check Book ID")
            bookInfo1.delete(0, END)
            root.destroy()
            delete()

    
def delete(): 
    
    if del_check() == True:
    
        global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
        
        root = Tk()
        root.title("Delete Books AVBIL LM")
        root.iconbitmap("media\logo.ico")
        root.minsize(width = 200, height = 200)
        root.geometry("500x400")
    
        
        Canvas1 = Canvas(root)
        
        Canvas1.config(bg = "#161616")
        Canvas1.pack(expand = True, fill = BOTH)
            
        headingFrame1 = Frame(root, bg = "#006B38",bd = 5)
        headingFrame1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)
            
        headingLabel = Label(headingFrame1, text = "Delete Book", bg= '#121212', fg = 'white', font = ('Segoe UI', 20))
        headingLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
        labelFrame = Frame(root, bg = '#121212')
        labelFrame.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.2)   
            
        # Book ID
        lb2 = Label(labelFrame, text = "Book ID : ", bg = '#121212', fg = 'white', font = ('Segoe UI',))
        lb2.place(relx = 0.05, rely = 0.4)
            
        bookInfo1 = Entry(labelFrame)
        bookInfo1.place(relx = 0.3, rely = 0.4, relwidth  = 0.62)
        
        # Delete Button
        SubmitBtn = Button(root,text = "DELETE",bg = '#121212', fg = 'white', font = ('Segoe UI',12), command = lambda:[click(),deleteBook()])
        SubmitBtn.place(relx = 0.26, rely = 0.85, relwidth = 0.2, relheight = 0.1)
        
        def SubmitBtn_hoverin(event):
            SubmitBtn["bg"] = "#222222"
            SubmitBtn["font"]= 'Segoe UI',15
        
        def SubmitBtn_hoverout(event):
            SubmitBtn["bg"] = "#121212"
            SubmitBtn["font"]= 'Segoe UI',12
        
        SubmitBtn.bind("<Enter>", SubmitBtn_hoverin)
        SubmitBtn.bind("<Leave>", SubmitBtn_hoverout)  
        
        #Back Button
        backBtn = Button(root,text="CANCEL",bg='#121212', fg='white', font=('Segoe UI',12), command = lambda:[click(), del_close(),root.destroy()])
        backBtn.place(relx = 0.55, rely = 0.85, relwidth = 0.2, relheight = 0.1)
    
        def backBtn_hoverin(event):
            backBtn["bg"] = "#222222"
            backBtn["font"]= 'Segoe UI',15
        
        def backBtn_hoverout(event):
            backBtn["bg"] = "#121212"
            backBtn["font"]= 'Segoe UI',12
        
        backBtn.bind("<Enter>", backBtn_hoverin)
        backBtn.bind("<Leave>", backBtn_hoverout) 
        
        root.mainloop()