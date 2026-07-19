from datetime import date
def get_today_date():
    today = date.today()
    return str(today)

def add_expense(category, amount, description, expense_list):
    new_id = len(expense_list) + 1
    expense = {
        'id': new_id,
        'amount': amount,
        'description': description,
        'category': category,
        'date': get_today_date()
    }
    expense_list.append(expense)

if __name__ == "__main__":
    my_expenses = []
    add_expense("Food", 50.5, "Lunch", my_expenses)
    add_expense("Transport", 20, "Uber", my_expenses)
    print(my_expenses)
    