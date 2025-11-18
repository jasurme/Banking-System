from abc import ABC, abstractmethod
from datetime import datetime
import json
import os


class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str, address: str):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__accounts_list = []
        self.__date_joined = datetime.now().strftime("%Y-%m-%d")
    
    def get_customer_id(self):
        return self.__customer_id
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_accounts_list(self):
        return self.__accounts_list
    
    def add_account(self, account):
        if account not in self.__accounts_list:
            self.__accounts_list.append(account)
    
    def remove_account(self, account):
        if account in self.__accounts_list:
            self.__accounts_list.remove(account)
    
    def get_total_balance(self):
        return sum(acc.get_balance() for acc in self.__accounts_list)
    
    def get_info(self):
        print(f"\n[1] ID  [2] Name  [3] Email  [4] Phone  [5] Accounts  [6] Total Balance  [7] All")
        choice = input("Select: ").strip()
        
        if choice == "1":
            print(f"ID: {self.__customer_id}")
        elif choice == "2":
            print(f"Name: {self.__name}")
        elif choice == "3":
            print(f"Email: {self.__email}")
        elif choice == "4":
            print(f"Phone: {self.__phone}")
        elif choice == "5":
            for acc in self.__accounts_list:
                print(f"  {acc.get_account_number()}: ${acc.get_balance():.2f}")
        elif choice == "6":
            print(f"Total: ${self.get_total_balance():.2f}")
        elif choice == "7":
            print(f"ID: {self.__customer_id} | Name: {self.__name} | Email: {self.__email} | Phone: {self.__phone} | Balance: ${self.get_total_balance():.2f}")
    
    def __eq__(self, other):
        return isinstance(other, Customer) and self.__customer_id == other.__customer_id
    
    def __str__(self):
        return f"{self.__name} ({self.__customer_id})"
    
    def to_dict(self):
        return {
            "customer_id": self.__customer_id,
            "customer_type": self.__class__.__name__,
            "name": self.__name,
            "email": self.__email,
            "phone": self.__phone,
            "address": self.__address,
            "date_joined": self.__date_joined
        }


class IndividualCustomer(Customer):
    def __init__(self, customer_id: str, name: str, email: str, phone: str, address: str, date_of_birth: str = "1990-01-01"):
        super().__init__(customer_id, name, email, phone, address)
        self.__date_of_birth = date_of_birth
        self.__credit_score = 700
    
    def get_credit_score(self):
        return self.__credit_score
    
    def update_credit_score(self, score):
        if 300 <= score <= 850:
            self.__credit_score = score
    
    def to_dict(self):
        data = super().to_dict()
        data.update({"date_of_birth": self.__date_of_birth, "credit_score": self.__credit_score})
        return data


class CorporateCustomer(Customer):
    def __init__(self, customer_id: str, name: str, email: str, phone: str, address: str, company_name: str, tax_id: str):
        super().__init__(customer_id, name, email, phone, address)
        self.__company_name = company_name
        self.__tax_id = tax_id
    
    def get_company_name(self):
        return self.__company_name
    
    def to_dict(self):
        data = super().to_dict()
        data.update({"company_name": self.__company_name, "tax_id": self.__tax_id})
        return data


class Account(ABC):
    def __init__(self, account_number: str, account_holder, initial_balance: float = 0.0):
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__account_holder = account_holder
        self.__date_opened = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transaction_history = []
        self.__status = "active"
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder
    
    def get_status(self):
        return self.__status
    
    def _set_balance(self, amount):
        self.__balance = amount
    
    def _add_transaction(self, transaction_dict):
        self.__transaction_history.append(transaction_dict)
    
    @abstractmethod
    def calculate_interest(self):
        pass
    
    def deposit(self, amount):
        if self.__status != "active":
            raise Exception(f"Account is {self.__status}")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self.__balance += amount
        self.__transaction_history.append({
            "type": "deposit",
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after": self.__balance
        })
        print(f"✓ Deposited ${amount:.2f}. Balance: ${self.__balance:.2f}")
        return True
    
    def withdraw(self, amount):
        if self.__status != "active":
            raise Exception(f"Account is {self.__status}")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        
        self.__balance -= amount
        self.__transaction_history.append({
            "type": "withdrawal",
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after": self.__balance
        })
        print(f"✓ Withdrew ${amount:.2f}. Balance: ${self.__balance:.2f}")
        return True
    
    def view_balance(self):
        print(f"Account: {self.__account_number} | Holder: {self.__account_holder.get_name()} | Balance: ${self.__balance:.2f}")
    
    def __str__(self):
        return f"{self.__class__.__name__} #{self.__account_number}: ${self.__balance:.2f}"
    
    def __gt__(self, other):
        return isinstance(other, Account) and self.__balance > other.__balance
    
    def __lt__(self, other):
        return isinstance(other, Account) and self.__balance < other.__balance
    
    def to_dict(self):
        return {
            "account_number": self.__account_number,
            "account_type": self.__class__.__name__,
            "balance": self.__balance,
            "holder_id": self.__account_holder.get_customer_id(),
            "date_opened": self.__date_opened,
            "status": self.__status
        }


class SavingsAccount(Account):
    def __init__(self, account_number: str, account_holder, initial_balance: float = 0.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.__interest_rate = 0.03
        self.__minimum_balance = 500.0
        self.__withdrawal_limit = 2
        self.__current_withdrawal_count = 0
    
    def calculate_interest(self):
        balance = self.get_balance()
        return balance * self.__interest_rate if balance > 0 else 0.0
    
    def credit_interest(self):
        monthly_interest = self.calculate_interest() / 12
        if monthly_interest > 0:
            self._set_balance(self.get_balance() + monthly_interest)
            self._add_transaction({"type": "interest", "amount": monthly_interest, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            print(f"✓ Interest: ${monthly_interest:.2f}")
            return monthly_interest
        return 0.0
    
    def withdraw(self, amount):
        if self.__current_withdrawal_count >= self.__withdrawal_limit:
            raise Exception(f"Withdrawal limit ({self.__withdrawal_limit}) reached")
        if self.get_balance() - amount < self.__minimum_balance:
            raise ValueError(f"Minimum balance ${self.__minimum_balance} required")
        
        super().withdraw(amount)
        self.__current_withdrawal_count += 1
        return True
    
    def reset_withdrawal_count(self):
        self.__current_withdrawal_count = 0


class CheckingAccount(Account):
    def __init__(self, account_number: str, account_holder, initial_balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.__overdraft_limit = overdraft_limit
        self.__monthly_fee = 10.0
    
    def get_total_spendable_balance(self):
        return self.get_balance() + self.__overdraft_limit
    
    def calculate_interest(self):
        balance = self.get_balance()
        return balance * 0.001 if balance > 0 else 0.0
    
    def withdraw(self, amount):
        if self.get_status() != "active":
            raise Exception(f"Account is {self.get_status()}")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        balance_after = self.get_balance() - amount
        if balance_after < -self.__overdraft_limit:
            raise ValueError(f"Insufficient funds. Available: ${self.get_total_spendable_balance():.2f}")
        
        current_balance = self.get_balance()
        self._set_balance(balance_after)
        
        if current_balance >= 0 and balance_after < 0:
            overdraft_fee = 35.0
            self._set_balance(self.get_balance() - overdraft_fee)
            print(f"⚠ Overdraft fee: ${overdraft_fee:.2f}")
        
        self._add_transaction({"type": "withdrawal", "amount": amount, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        print(f"✓ Withdrew ${amount:.2f}. Balance: ${self.get_balance():.2f}")
        return True


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

