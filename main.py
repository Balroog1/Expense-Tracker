"""
Expense Tracker
Version: 0.9

Author: Abhinav
"""

import sqlite3

DATABASE_FILE = "expenses.db"
TABLE_NAME = "expenses"

expenses = []

def initialize_database():
    """Create the SQLite database if it doesn't exist."""

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT NOT NULL,
        payment_method TEXT NOT NULL
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()

def get_database_connection():
    """Return a connection to the SQLite database."""

    return sqlite3.connect(DATABASE_FILE)

def save_expense_to_database(expense):
    """Save one expense into the SQLite database."""
    connection = get_database_connection()
    cursor = connection.cursor()

    insert_query = f"""
    INSERT INTO {TABLE_NAME} (
        amount,
        category,
        description,
        payment_method
    )
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(
        insert_query,
        (
            expense["amount"],
            expense["category"],
            expense["description"],
            expense["payment_method"]
        )
    )
    connection.commit()
    connection.close()

def load_expenses_from_database():
    """Load all expenses from the SQLite database."""
    
    connection = get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT * FROM {TABLE_NAME}"

    cursor.execute(select_query)
    rows = cursor.fetchall()
    expenses.clear()
    for row in rows:
        expense = {
            "amount": row[1],
            "category": row[2],
            "description": row[3],
            "payment_method": row[4]
        }

        expenses.append(expense)
    connection.close()    
    

def display_menu():
    """Display the main menu."""

    print("=" * 40)
    print("      Personal Expense Tracker")
    print("=" * 40)

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Report")
    print("4. Exit")

def get_valid_amount():
    """Ask the user for a valid expense amount."""

    while True:

        try:

            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.\n")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Please enter a number.\n")


def add_expense():
    """Collect expense details from the user."""

    print("\n----- Add Expense -----")

    amount = get_valid_amount()
    category = input("Category: ")
    description = input("Description: ")
    payment_method = input("Payment Method: ")

    expense = {
    "amount": amount,
    "category": category,
    "description": description,
    "payment_method": payment_method
    }
    expenses.append(expense)

    save_expense_to_database(expense)
    
    print("\nExpense Added Successfully!")

    print("\nExpense Details")

    print(f"Amount          : {amount}")
    print(f"Category        : {category}")
    print(f"Description     : {description}")
    print(f"Payment Method  : {payment_method}")

def view_expenses():
    print("\n" + "=" * 50)
    print("              VIEW EXPENSES")
    print("=" * 50)

    if not expenses:
        print("No expenses found.")
    else:
        for index, expense in enumerate(expenses, start=1):
            print(f"\nExpense #{index}")
            print("-" * 50)
            print(f"Amount          : {expense['amount']:.2f}")
            print(f"Category        : {expense['category']}")
            print(f"Description     : {expense['description']}")
            print(f"Payment Method  : {expense['payment_method']}")
            print()

        print("=" * 50)    

def print_statistics(number_of_expenses,
                     total_expense,
                     highest_expense,
                     lowest_expense,
                     average_expense):
    """Display general expense statistics."""

    print("\nGeneral Statistics")
    print("-" * 18)

    print(f"Number of Expenses : {number_of_expenses}")
    print(f"Total Expenses     : {total_expense:.2f}")
    print(f"Highest Expense    : {highest_expense:.2f}")
    print(f"Lowest Expense     : {lowest_expense:.2f}")
    print(f"Average Expense    : {average_expense:.2f}")

def print_breakdown(title, totals):
    """Display a formatted breakdown report."""

    print("\n" + "-" * 50)
    print(title)
    print("-" * len(title))

    for key, total in totals.items():
        print(f"{key:<18}: {total:.2f}")


def generate_report():
    """Generate and display an expense summary."""

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 50)
    print("               EXPENSE REPORT")
    print("=" * 50)

    number_of_expenses = len(expenses)
    
    total_expense = 0
    highest_expense = expenses[0]["amount"]
    lowest_expense = expenses[0]["amount"]

    category_totals = {}
    payment_totals = {}

    for expense in expenses:
        total_expense += expense["amount"]

        if expense["amount"] > highest_expense:
            highest_expense = expense["amount"]
           
        if expense["amount"] < lowest_expense:
            lowest_expense = expense["amount"]

        category = expense["category"]
        amount = expense["amount"]    
        payment_method = expense["payment_method"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

        if payment_method in payment_totals:
            payment_totals[payment_method] += amount
        else:
            payment_totals[payment_method] = amount    
            
    average_expense = total_expense / number_of_expenses


    print_statistics(
       number_of_expenses,
       total_expense,
       highest_expense,
       lowest_expense,
       average_expense
    )

    print_breakdown("Category Breakdown", category_totals)
    
    print_breakdown("Payment Method Breakdown", payment_totals)
   
    print("\n" + "=" * 50)

       
    
def main():

    """Main application loop."""

    print("\nStarting Expense Tracker...\n")
    
    initialize_database()
    load_expenses_from_database()

    print("Expense database loaded successfully.\n")

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            generate_report()

        elif choice == "4":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid Choice! Please try again.")


main()