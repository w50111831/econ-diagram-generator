import tkinter as tk
from tkinter import ttk
#diag_list = ['PPC','PPF', 'D', 'S', 'DS','SURPLUS', 'SHORTAGE', 'PED', 'XED']

#Main class
class Main():
    def __init__(self):
        self.window = Window() #instantiate window in main
        self.createstyles()
        page = HomePage(self.window, self) 
        self.showpage(page) #set page to homepage, then show the new page value.
        self.window.mainloop()

    def showpage(self, page):
        self.window.page.destroy()
        self.window.page = page
        self.window.title(page.title)
        self.window.geometry(f"{page.WIDTH}x{page.HEIGHT}")
    
    def createstyles(self):
        titlestyle= ttk.Style()
        titlestyle.configure('Title.TButton', font=('helvetica', 20), padding=0)


#Window wrapper for tkinter canvas.
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.page = tk.Frame(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)



#Base page class as a framework for future Pages:
class BasePage(tk.Frame):
    def __init__(self, window, main):
        super().__init__(window)
        self.main = main
        self.grid(column=0, row=0, sticky="nsew")
        for i in range(15):
            self.grid_rowconfigure(i, weight=1, uniform="grid")
            self.grid_columnconfigure(i, weight=1, uniform="grid")
        #self.grid_propagate(False)
    
    def strictboxwidget(self, column=0, row=0, columnspan=1, rowspan=1):
        frame = tk.Frame(self)
        frame.grid(column=column, row=row, columnspan=columnspan, sticky="nsew")
        frame.grid_propagate(False)
        return frame



    title = "Default title"
    WIDTH = 900
    HEIGHT = 900

#All pages:
class HomePage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)

        ttk.Label(self.strictboxwidget(row=1, column=4, columnspan=6), text="Homepage", style="Title.TButton", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)

        ttk.Button(self, text="Demand curve", command=lambda: main.showpage(DPage(window, main))).grid(column=2, row=4, columnspan=2, sticky="nsew")
        ttk.Button(self, text="Supply curve", command=lambda: main.showpage(SPage(window, main))).grid(column=2, row=6, columnspan=2, stick="nsew")
    title = "Homepage"

class DPage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)

        frame = tk.Frame(self)
        frame.grid(column=4, row=1, columnspan=6, rowspan=1, sticky="nsew")
        frame.grid_propagate(False)
        ttk.Label(frame, text="Demand curve generator", style="Title.TButton", anchor="center").place(relx=0, rely=0, relwidth=1, relheight=1)
        
        
        ttk.Button(self, text="HomePage", command=lambda: main.showpage(HomePage(window, main))).grid(column=1, row=4, columnspan=2, sticky="nsew")
        

    title = "Demand curve generator"

class SPage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)
        ttk.Label(self, text="Supply curve generator", style="Title.TButton", anchor="center").grid(column=4, row=1, columnspan=6, rowspan=1, sticky="nsew")
        ttk.Button(self, text="HomePage", command=lambda: main.showpage(HomePage(window, main))).grid(column=1, row=4, columnspan=2, sticky="nsew")
    title = "Supply curve generator"


main = Main() #instantiate main object

        