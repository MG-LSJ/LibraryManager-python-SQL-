from tkinter import *
from tkinter import messagebox, ttk
from modules.Sounds import click
from modules.Credentials import db_connection, bookTable


def view_check():
    with open(r"counters\viewbook.txt", "r") as file:
        a = file.read()
    return True if a == "1" else False


def view_open():
    with open(r"counters\viewbook.txt", "a") as file:
        file.write("1")


def view_close():
    with open(r"counters\viewbook.txt", "w") as file:
        file.write("")


def View():

    if view_check() == True:

        ViewWindow = Toplevel()
        ViewWindow.title("View Books AVBIL LM")
        ViewWindow.iconbitmap("media\logo.ico")
        ViewWindow.minsize(width=500, height=400)
        ViewWindow.geometry("600x500")

        Canvas1 = Canvas(ViewWindow)
        Canvas1.config(bg="#161616")
        Canvas1.pack(expand=True, fill=BOTH)

        headingFrame1 = Frame(ViewWindow, bg="#12a4d9", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

        headingLabel = Label(
            headingFrame1,
            text="View Books",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 20),
        )
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        treeFrame = ttk.Treeview(ViewWindow)
        treeFrame["columns"] = ("bid", "title", "author", "issued", "issuedTo")
        treeFrame.column("#0", width=0, stretch=NO)
        treeFrame.column("bid", anchor=CENTER, width=100)
        treeFrame.column("title", anchor=W, width=100)
        treeFrame.column("author", anchor=W, width=100)
        treeFrame.column("issued", anchor=CENTER, width=100)
        treeFrame.column("issuedTo", anchor=W, width=100)

        treeFrame.heading("#0", text="")
        treeFrame.heading("bid", text="Book ID", anchor=CENTER)
        treeFrame.heading("title", text="Title", anchor=CENTER)
        treeFrame.heading("author", text="Author", anchor=CENTER)
        treeFrame.heading("issued", text="Status", anchor=CENTER)
        treeFrame.heading("issuedTo", text="Issued To", anchor=CENTER)

        treeFrame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.5)

        try:
            con = db_connection()
            cur = con.cursor()

            cur.execute(f"select * from {bookTable}")
            con.commit()

            data = cur.fetchall()
            for counter, record in enumerate(data):
                treeFrame.insert(
                    parent="",
                    index="end",
                    iid=counter,
                    values=[
                        record[0],
                        record[1],
                        record[2],
                        "Issued" if record[3] == 1 else "Available",
                        "" if record[4] == None else record[4],
                    ],
                )

        except:
            messagebox.showerror("Error", "Failed to fetch files from database.")
            ViewWindow.destroy()

        # Back Button
        backBtn = Button(
            ViewWindow,
            text="BACK",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), view_close(), ViewWindow.destroy()],
        )
        backBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

        def backBtn_hoverin(event):
            backBtn["bg"] = "#222222"
            backBtn["font"] = "Segoe UI", 15

        def backBtn_hoverout(event):
            backBtn["bg"] = "#121212"
            backBtn["font"] = "Segoe UI", 12

        backBtn.bind("<Enter>", backBtn_hoverin)
        backBtn.bind("<Leave>", backBtn_hoverout)

        ViewWindow.protocol(
            "WM_DELETE_WINDOW", lambda: [click(), view_close(), ViewWindow.destroy()]
        )
        ViewWindow.mainloop()

    else:
        messagebox.showinfo("Caution", "View Books AVBIL LM is already open.")
