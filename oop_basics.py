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

account1 = BankAccount("Ali", 1000, "ACC-001")
account2 = BankAccount("Ahmed", 500, "ACC-002")

account1.display_info()
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)  # Should say insufficient funds

account2.display_info()
account2.deposit(100)