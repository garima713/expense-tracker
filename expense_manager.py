# expense_manager.py
# Expense Management: add, view, search and remove expenses.
# The expenses are kept in a list that is passed to each function.

from expense import Expense


def add_expense(expenses, name, amount, category):
    expense = Expense(name, amount, category)
    expenses.append(expense)
    return expense


def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return
    position = 1
    for expense in expenses:
        print(str(position) + ". " + expense.display_text())
        position += 1


def search_expenses(expenses, keyword):
    keyword = keyword.lower()
    matches = []
    for expense in expenses:
        if keyword in expense.name.lower() or keyword in expense.category:
            matches.append(expense)
    return matches


def remove_expense(expenses, position):
    # position is the number shown by view_expenses (starts at 1)
    return expenses.pop(position - 1)
