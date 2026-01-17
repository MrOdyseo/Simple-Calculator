import tkinter as tk
from tkinter import messagebox

def evaluate():
    choice = math_choice.get()
    entry1 = num_1.get()
    entry2 = num_2.get()

    if not validate_input(entry1):
        messagebox.showwarning("Math Error!", "Please enter a valid number, higher than 0")
        num_1.focus()
    if not validate_input(entry2):
        messagebox.showwarning("Math Error!", "Please enter a valid number, higher than 0")
        num_2.focus()
    
    num1 = int(entry1)
    num2 = int(entry2)

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 / num2
    elif choice == "4":
        result = num1 * num2
    messagebox.showinfo("Result", f"Result = {result}")    

def validate_input(value):
    if value == "":
        return False
    return value.isdigit() and int(value) > 0

calc = tk.Tk()
calc.title("Calculator")
num_1 = tk.Entry(calc)
num_1.grid(row = 2, column = 1)
num_2 = tk.Entry(calc)
num_2.grid(row = 2, column = 3)

math_choice = tk.StringVar()
math_choice.set("1")
sum_choice = tk.Radiobutton(calc, text = "+", variable = math_choice, value="1")
minus_choice = tk.Radiobutton(calc, text = "-", variable = math_choice, value="2")
div_choice = tk.Radiobutton(calc, text = "/", variable = math_choice, value="3")
mult_choice = tk.Radiobutton(calc, text = "*", variable = math_choice, value="4")
sum_choice.grid(row = 1, column = 2)
minus_choice.grid(row = 2, column = 2)
div_choice.grid(row = 3, column = 2)
mult_choice.grid(row = 4, column = 2)

eval_button = tk.Button(text = "Evaluate", command = evaluate)
eval_button.grid(row = 5, column = 2)

calc.mainloop()
