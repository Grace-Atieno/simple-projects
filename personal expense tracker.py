import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("400x500")
root.configure(bg="white")

expenses = []
total_amount = 0

# Function to add expense
def add_expense():
    global total_amount
    name = entry_name.get()
    amount = entry_amount.get()

    if name == "" or amount == "":
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number")
        return

    expenses.append((name, amount))
    total_amount += amount

    listbox.insert(tk.END, f"{name}: Ksh {amount}")
    label_total.config(text=f"Total: Ksh {total_amount}")

    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Heading
tk.Label(root, text="Expense Tracker", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

# Name input
tk.Label(root, text="Expense Name", bg="white").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Amount input
tk.Label(root, text="Amount (Ksh)", bg="white").pack()
entry_amount = tk.Entry(root, width=30)
entry_amount.pack(pady=5)

# Add button
btn_add = tk.Button(root, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white", padx=10, pady=5)
btn_add.pack(pady=10)

# Listbox to show expenses
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Total display
label_total = tk.Label(root, text="Total: Ksh 0", font=("Helvetica", 14), bg="white")
label_total.pack(pady=10)

# Run the GUI
root.mainloop()
