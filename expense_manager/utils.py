def get_valid_amount():
    """Get a valid positive expense amount from the user."""

    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("❌ Please enter a valid number.")