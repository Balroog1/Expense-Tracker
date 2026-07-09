"""
Expense Tracker
Version: 0.8

Author: Abhinav
"""
import csv
import os

CSV_FILE = "expenses.csv"
expenses = []

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

    save_expense_to_csv(expense)
    
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

def initialize_csv():
    """Create expenses.csv with headers if it does not exist."""

    print("Initializing storage...")

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Amount",
                "Category",
                "Description",
                "Payment Method"
            ])
    print("Storage ready.\n")        

def save_expense_to_csv(expense):
    """Save a single expense to the CSV file."""

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            expense["amount"],
            expense["category"],
            expense["description"],
            expense["payment_method"]
        ])

def load_expenses_from_csv():
    """Load all expenses from the CSV file into memory."""

    print("Loading expenses...")

    expenses.clear()
    invalid_rows = 0

    with open(CSV_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            try:
                expense = {
                    "amount": float(row["Amount"]),
                    "category": row["Category"],
                    "description": row["Description"],
                    "payment_method": row["Payment Method"],
                }

                expenses.append(expense)

            except (ValueError, KeyError):
                invalid_rows += 1
                print("Warning: Skipped an invalid expense record.")

    if expenses:
        print(f"Loaded {len(expenses)} expense(s).")
    else:
        print("No previous expenses found.")

    if invalid_rows > 0:
        print(f"Warning: Skipped {invalid_rows} invalid record(s).")

    print() 

    
def main():

    """Main application loop."""

    print("\nStarting Expense Tracker...\n")
    
    initialize_csv()
    load_expenses_from_csv()

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