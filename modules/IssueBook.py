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

def issue_check():
    file = open(r"counters\deletebook.txt","r")
    a = file.read()
    file.close()
    if a == "1":
        return True
    else:
        return False
    
def issue_open():
    file = open(r"counters\deletebook.txt","a")
    file.write("1")
    file.close()

def issue_close():
    file = open(r"counters\deletebook.txt","w")
    file.write("")
    file.close()
    
#Book IDs List
allBid = [] 

def issue():
    
    global root
    
    bid = inf1.get()
    issuedto = inf2.get()

    
    if bid == "" and issuedto =="":
        messagebox.showinfo("Caution","All fields must be filled")
        root.destroy()
        issueBook()
        return
    else:
        extractBid = "select bid from "+bookTable
        try:
            cur.execute(extractBid)
            con.commit()
            for i in cur:
                allBid.append(i[0])
        
            if bid in allBid:
                checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
                cur.execute(checkAvail)
                con.commit()
                for i in cur:
                    check = i[0]
                
                if check == 'avail':
                    status = True
                else:
                    status = False

            else:
                messagebox.showinfo("Caution","Book ID not present")
                root.destroy()
                issueBook()
                return
            
        except:
            messagebox.showinfo("Error","Unable to fetch Book IDs")
    
        issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issuedto+"')"
        show = "select issuedto from "+issueTable+" where bid = '"+bid+"'"
    
        updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
        try:
            if bid in allBid and status == True:
                cur.execute(issueSql)
                con.commit()
                cur.execute(updateStatus)
                con.commit()
                messagebox.showinfo('Success',"Book Issued Successfully to "+issuedto)
                allBid.clear()
                root.destroy()
                issue_close()
            else:
                cur.execute(show)
                con.commit()
                a = cur.fetchone()
                allBid.clear()
                messagebox.showinfo('Caution',"Book Already Issued to "+a[0])
                root.destroy()
                issueBook()
                return
        except:
            messagebox.showinfo("Error","Book ID not found, Try again")
            allBid.clear()
            root.destroy()
            issueBook()
    
def issueBook(): 
    
    if issue_check() == True:
    
        global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
        
        root = Tk()
        root.title("Issue Book AVBIL LM")
        root.iconbitmap("media\logo.ico")
        root.minsize(width = 400, height = 400)
        root.geometry("500x400")
        
        Canvas1 = Canvas(root)
        Canvas1.config(bg = "#161616")
        Canvas1.pack(expand = True, fill = BOTH)
    
        headingFrame1 = Frame(root,bg="#D6ED17",bd=5)
        headingFrame1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)
            
        headingLabel = Label(headingFrame1, text = "Issue Book", bg = '#121212', fg = 'white', font = ('Segoe UI',20))
        headingLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
        labelFrame = Frame(root,bg='#121212')
        labelFrame.place(relx = 0.1,rely = 0.3, relwidth = 0.8, relheight = 0.2)  
            
        # Book ID
        lb1 = Label(labelFrame,text = "Book ID : ", bg = '#121212', fg = 'white', font = ('Segoe UI',))
        lb1.place(relx = 0.05,rely = 0.2)
            
        inf1 = Entry(labelFrame)
        inf1.place(relx = 0.3, rely = 0.25, relwidth = 0.62)
        
        # Student name 
        lb2 = Label(labelFrame, text = "Issued To : ", bg = '#121212', fg = 'white', font = ('Segoe UI',))
        lb2.place(relx = 0.05, rely = 0.5)
            
        inf2 = Entry(labelFrame)
        inf2.place(relx = 0.3, rely = 0.55, relwidth = 0.62)
            
        #Issue Button
        issueBtn = Button(root, text = "ISSUE", bg = '#121212', fg ='white', font = ('Segoe UI',12),command = lambda:[click(),issue()])
        issueBtn.place(relx = 0.26, rely = 0.85, relwidth = 0.2, relheight = 0.1)
    
        def issueBtn_hoverin(event):
            issueBtn["bg"] = "#222222"
            issueBtn["font"]= 'Segoe UI',15
        
        def issueBtn_hoverout(event):
            issueBtn["bg"] = "#121212"
            issueBtn["font"]= 'Segoe UI',12
        
        issueBtn.bind("<Enter>", issueBtn_hoverin)
        issueBtn.bind("<Leave>", issueBtn_hoverout)  
        
        #Back Button
        backBtn = Button(root,text="CANCEL",bg='#121212', fg='white', font=('Segoe UI',12), command = lambda:[click(), issue_close(), root.destroy()])
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