import tkinter as tk
from tkinter import messagebox
from services.tracker import Tracker

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")
        self.tracker = Tracker()

        self.amount_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.type_var = tk.StringVar(value="expense")

        tk.Label(root, text="Amount:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.amount_var).grid(row=0, column=1)

        tk.Label(root, text="Category:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.category_var).grid(row=1, column=1)

        tk.Label(root, text="Type:").grid(row=2, column=0)
        tk.OptionMenu(root, self.type_var, "income", "expense").grid(row=2, column=1)

        tk.Button(root, text="Add Transaction", command=self.add_transaction).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Show Report", command=self.show_report).grid(row=4, column=0, columnspan=2)

    def add_transaction(self):
        try:
            amount = float(self.amount_var.get())
            category = self.category_var.get()
            trans_type = self.type_var.get()
            self.tracker.add_transaction(amount, category, trans_type)
            messagebox.showinfo("Success", "Transaction added.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    def show_report(self):
        income = sum(t["amount"] for t in self.tracker.transactions if t["type"] == "income")
        expense = sum(t["amount"] for t in self.tracker.transactions if t["type"] == "expense")
        balance = income - expense
        messagebox.showinfo("Report", f"Income: ${income}\nExpense: ${expense}\nBalance: ${balance}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()
