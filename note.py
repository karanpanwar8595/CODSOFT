import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry fields for contact details
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for operations
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, padx=5, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, padx=5, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, padx=5, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, padx=5, pady=10)

        # Listbox to display contacts
        self.contacts_listbox = tk.Listbox(self.root, width=40, height=10)
        self.contacts_listbox.grid(row=9, column=0, columnspan=2, padx=5, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:  # Check if name and phone are provided
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)  # Clear existing contacts
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = self.name_entry.get()
        search_results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
        self.contacts_listbox.delete(0, tk.END)  # Clear existing contacts
        for result in search_results:
            self.contacts_listbox.insert(tk.END, f"{result.name} - {result.phone}")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            updated_phone = self.phone_entry.get()
            updated_email = self.email_entry.get()
            updated_address = self.address_entry.get()
            selected_contact.phone = updated_phone
            selected_contact.email = updated_email
            selected_contact.address = updated_address
            self.clear_entries()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact from the list.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.view_contacts()  # Refresh contacts list
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact from the list.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
