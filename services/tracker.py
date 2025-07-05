import json
import os
from models.transaction import Transaction

class Tracker:
    def __init__(self, file_path="data/transactions.json"):
        self.file_path = file_path
        self.transactions = self._load_transactions()

    def _load_transactions(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _save_transactions(self):
        with open(self.file_path, "w") as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, amount, category, trans_type):
        transaction = Transaction.create(amount, category, trans_type)
        self.transactions.append(transaction)
        self._save_transactions()
        print("Transaction added.")

    def remove_transaction(self, trans_id):
        self.transactions = [t for t in self.transactions if t["id"] != trans_id]
        self._save_transactions()
        print("Transaction removed.")

    def list_transactions(self):
        for t in self.transactions:
            print(t)

    def generate_report(self):
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        print(f"Total Income: ${income}")
        print(f"Total Expense: ${expense}")
        print(f"Balance: ${income - expense}")

