from tkinter import *
from tkinter import messagebox
from modules.Credentials import db_connection, bookTable
from modules.Sounds import click


def issue_check():
    with open(r"counters\issuebook.txt", "r") as file:
        a = file.read()
    return True if a == "1" else False


def issue_open():
    with open(r"counters\issuebook.txt", "a") as file:
        file.write("1")


def issue_close():
    with open(r"counters\issuebook.txt", "w") as file:
        file.write("")


def issue():

    bid = bidEntry.get()
    issuedTo = issuedToEntry.get()

    if bid == "" or issuedTo == "":
        messagebox.showwarning("Caution", "All fields must be filled")
        IssueBookWindow.lift()
        return
    else:
        try:
            con = db_connection()
            cur = con.cursor()

            cur.execute(f"select * from {bookTable} where bid = '{bid}'")
            con.commit()

            data = cur.fetchone()

            if not data:
                messagebox.showwarning("Caution", "Book ID does not exist in Database")
                IssueBookWindow.lift()
                return

            if data[3] == 1:
                messagebox.showwarning(
                    "Caution", f"Book is already issued to {data[4]}."
                )
                IssueBookWindow.lift()
                return

            cur.execute(
                f"update {bookTable} set issued = 1, issuedTo = '{issuedTo}' where bid = '{bid}' "
            )
            con.commit()
            con.close()

            messagebox.showinfo("Success", f"Book issued scuucessfully to {issuedTo}.")
            IssueBookWindow.destroy()
            issue_close()

        except:
            messagebox.showerror("Error", "Unable to fetch Book IDs")
            IssueBookWindow.destroy()
            issueBook()


def issueBook():

    if issue_check() == True:

        global bidEntry, issuedToEntry, IssueBookWindow

        IssueBookWindow = Toplevel()
        IssueBookWindow.title("Issue Book AVBIL LM")
        IssueBookWindow.iconbitmap("media\logo.ico")
        IssueBookWindow.minsize(width=400, height=400)
        IssueBookWindow.geometry("500x400")

        Canvas1 = Canvas(IssueBookWindow)
        Canvas1.config(bg="#161616")
        Canvas1.pack(expand=True, fill=BOTH)

        headingFrame1 = Frame(IssueBookWindow, bg="#D6ED17", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

        headingLabel = Label(
            headingFrame1,
            text="Issue Book",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 20),
        )
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(IssueBookWindow, bg="#121212")
        labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.2)

        # Book ID
        bidLbl = Label(
            labelFrame, text="Book ID : ", bg="#121212", fg="white", font=("Segoe UI",)
        )
        bidLbl.place(relx=0.05, rely=0.2)

        bidEntry = Entry(labelFrame)
        bidEntry.place(relx=0.3, rely=0.25, relwidth=0.62)

        # Student name
        issuedToLbl = Label(
            labelFrame,
            text="Issued To : ",
            bg="#121212",
            fg="white",
            font=("Segoe UI",),
        )
        issuedToLbl.place(relx=0.05, rely=0.5)

        issuedToEntry = Entry(labelFrame)
        issuedToEntry.place(relx=0.3, rely=0.55, relwidth=0.62)

        # Issue Button
        issueBtn = Button(
            IssueBookWindow,
            text="ISSUE",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), issue()],
        )
        issueBtn.place(relx=0.26, rely=0.85, relwidth=0.2, relheight=0.1)

        def issueBtn_hoverin(event):
            issueBtn["bg"] = "#222222"
            issueBtn["font"] = "Segoe UI", 15

        def issueBtn_hoverout(event):
            issueBtn["bg"] = "#121212"
            issueBtn["font"] = "Segoe UI", 12

        issueBtn.bind("<Enter>", issueBtn_hoverin)
        issueBtn.bind("<Leave>", issueBtn_hoverout)

        # Back Button
        backBtn = Button(
            IssueBookWindow,
            text="CANCEL",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), issue_close(), IssueBookWindow.destroy()],
        )
        backBtn.place(relx=0.55, rely=0.85, relwidth=0.2, relheight=0.1)

        def backBtn_hoverin(event):
            backBtn["bg"] = "#222222"
            backBtn["font"] = "Segoe UI", 15

        def backBtn_hoverout(event):
            backBtn["bg"] = "#121212"
            backBtn["font"] = "Segoe UI", 12

        backBtn.bind("<Enter>", backBtn_hoverin)
        backBtn.bind("<Leave>", backBtn_hoverout)

        IssueBookWindow.protocol(
            "WM_DELETE_WINDOW",
            lambda: [click(), issue_close(), IssueBookWindow.destroy()],
        )
        IssueBookWindow.mainloop()

    else:
        messagebox.showinfo("Caution", "Issue Book AVBIL LM is already open.")
