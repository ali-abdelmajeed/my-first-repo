class BankAccount:
    def __init__(self, owner, balance, account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New balance: {self.balance}")
    
    def withdraw(self, amount):
        if  amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        
        else:
            print("Insufficient funds!")

    def display_info(self):
        print(f"Name: {self.owner} \n Balance: {self.balance} \n Account_number: {self.account_number}")

class SavingAccount(BankAccount):
    def __init__(self, owner, balance, account_number, interest_rate):
        super().__init__(owner, balance, account_number)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added {interest}, New balance {self.balance}")

class PremiumAccount(BankAccount):
    def __init__(self, owner, balance, account_number, credit_limit):
        super().__init__(owner, balance, account_number)
        self.credit_limit = credit_limit

    def borrow(self, amount):
        if amount > self.balance:
            if amount <= self.credit_limit:
                self.credit_limit -= amount
                print(f"Borrowed {amount} from credit. Remaining credit: {self.credit_limit}")
            else:
                print("Can't borrow. Exceeds credit limit!")
        else:
            self.withdraw(amount)

    def display_info(self):
        super().display_info()
        print(f"Credit Limit: {self.credit_limit}")
        


premium1 = PremiumAccount("Ali", 1000, "PRE-001", 5000)
premium1.display_info()
premium1.withdraw(500)
premium1.borrow(2000)
premium1.display_info()

savings1 = SavingAccount("Ali", 1000, "SAV-001", 0.05)
savings1.display_info()
savings1.deposit(500)
savings1.add_interest()
savings1.withdraw(200)

account1 = BankAccount("Ali", 1000, "ACC-001")
account2 = BankAccount("Ahmed", 500, "ACC-002")

account1.display_info()
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)  # Should say insufficient funds

account2.display_info()
account2.deposit(100)