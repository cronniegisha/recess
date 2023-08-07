from tkinter import *

class ReceiptPrinter:
    def __init__(self, master):
        self.master = master
        master.title("Receipt Printer")

        self.label = Label(master, text="Enter your receipt information below:")
        self.label.pack()

        self.name_label = Label(master, text="Name:")
        self.name_label.pack()

        self.name_entry = Entry(master)
        self.name_entry.pack()

        self.price_label = Label(master, text="Price:")
        self.price_label.pack()

        self.price_entry = Entry(master)
        self.price_entry.pack()

        self.submit_button = Button(master, text="Submit", command=self.print_receipt)
        self.submit_button.pack()

    def print_receipt(self):
        name = self.name_entry.get()
        price = self.price_entry.get()

        receipt = f"Name: {name}\nPrice: {price}"

        print(receipt)

root = Tk()
my_gui = ReceiptPrinter(root)
root.mainloop()
