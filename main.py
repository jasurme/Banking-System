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

#### Ibrohimjon's Code

class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: int, address: str, accounts_list: list):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.accounts_list = accounts_list

        def add_account(self):
            pass

        def remove_account(self):
            pass

        def get_total_balance(self):
            pass


class IndividualAccount(Customer):
    def __init__(self, customer_id: str, name: str, email: str, phone: int, address: str, accounts_list: list, date_of_birth, SSN, employment_status):
        super().__init__(customer_id, name, email, phone, address, accounts_list)
        self.date_of_birth = date_of_birth
        self.SSN = SSN
        self.employment_status = employment_status

    def credit_score_calculation(self):
        pass

    def personal_lone_eligibility(self):
        pass

class CorporateAccount(Customer):
    def __init__(self, customer_id: str, name: str, email: str, phone: int, address: str, accounts_list: list, company_name, tax_id, business_type, num_of_employees):
        super().__init__(customer_id, name, email, phone, address, accounts_list)
        self.company_name = company_name
        self.tax_id = tax_id
        self.business_type = business_type
        self.num_of_employees = num_of_employees

    def business_loan_eligibility(self):
        pass

    def bulk_transactions(self):
        pass


class Transaction:
    def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account):
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        self.amount = amount
        self.transaction_type = transaction_type
        self.from_account = from_account
        self.to_account = to_account

    def execute(self):
        pass

    def reverse(self):
        pass

    def validate(self):
        pass

class Deposit(Transaction):
    def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account, deposit_method):
        super().__init__(transaction_id, timestamp, amount, transaction_type, from_account, to_account)
        self.deposit_method = deposit_method

    def execute(self):
        pass
    """adds to balance """

class Withdraw(Transaction):
    def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account, withdrawal_method):
        super().__init__(transaction_id, timestamp, amount, transaction_type, from_account, to_account)
        self.deposit_method = withdrawal_method

    def execute(self):
        pass
    """ deducts from balance with validation"""

class Transfer(Transaction):
    def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account, source_account, destination_account, transfer_fee):
        super().__init__(transaction_id, timestamp, amount, transaction_type, from_account, to_account)
        self.source_account = source_account
        self.destination_account = destination_account
        self.transfer_fee = transfer_fee

    def execute(self):
        pass
    """Moves money between accounts"""

