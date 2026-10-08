from bank_account import BankAccount


def main():
    customer = BankAccount("Samyak", "9876543210", 1234, 5678, 100000)
    recipient = BankAccount("Rahul", "9999999999", 4321, 8765, 50000)

    print("===== Welcome to Secure Mobile Banking =====")

    if not customer.login():
        return

    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Send Money")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                customer.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                customer.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "3":
            try:
                amount = float(input("Enter transfer amount: "))
                customer.transfer(amount, recipient)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "4":
            customer.check_balance()

        elif choice == "5":
            customer.show_transactions()

        elif choice == "6":
            print("Thank you for using Mobile Banking System.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()