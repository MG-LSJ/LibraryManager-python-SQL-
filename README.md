# Library-Manager-python-

AVBIL Library Manager
Software Requirements:
•	Python 3.x
•	MySQL
•	Pip (To install modules)
Python (Required Modules)
•	Tkinter ( pip install tk )
•	PyMySQL ( pip install pymysql )
•	Pillow ( pip install pillow )
Or run “modules.bat” in prerequisites folder
MySQL Requirements
•	Database with two tables: Book table and Issue table
Or run these 4 commands in MySQL Commandline Client one by one:
create database db;
use db;
create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
Authentication
Put your MySQL connection details on the credentials.txt in the following format:
HOST
USER
PASSWORD	
DATABASE NAME
Do not change anything if using defaults in MySQL.
How to Launch
Click on launch.bat
OR 
Open main.py in a python compiler of choice.
