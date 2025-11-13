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

class Account:
    pass

class Account:
    pass
