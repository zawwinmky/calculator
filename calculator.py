from cgitb import reset
from tkinter import *
from tkinter import messagebox

from numpy.ma.core import multiply

# Create the main window
root = Tk()
root.title("Simple Calculator App by DCS-146")
root.geometry("400x300")
root.configure(bg="lightskyblue")

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        messagebox.showinfo("showinfo", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("show error", "Please enter valid numbers.")

def calculate_sub():
    try:
        num_1 = float(entry1.get())
        num_2 = float(entry2.get())
        result = num_1 - num_2
        messagebox.showinfo("Result", f"The subtraction is: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def calculate_multiply():
    try:
        num_1 = float(entry1.get())
        num_2 = float(entry2.get())
        result = num_1 * num_2
        messagebox.showinfo("Result", f"The multiplication is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def calculate_divide():
    try:
        num_1 = float(entry1.get())
        num_2 = float(entry2.get())
        if num_2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero")
        else:
            result = round(num_1/num_2, 2)
            messagebox.showinfo("Result", f"The division is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


label1 = Label(root, text="Enter first number:", bg='grey')
label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry1 = Entry(root, width=20, bg='grey', selectforeground='lightskyblue')
entry1.grid(row=0, column=1, padx=5, pady=5)

# Label and Entry for the second number (in the next row)
label2 = Label(root, text="Enter second number:", bg='grey')
label2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry2 = Entry(root, width=20, bg='grey', selectforeground='lightskyblue')
entry2.grid(row=1, column=1, padx=5, pady=5)

# Buttons for calculations (each in a new row, spanning two columns)
sum_button = Button(root, text="Calculate Sum", command=calculate_sum, bg='lightskyblue')
sum_button.grid(row=2, column=0, columnspan=2, pady=5)

sub_button = Button(root, text="Calculate Subtraction", command=calculate_sub, bg='lightskyblue')
sub_button.grid(row=3, column=0, columnspan=2, pady=5)

multiply_button = Button(root, text="Calculate Multiplication", command=calculate_multiply, bg='lightskyblue')
multiply_button.grid(row=4, column=0, columnspan=2, pady=5)

divide_button = Button(root, text="Calculate Division", command=calculate_divide, bg='lightskyblue')
divide_button.grid(row=5, column=0, columnspan=2, pady=5)
# Run the application
root.mainloop()