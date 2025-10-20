import tkinter as tk
from tkinter import ttk
#diag_list = ['PPC','PPF', 'D', 'S', 'DS','SURPLUS', 'SHORTAGE', 'PED', 'XED']

#Main class
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


#Window wrapper for tkinter canvas.
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.page = tk.Frame(self)


#Base page class as a framework for future Pages:
class BasePage(tk.Frame):
    def __init__(self, window, main):
        super().__init__(window)
        self.main = main
    title = "Default title"

#All pages:
class HomePage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)
        ttk.Label(self, text="Homepage").pack(expand=True)
        ttk.Button(self, text="Demand curve", command=lambda: main.showpage(DPage(window, main))).pack()
        ttk.Button(self, text="Supply curve", command=lambda: main.showpage(SPage(window, main))).pack()
    title = "Homepage"

class DPage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)
        ttk.Label(self, text="Demand curve generator").pack(expand=True)
        ttk.Button(self, text="HomePage", command=lambda: main.showpage(HomePage(window, main))).pack()
    title = "Demand curve generator"

class SPage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)
        ttk.Label(self, text="Supply curve generator").pack(expand=True)
        ttk.Button(self, text="HomePage", command=lambda: main.showpage(HomePage(window, main))).pack()
    title = "Supply curve generator"

main = Main() #instantiate main object

        