import os
import tempfile

from expense_manager.manager import ExpenseManager


def test_add_expense():
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".json"
    ) as file:

        filename = file.name

    manager = ExpenseManager(filename)

    manager.add_expense(
        "Food",
        "Lunch",
        150
    )

    expenses = manager.get_expenses()

    assert len(expenses) == 1
    assert expenses[0]["category"] == "Food"
    assert expenses[0]["amount"] == 150

    os.remove(filename)


def test_total_expenses():
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".json"
    ) as file:

        filename = file.name

    manager = ExpenseManager(filename)

    manager.add_expense("Food", "Lunch", 150)
    manager.add_expense("Travel", "Bus", 50)

    assert manager.get_total() == 200

    os.remove(filename)


def test_delete_expense():
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".json"
    ) as file:

        filename = file.name

    manager = ExpenseManager(filename)

    manager.add_expense("Food", "Lunch", 150)

    result = manager.delete_expense(1)

    assert result is True
    assert len(manager.get_expenses()) == 0

    os.remove(filename)