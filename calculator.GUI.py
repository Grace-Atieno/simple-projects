import tkinter as tk

def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=4, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Create buttons
row = 1
col = 0
for b in buttons:
    tk.Button(root, text=b, width=5, height=2, font=('Arial', 18),
              command=lambda b=b: click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="C", width=22, height=2, font=('Arial', 18),
          command=lambda: click("C")).grid(row=row, column=0, columnspan=4, padx=5, pady=5)

# Start the app
root.mainloop()

