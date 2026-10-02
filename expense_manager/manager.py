import json
import os


class ExpenseManager:

    def __init__(self, filename="data/expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from JSON file."""

        try:
            if not os.path.exists(self.filename):
                os.makedirs(
                    os.path.dirname(self.filename),
                    exist_ok=True
                )

                with open(self.filename, "w") as file:
                    json.dump([], file)

            with open(self.filename, "r") as file:
                self.expenses = json.load(file)

        except (json.JSONDecodeError, OSError):
            print("⚠️ Warning: Could not load expense data.")
            self.expenses = []

    def save_expenses(self):
        """Save expenses to JSON file."""

        try:
            os.makedirs(
                os.path.dirname(self.filename),
                exist_ok=True
            )

            with open(self.filename, "w") as file:
                json.dump(self.expenses, file, indent=4)

        except OSError as error:
            print(f"❌ Error saving expenses: {error}")

    def add_expense(self, category, description, amount):
        """Add a new expense."""

        new_id = 1

        if self.expenses:
            new_id = max(
                expense["id"] for expense in self.expenses
            ) + 1

        expense = {
            "id": new_id,
            "category": category,
            "description": description,
            "amount": float(amount)
        }

        self.expenses.append(expense)
        self.save_expenses()

    def get_expenses(self):
        """Return all expenses."""

        return self.expenses

    def get_total(self):
        """Calculate total expenses."""

        return sum(
            expense["amount"]
            for expense in self.expenses
        )

    def get_category_summary(self):
        """Return expenses grouped by category."""

        summary = {}

        for expense in self.expenses:
            category = expense["category"]

            if category not in summary:
                summary[category] = 0

            summary[category] += expense["amount"]

        return summary

    def delete_expense(self, expense_id):
        """Delete an expense using its ID."""

        original_count = len(self.expenses)

        self.expenses = [
            expense
            for expense in self.expenses
            if expense["id"] != expense_id
        ]

        if len(self.expenses) < original_count:
            self.save_expenses()
            return True

        return False