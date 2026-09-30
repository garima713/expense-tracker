# Expense Tracker and Report System

## Overview
A command-line Python program for recording expenses, checking them against a budget and producing simple reports. It is a first-year Python Essentials course project and uses only basic Python concepts from the course syllabus.

## Features
- **Expense Management:** add, view, search (by name or category) and remove expenses.
- **Budget Management:** set a budget, calculate total spending and remaining budget, and warn when spending crosses the budget.
- **Reporting:** total expense report, category-wise report, highest expense and a numerical summary (average, smallest, largest).
- Simple numbered menu; input is checked without exception handling.

Note: data is kept in memory only. When the program exits, the expenses and budget are lost.

## Technologies Used
- Python 3 (standard library only; the `array` module is used for expense amounts in reports)
- Lists, dictionaries, sets, tuples, frozenset, functions, modules and one simple class
- Plain `assert` statements for testing

## Project Structure
```
expense-tracker/
├── main.py             # menu and program loop
├── expense.py          # Expense class
├── expense_manager.py  # add, view, search, remove
├── budget.py           # total, remaining budget, budget check
├── reports.py          # reports and summary
├── input_utils.py      # reading and checking user input
├── constants.py        # menu text and valid categories
├── tests/
│   └── test_project.py # assert-based tests
├── README.md
├── statement.md
└── .gitignore
```

## Installation / Setup
1. Install Python 3 (no other packages are needed).
2. Download or copy the `expense-tracker` folder.
3. Open a terminal inside the `expense-tracker` folder.

## How to Run
```
python main.py
```
Type the number of a menu option and press Enter.

Input rules:
- Menu choice: a whole number from 1 to 8.
- Amount and budget: a positive number, for example `250` or `99.50` (no letters, no minus sign, no commas).
- Category: one of `bills`, `education`, `food`, `health`, `other`, `shopping`, `travel` (upper or lower case).
- Names and search words must not be empty.
- If the input is not valid, the program shows a message and asks again.

## How to Test
From the project folder:
```
python tests/test_project.py
```
If everything is correct, it prints `All tests passed.`

## Example Usage
```
===== Expense Tracker =====
1. Add Expense
...
8. Exit
Enter your choice: 5
Enter your budget: 200
Budget set.

Enter your choice: 1
Expense name: Lunch
Amount: 100
Category: food
Expense added.

Enter your choice: 6
Budget         : Rs. 200.00
Total spent    : Rs. 175.50
Remaining      : Rs. 24.50
You are within your budget.

Enter your choice: 7
--- Total Expense Report ---
Number of expenses: 3
Total expense     : Rs. 175.50

--- Category-wise Report ---
Categories used: 2
  food: Rs. 125.00
  travel: Rs. 50.50

--- Highest Expense ---
Highest expense: Lunch - Rs. 100.00

--- Numerical Summary ---
Average expense: Rs. 58.50
Smallest expense: Rs. 25.00
Largest expense : Rs. 100.00
```
