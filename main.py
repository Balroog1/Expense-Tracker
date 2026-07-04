"""
Expense Tracker
Version: 0.3

Author: Abhinav
"""


def display_menu():
    """Display the main menu."""

    print("=" * 40)
    print("      Personal Expense Tracker")
    print("=" * 40)

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Report")
    print("4. Exit")


def add_expense():
    """Collect expense details from the user."""

    print("\n----- Add Expense -----")

    amount = input("Amount: ")
    category = input("Category: ")
    description = input("Description: ")
    payment_method = input("Payment Method: ")

    print("\nExpense Added Successfully!")

    print("\nExpense Details")

    print(f"Amount          : {amount}")
    print(f"Category        : {category}")
    print(f"Description     : {description}")
    print(f"Payment Method  : {payment_method}")


def main():

    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        print("\nView Expense feature coming soon!")

    elif choice == "3":
        print("\nGenerate Report feature coming soon!")

    elif choice == "4":
        print("\nThank you for using Expense Tracker!")

    else:
        print("\nInvalid Choice!")


main()