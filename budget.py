# budget.py
# Budget Management: total spending, remaining budget and budget check.

from constants import CURRENCY


def calculate_total(expenses):
    total = 0.0
    for expense in expenses:
        total += expense.amount
    return total


def calculate_remaining(budget, total):
    return budget - total


def is_over_budget(budget, total):
    return total > budget


def budget_status(budget, expenses):
    # budget is None until the user sets it
    if budget is None:
        print("No budget set. Use option 5 to set a budget.")
        return
    total = calculate_total(expenses)
    remaining = calculate_remaining(budget, total)
    print("Budget         :", CURRENCY, f"{budget:.2f}")
    print("Total spent    :", CURRENCY, f"{total:.2f}")
    print("Remaining      :", CURRENCY, f"{remaining:.2f}")
    if is_over_budget(budget, total):
        print("WARNING: You have crossed your budget by", CURRENCY, f"{-remaining:.2f}")
    else:
        print("You are within your budget.")
