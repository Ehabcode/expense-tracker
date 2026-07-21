def total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)
