from tkinter import *
from tkinter import messagebox, ttk
import csv
import os

FILE_NAME = "database_proj.csv"
PASSWORD = "admin123"  # Set your authority password here


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Pharmacy Management System")
        self.root.configure(width=1500, height=600, bg='pale turquoise')

        self.fields = ['Item Name', 'Item Price', 'Item Quantity', 'Item Category', 'Item Discount']
        self.data = []
        self.current_index = -1

        self.load_data()
        self.create_login_window()

    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r', newline='') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)

    def save_data(self):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(self.data)

    def add_item(self):
        new_item = {
            'Item Name': self.entry1.get(),
            'Item Price': self.entry2.get(),
            'Item Quantity': self.entry3.get(),
            'Item Category': self.entry4.get(),
            'Item Discount': self.entry5.get()
        }
        self.data.append(new_item)
        self.save_data()
        self.clear_item()
        self.populate_treeview()

    def delete_item(self):
        item_name = self.entry1.get()
        self.data = [item for item in self.data if item['Item Name'] != item_name]
        self.save_data()
        self.clear_item()
        self.populate_treeview()

    def first_item(self):
        if self.data:
            self.current_index = 0
            self.display_item(self.current_index)

    def next_item(self):
        if self.data and self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.display_item(self.current_index)

    def previous_item(self):
        if self.data and self.current_index > 0:
            self.current_index -= 1
            self.display_item(self.current_index)

    def last_item(self):
        if self.data:
            self.current_index = len(self.data) - 1
            self.display_item(self.current_index)

    def update_item(self):
        if 0 <= self.current_index < len(self.data):
            self.data[self.current_index] = {
                'Item Name': self.entry1.get(),
                'Item Price': self.entry2.get(),
                'Item Quantity': self.entry3.get(),
                'Item Category': self.entry4.get(),
                'Item Discount': self.entry5.get()
            }
            self.save_data()
            self.clear_item()
            self.populate_treeview()

    def search_item(self):
        item_name = self.entry1.get()
        for index, item in enumerate(self.data):
            if item['Item Name'] == item_name:
                self.display_item(index)
                return
        messagebox.showinfo("Title", "Item not found")

    def clear_item(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

    def display_item(self, index):
        item = self.data[index]
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry1.insert(0, item['Item Name'])
        self.entry2.insert(0, item['Item Price'])
        self.entry3.insert(0, item['Item Quantity'])
        self.entry4.insert(0, item['Item Category'])
        self.entry5.insert(0, item['Item Discount'])

    def authenticate(self):
        if self.password_entry.get() == PASSWORD:
            self.login_window.destroy()
            self.root.deiconify()  # Show the main application window
            self.create_main_application()
        else:
            messagebox.showerror("Error", "Invalid Password")

    def create_login_window(self):
        self.login_window = Toplevel(self.root)
        self.login_window.title("Login")
        self.login_window.geometry("300x150")

        Label(self.login_window, text="Enter Password", font=("Times", 12)).pack(pady=10)
        self.password_entry = Entry(self.login_window, show='*', font=("Times", 12))
        self.password_entry.pack(pady=10)
        Button(self.login_window, text="Login", command=self.authenticate, font=("Times", 12)).pack(pady=10)

        self.root.withdraw()

    def create_main_application(self):
        self.label0 = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bg="white", fg="black", font=("Times", 30))
        self.label1 = Label(self.root, text="ENTER ITEM NAME", bg="green", relief="ridge", fg="white", font=("Times", 12, "bold"), width=25)
        self.entry1 = Entry(self.root, font=("Times", 12))
        self.label2 = Label(self.root, text="ENTER ITEM PRICE", bd="2", relief="ridge", height="1", bg="green", fg="white", font=("Times", 12, "bold"), width=25)
        self.entry2 = Entry(self.root, font=("Times", 12))
        self.label3 = Label(self.root, text="ENTER ITEM QUANTITY", bd="2", relief="ridge", bg="green", fg="white", font=("Times", 12, "bold"), width=25)
        self.entry3 = Entry(self.root, font=("Times", 12))
        self.label4 = Label(self.root, text="ENTER ITEM CATEGORY", bd="2", relief="ridge", bg="green", fg="white", font=("Times", 12, "bold"), width=25)
        self.entry4 = Entry(self.root, font=("Times", 12))
        self.label5 = Label(self.root, text="ENTER ITEM DISCOUNT", bg="green", relief="ridge", fg="white", font=("Times", 12, "bold"), width=25)
        self.entry5 = Entry(self.root, font=("Times", 12))
        self.button1 = Button(self.root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.add_item)
        self.button2 = Button(self.root, text="DELETE ITEM", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.delete_item)
        self.button3 = Button(self.root, text="VIEW FIRST ITEM", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.first_item)
        self.button4 = Button(self.root, text="VIEW NEXT ITEM", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.next_item)
        self.button5 = Button(self.root, text="VIEW PREVIOUS ITEM", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.previous_item)
        self.button6 = Button(self.root, text="VIEW LAST ITEM", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.last_item)
        self.button7 = Button(self.root, text="UPDATE ITEM", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.update_item)
        self.button8 = Button(self.root, text="SEARCH ITEM", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.search_item)
        self.button9 = Button(self.root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12, "bold"), command=self.clear_item)

        self.label0.grid(columnspan=6, padx=10, pady=10)
        self.label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
        self.label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        self.label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        self.label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
        self.label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)
        self.entry1.grid(row=1, column=1, padx=40, pady=10)
        self.entry2.grid(row=2, column=1, padx=10, pady=10)
        self.entry3.grid(row=3, column=1, padx=10, pady=10)
        self.entry4.grid(row=4, column=1, padx=10, pady=10)
        self.entry5.grid(row=5, column=1, padx=10, pady=10)
        self.button1.grid(row=1, column=4, padx=40, pady=10)
        self.button2.grid(row=1, column=5, padx=40, pady=10)
        self.button3.grid(row=2, column=4, padx=40, pady=10)
        self.button4.grid(row=2, column=5, padx=40, pady=10)
        self.button5.grid(row=3, column=4, padx=40, pady=10)
        self.button6.grid(row=3, column=5, padx=40, pady=10)
        self.button7.grid(row=4, column=4, padx=40, pady=10)
        self.button8.grid(row=4, column=5, padx=40, pady=10)
        self.button9.grid(row=5, column=5, padx=40, pady=10)

        
        self.tree = ttk.Treeview(self.root, columns=self.fields, show='headings')
        for field in self.fields:
            self.tree.heading(field, text=field)
            self.tree.column(field, minwidth=0, width=100)

        self.tree.grid(row=6, column=0, columnspan=6, padx=10, pady=10, sticky='nsew')

        
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=6, column=6, sticky='ns')

        self.populate_treeview()

    def populate_treeview(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Insert new data
        for row in self.data:
            self.tree.insert("", END, values=[row[field] for field in self.fields])


if __name__ == "__main__":
    root = Tk()
    app = PharmacyManagementSystem(root)
    root.mainloop()
