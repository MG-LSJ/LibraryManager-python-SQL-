from tkinter import *
from tkinter import messagebox
from modules.Sounds import click
from modules.Credentials import db_connection, bookTable, bid_check


def del_check():
    with open(r"counters\deletebook.txt", "r") as file:
        a = file.read()
    return True if a == "1" else False


def del_open():
    with open(r"counters\deletebook.txt", "a") as file:
        file.write("1")


def del_close():
    with open(r"counters\deletebook.txt", "w") as file:
        file.write("")


def deleteBook():

    bid = bidEntry.get()

    if bid == "":
        messagebox.showwarning("Caution", "Book ID can't be empty")
        DelBookWindow.lift()
        return

    else:
        try:
            con = db_connection()
            cur = con.cursor()

            if not bid_check(bid, con, cur):
                messagebox.showwarning("Caution", "Book ID dosen't exist.")
                DelBookWindow.lift()
                return

            if not messagebox.askyesno(
                "Confrim", "Are you sure you want to delete the book?"
            ):
                DelBookWindow.lift()
                return

            cur.execute(f"delete from {bookTable} where bid = '{bid}'")
            con.commit()

            messagebox.showinfo("Success", "Book Record Deleted Successfully")

            con.close()
            DelBookWindow.destroy()
            del_close()

        except:
            messagebox.showerror("Error", "Please check Book ID")
            DelBookWindow.lift()


def deleteBookWin():

    if del_check() == True:

        global bidEntry, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, DelBookWindow

        DelBookWindow = Toplevel()
        DelBookWindow.title("Delete Books AVBIL LM")
        DelBookWindow.iconbitmap("media\logo.ico")
        DelBookWindow.minsize(width=200, height=200)
        DelBookWindow.geometry("500x400")

        # Canvas
        Canvas1 = Canvas(DelBookWindow)
        Canvas1.config(bg="#161616")
        Canvas1.pack(expand=True, fill=BOTH)

        # Heading
        headingFrame1 = Frame(DelBookWindow, bg="#006B38", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

        headingLabel = Label(
            headingFrame1,
            text="Delete Book",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 20),
        )
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Label Frame
        labelFrame = Frame(DelBookWindow, bg="#121212")
        labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.2)

        # Book ID
        bidLbl = Label(
            labelFrame, text="Book ID : ", bg="#121212", fg="white", font=("Segoe UI",)
        )
        bidLbl.place(relx=0.05, rely=0.4)

        bidEntry = Entry(labelFrame)
        bidEntry.place(relx=0.3, rely=0.4, relwidth=0.62)

        # Delete Button
        SubmitBtn = Button(
            DelBookWindow,
            text="DELETE",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), deleteBook()],
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
            DelBookWindow,
            text="CANCEL",
            bg="#121212",
            fg="white",
            font=("Segoe UI", 12),
            command=lambda: [click(), del_close(), DelBookWindow.destroy()],
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

        DelBookWindow.protocol(
            "WM_DELETE_WINDOW", lambda: [click(), del_close(), DelBookWindow.destroy()]
        )
        DelBookWindow.mainloop()

    else:
        messagebox.showinfo("Caution", "Delete Books AVBIL LM is already open.")
