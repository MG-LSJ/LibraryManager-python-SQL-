from tkinter import *
from tkinter import messagebox
import pymysql
import pickle
from modules.Sounds import click

bookTable = "books"
issueTable = "books_issued"


def bid_check(bid, con, cur):
    cur.execute(f"select * from {bookTable} where bid = '{bid}'")
    con.commit()
    return True if cur.fetchall() else False


def db_connection():
    with open("credentials.dat", "rb") as file:
        data = pickle.load(file)
    con = pymysql.connect(
        host=data["host"],
        user=data["user"],
        password=data["password"],
        database=data["database"],
    )
    return con


def test_db(host, user, password, database):
    try:
        con = pymysql.connect(
            host=host, user=user, password=password, database=database
        )
        cur = con.cursor()
        cur.execute(
            f"create table if not exists {bookTable}(bid varchar(20) primary key, title varchar(30), author varchar(30), issued bool, issuedTo varchar(30))"
        )
        con.commit()
        con.close()
        return True
    except:
        return False


def check_cred():
    global bool_check
    bool_check = False
    try:
        with open("credentials.dat", "rb") as file:
            data = pickle.load(file)
    except FileNotFoundError:
        with open("credentials.dat", "w") as file:
            data = False
    except EOFError:
        data = False
    if data and test_db(data["host"], data["user"], data["password"], data["database"]):
        bool_check = True
    else:
        credWin()
    return bool_check


def submitCred():

    global bool_check

    host = hostEntry.get()
    user = userEntry.get()
    password = passEntry.get()
    database = dbEntry.get()

    if not (host and user and password and database):
        messagebox.showinfo("Caution", f"Please fill all fields.")
        return

    if test_db(host, user, password, database):
        messagebox.showinfo("Success", f"Successfylly connected to database.")
    else:
        messagebox.showinfo("Error", f"Unable to connect to database.\nTry again!")
        return

    with open("credentials.dat", "wb+") as file:
        data = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
        }
        pickle.dump(data, file)

    credWindow.destroy()
    bool_check = True


def credWin():

    global credWindow, Canvas1, hostEntry, userEntry, passEntry, dbEntry

    credWindow = Tk()
    credWindow.title("Credentials.")
    credWindow.iconbitmap("media\logo.ico")
    credWindow.minsize(width=400, height=400)
    credWindow.geometry("400x400")

    # Canvas
    Canvas1 = Canvas(credWindow)
    Canvas1.config(bg="#161616")
    Canvas1.pack(expand=True, fill=BOTH)

    # Heading
    headingFrame1 = Frame(credWindow, bg="#ff6e40", bd=5)
    headingFrame1.place(relx=0.10, rely=0.1, relwidth=0.80, relheight=0.13)

    headingLabel = Label(
        headingFrame1,
        text="Enter MySQL Credentials",
        bg="#121212",
        fg="white",
        font=("Segoe UI", 20),
    )
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Label Frame
    labelFrame = Frame(credWindow, bg="#121212")
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Host
    hostLbl = Label(
        labelFrame, text="Host : ", bg="#121212", fg="white", font=("Segoe UI",)
    )
    hostLbl.place(relx=0.05, rely=0.2, relheight=0.08)

    hostEntry = Entry(labelFrame)
    hostEntry.insert(0, "localhost")
    hostEntry.place(relx=0.4, rely=0.2, relwidth=0.52, relheight=0.08)

    # User
    userLbl = Label(
        labelFrame, text="User : ", bg="#121212", fg="white", font=("Segoe UI",)
    )
    userLbl.place(relx=0.05, rely=0.35, relheight=0.08)

    userEntry = Entry(labelFrame)
    userEntry.insert(0, "root")
    userEntry.place(relx=0.4, rely=0.35, relwidth=0.52, relheight=0.08)

    # Password
    passLbl = Label(
        labelFrame, text="Password : ", bg="#121212", fg="white", font=("Segoe UI",)
    )
    passLbl.place(relx=0.05, rely=0.50, relheight=0.08)

    passEntry = Entry(labelFrame, show="*")
    passEntry.place(relx=0.4, rely=0.50, relwidth=0.52, relheight=0.08)

    # Database
    dbLbl = Label(
        labelFrame, text="Database : ", bg="#121212", fg="white", font=("Segoe UI",)
    )
    dbLbl.place(relx=0.05, rely=0.65, relheight=0.08)

    dbEntry = Entry(labelFrame)
    dbEntry.insert(0, "Database Name")
    dbEntry.place(relx=0.4, rely=0.65, relwidth=0.52, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(
        credWindow,
        text="SUBMIT",
        bg="#121212",
        fg="white",
        font=("Segoe UI", 12),
        command=lambda: [click(), submitCred()],
    )
    SubmitBtn.place(relx=0.40, rely=0.85, relwidth=0.20, relheight=0.1)

    def SubmitBtn_hoverin(event):
        SubmitBtn["bg"] = "#222222"
        SubmitBtn["font"] = "Segoe UI", 15

    def SubmitBtn_hoverout(event):
        SubmitBtn["bg"] = "#121212"
        SubmitBtn["font"] = "Segoe UI", 12

    SubmitBtn.bind("<Enter>", SubmitBtn_hoverin)
    SubmitBtn.bind("<Leave>", SubmitBtn_hoverout)

    def confirm():
        if messagebox.askokcancel(
            "Confirm",
            "Are you sure you want to cancel.\nApp will not work without database.",
        ):
            credWindow.destroy()

    credWindow.protocol("WM_DELETE_WINDOW", lambda: [click(), confirm()])
    credWindow.mainloop()
