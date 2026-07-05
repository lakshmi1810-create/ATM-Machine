class ATM:
    """A simple ATM Machine Simulation."""

    MAX_ATTEMPTS = 3
    CORRECT_PIN = 12345

    def __init__(self):
        self.balance = 10000
        self.transactions = []

    def authenticate(self):
        """Authenticate user using PIN."""
        attempts = 0

        while attempts < self.MAX_ATTEMPTS:
            try:
                pin = int(input("Enter your PIN: "))

                if pin == self.CORRECT_PIN:
                    print("\nLogin Successful!\n")
                    return True

                attempts += 1
                print(f"Incorrect PIN! Attempts left: {self.MAX_ATTEMPTS - attempts}")

            except ValueError:
                print("PIN should contain numbers only.")

        print("\nAccount Locked! Too many incorrect attempts.")
        return False

    def deposit(self):
        """Deposit money into account."""
        try:
            amount = float(input("Enter deposit amount: ₹"))

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            self.balance += amount
            self.transactions.append(
                f"Deposited ₹{amount:.2f} | Balance: ₹{self.balance:.2f}"
            )

            print(f"Deposit Successful!")
            print(f"Current Balance: ₹{self.balance:.2f}")

        except ValueError as e:
            print(f"Error: {e}")

    def withdraw(self):
        """Withdraw money from account."""
        try:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            if amount > self.balance:
                raise Exception("Insufficient Balance!")

            self.balance -= amount
            self.transactions.append(
                f"Withdrawn ₹{amount:.2f} | Balance: ₹{self.balance:.2f}"
            )

            print("Withdrawal Successful!")
            print(f"Current Balance: ₹{self.balance:.2f}")

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")

    def check_balance(self):
        """Display current balance."""
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def transaction_history(self):
        """Display all transactions."""
        print("\n========== Transaction History ==========")

        if not self.transactions:
            print("No transactions yet.")
            return

        for transaction in self.transactions:
            print(transaction)

    def menu(self):
        """Display ATM menu."""
        while True:
            print("\n========== ATM MENU ==========")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.deposit()

                elif choice == 2:
                    self.withdraw()

                elif choice == 3:
                    self.check_balance()

                elif choice == 4:
                    self.transaction_history()

                elif choice == 5:
                    print("\nThank you for using our ATM!")
                    print(f"Final Balance: ₹{self.balance:.2f}")
                    break

                else:
                    print("Please choose a number between 1 and 5.")

            except ValueError:
                print("Please enter a valid numeric choice.")


def main():
    atm = ATM()

    if atm.authenticate():
        atm.menu()


if __name__ == "__main__":
    main()