from tkinter import *
from tkinter import messagebox
from modules.Sounds import click
from modules.Credentials import db_connection, bookTable, bid_check


def add_check():
    with open(r"counters\addbook.txt", "r") as file:
        a = file.read()
    return True if a == "1" else False


def add_open():
    with open(r"counters\addbook.txt", "a") as file:
        file.write("1")


def add_close():
    with open(r"counters\addbook.txt", "w") as file:
        file.write("")


def bookRegister():

    bid = bidEntry.get()
    title = titleEntry.get()
    author = authEntry.get()
    status = statusVar.get()
    issued = 1 if status else 0
    issuedTo = issuedToEntry.get()

    if bid == "" or title == "" or author == "" or (status and not issuedTo):
        messagebox.showwarning("Caution", "All fields must be filled")
        AddBookWindow.lift()
        return

    else:
        try:
            con = db_connection()
            cur = con.cursor()

            if bid_check(bid, con, cur):
                messagebox.showwarning("Caution", "Book ID already exist.")
                AddBookWindow.lift()
                return

            if status:
                cur.execute(
                    f"insert into {bookTable} values('{bid}','{title}','{author}',{issued},'{issuedTo}')"
                )
            else:
                cur.execute(
                    f"insert into {bookTable}(bid, title, author, issued) values('{bid}','{title}','{author}',{status})"
                )
            con.commit()
            con.close()

            messagebox.showinfo("Success", f"Book named {title} added successfully.")
            AddBookWindow.destroy()
            add_close()

        except:
            messagebox.showerror("Error", "Can't add data into Database")
            AddBookWindow.destroy()
            addBookWin()


def addBookWin():
    if add_check():

        global bidEntry, titleEntry, authEntry, statusVar, issuedToEntry, AddBookWindow

        AddBookWindow = Toplevel()
        AddBookWindow.title("Add Book AVBIL LM")
        AddBookWindow.iconbitmap("media\logo.ico")
        AddBookWindow.minsize(width=550, height=450)
        AddBookWindow.geometry("600x500")
        AddBookWindow.lift()

        # Canvas
        Canvas1 = Canvas(AddBookWindow)
        Canvas1.config(bg="#161616")
        Canvas1.pack(expand=True, fill=BOTH)

        # Heading
        headingFrame1 = Frame(AddBookWindow, bg="#ff6e40", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

        headingLabel = Label(
            headingFrame1,
            text="Add Book",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 20),
        )
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Label Frame
        labelFrame = Frame(AddBookWindow, bg="#121212")
        labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

        # Book ID
        bidLbl = Label(
            labelFrame, text="Book ID : ", bg="#121212", fg="white", font=("Segoe UI",)
        )
        bidLbl.place(relx=0.05, rely=0.2, relheight=0.08)

        bidEntry = Entry(labelFrame)
        bidEntry.place(relx=0.4, rely=0.2, relwidth=0.52, relheight=0.08)

        # Title
        titleLbl = Label(
            labelFrame, text="Title : ", bg="#121212", fg="white", font=("Segoe UI",)
        )
        titleLbl.place(relx=0.05, rely=0.35, relheight=0.08)

        titleEntry = Entry(labelFrame)
        titleEntry.place(relx=0.4, rely=0.35, relwidth=0.52, relheight=0.08)

        # Book Author
        authLbl = Label(
            labelFrame, text="Author : ", bg="#121212", fg="white", font=("Segoe UI",)
        )
        authLbl.place(relx=0.05, rely=0.50, relheight=0.08)

        authEntry = Entry(labelFrame)
        authEntry.place(relx=0.4, rely=0.50, relwidth=0.52, relheight=0.08)

        # Book Status
        statusLbl = Label(
            labelFrame,
            text="Issued : ",
            bg="#121212",
            fg="white",
            font=("Segoe UI",),
        )
        statusLbl.place(relx=0.05, rely=0.65, relheight=0.08)

        statusVar = BooleanVar()

        def issuedTo():
            if statusVar.get():
                issuedToLbl["fg"] = "white"
                issuedToEntry["state"] = "normal"
            else:
                issuedToLbl["fg"] = "grey"
                issuedToEntry["state"] = "disabled"

        statusEntry = Checkbutton(
            labelFrame,
            bg="#121212",
            activebackground="#161616",
            onvalue=True,
            offvalue=False,
            variable=statusVar,
            command=issuedTo,
        )
        # statusEntry.deselect()
        statusEntry.place(relx=0.4, rely=0.65)

        # Issued To
        issuedToLbl = Label(
            labelFrame,
            text="Issued to : ",
            bg="#121212",
            fg="grey",
            font=("Segoe UI",),
        )
        issuedToLbl.place(relx=0.05, rely=0.8, relheight=0.08)

        issuedToEntry = Entry(labelFrame, state="disabled")
        issuedToEntry.place(relx=0.4, rely=0.8, relwidth=0.52, relheight=0.08)

        # Add Button
        SubmitBtn = Button(
            AddBookWindow,
            text="ADD",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), bookRegister()],
        )
        SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

        def SubmitBtn_hoverin(event):
            SubmitBtn["bg"] = "#222222"
            SubmitBtn["font"] = "Segoe UI", 15

        def SubmitBtn_hoverout(event):
            SubmitBtn["bg"] = "#121212"
            SubmitBtn["font"] = "Segoe UI", 12

        SubmitBtn.bind("<Enter>", SubmitBtn_hoverin)
        SubmitBtn.bind("<Leave>", SubmitBtn_hoverout)

        # Back Button
        backBtn = Button(
            AddBookWindow,
            text="CANCEL",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), add_close(), AddBookWindow.destroy()],
        )
        backBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

        def backBtn_hoverin(event):
            backBtn["bg"] = "#222222"
            backBtn["font"] = "Segoe UI", 15

        def backBtn_hoverout(event):
            backBtn["bg"] = "#121212"
            backBtn["font"] = "Segoe UI", 12

        backBtn.bind("<Enter>", backBtn_hoverin)
        backBtn.bind("<Leave>", backBtn_hoverout)

        AddBookWindow.protocol(
            "WM_DELETE_WINDOW", lambda: [click(), add_close(), AddBookWindow.destroy()]
        )
        AddBookWindow.mainloop()

    else:
        messagebox.showinfo("Caution", "Add Book AVBIL LM is already open.")
