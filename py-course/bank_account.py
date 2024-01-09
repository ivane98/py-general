class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_account, acct_name):
        self.balance = initial_account
        self.name = acct_name
        # print(f"Account '{self.name}' created with initial balance of {self.balance:.2f}")

    def get_balance(self):
        print(f"Account '{self.name} has a balance of ${self.balance:.2f}'")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Deposit complete')
        self.get_balance()
        
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(f"Account'{self.name}' only has a balance of {self.balance}")