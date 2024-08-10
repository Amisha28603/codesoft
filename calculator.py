import tkinter as tk
from tkinter import messagebox

def button_click(value):
    current = entry_display.get()
    if value == 'AC':
        entry_display.delete(0, tk.END)
    elif value == 'C':
        entry_display.delete(len(current) - 1, tk.END)
    elif value == '=':
        try:
            result = eval(current)
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input or calculation error.")
    elif value == '%':
        try:
            result = eval(current) / 100
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for percentage.")
    else:
        entry_display.insert(tk.END, value)

root = tk.Tk()
root.title("Simple Calculator")

entry_display = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0','.', '=', '+'),
    ('AC', 'C','%')
]
for row_idx, row in enumerate(buttons):
    for col_idx, button in enumerate(row):
        tk.Button(root, text=button, width=5, height=3, font=('Arial', 18), command=lambda b=button: button_click(b)).grid(row=row_idx+1, column=col_idx, padx=5, pady=5)

root.mainloop()
