from expense_manager.manager import ExpenseManager
from expense_manager.utils import get_valid_amount


def display_menu():
    print("\n" + "=" * 45)
    print("        EXPENSE MANAGER")
    print("=" * 45)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. View Category Summary")
    print("5. Delete Expense")
    print("6. Exit")
    print("=" * 45)


def main():
    manager = ExpenseManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n--- Add Expense ---")

            category = input("Enter category: ").strip()
            description = input("Enter description: ").strip()
            amount = get_valid_amount()

            if not category or not description:
                print("❌ Category and description cannot be empty.")
                continue

            manager.add_expense(category, description, amount)
            print("✅ Expense added successfully.")

        elif choice == "2":
            print("\n--- All Expenses ---")

            expenses = manager.get_expenses()

            if not expenses:
                print("No expenses found.")
                continue

            for expense in expenses:
                print(
                    f"ID: {expense['id']} | "
                    f"Category: {expense['category']} | "
                    f"Description: {expense['description']} | "
                    f"Amount: ₹{expense['amount']:.2f}"
                )

        elif choice == "3":
            total = manager.get_total()
            print(f"\n💰 Total Expenses: ₹{total:.2f}")

        elif choice == "4":
            print("\n--- Category Summary ---")

            summary = manager.get_category_summary()

            if not summary:
                print("No expenses found.")
                continue

            for category, amount in summary.items():
                print(f"{category}: ₹{amount:.2f}")

        elif choice == "5":
            try:
                expense_id = int(input("Enter expense ID to delete: "))
                if manager.delete_expense(expense_id):
                    print("✅ Expense deleted successfully.")
                else:
                    print("❌ Expense ID not found.")
            except ValueError:
                print("❌ Please enter a valid numeric ID.")

        elif choice == "6":
            print("\nThank you for using Expense Manager! 👋")
            break

        else:
            print("❌ Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()