import tkinter as tk
from tkinter import ttk

'''class Window(tk.Toplevel):
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
        window3.grab_set()'''


class Inventory(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.config(width=500, height=300, bg="BLUE")
        self.title('Menu')


        l1 = ttk.Label(self, text="Enter Inventory Data").pack(expand=True, padx=10, pady=10)
        #Supplier_ID
        l2 = ttk.Label(self, text="Enter Supplier ID").pack(expand=True)

        supplier_id = ttk.Entry(self, background="WHITE").pack(expand=True)

        #Name
        l3= ttk.Label(self, text="Enter Supplier name").pack(expand=True)

        supplier_name = ttk.Entry(self).pack(expand=True)
        #Address
        l4 = ttk.Label(self, text="Enter Supplier Address").pack(expand=True)

        supplier_add = ttk.Entry(self).pack(expand=True)
        #Phone
        l5 = ttk.Label(self, text="Enter Supplier name").pack(expand=True)

        supplier_ph = ttk.Entry(self).pack(expand=True)
        #Email
        l6 = ttk.Label(self, text="Enter Supplier name").pack(expand=True)

        supplier_email = ttk.Entry(self).pack(expand=True)



        supp_next = ttk.Button(self, text='Next', command=self.open_window2).pack(expand=True)



