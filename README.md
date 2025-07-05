# 💰 Finance Tracker

A personal finance tracking tool with a CLI, GUI, and JSON-based data storage. Easily manage income and expenses, generate reports, and keep your spending organized.

---

## 🚀 Features

- ✅ Add, remove, and list transactions from the command line
- 🪟 GUI built with Tkinter
- 📊 Generate income/expense reports
- 📁 JSON file storage for simplicity and portability
- 🧪 Unit tests with `unittest`

---

## 📦 Requirements

- Python 3.8+
- Tkinter (comes bundled with most Python installs)

---

## 📂 Project Structure

```
finance-tracker/
├── main.py                 # Entry point
├── cli.py                  # Command-line interface
├── gui.py                  # Graphical UI using tkinter
├── services/
│   └── tracker.py          # Core logic for managing transactions
├── models/
│   └── transaction.py      # Transaction model
├── tests/
│   └── test_tracker.py     # Unit tests
├── data/
│   └── transactions.json   # Transaction storage (created automatically)
├── pyproject.toml
└── README.md
```

---

## 🧑‍💻 CLI Usage

```bash
# Add a transaction
python main.py add --amount 100 --category groceries --type expense

# List all transactions
python main.py list

# Remove a transaction
python main.py remove --id 1625647382

# Generate a simple report
python main.py report
```

---

## 🖼️ GUI Usage

```bash
python gui.py
```

- Fill in amount, category, and type (income/expense)
- Click “Add Transaction” to save
- Click “Show Report” to view a summary

---

## 🧪 Running Tests

```bash
python -m unittest discover tests
```

---

## 📌 Future Enhancements

- SQLite or PostgreSQL backend
- Charts using `matplotlib` or `plotly`
- Filtering by date or category
- Export to CSV/PDF

---

## 📜 License

MIT License © 2025 Your Name