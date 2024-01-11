import tkinter as tk
from tkinter import *
from main import *
import mysql.connector

def add():
    print("i add")
def edit():
    print("i edit")
def delete():
    print("i delete")


tasks_db = mysql.connector.connect(host="localhost", user="root", password="Todois14*", database = "todo")
cursor = tasks_db.cursor()

if tasks_db.is_connected():
    db_info = tasks_db.get_server_info()
    print(f'Connected to MySQL server version: {db_info}')
    cursor.execute("select database();")
    record = cursor.fetchone()
    print(f"You're connected to database: {record}")

table = '''CREATE TABLE TASKS(
    CLASS VARCHAR(8),
    ASIGNMENT VARCHAR(60),
    OPEN_DATE DATE,
    DUE_DATE DATE,
    STATUS VARCHAR(13),
    GRADE FLOAT)
'''

try:
    cursor.execute(table)   # creates table, returns error if table exists
except mysql.connector.errors.ProgrammingError:
    pass    # if table exists, continue


# cursor.execute('SHOW TABLES;')
# ans = cursor.fetchall()
# print(ans)
