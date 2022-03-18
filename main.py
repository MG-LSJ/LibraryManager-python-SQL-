from tkinter import *
import PIL.Image, PIL.ImageTk

from modules.AddBook import *
from modules.DeleteBook import *
from modules.ViewBooks import *
from modules.Sounds import click
from modules.IssueBook import *
from modules.ReturnBook import *
from modules.Credentials import *

if check_cred():

    # Check clear
    add_close()
    del_close()
    issue_close()
    rtn_close()
    view_close()

    root = Tk()

    root.title("Library Manager AVBIL")
    root.minsize(848, 480)
    root.iconbitmap("media\logo.ico")

    img = PIL.ImageTk.PhotoImage(PIL.Image.open("media\lib.png"))
    Canvas = Canvas(root, width=960, height=540)
    Canvas.pack(fill=BOTH, expand=True)
    Canvas.create_image(0, 0, image=img, anchor="nw")

    # Heading Frame
    headingFrame1 = Frame(root, bg="#2F2F87", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    # Heading Label
    headingLabel = Label(
        headingFrame1,
        text="AVBIL Library Manager",
        bg="#121212",
        fg="white",
        font=("Segoe UI", 30),
    )
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Status Label
    status_label = Label(
        root,
        text="Made by Lakshyajeet Jalal and Sagar Giri ",
        bg="#121212",
        fg="white",
        relief=SUNKEN,
        font=("Segoe UI", 10),
        anchor=E,
    )
    status_label.pack(fill=X, side=BOTTOM, ipady=2)

    # Status Label reset
    def status_label_rst():
        status_label.config(text="Made by Lakshyajeet Jalal and Sagar Giri ")

    # addBook Button
    addBookBtn = Button(
        root,
        text="Add Book",
        bg="#121212",
        fg="white",
        font=("Segoe UI", 20),
        command=lambda: [click(), add_open(), addBookWin()],
    )
    addBookBtn.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.09)

    def addBookBtn_hoverin(event):
        addBookBtn["bg"] = "#222222"
        addBookBtn["font"] = "Segoe UI", 22
        status_label.config(text="Click To Add Book ")

    def addBookBtn_hoverout(event):
        addBookBtn["bg"] = "#121212"
        addBookBtn["font"] = "Segoe UI", 20
        status_label_rst()

    addBookBtn.bind("<Enter>", addBookBtn_hoverin)
    addBookBtn.bind("<Leave>", addBookBtn_hoverout)

    # delBook Button
    delBookBtn = Button(
        root,
        text="Delete Book",
        bg="#121212",
        fg="white",
        font=("Segoe UI", 20),
        command=lambda: [click(), del_open(), deleteBookWin()],
    )
    delBookBtn.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.09)

    def delBookBtn_hoverin(event):
        delBookBtn["bg"] = "#222222"
        delBookBtn["font"] = "Segoe UI", 22
        status_label.config(text="Click To Delete Book ")

    def delBookBtn_hoverout(event):
        delBookBtn["bg"] = "#121212"
        delBookBtn["font"] = "Segoe UI", 20
        status_label_rst()

    delBookBtn.bind("<Enter>", delBookBtn_hoverin)
    delBookBtn.bind("<Leave>", delBookBtn_hoverout)

    # viewBook Button
    viewBookBtn = Button(
        root,
        text="View Book List",
        bg="#121212",
        fg="white",
        font=("Segoe UI", 20),
        command=lambda: [click(), view_open(), View()],
    )
    viewBookBtn.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.09)

    def viewBookBtn_hoverin(event):
        viewBookBtn["bg"] = "#222222"
        viewBookBtn["font"] = "Segoe UI", 22
        status_label.config(text="Click To View Book List ")

    def viewBookBtn_hoverout(event):
        viewBookBtn["bg"] = "#121212"
        viewBookBtn["font"] = "Segoe UI", 20
        status_label_rst()

    viewBookBtn.bind("<Enter>", viewBookBtn_hoverin)
    viewBookBtn.bind("<Leave>", viewBookBtn_hoverout)

    # issueBook Button
    issueBookBtn = Button(
        root,
        text="Issue Book",
        bg="#121212",
        fg="white",
        font=("Segoe UI", 20),
        command=lambda: [click(), issue_open(), issueBook()],
    )
    issueBookBtn.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.09)

    def issueBookBtn_hoverin(event):
        issueBookBtn["bg"] = "#222222"
        issueBookBtn["font"] = "Segoe UI", 22
        status_label.config(text="Click To Issue Book ")

    def issueBookBtn_hoverout(event):
        issueBookBtn["bg"] = "#121212"
        issueBookBtn["font"] = "Segoe UI", 20
        status_label_rst()

    issueBookBtn.bind("<Enter>", issueBookBtn_hoverin)
    issueBookBtn.bind("<Leave>", issueBookBtn_hoverout)

    # returnBook Button
    returnBookBtn = Button(
        root,
        text="Return Book",
        bg="#121212",
        fg="white",
        font=("Segoe UI", 20),
        command=lambda: [click(), rtn_open(), returnBook()],
    )
    returnBookBtn.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.09)

    def returnBookBtn_hoverin(event):
        returnBookBtn["bg"] = "#222222"
        returnBookBtn["font"] = "Segoe UI", 22
        status_label.config(text="Click To Return Book ")

    def returnBookBtn_hoverout(event):
        returnBookBtn["bg"] = "#121212"
        returnBookBtn["font"] = "Segoe UI", 20
        status_label_rst()

    returnBookBtn.bind("<Enter>", returnBookBtn_hoverin)
    returnBookBtn.bind("<Leave>", returnBookBtn_hoverout)

    def confirm():
        if messagebox.askyesno(title="Confirm", message="Are you sure that you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", lambda: [click(), confirm()])
    root.mainloop()
