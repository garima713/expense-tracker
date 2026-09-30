# input_utils.py
# Functions that read input from the user and check it.
# try/except is not used, so every value is checked BEFORE it is converted.

from constants import MIN_CHOICE, MAX_CHOICE, VALID_CATEGORIES


def is_valid_amount(text):
    # A valid amount is a positive number such as 250 or 99.50
    text = text.strip()
    digits_only = text.replace(".", "", 1)
    return digits_only.isdigit() and float(text) > 0


def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("Input cannot be empty. Please try again.")


def get_amount(prompt):
    while True:
        text = input(prompt)
        if is_valid_amount(text):
            return float(text)
        print("Please enter a positive number, for example 250 or 99.50.")


def get_category(prompt):
    print("Categories:", ", ".join(sorted(VALID_CATEGORIES)))
    while True:
        category = input(prompt).strip().lower()
        if category in VALID_CATEGORIES:
            return category
        print("Invalid category. Please choose one from the list.")


def get_menu_choice():
    while True:
        text = input("Enter your choice: ").strip()
        if text.isdigit():
            choice = int(text)
            if choice >= MIN_CHOICE and choice <= MAX_CHOICE:
                return choice
        print("Please enter a number from", MIN_CHOICE, "to", MAX_CHOICE)


def get_position(prompt, count):
    while True:
        text = input(prompt).strip()
        if text.isdigit():
            position = int(text)
            if position >= 1 and position <= count:
                return position
        print("Please enter a number from 1 to", count)
