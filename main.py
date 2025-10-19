import tkinter as tk
from tkinter import ttk

root = tk.Tk()

diag_list = ['PPC','PPF', 'D', 'S', 'DS','SURPLUS', 'SHORTAGE', 'PED', 'XED']




pagetitle = ttk.Label(root)
pagetitle['text'] = 'Economics diagram generator'
pagetitle.pack()

root.mainloop()
