<h1 align="center"> Library Manager (python, SQL, and tkinter)</h1>

AVBIL Library Manager
-------------


<h3>Software Requirements:</h3>

- Python 3.x
- MySQL
- Pip (To install modules)

<h3>Python (Required Modules)</h3>

- Tkinter
```sh
pip install tk
``` 
- PyMySQL
```sh
pip install pymysql
``` 
- Pillow
```sh
pip install pillow
``` 

Or run “modules.bat” in prerequisites folder

<h3>MySQL Requirements</h3>

Database with two tables: 
- Book table 
- Issue table

Or run these 4 commands in MySQL Commandline Client one by one:
```sql
create database db;
use db;
create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
```
<h3>Authentication</h3>

Put your MySQL connection details on the credentials.txt in the following format:
```
HOST
USER
PASSWORD	
DATABASE NAME
```
Do not change anything if using defaults in MySQL.

![image](https://user-images.githubusercontent.com/73988826/133984139-50a13548-b3f9-46fb-8108-d6b248799ac1.png)

<h3>How to Launch</h3>

Click on launch.bat

<b>OR</b>

Open main.py in a python compiler of choice.
