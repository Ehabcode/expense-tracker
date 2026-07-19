from expenses import add_expense
from storage import load_expenses, save_expenses

expenses = load_expenses()

while True:
    print ("expense menu")
    print ("1. Add expense")
    print ("2. View all expenses")
    print ("3. Exit")

    choice = int(input("Enter your choice from (1-3): "))

    if choice > 3 or choice < 1:
        print("Exiting the program.")
        break

    elif choice == 1:
        expense_category = input("enter category: ")
        expense_amount = float(input("enter amount: "))
        expense_description = input("enter description: ")
        add_expense(expense_category, expense_amount, expense_description, expenses)
        save_expenses(expenses)
        print("Expense added successfully!")
        
    elif choice == 2:
        for expense in expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

