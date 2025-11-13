from abc import ABC, abstractmethod
from datetime import datetime
class Account(ABC):
    def __init__(self, account_number: str, balance: float, account_holder: Customer):
        self.__account_number = account_number
        self.__balance = balance
        self.__account_holder = account_holder
        self.__date_opened = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transaction_history = []
        #__status ?
    @abstractmethod
    def calculate_interest(self):
        pass
    @abstractmethod
    def apply_fees(self):
        pass

    def deposit(self):
        pass
    def withdraw(self):
        pass
    def get_balance(self):
        pass 





class SavingsAccount(Account):
    def __init__(self, account_number, balance, account_holder, interest_rate: float, minimum_balance: float ,withdrawal_limit: float):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
        self.withdrawal_limit = withdrawal_limit
    
    def calculate_interest(self):
        pass
    def apply_fees(self):
        pass

    def monthly_interest_calculation(self):
        pass  



class CheckingAccount(Account):
    def __init__(self, account_number, balance, account_holder, overdraft_limit: float, monthly_fee: float, free_transactions: float): # is free float?
        super().__init__(account_number, balance, account_holder)
        self.overdraft_limit = overdraft_limit
        self.monthly_fee = monthly_fee
        self.free_transactions = free_transactions

    def calculate_interest(self):
        pass

    def apply_fees(self):
        pass

    def allow_overdraft_to_limit(self):
        pass

class LoanAccount(Account):
    def __init__(self, account_number, balance, account_holder, loan_amount, interest_rate, monthly_payment, remaining_balance):
        super().__init__(account_number, balance, account_holder)
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.monthly_payment = monthly_payment
        self.remaining_balance = remaining_balance

class Account:
    pass

class Account:
    pass

class Account:
    pass

class Account:
    pass

class Account:
    pass

class Account:
    pass


