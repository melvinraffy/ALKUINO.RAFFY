class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₱{amount}. New balance: ₱{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
       
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₱{amount}. New balance: ₱{self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        
        print(f"Account balance: ₱{self.balance}")

account = BankAccount(account_number="09488578091", owner="Floyd", balance=5000)

account.deposit(1000)  
account.withdraw(700)  
account.display_balance()  
