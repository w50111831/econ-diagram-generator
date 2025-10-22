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
        titlestyle.configure('Title.TLabel', font=('helvetica', 20), padding=0)

        diagramtext = ttk.Style()
        diagramtext.configure('Diagram.TLabel', font=('helvetica', 20), padding=0, background='gray75')


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
    
    def strictboxwidget(self, column=0, row=0, columnspan=1, rowspan=1):
        frame = tk.Frame(self)
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky="nsew")
        frame.grid_propagate(False)
        return frame
    
    def line_coords(self, x1, y1, x2, y2, canvas):
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        x1 = x1*canvas_width
        x2 = x2*canvas_width
        y1 = y1*canvas_height
        y2 = y2*canvas_height
        coords = [x1,y1,x2,y2]
        return canvas.create_line(coords, fill='black', width=2)
    
    def text_coords(self, x1, y1, canvas):
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        coords = [x1*canvas_width, y1*canvas_height]
        return coords
    
    


    title = "Default title"
    WIDTH = 900
    HEIGHT = 900

#All pages:
class HomePage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)

        ttk.Label(self.strictboxwidget(row=1, column=4, columnspan=6), text="Homepage", style="Title.TLabel", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        ttk.Button(self.strictboxwidget(column=2, row=4, columnspan=2 ), text="Demand curve", command=lambda: main.showpage(DPage(window, main))).place(relx=0, rely=0, relwidth=1, relheight=1)
        ttk.Button(self.strictboxwidget(column=2, row=6, columnspan=2 ), text="Supply curve", command=lambda: main.showpage(SPage(window, main))).place(relx=0, rely=0, relwidth=1, relheight=1)
        ttk.Button(self.strictboxwidget(column=2, row=8, columnspan=2), text="D + S curve", command=lambda: main.showpage(DSPage(window, main))).place(relx=0, rely=0, relwidth=1, relheight=1)

    title = "Homepage"

class DPage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)

        ttk.Label(self.strictboxwidget(row=1, column=4, columnspan=6), text="Demand curve generator", style="Title.TLabel", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        ttk.Button(self.strictboxwidget(row=4, column=1, columnspan=2), text="HomePage", command=lambda: main.showpage(HomePage(window, main))).place(relx=0, rely=0, relwidth=1, relheight=1)

        ttk.Label(self.strictboxwidget(row=13, column=12, columnspan=6), text="Quantity", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        self.currentquantity = ttk.Label(self.strictboxwidget(row=10, column=3, columnspan=2), text="Quantity is 20", anchor="center" )
        self.currentquantity.place(relx=0, rely=0, relwidth=1, relheight=1)

        ttk.Label(self.strictboxwidget(row=5, column=4, columnspan=2), text="Price", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        self.currentprice = ttk.Label(self.strictboxwidget(row=10, column=1, columnspan=2), text="Price is 80", anchor="center" )
        self.currentprice.place(relx=0, rely=0, relwidth=1, relheight=1)

        #diagram area:
        diagram = tk.Canvas(self.strictboxwidget(row=5, column=6, columnspan=8, rowspan=8), width=100, height=100, background='gray75')
        diagram.place(relx=0, rely=0, relwidth=1, relheight=1)
        diagram.update()
        self.line_coords(0.1, 0.9, 0.9, 0.9, diagram)
        self.line_coords(0.1, 0.9, 0.1, 0.1, diagram)
        D = self.line_coords(0.2, 0.8, 0.8, 0.2, diagram)
        self.UptoD = self.line_coords(0.2, 0.9, 0.2, 0.8, diagram)
        self.RighttoD = self.line_coords(0.1, 0.8, 0.2, 0.8, diagram)
        
        
        #diagram.create_text(self.text_coords(0.5, 0.5, diagram), text="D", font=("helvetica", 16), fill="black")
        Doffsetscale = ttk.Scale(self.strictboxwidget(row=13, column=7, columnspan=5), orient='horizontal', length = 100, from_=20, to=75, command=lambda Doffset:self.updateequilibrium(Doffset, diagram))
        Doffsetscale.place(relx=0, rely=0, relwidth=1, relheight=1)
        

        ttk.Label(self.strictboxwidget(row=6, column=12, columnspan=1), text="D", style="Diagram.TLabel", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)

    def updateequilibrium(self, Doffset, diagram):
        Doffset=int(round(float(Doffset)))
        diagram.delete(self.UptoD, self.RighttoD)
        self.UptoD = self.line_coords(Doffset/100, 0.9, Doffset/100, (1-(Doffset/100)), diagram)
        self.RighttoD = self.line_coords(0.1, (1-(Doffset/100)), (Doffset/100), (1-(Doffset/100)), diagram)
        self.currentquantity.config(text=f"quantity = {Doffset}")
        self.currentprice.config(text=f"price = {(100-Doffset)}")




    title = "Demand curve generator"

class SPage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)

        ttk.Label(self.strictboxwidget(row=1, column=4, columnspan=6), text="Supply curve generator", style="Title.TLabel", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        ttk.Button(self.strictboxwidget(row=4, column=1, columnspan=2), text="HomePage", command=lambda: main.showpage(HomePage(window, main))).place(relx=0, rely=0, relwidth=1, relheight=1)

        ttk.Label(self.strictboxwidget(row=13, column=12, columnspan=6), text="Quantity", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        self.currentquantity = ttk.Label(self.strictboxwidget(row=10, column=3, columnspan=2), text="Quantity is 20", anchor="center" )
        self.currentquantity.place(relx=0, rely=0, relwidth=1, relheight=1)

        ttk.Label(self.strictboxwidget(row=5, column=4, columnspan=2), text="Price", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        self.currentprice = ttk.Label(self.strictboxwidget(row=10, column=1, columnspan=2), text="Price per unit is 20", anchor="center" )
        self.currentprice.place(relx=0, rely=0, relwidth=1, relheight=1)

        #diagram area:
        diagram = tk.Canvas(self.strictboxwidget(row=5, column=6, columnspan=8, rowspan=8), width=100, height=100, background='gray75')
        diagram.place(relx=0, rely=0, relwidth=1, relheight=1)
        diagram.update()
        self.line_coords(0.1, 0.9, 0.9, 0.9, diagram)
        self.line_coords(0.1, 0.9, 0.1, 0.1, diagram)
        S = self.line_coords(0.2, 0.2, 0.8, 0.8, diagram)
        self.UptoS = self.line_coords(0.2, 0.9, 0.2, 0.2, diagram)
        self.RighttoS = self.line_coords(0.1, 0.2, 0.2, 0.2, diagram)
        
        
        #diagram.create_text(self.text_coords(0.5, 0.5, diagram), text="D", font=("helvetica", 16), fill="black")
        Doffsetscale = ttk.Scale(self.strictboxwidget(row=13, column=7, columnspan=5), orient='horizontal', length = 100, from_=20, to=75, command=lambda Doffset:self.updateequilibrium(Doffset, diagram))
        Doffsetscale.place(relx=0, rely=0, relwidth=1, relheight=1)
        

        ttk.Label(self.strictboxwidget(row=10, column=12, columnspan=1), text="S", style="Diagram.TLabel", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)

    def updateequilibrium(self, Doffset, diagram):
        Doffset=int(round(float(Doffset)))
        diagram.delete(self.UptoS, self.RighttoS)
        self.UptoS = self.line_coords(Doffset/100, 0.9, Doffset/100, (Doffset/100), diagram)
        self.RighttoS = self.line_coords(0.1, (Doffset/100), (Doffset/100), (Doffset/100), diagram)
        self.currentquantity.config(text=f"quantity = {Doffset}")
        self.currentprice.config(text=f"price per unit = {Doffset}")


class DSPage(BasePage):
    def __init__(self, window, main):
        super().__init__(window, main)

        ttk.Label(self.strictboxwidget(row=1, column=4, columnspan=6), text="D+S curve generator", style="Title.TLabel", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        ttk.Button(self.strictboxwidget(row=4, column=1, columnspan=2), text="HomePage", command=lambda: main.showpage(HomePage(window, main))).place(relx=0, rely=0, relwidth=1, relheight=1)

        ttk.Label(self.strictboxwidget(row=13, column=12, columnspan=6), text="Quantity", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        self.currentquantity = ttk.Label(self.strictboxwidget(row=10, column=3, columnspan=2), text="Quantity is 50", anchor="center" )
        self.currentquantity.place(relx=0, rely=0, relwidth=1, relheight=1)

        ttk.Label(self.strictboxwidget(row=5, column=4, columnspan=2), text="Price", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)
        self.currentprice = ttk.Label(self.strictboxwidget(row=10, column=1, columnspan=2), text="Price per unit is 50", anchor="center" )
        self.currentprice.place(relx=0, rely=0, relwidth=1, relheight=1)

        #diagram area:
        diagram = tk.Canvas(self.strictboxwidget(row=5, column=6, columnspan=8, rowspan=8), width=100, height=100, background='gray75')
        diagram.place(relx=0, rely=0, relwidth=1, relheight=1)
        diagram.update()
        self.line_coords(0.1, 0.9, 0.9, 0.9, diagram) #x-axis line
        self.line_coords(0.1, 0.9, 0.1, 0.1, diagram) #y-axis line
        self.S = self.line_coords(0.2, 0.2, 0.8, 0.8, diagram)
        self.D = self.line_coords(0.2, 0.8, 0.8, 0.2, diagram)
        self.UptoE = self.line_coords(0.5, 0.9, 0.5, 0.5, diagram)
        self.RighttoE = self.line_coords(0.1, 0.5, 0.5, 0.5, diagram)
        
        ttk.Label(self.strictboxwidget(row=10, column=12, columnspan=1), text="S", style="Diagram.TLabel", anchor="center" ).place(relx=0, rely=0, relwidth=1, relheight=1)

        self.DLabelBackgroundFrame = self.strictboxwidget(row=5, column=8, columnspan=5)
        self.DLabelBackground = ttk.Label(self.DLabelBackgroundFrame, text="", style="Diagram.TLabel", anchor="center" )
        self.DLabelBackground.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.DLabelFrame = self.strictboxwidget(row=5, column=12, columnspan=1)
        self.DLabel = ttk.Label(self.DLabelFrame, text="D", style="Diagram.TLabel", anchor="center" )
        self.DLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        

        #diagram.create_text(self.text_coords(0.5, 0.5, diagram), text="D", font=("helvetica", 16), fill="black")
        Doffsetscale = ttk.Scale(self.strictboxwidget(row=13, column=7, columnspan=5), orient='horizontal', length = 100, from_=20, to=75, command=lambda Doffset:self.updateequilibrium(Doffset, diagram))
        Doffsetscale.set(50)
        Doffsetscale.place(relx=0, rely=0, relwidth=1, relheight=1)
        

        

    def updateequilibrium(self, Doffset, diagram):
        Doffset=int(round(float(Doffset)))

        diagram.delete(self.D)
        self.D = self.line_coords((-0.3+Doffset/100), 0.8, (0.3+Doffset/100), 0.2, diagram)
        self.DLabel.destroy()
        self.DLabelBackgroundFrame.destroy()
        self.DLabelFrame.destroy()

        self.DlabelBackgroundFrame = self.strictboxwidget(row=5, column=6, columnspan=8)
        self.DLabelBackground = ttk.Label(self.DlabelBackgroundFrame, text="", style="Diagram.TLabel", anchor="center" )
        self.DLabelBackground.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.DLabelFrame = self.strictboxwidget(row=5, column=(round(7+Doffset/10)))
        self.DLabel = ttk.Label(self.DLabelFrame, text="D", style="Diagram.TLabel", anchor="center" )
        self.DLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        diagram.delete(self.UptoE, self.RighttoE)
        self.UptoE = self.line_coords((0.5+(Doffset/100))/2, 0.9, (0.5+(Doffset/100))/2, (0.5+(Doffset/100))/2, diagram)
        self.RighttoE = self.line_coords(0.1, (0.5+(Doffset/100))/2, (0.5+(Doffset/100))/2, (0.5+(Doffset/100))/2, diagram)
        self.currentquantity.config(text=f"quantity = {Doffset}")
        self.currentprice.config(text=f"price per unit = {Doffset}")

    title = "Supply curve generator"

main = Main() #instantiate main object