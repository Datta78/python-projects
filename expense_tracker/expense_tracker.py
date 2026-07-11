# Simple Expense Tracker - Dattatray Bhosale
# For Job Portfolio

import json
from datetime import datetime

EXPENSES_FILE = "expenses.json"

def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Transport, etc): ")
    description = input("Enter description: ")
    
    expense = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "amount": amount,
        "category": category,
        "description": description
    }
    
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    
    total = 0
    print("\n--- All Expenses ---")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | Rs.{exp['amount']} | {exp['description']}")
        total += exp['amount']
    print(f"\nTotal Spent: Rs.{total}")

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
