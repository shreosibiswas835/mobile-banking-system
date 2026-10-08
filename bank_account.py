class BankAccount:
    """
    A simple CLI Mobile Banking System supporting:
    - MPIN login
    - TPIN secured transactions
    - Daily transfer limits
    - Account locking after multiple failed attempts
    - Transaction history tracking
    """

    DAILY_TRANSFER_LIMIT = 200000
    MAX_PIN_ATTEMPTS = 3

    def __init__(self, name, mobile_number, mpin, tpin, balance=0):
        self.name = name
        self.mobile_number = mobile_number
        self._mpin = mpin
        self._tpin = tpin
        self.balance = balance

        self.account_locked = False
        self.failed_mpin_attempts = 0
        self.failed_tpin_attempts = 0
        self.daily_transfer_total = 0
        self.transaction_history = []

    def login(self):
        if self.account_locked:
            print("Account is locked.")
            return False

        while self.failed_mpin_attempts < BankAccount.MAX_PIN_ATTEMPTS:
            try:
                entered_mpin = int(input("Enter MPIN: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if entered_mpin == self._mpin:
                self.failed_mpin_attempts = 0
                print("Login successful.")
                return True
            else:
                self.failed_mpin_attempts += 1
                print("Incorrect MPIN.")

        self.account_locked = True
        print("Account locked due to multiple incorrect MPIN attempts.")
        return False

    def validate_tpin(self):
        if self.account_locked:
            print("Account is locked.")
            return False

        while self.failed_tpin_attempts < BankAccount.MAX_PIN_ATTEMPTS:
            try:
                entered_tpin = int(input("Enter TPIN: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if entered_tpin == self._tpin:
                self.failed_tpin_attempts = 0
                return True
            else:
                self.failed_tpin_attempts += 1
                print("Incorrect TPIN.")

        self.account_locked = True
        print("Account locked due to multiple incorrect TPIN attempts.")
        return False

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self.balance += amount
        self.transaction_history.append(("Deposit", amount))
        print(f"Deposit successful. New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if not self.validate_tpin():
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self.transaction_history.append(("Withdraw", amount))
        print(f"Withdrawal successful. New balance: {self.balance:.2f}")

    def transfer(self, amount, recipient_account):
        if amount <= 0:
            print("Invalid transfer amount.")
            return

        if not self.validate_tpin():
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        if self.daily_transfer_total + amount > BankAccount.DAILY_TRANSFER_LIMIT:
            print("Daily transfer limit exceeded.")
            return

        self.balance -= amount
        recipient_account.balance += amount
        self.daily_transfer_total += amount

        self.transaction_history.append(("Transfer Sent", amount, recipient_account.name))
        recipient_account.transaction_history.append(("Transfer Received", amount, self.name))

        print(f"Transfer successful. New balance: {self.balance:.2f}")

    def check_balance(self):
        print(f"Current balance: {self.balance:.2f}")

    def show_transactions(self):
        print(f"\nTransaction History for {self.name}:")
        for txn in self.transaction_history:
            print(txn)