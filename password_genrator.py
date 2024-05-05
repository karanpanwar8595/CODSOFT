
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_entry.get()

    if length.isdigit() and int(length) > 0:
        length = int(length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_display.config(text=f"Generated Password: {password}")
        generated_password = password  # Store generated password for copying
    else:
        messagebox.showerror("Error", "Please enter a valid positive integer for length.")

def copy_password():
    if password_display.cget("text") != "Generated Password will appear here.":
        pyperclip.copy(password_display.cget("text").split(": ")[1])
        messagebox.showinfo("Info", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_display = tk.Label(root, text="Generated Password will appear here.", wraplength=200)
password_display.pack(pady=20)

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack(pady=5)

root.mainloop()

