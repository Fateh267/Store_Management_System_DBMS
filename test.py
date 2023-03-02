import tkinter as tk
from tkinter import ttk
import test2
import database

class Retrieve(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('500x300')
        self.title('Menu')

        ttk.Button(self, text='Close').pack(expand=True)

class Input(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('500x300')
        self.title('Menu')

        ttk.Button(self, text='Close',command=self.open_inventory).pack(expand=True)

    def open_inventory(self):
        inventory_window = test2.Inventory(self)
        inventory_window.grab_set()

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('500x300')
        self.title('Menu')

        l1 = ttk.Label(self, text="WELCOME TO MAIN MENU").pack(expand=True)
        l2 = ttk.Label(self, text="Please select an option").pack(expand=True)



        b_input = ttk.Button(self, text='Input Data', command=self.open_window2).pack(expand=True)

        b_retrieve = ttk.Button(self, text="Retrieve", command= self.open_window3).pack(expand=True)

    def open_window2(self):
        window2 = Input(self)
        window2.grab_set()

    def open_window3(self):
        window3 = Retrieve(self)
        window3.grab_set()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x300')
        self.title('Main Window')

        usr = ttk.Label(self, text="Enter Username").pack(expand=True)
        usr_ip = ttk.Entry(self).pack(expand=True)
        pwd = ttk.Label(self, text="Enter Password").pack(expand=True)
        pwd_ip = ttk.Entry(self).pack(expand=True)

        # place a button on the root window
        ttk.Button(self,
                text='Login',
                command=self.open_window).pack(expand=True)

    def open_window(self):
        window = Window(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()