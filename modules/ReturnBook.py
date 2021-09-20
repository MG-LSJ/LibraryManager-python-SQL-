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


allBid = [] #Book IDs List
existBid = []

def rtn_check():
    file = open(r"counters\returnbook.txt","r")
    a = file.read()
    file.close()
    if a == "1":
        return True
    else:
        return False
    
def rtn_open():
    file = open(r"counters\returnbook.txt","a")
    file.write("1")
    file.close()

def rtn_close():
    file = open(r"counters\returnbook.txt","w")
    file.write("")
    file.close()

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()
    
    if bid == "":
        messagebox.showinfo("Caution","Please Enter a Book ID")
        root.destroy()
        returnBook()
        return
    
    else:

        extractIssueBid = "select bid from "+issueTable
        extractBid = "select bid from "+bookTable
        
        try:
            cur.execute(extractBid)
            con.commit()
            for j in cur:
                existBid.append(j[0])
            
            cur.execute(extractIssueBid)
            con.commit()            
            for i in cur:
                allBid.append(i[0])
            
            if bid in allBid and bid in existBid:
                checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
                cur.execute(checkAvail)
                con.commit()
                for i in cur:
                    check = i[0]
                        
                if check == 'issued':
                            issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"
                            updateStatus = "update "+bookTable+" set status = 'avail' where bid = '"+bid+"'"
                            cur.execute(issueSql)
                            con.commit()
                            cur.execute(updateStatus)
                            con.commit()
                            messagebox.showinfo('Success',"Book Returned Successfully")
                        
                else:
                    messagebox.showinfo('Database Manupulated',"Book isn't issued but value exist in Issue Table")
                    print("e1")
                    pass
                        
                existBid.clear()
                allBid.clear()
                root.destroy()
                rtn_close()

            elif bid in existBid:
                messagebox.showinfo("Caution","Book is not issued")
                allBid.clear()
                existBid.clear()
                root.destroy()
                returnBook()
                return       
                    
            else:
                messagebox.showinfo("Caution","Book ID does not exist in Database")
                allBid.clear()
                existBid.clear()
                root.destroy()
                returnBook()
                return       
        except:
            messagebox.showinfo("Error","Can't fetch Book IDs") 
            existBid.clear()
            allBid.clear()
            root.destroy()
            returnBook()
                  
    
def returnBook(): 
    
    if rtn_check() == True:
    
        global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
        
        root = Tk()
        root.title("Return Book AVBIL LM")
        root.iconbitmap("media\logo.ico")
        root.minsize(width = 400, height = 400)
        root.geometry("500x400")
    
        
        Canvas1 = Canvas(root)
        
        Canvas1.config(bg = "#161616")
        Canvas1.pack(expand = True,fill = BOTH)
            
        headingFrame1 = Frame(root, bg = "#006B38", bd = 5)
        headingFrame1.place(relx = 0.25,rely = 0.1, relwidth = 0.5, relheight = 0.13)
            
        headingLabel = Label(headingFrame1, text = "Return Book", bg = '#121212', fg = 'white', font = ('Segoe UI',20))
        headingLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
        labelFrame = Frame(root, bg = '#121212')
        labelFrame.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.2)   
            
        # Book ID to Delete
        lb1 = Label(labelFrame, text = "Book ID : ", bg = '#121212', fg = 'white', font = ('Segoe UI',))
        lb1.place(relx = 0.05, rely = 0.4)
            
        bookInfo1 = Entry(labelFrame)
        bookInfo1.place(relx = 0.3, rely = 0.4, relwidth = 0.62)
        
        #Submit Button
        SubmitBtn = Button(root, text = "RETURN", bg = '#121212', fg = 'white', font = ('Segoe UI',12), command = lambda:[click(),returnn()])
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
        backBtn = Button(root,text="CANCEL",bg='#121212', fg='white', font=('Segoe UI',12), command = lambda:[click(), rtn_close(),root.destroy()])
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