# expense.py
# The Expense class: one object represents one expense.

from constants import CURRENCY


class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def display_text(self):
        return self.name + " | " + self.category + " | " + CURRENCY + " " + f"{self.amount:.2f}"
