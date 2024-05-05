import tkinter as tk
from tkinter import messagebox

used_priorities = set()  # Set to store used priorities

def add_task():
    task_name = task_entry.get()
    priority = priority_entry.get()
    due_date = due_date_entry.get()
    
    # Validate priority to ensure it's a number
    try:
        priority = int(priority)
    except ValueError:
        # If priority is not a valid number, show an error message
        messagebox.showerror("Error", "Priority must be a number.")
        return
    
    # Check if task name is provided and priority is not negative
    if task_name and priority >= 0:
        if priority in used_priorities:
            # If the priority is already used, show an error message
            messagebox.showerror("Error", f"Priority {priority} is already in use.")
            return
        used_priorities.add(priority)  # Add the priority to used priorities set
        tasks_listbox.insert(tk.END, f"Task: {task_name} - Priority: {priority} - Due Date: {due_date}")
    else:
        # If task name is not provided or priority is negative, show an error message
        messagebox.showerror("Error", "Task name is required and priority must be a non-negative number.")

def complete_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        tasks_listbox.itemconfig(selected_index, {'bg': 'light grey', 'fg': 'grey'})

root = tk.Tk()
root.title("To-Do List")

input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

list_frame = tk.Frame(root, padx=10, pady=10)
list_frame.pack()

tk.Label(input_frame, text="Task:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
task_entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
task_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Priority:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
priority_entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
priority_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Due Date:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
due_date_entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
due_date_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

complete_button = tk.Button(input_frame, text="Mark Complete", font=("Helvetica", 12), command=complete_task)
complete_button.grid(row=4, column=0, columnspan=2, pady=10)

tasks_listbox = tk.Listbox(list_frame, width=50, height=10, font=("Helvetica", 12))
tasks_listbox.pack()

root.mainloop()
