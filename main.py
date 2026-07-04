"""
Expense Tracker
Version: 0.2

Author: Abhinav
"""

print("=" * 40)
print("      Personal Expense Tracker")
print("=" * 40)

print("\n1. Add Expense")
print("2. View Expenses")
print("3. Generate Report")
print("4. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    print("\nYou selected: Add Expense")

elif choice == "2":
    print("\nYou selected: View Expenses")

elif choice == "3":
    print("\nYou selected: Generate Report")

elif choice == "4":
    print("\nThank you for using Expense Tracker!")

else:
    print("\nInvalid Choice!")