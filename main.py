from expenses import add_expense
from storage import load_expenses, save_expenses

expenses = load_expenses()

while True:
    print ("expense menu")
    print ("1. Add expense")
    print ("2. View all expenses")
    print ("3. to delete the history")
    print ("4. Exit")

    choice = int(input("Enter your choice from (1-4): "))

    if choice > 4 or choice < 1:
        print("Poor input, please enter a valid choice from (1-4) next time.")
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

    elif choice == 3:
        expenses.clear()
        print("All expenses have been deleted.")

    elif choice == 4:
        print("Exiting the program.")
        break
