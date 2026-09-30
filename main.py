# main.py
# Command-line menu for the Expense Tracker and Report System.
# Run with:  python main.py

from constants import MENU_OPTIONS
from input_utils import get_text, get_amount, get_category, get_menu_choice, get_position
from expense_manager import add_expense, view_expenses, search_expenses, remove_expense
from budget import budget_status
from reports import generate_report


def show_menu():
    print()
    print("===== Expense Tracker =====")
    for option in MENU_OPTIONS:
        print(option)


def main():
    expenses = []
    budget = None

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            name = get_text("Expense name: ")
            amount = get_amount("Amount: ")
            category = get_category("Category: ")
            add_expense(expenses, name, amount, category)
            print("Expense added.")
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            keyword = get_text("Search by name or category: ")
            matches = search_expenses(expenses, keyword)
            if matches:
                view_expenses(matches)
            else:
                print("No matching expenses found.")
        elif choice == 4:
            if not expenses:
                print("No expenses to remove.")
            else:
                view_expenses(expenses)
                position = get_position("Number of the expense to remove: ", len(expenses))
                removed = remove_expense(expenses, position)
                print("Removed:", removed.display_text())
        elif choice == 5:
            budget = get_amount("Enter your budget: ")
            print("Budget set.")
        elif choice == 6:
            budget_status(budget, expenses)
        elif choice == 7:
            generate_report(expenses)
        else:
            print("Thank you for using Expense Tracker. Goodbye!")
            break


main()
