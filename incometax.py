import tkinter as tk
from tkinter import messagebox


def calculate_income_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (500000 - 250000) * 0.05 + (income - 500000) * 0.20
    else:
        tax = (500000 - 250000) * 0.05 + (1000000 - 500000) * 0.20 + (income - 1000000) * 0.30
    
    return tax

def display_tax_slabs(income):
    breakdown = "\nIncome Breakdown by Slabs:\n"
    breakdown += "Slab                Amount to Tax       Rate     Tax Amount\n"
    
    if income > 250000:
        slab_1_tax = (min(250000, income) - 0) * 0.00
        breakdown += f"₹0 - ₹2,50,000     ₹{min(250000, income):,.2f}        Nil      ₹{slab_1_tax:,.2f}\n"
        
    if income > 250000:
        slab_2_tax = (min(500000, income) - 250000) * 0.05
        breakdown += f"₹2,50,000 - ₹5L    ₹{min(500000, income) - 250000:,.2f}    5%       ₹{slab_2_tax:,.2f}\n"

    if income > 500000:
        slab_3_tax = (min(1000000, income) - 500000) * 0.20
        breakdown += f"₹5,00,000 - ₹10L   ₹{min(1000000, income) - 500000:,.2f}    20%      ₹{slab_3_tax:,.2f}\n"

    if income > 1000000:
        slab_4_tax = (income - 1000000) * 0.30
        breakdown += f"Above ₹10L         ₹{income - 1000000:,.2f}       30%      ₹{slab_4_tax:,.2f}\n"

    return breakdown

def on_calculate():
    try:
        name = name_entry.get()
        income = float(income_entry.get())
        
        if income <= 0:
            raise ValueError("Income must be a positive number.")

        tax = calculate_income_tax(income)

        breakdown = display_tax_slabs(income)
        result_label.config(text=f"{name}, your total calculated income tax is: ₹{tax:,.2f}")
        breakdown_label.config(text=breakdown)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))



root = tk.Tk()
root.title("Income Tax Calculator")

name_label = tk.Label(root, text="Enter your name:")
name_label.grid(row=0, column=0, padx=10, pady=10)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

income_label = tk.Label(root, text="Enter your taxable income (₹):")
income_label.grid(row=1, column=0, padx=10, pady=10)

income_entry = tk.Entry(root)
income_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Tax", command=on_calculate)
calculate_button.grid(row=2, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

breakdown_label = tk.Label(root, text="", justify="left")
breakdown_label.grid(row=4, columnspan=2, padx=10, pady=10)


root.mainloop()
