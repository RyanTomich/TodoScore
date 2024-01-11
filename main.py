import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import *


root = Tk()
root.title("<TodoScore>")
root.geometry('1000x800')

tab_paretn = ttk.Notebook(root)

tab_todo = ttk.Frame(tab_paretn)
tab_score = ttk.Frame(tab_paretn)

tab_paretn.add(tab_todo, text='todo')
tab_paretn.add(tab_score, text='grades')
tab_paretn.pack(expand=1, fill = 'both')

############
# tab_todo #
############

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
all_tree['columns'] = ("Class", "Asignment", "Open-Date", "Due-Date", "Status")
all_tree.column("#0", width=0, stretch=NO)
all_tree.column("Class", anchor=W, width=100)
all_tree.column("Asignment", anchor=W, width=400)
all_tree.column("Open-Date", anchor=CENTER, width=150)
all_tree.column("Due-Date", anchor=CENTER, width=150)
all_tree.column("Status", anchor=W, width=100)

all_tree.heading("#0", text="", anchor=W)
all_tree.heading("Class", text="Class", anchor=W)
all_tree.heading("Asignment", text="Asignment", anchor=W)
all_tree.heading("Open-Date", text="Open-Date", anchor=CENTER)
all_tree.heading("Due-Date", text="Due-Date", anchor=CENTER)
all_tree.heading("Status", text="Status", anchor=W)

all_tree.tag_configure('oddrow', background="grey50")
all_tree.tag_configure('evenrow', background="grey70")


# Data Enrty
data_frame = LabelFrame(tab_todo, text="Assignment_entry")
data_frame.grid(column=0, row=2, padx="5", pady="5")

class_label = Label(data_frame, text="Class")
class_label.grid(row=0, column=0, padx=10, pady=5)
class_entry = Entry(data_frame, width= 10)
class_entry.grid(row=1, column=0, padx=10, pady=5)

assignment_lable = Label(data_frame, text="Asignment")
assignment_lable.grid(row=0, column=1, padx=10, pady=5)
assignment_entry = Entry(data_frame, width= 40)
assignment_entry.grid(row=1, column=1, padx=10, pady=5)

open_lable = Label(data_frame, text="Open_Date")
open_lable.grid(row=0, column=2, padx=10, pady=5)
open_entry = Entry(data_frame, width= 10)
open_entry.grid(row=1, column=2, padx=10, pady=5)

due_lable = Label(data_frame, text="Due_Date")
due_lable.grid(row=0, column=3, padx=10, pady=5)
due_entry = Entry(data_frame, width= 10)
due_entry.grid(row=1, column=3, padx=10, pady=5)

status_lable = Label(data_frame, text="status")
status_lable.grid(row=0, column=4, padx=10, pady=5)
status_entry = Entry(data_frame, width= 10)
status_entry.grid(row=1, column=4, padx=10, pady=5)


button_frame = LabelFrame(tab_todo)
button_frame.grid(column=0, row=3, padx="5", pady="5")

add_button = Button(button_frame, text = "Add", command = add, height= 3, width=28)
add_button.grid(row=0, column=0, padx=5, pady=5)
edit_button = Button(button_frame, text = "Edit", command = edit, height= 3, width=28)
edit_button.grid(row=0, column=1, padx=5, pady=5)
delete_button = Button(button_frame, text = "Delete", command = delete, height= 3, width=28)
delete_button.grid(row=0, column=2, padx=5, pady=5)




#############
# tab_score #
#############

title = Label(tab_score, text = "<Score>", pady=10, padx=10, font=('Terminal', 60))
title.grid(column = 0, row = 0)


root.mainloop()

# close connection (run after gui is exited)
cursor.close()
tasks_db.close()
print ("Database connection was cloased") # only one connection is made per run
