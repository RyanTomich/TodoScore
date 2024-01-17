import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector


#######
# SQL #
#######

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
    ID AUTO_INCREMENT PRIMARY KEY
'''

try:
    cursor.execute(table)   # creates table, returns error if table exists
except mysql.connector.errors.ProgrammingError:
    pass    # if table exists, continue



###################
# Buttion Actions #
###################

def add():
    id = cursor.lastrowid
    insert_query = (f"""INSERT INTO TASKS (CLASS, ASIGNMENT, OPEN_DATE, DUE_DATE, STATUS, GRADE, ID)
                           VALUES
                           ('{class_entry.get()}', '{assignment_entry.get()}', '{open_entry.get()}', '{due_entry.get()}', '{status_entry.get()}', '{grade_entry.get()}', {id} ) """)
    cursor.execute(insert_query)
    tasks_db.commit()
    populate()
    print(cursor.rowcount, "Record inserted successfully into TASKS table")

def edit():
    selected = all_tree.item(all_tree.focus())["values"][6]
    edit_query = f"""UPDATE TASKS
                    SET CLASS = '{class_entry.get()}', ASIGNMENT = '{assignment_entry.get()}', OPEN_DATE = '{open_entry.get()}', DUE_DATE = '{due_entry.get()}', STATUS = '{status_entry.get()}', GRADE = '{grade_entry.get()}'
                    WHERE id= %s """
    cursor.execute(edit_query, (selected,))
    tasks_db.commit()
    populate()

def delete():
    selected = all_tree.item(all_tree.focus())["values"][6]
    delete_query = "DELETE FROM TASKS WHERE id= %s "
    cursor.execute(delete_query, (selected,))
    tasks_db.commit()
    populate()


# populating Treeview
def populate():
    all_tree.delete(*all_tree.get_children())
    query = 'SELECT * FROM TASKS'
    cursor.execute(query)
    result = cursor.fetchall()

    all_tree.tag_configure('normal', background='grey40')
    all_tree.tag_configure('unstarted', background='grey50')
    all_tree.tag_configure('woi', background='yellow')
    all_tree.tag_configure('done', background='green')
    tag = 'working on it'

    for row in result:
        tag = row[4]
        all_tree.insert("",'end',iid=None,
            values=(row), tags=(tag))

def select_record(e):
    class_entry.delete(0, END)
    assignment_entry.delete(0, END)
    open_entry.delete(0, END)
    due_entry.delete(0, END)
    status_entry.delete(0, END)
    grade_entry.delete(0, END)

    selected = all_tree.focus()
    values = all_tree.item(selected, 'values')

    class_entry.insert(0, values[0])
    assignment_entry.insert(0, values[1])
    open_entry.insert(0, values[2])
    due_entry.insert(0, values[3])
    status_entry.insert(0, values[4])
    grade_entry.insert(0, values[5])

############
# Tkinter #
############

root = Tk()
root.title("<TodoScore>")
root.geometry('1200x800')

tab_paretn = ttk.Notebook(root)

tab_todo = ttk.Frame(tab_paretn)
tab_score = ttk.Frame(tab_paretn)

tab_paretn.add(tab_todo, text='todo')
tab_paretn.add(tab_score, text='grades')
tab_paretn.pack(expand=1, fill = 'both')

# tab_todo #

# creating treeview
style = ttk.Style()
style.configure("Treeview", background="grey40", foreground="black", rowheight=35, fieldbackground="grey10")
style.map("Treeview", background=[('selected', 'grey100')])

# treeview frame
tree_frame = Frame(tab_todo)
tree_frame.grid(column=0, row=1, padx=5, pady=5)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
all_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
all_tree.pack()
tree_scroll.config(command=all_tree.yview)

# columns
all_tree['columns'] = ("Class", "Asignment", "Open-Date", "Due-Date", "Status", "Grade", "Id")
all_tree.column("#0", width=0, stretch=NO)
all_tree.column("Class", anchor=W, width=100)
all_tree.column("Asignment", anchor=W, width=400)
all_tree.column("Open-Date", anchor=CENTER, width=150)
all_tree.column("Due-Date", anchor=CENTER, width=150)
all_tree.column("Status", anchor=W, width=100)
all_tree.column("Grade", anchor=W, width=100)
all_tree.column("Id", anchor=W, width=100)

all_tree.heading("#0", text="", anchor=W)
all_tree.heading("Class", text="Class", anchor=W)
all_tree.heading("Asignment", text="Asignment", anchor=W)
all_tree.heading("Open-Date", text="Open-Date", anchor=CENTER)
all_tree.heading("Due-Date", text="Due-Date", anchor=CENTER)
all_tree.heading("Status", text="Status", anchor=W)
all_tree.heading("Grade", text="Status", anchor=W)

all_tree.tag_configure('oddrow', background="grey50")
all_tree.tag_configure('evenrow', background="grey70")

all_tree.bind("<ButtonRelease-1>", select_record)


# Data Enrty
data_frame = LabelFrame(tab_todo, text="Assignment_entry")
data_frame.grid(column=0, row=2, padx="5", pady="5")

class_label = Label(data_frame, text="Class")
class_label.grid(row=0, column=0, padx=5, pady=5)
class_entry = Entry(data_frame, width= 10)
class_entry.grid(row=1, column=0, padx=5, pady=5)

assignment_lable = Label(data_frame, text="Asignment")
assignment_lable.grid(row=0, column=1, padx=5, pady=5)
assignment_entry = Entry(data_frame, width= 40)
assignment_entry.grid(row=1, column=1, padx=5, pady=5)

open_lable = Label(data_frame, text="Open_Date")
open_lable.grid(row=0, column=2, padx=5, pady=5)
open_entry = Entry(data_frame, width= 10)
open_entry.grid(row=1, column=2, padx=5, pady=5)

due_lable = Label(data_frame, text="Due_Date")
due_lable.grid(row=0, column=3, padx=5, pady=5)
due_entry = Entry(data_frame, width= 10)
due_entry.grid(row=1, column=3, padx=5, pady=5)

status_lable = Label(data_frame, text="Status")
status_lable.grid(row=0, column=4, padx=5, pady=5)
status_entry = Entry(data_frame, width= 10)
status_entry.grid(row=1, column=4, padx=5, pady=5)

grade_lable = Label(data_frame, text="Grade")
grade_lable.grid(row=0, column=5, padx=5, pady=5)
grade_entry = Entry(data_frame, width= 10)
grade_entry.grid(row=1, column=5, padx=5, pady=5)

# Buttons
button_frame = LabelFrame(tab_todo)
button_frame.grid(column=0, row=3, padx="5", pady="5")

add_button = Button(button_frame, text = "Add", command = add, height= 3, width=30)
add_button.grid(row=0, column=0, padx=5, pady=5)
edit_button = Button(button_frame, text = "Edit", command = edit, height= 3, width=30)
edit_button.grid(row=0, column=1, padx=5, pady=5)
delete_button = Button(button_frame, text = "Delete", command = delete, height= 3, width=30)
delete_button.grid(row=0, column=2, padx=5, pady=5)

populate()

# tab_score #

title = Label(tab_score, text = "<Score>", pady=10, padx=10, font=('Terminal', 60))
title.grid(column = 0, row = 0)


root.mainloop()

# close connection (run after gui is exited)
cursor.close()
tasks_db.close()
print ("Database connection was cloased") # only one connection is made per run
