"""
Expense Tracker
Version: 0.5

Author: Abhinav
"""

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

    print("\nExpense Added Successfully!")

    print("\nExpense Details")

    print(f"Amount          : {amount}")
    print(f"Category        : {category}")
    print(f"Description     : {description}")
    print(f"Payment Method  : {payment_method}")

    print("\nCurrent Expenses:")

    for expense in expenses:
        print(expense)

def generate_report():
    """Generate and display an expense summary."""

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n========== Expense Report ==========")

    number_of_expenses = len(expenses)
    
    total_expense = 0

    for expense in expenses:
        total_expense += expense["amount"]

    print(f"Number of Expenses : {number_of_expenses}")
    print(f"Total Expenses     : {total_expense}")

def main():

    """Main application loop."""

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            print("\n----- View Expenses -----")

            if not expenses:
                print("No expenses found.")

            else:
                for index, expense in enumerate(expenses, start=1):
                    print(f"\nExpense {index}")
                    print(f"Amount          : {expense['amount']}")
                    print(f"Category        : {expense['category']}")
                    print(f"Description     : {expense['description']}")
                    print(f"Payment Method  : {expense['payment_method']}")

        elif choice == "3":
            generate_report()

        elif choice == "4":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid Choice! Please try again.")


main()