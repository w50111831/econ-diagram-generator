import tkinter as tk
from tkinter import ttk
#diag_list = ['PPC','PPF', 'D', 'S', 'DS','SURPLUS', 'SHORTAGE', 'PED', 'XED']
class Main():
    def __init__(self):
        self.window = Window() #instantiate window in main
        page = HomePage(self.window, self) 
        self.showpage(page) #set page to homepage, then show the new page value.
        self.window.mainloop()

    def showpage(self, page):
        self.window.page.destroy()
        self.window.page = page
        self.window.title(page.title)
        page.pack(fill="both", expand=True)


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.page = tk.Frame(self)

class HomePage(tk.Frame):
    def __init__(self, window, main):
        super().__init__(window)
        ttk.Label(self, text="Homepage").pack(expand=True,)
        ttk.Button(self, text="Demand curve").pack()
        self.title = "Homepage"

main = Main() #instantiate main object

        