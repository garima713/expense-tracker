# tests/test_project.py
# Plain assert tests. Run from the project folder with:
#   python tests/test_project.py

import os
import sys

# Let this file find the project modules that are in the parent folder.
project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_folder)

from expense import Expense
from expense_manager import add_expense, search_expenses, remove_expense
from budget import calculate_total, calculate_remaining, is_over_budget
from reports import category_totals, unique_categories, highest_expense, amounts_array
from input_utils import is_valid_amount


def make_sample_list():
    expenses = []
    add_expense(expenses, "Lunch", 100.0, "food")
    add_expense(expenses, "Bus Ticket", 50.5, "travel")
    add_expense(expenses, "Dinner", 25.0, "food")
    return expenses


def test_expense_class():
    expense = Expense("Notebook", 40.0, "education")
    assert expense.name == "Notebook"
    assert expense.amount == 40.0
    assert expense.category == "education"
    assert "Notebook" in expense.display_text()


def test_add_and_search():
    expenses = make_sample_list()
    assert len(expenses) == 3
    assert len(search_expenses(expenses, "lunch")) == 1      # not case sensitive
    assert len(search_expenses(expenses, "food")) == 2       # matches category
    assert len(search_expenses(expenses, "movie")) == 0


def test_remove():
    expenses = make_sample_list()
    removed = remove_expense(expenses, 2)
    assert removed.name == "Bus Ticket"
    assert len(expenses) == 2


def test_budget():
    expenses = make_sample_list()
    total = calculate_total(expenses)
    assert total == 175.5
    assert type(total) == float
    assert calculate_remaining(200.0, total) == 24.5
    assert not is_over_budget(200.0, total)
    assert is_over_budget(150.0, total)
    assert calculate_total([]) == 0.0


def test_reports():
    expenses = make_sample_list()
    totals = category_totals(expenses)
    assert totals["food"] == 125.0
    assert totals["travel"] == 50.5
    assert unique_categories(expenses) == {"food", "travel"}
    assert highest_expense(expenses) == ("Lunch", 100.0)
    assert highest_expense([]) is None


def test_amounts_array():
    expenses = make_sample_list()
    amounts = amounts_array(expenses)
    assert len(amounts) == 3
    assert sum(amounts) == 175.5
    assert max(amounts) == 100.0
    assert min(amounts) == 25.0


def test_amount_validation():
    assert is_valid_amount("250")
    assert is_valid_amount("99.50")
    assert is_valid_amount(".5")
    assert not is_valid_amount("0")
    assert not is_valid_amount("-5")
    assert not is_valid_amount("abc")
    assert not is_valid_amount("")
    assert not is_valid_amount("1.2.3")


test_expense_class()
test_add_and_search()
test_remove()
test_budget()
test_reports()
test_amounts_array()
test_amount_validation()

print("All tests passed.")
