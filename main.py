from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox,ttk

from modules.AddBook import *
from modules.DeleteBook import *
from modules.ViewBooks import *
from modules.Sounds import click
from modules.IssueBook import *
from modules.ReturnBook import *

root = Tk()

root.title("Library Manager AVBIL")
root.minsize(848, 480)
root.iconbitmap("media\logo.ico")


img = ImageTk.PhotoImage(Image.open("media\lib.png"))
Canvas = Canvas(root, width = 960, height = 540)     
Canvas.pack(fill = BOTH, expand = True)
Canvas.create_image(0,0,image = img, anchor="nw") 

headingFrame1 = Frame(root, bg = "#2F2F87", bd = 5)
headingFrame1.place(relx = 0.2, rely = 0.1, relwidth = 0.6, relheight = 0.16)
headingLabel = Label(headingFrame1, text="AVBIL Library Manager", bg='#121212', fg='white', font=('Segoe UI',30))
headingLabel.place(relx = 0, rely = 0, relwidth = 1, relheight =1)

status_label = Label(root, text = "Made by Lakshyajeet Jalal and Sagar Giri ", bg = "#121212", fg = "white", relief = SUNKEN, font = ('Segoe UI',10), anchor = E)
status_label.pack(fill = X, side = BOTTOM, ipady = 2)

#Button 1
btn1 = Button(root, text = "Add Book", bg = '#121212', fg = 'white', font=('Segoe UI',20), command = lambda:[click(),add_open(),addBook()])
btn1.place(relx = 0.28, rely = 0.4, relwidth = 0.45, relheight = 0.09)

def btn1_hoverin(event):
    btn1["bg"] = "#222222"
    btn1["font"]= 'Segoe UI',22
    status_label.config(text = "Click To Add Book ")
    
def btn1_hoverout(event):
    btn1["bg"] = "#121212"
    btn1["font"]= 'Segoe UI',20
    status_label.config(text = "Made by Lakshyajeet Jalal and Sagar Giri ")
    
btn1.bind("<Enter>", btn1_hoverin)
btn1.bind("<Leave>", btn1_hoverout)

#Button 2
btn2 = Button(root, text= "Delete Book", bg = '#121212', fg = 'white', font=('Segoe UI',20), command = lambda:[click(), del_open(),delete()])
btn2.place(relx = 0.28, rely = 0.5, relwidth = 0.45, relheight = 0.09)

def btn2_hoverin(event):
    btn2["bg"] = "#222222"
    btn2["font"]= 'Segoe UI',22
    status_label.config(text = "Click To Delete Book ")
    
def btn2_hoverout(event):
    btn2["bg"] = "#121212"
    btn2["font"]= 'Segoe UI',20
    status_label.config(text = "Made by Lakshyajeet Jalal and Sagar Giri ")
    
btn2.bind("<Enter>", btn2_hoverin)
btn2.bind("<Leave>", btn2_hoverout)

#Button 3    
btn3 = Button(root, text= "View Book List", bg = '#121212', fg = 'white', font=('Segoe UI',20), command = lambda:[click(), view_open(), View()])
btn3.place(relx = 0.28, rely= 0.6, relwidth = 0.45,relheight = 0.09)
  
def btn3_hoverin(event):
    btn3["bg"] = "#222222"
    btn3["font"]= 'Segoe UI',22
    status_label.config(text = "Click To View Book List ")
    
def btn3_hoverout(event):
    btn3["bg"] = "#121212"
    btn3["font"]= 'Segoe UI',20
    status_label.config(text = "Made by Lakshyajeet Jalal and Sagar Giri ")
    
btn3.bind("<Enter>", btn3_hoverin)
btn3.bind("<Leave>", btn3_hoverout)

#Button 4  
btn4 = Button(root, text= "Issue Book", bg = '#121212', fg = 'white', font=('Segoe UI',20), command = lambda:[click(), issue_open(), issueBook()])
btn4.place(relx = 0.28, rely= 0.7, relwidth = 0.45,relheight = 0.09)

def btn4_hoverin(event):
    btn4["bg"] = "#222222"
    btn4["font"]= 'Segoe UI',22
    status_label.config(text = "Click To Issue Book ")
    
def btn4_hoverout(event):
    btn4["bg"] = "#121212"
    btn4["font"]= 'Segoe UI',20
    status_label.config(text = "Made by Lakshyajeet Jalal and Sagar Giri ")
    
btn4.bind("<Enter>", btn4_hoverin)
btn4.bind("<Leave>", btn4_hoverout)

#Button 5   
btn5 = Button(root, text= "Return Book", bg= '#121212', fg = 'white', font=('Segoe UI',20), command = lambda:[click(), rtn_open(), returnBook()])
btn5.place(relx = 0.28, rely= 0.8, relwidth = 0.45,relheight = 0.09) 

def btn5_hoverin(event):
    btn5["bg"] = "#222222"
    btn5["font"]= 'Segoe UI',22
    status_label.config(text = "Click To Return Book ")
    
def btn5_hoverout(event):
    btn5["bg"] = "#121212"
    btn5["font"]= 'Segoe UI',20
    status_label.config(text = "Made by Lakshyajeet Jalal and Sagar Giri ")
    
btn5.bind("<Enter>", btn5_hoverin)
btn5.bind("<Leave>", btn5_hoverout)

root.mainloop()
