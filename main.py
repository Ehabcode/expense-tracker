from expenses import add_expense
from storage import load_expenses, save_expenses
from reports import total_expenses

expenses = load_expenses()

while True:
    print ("Expense menu")
    print ("1. Add expense")
    print ("2. View all expenses")
    print ("3. To delete the history")
    print ("4. view report")
    print ("5. Exit")

    choice = int(input("Enter your choice from (1-5): "))

    if choice > 5 or choice < 1:
        print("Poor input, Please enter a valid choice from (1-5) next time.")
        break


    elif choice == 1:

        expense_category = input("Enter category: ")
        expense_amount = float(input("Enter amount: "))
        expense_description = input("Enter description: ")
        add_expense(expense_category, expense_amount, expense_description, expenses)
        save_expenses(expenses)
        print("Expense added successfully!")
        

    elif choice == 2:

        for expense in expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")


    elif choice == 3:

        expenses.clear()
        save_expenses(expenses)
        print("All expenses have been deleted.")


    elif choice == 4:
       total = total_expenses(expenses)
       print(f"total expenses: {total}")


    elif choice == 5:
        

        print("Exiting the program.")
        break
