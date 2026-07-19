import json

def load_expenses():
    with open("data/expenses.json", "r") as file:
        expenses = json.load(file)
        return expenses

def save_expenses(expenses_list):
    with open("data/expenses.json", "w") as file:
        json.dump(expenses_list, file, indent=4)



