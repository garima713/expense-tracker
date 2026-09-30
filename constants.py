# constants.py
# Fixed values shared by the whole project.

CURRENCY = "Rs."

MENU_OPTIONS = [
    "1. Add Expense",
    "2. View Expenses",
    "3. Search Expense",
    "4. Remove Expense",
    "5. Set Budget",
    "6. View Budget Status",
    "7. Generate Report",
    "8. Exit",
]

MIN_CHOICE = 1
MAX_CHOICE = 8

# The allowed categories never change while the program runs,
# so a frozenset is used. It is only needed for membership checks.
VALID_CATEGORIES = frozenset({
    "food",
    "travel",
    "shopping",
    "bills",
    "health",
    "education",
    "other",
})
