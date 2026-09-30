# reports.py
# Reporting: total, category-wise report, highest expense and summary.

from array import array
from budget import calculate_total
from constants import CURRENCY


def total_report(expenses):
    total = calculate_total(expenses)
    print("Number of expenses:", len(expenses))
    print("Total expense     :", CURRENCY, f"{total:.2f}")


def category_totals(expenses):
    totals = {}
    for expense in expenses:
        if expense.category in totals:
            totals[expense.category] += expense.amount
        else:
            totals[expense.category] = expense.amount
    return totals


def unique_categories(expenses):
    categories = set()
    for expense in expenses:
        categories.add(expense.category)
    return categories


def category_report(expenses):
    totals = category_totals(expenses)
    categories = unique_categories(expenses)
    print("Categories used:", len(categories))
    for category in sorted(categories):
        print("  " + category + ":", CURRENCY, f"{totals[category]:.2f}")


def highest_expense(expenses):
    # Returns the pair (name, amount), or None if there are no expenses.
    if not expenses:
        return None
    highest = expenses[0]
    for expense in expenses:
        if expense.amount > highest.amount:
            highest = expense
    return (highest.name, highest.amount)


def highest_report(expenses):
    result = highest_expense(expenses)
    if result is None:
        print("No expenses recorded.")
    else:
        name, amount = result
        print("Highest expense:", name, "-", CURRENCY, f"{amount:.2f}")


def amounts_array(expenses):
    amounts = array("d")
    for expense in expenses:
        amounts.append(expense.amount)
    return amounts


def summary_report(expenses):
    amounts = amounts_array(expenses)
    total = sum(amounts)
    count = len(amounts)
    average = total / count
    print("Average expense:", CURRENCY, f"{average:.2f}")
    print("Smallest expense:", CURRENCY, f"{min(amounts):.2f}")
    print("Largest expense :", CURRENCY, f"{max(amounts):.2f}")


def generate_report(expenses):
    if not expenses:
        print("No expenses recorded, so there is nothing to report.")
        return
    print("--- Total Expense Report ---")
    total_report(expenses)
    print()
    print("--- Category-wise Report ---")
    category_report(expenses)
    print()
    print("--- Highest Expense ---")
    highest_report(expenses)
    print()
    print("--- Numerical Summary ---")
    summary_report(expenses)
