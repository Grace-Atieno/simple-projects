import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.configure(bg="#f2f2f2")

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        tasks.clear()
        update_listbox()

# Entry field
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=20)

# Add Button
add_btn = tk.Button(root, text="Add Task", width=15, command=add_task, bg="#4CAF50", fg="white")
add_btn.pack()

# Listbox to show tasks
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

# Delete Button
delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task, bg="#f44336", fg="white")
delete_btn.pack(pady=5)

# Clear All Button
clear_btn = tk.Button(root, text="Clear All", width=15, command=clear_tasks, bg="#ff9800", fg="white")
clear_btn.pack(pady=5)

# Start GUI loop
root.mainloop()
