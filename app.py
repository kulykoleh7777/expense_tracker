import json

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_expense(amount, category):
    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category})
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

add_expense(20, "Transport")
