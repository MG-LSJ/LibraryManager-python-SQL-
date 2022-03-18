from tkinter import *
from tkinter import messagebox
from modules.Sounds import click
from modules.Credentials import db_connection, bookTable


def rtn_check():
    with open(r"counters\returnbook.txt", "r") as file:
        a = file.read()
    return True if a == "1" else False


def rtn_open():
    with open(r"counters\returnbook.txt", "a") as file:
        file.write("1")


def rtn_close():
    with open(r"counters\returnbook.txt", "w") as file:
        file.write("")


def return_book():

    bid = bookInfo1.get()

    if bid == "":
        messagebox.showinfo("Caution", "Please Enter a Book ID")
        ReturnBookWindow.lift()
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
                ReturnBookWindow.lift()
                return

            if data[3] == 0:
                messagebox.showwarning("Caution", "Book is not issued.")
                ReturnBookWindow.lift()
                return

            cur.execute(
                f"update {bookTable} set issued = 0, issuedTo = null where bid = '{bid}' "
            )
            con.commit()
            con.close()

            messagebox.showinfo("Success", "Book succesfullt returned.")
            ReturnBookWindow.destroy()
            rtn_close()

        except:
            messagebox.showinfo("Error", "Can't fetch Book IDs")
            ReturnBookWindow.destroy()
            returnBook()


def returnBook():

    if rtn_check() == True:

        global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, ReturnBookWindow, labelFrame, lb1

        ReturnBookWindow = Toplevel()
        ReturnBookWindow.title("Return Book AVBIL LM")
        ReturnBookWindow.iconbitmap("media\logo.ico")
        ReturnBookWindow.minsize(width=400, height=400)
        ReturnBookWindow.geometry("500x400")

        Canvas1 = Canvas(ReturnBookWindow)

        Canvas1.config(bg="#161616")
        Canvas1.pack(expand=True, fill=BOTH)

        headingFrame1 = Frame(ReturnBookWindow, bg="#006B38", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

        headingLabel = Label(
            headingFrame1,
            text="Return Book",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 20),
        )
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(ReturnBookWindow, bg="#121212")
        labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.2)

        # Book ID to Delete
        lb1 = Label(
            labelFrame, text="Book ID : ", bg="#121212", fg="white", font=("Segoe UI",)
        )
        lb1.place(relx=0.05, rely=0.4)

        bookInfo1 = Entry(labelFrame)
        bookInfo1.place(relx=0.3, rely=0.4, relwidth=0.62)

        # Submit Button
        SubmitBtn = Button(
            ReturnBookWindow,
            text="RETURN",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), return_book()],
        )
        SubmitBtn.place(relx=0.26, rely=0.85, relwidth=0.2, relheight=0.1)

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
            ReturnBookWindow,
            text="CANCEL",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), rtn_close(), ReturnBookWindow.destroy()],
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

        ReturnBookWindow.protocol(
            "WM_DELETE_WINDOW",
            lambda: [click(), rtn_close(), ReturnBookWindow.destroy()],
        )
        ReturnBookWindow.mainloop()

    else:
        messagebox.showinfo("Caution", "Return Book AVBIL LM is already open.")
