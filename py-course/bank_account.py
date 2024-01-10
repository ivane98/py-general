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
            raise BalanceException(f"Account '{self.name}' only has a balance of {self.balance}")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print('\nWithdraw complete')
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\n")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer compete\n**********')
        except BalanceException as error:
            print(f"\nTransfer interupted: {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount*1.05
        print('\nDeposit complete')
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_account, acct_name):
        super().__init__(initial_account, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdraw complete')
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interupted: {error}")
    
    