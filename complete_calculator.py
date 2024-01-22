import math
import tkinter as tk
from tkinter import messagebox

def perform_operation():
    try:
        operation = int(operation_var.get())
        
        if operation == 1:  # performs addition
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            result = num1 + num2
            result_label.config(text=f"Result: {result}")
          
        elif operation == 2:  # performs subtraction
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            result = num1 - num2
            result_label.config(text=f"Result: {result}")

        elif operation == 3:  # performs division
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            if num2 != 0:
                result = num1 / num2
                result_label.config(text=f"Result: {result}")
            else:
                messagebox.showerror("Error", "You cannot divide by zero")

        elif operation == 4:  # performs multiplication
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            result = num1 * num2
            result_label.config(text=f"Result: {result}")

        elif operation == 5:  # perform square root
            num = float(entry_num1.get())
            result = math.sqrt(num)
            result_label.config(text=f"Result: {result}")

        elif operation == 6:  # performs raise to power
            base_num = float(entry_num1.get())
            exponent_num = float(entry_num2.get())
            result = pow(base_num, exponent_num)
            result_label.config(text=f"Result: {result}")

        else:
            messagebox.showerror("Error", "You have entered an invalid choice")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Operation selection
operation_var = tk.StringVar(window)
operation_var.set("1")  # default value
operation_label = tk.Label(window, text="Select Operation:")
operation_menu = tk.OptionMenu(window, operation_var, "1", "2", "3", "4", "5", "6")

# Input fields
entry_num1 = tk.Entry(window, width=10)
entry_num2 = tk.Entry(window, width=10)

# Result display
result_label = tk.Label(window, text="Result: ")

# Perform Button
perform_button = tk.Button(window, text="Perform Operation", command=perform_operation)

# Layout
operation_label.grid(row=0, column=0, pady=5)
operation_menu.grid(row=0, column=1, pady=5)
entry_num1.grid(row=1, column=0, pady=5)
entry_num2.grid(row=1, column=1, pady=5)
perform_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
