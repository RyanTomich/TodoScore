import tkinter as tk
from tkinter import *
from tkinter import ttk

def test():
    lable = Label(root, text = "Are you a Geek?")
    lable.grid(column = 0, row = 1)


root = Tk()
root.title("<TodoScore>")
root.geometry('1000x700')

tab_paretn = ttk.Notebook(root)

tab_todo = ttk.Frame(tab_paretn)
tab_score = ttk.Frame(tab_paretn)

tab_paretn.add(tab_todo, text='todo')
tab_paretn.add(tab_score, text='grades')
tab_paretn.pack(expand=1, fill = 'both')

title = Label(tab_todo, text = "<Todo>", pady=10, padx=10, font=('Terminal', 60))
title.grid(column = 0, row = 0)

title = Label(tab_score, text = "<Score>", pady=10, padx=10, font=('Terminal', 60))
title.grid(column = 0, row = 0)


root.mainloop()
