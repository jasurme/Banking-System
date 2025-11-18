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
    def __init__(self, account_number: str, account_holder, loan_amount: float, interest_rate: float = 0.08, loan_term_months: int = 24):
        super().__init__(account_number, account_holder, -loan_amount)
        self.__loan_amount = loan_amount
        self.__interest_rate = interest_rate
        self.__loan_term_months = loan_term_months
        self.__remaining_balance = loan_amount
        self.__monthly_payment = self._calculate_monthly_payment()
        self.__payments_made = 0
    
    def _calculate_monthly_payment(self):
        if self.__interest_rate == 0:
            return self.__loan_amount / self.__loan_term_months
        monthly_rate = self.__interest_rate / 12
        payment = self.__loan_amount * (monthly_rate * (1 + monthly_rate)**self.__loan_term_months) / ((1 + monthly_rate)**self.__loan_term_months - 1)
        return round(payment, 2)
    
    def get_monthly_payment(self):
        return self.__monthly_payment
    
    def get_remaining_balance(self):
        return self.__remaining_balance
    
    def calculate_interest(self):
        return round(self.__remaining_balance * (self.__interest_rate / 12), 2)
    
    def deposit(self, amount):
        if amount < self.__monthly_payment:
            raise ValueError(f"Minimum payment: ${self.__monthly_payment:.2f}")
        
        interest_portion = self.calculate_interest()
        principal_portion = amount - interest_portion
        
        self.__remaining_balance -= principal_portion
        self._set_balance(self.get_balance() + principal_portion)
        self.__payments_made += 1
        
        self._add_transaction({"type": "payment", "amount": amount, "principal": principal_portion, "interest": interest_portion, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        print(f"✓ Payment: ${amount:.2f} (Principal: ${principal_portion:.2f}, Interest: ${interest_portion:.2f})")
        print(f"  Remaining: ${self.__remaining_balance:.2f}")
        return True
    
    def withdraw(self, amount):
        raise Exception("Cannot withdraw from loan account")


class Transaction(ABC):
    def __init__(self, transaction_id: str, amount: float):
        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__status = "pending"
    
    def get_transaction_id(self):
        return self.__transaction_id
    
    def get_amount(self):
        return self.__amount
    
    def get_status(self):
        return self.__status
    
    def _set_status(self, status):
        self.__status = status
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def validate(self):
        pass
    
    def __lt__(self, other):
        return isinstance(other, Transaction) and self.__amount < other.__amount
    
    def __str__(self):
        return f"{self.__class__.__name__} #{self.__transaction_id}: ${self.__amount:.2f}"


class DepositTransaction(Transaction):
    def __init__(self, transaction_id: str, account, amount: float, method: str = "cash"):
        super().__init__(transaction_id, amount)
        self.__account = account
        self.__method = method
    
    def validate(self):
        if self.__account.get_status() != "active":
            return False, f"Account is {self.__account.get_status()}"
        if self.get_amount() <= 0:
            return False, "Amount must be positive"
        return True, "Valid"
    
    def execute(self):
        is_valid, msg = self.validate()
        if not is_valid:
            self._set_status("failed")
            raise Exception(f"Failed: {msg}")
        
        self.__account.deposit(self.get_amount())
        self._set_status("completed")
        return True


class WithdrawalTransaction(Transaction):
    def __init__(self, transaction_id: str, account, amount: float, method: str = "ATM"):
        super().__init__(transaction_id, amount)
        self.__account = account
        self.__method = method
    
    def validate(self):
        if self.__account.get_status() != "active":
            return False, f"Account is {self.__account.get_status()}"
        if self.get_amount() <= 0:
            return False, "Amount must be positive"
        
        if isinstance(self.__account, CheckingAccount):
            if self.get_amount() > self.__account.get_total_spendable_balance():
                return False, "Insufficient funds"
        else:
            if self.get_amount() > self.__account.get_balance():
                return False, "Insufficient funds"
        
        return True, "Valid"
    
    def execute(self):
        is_valid, msg = self.validate()
        if not is_valid:
            self._set_status("failed")
            raise Exception(f"Failed: {msg}")
        
        self.__account.withdraw(self.get_amount())
        self._set_status("completed")
        return True


class TransferTransaction(Transaction):
    def __init__(self, transaction_id: str, source_account, dest_account, amount: float):
        super().__init__(transaction_id, amount)
        self.__source = source_account
        self.__dest = dest_account
    
    def validate(self):
        if self.__source.get_status() != "active":
            return False, "Source account not active"
        if self.__dest.get_status() != "active":
            return False, "Destination account not active"
        if self.get_amount() <= 0:
            return False, "Amount must be positive"
        
        if isinstance(self.__source, CheckingAccount):
            if self.get_amount() > self.__source.get_total_spendable_balance():
                return False, "Insufficient funds"
        else:
            if self.get_amount() > self.__source.get_balance():
                return False, "Insufficient funds"
        
        return True, "Valid"
    
    def execute(self):
        is_valid, msg = self.validate()
        if not is_valid:
            self._set_status("failed")
            raise Exception(f"Failed: {msg}")
        
        self.__source.withdraw(self.get_amount())
        self.__dest.deposit(self.get_amount())
        self._set_status("completed")
        print(f"✓ Transfer: ${self.get_amount():.2f} from {self.__source.get_account_number()} to {self.__dest.get_account_number()}")
        return True


class BankingSystem:
    def __init__(self):
        self.__customers = {}
        self.__accounts = {}
        self.__transactions = []
        self.__next_customer_id = 1
        self.__next_account_number = 1000
        self.__next_transaction_id = 1
        self.__data_file = "banking_data.json"
    
    def generate_customer_id(self):
        cust_id = f"CUST{self.__next_customer_id:04d}"
        self.__next_customer_id += 1
        return cust_id
    
    def generate_account_number(self):
        acc_num = f"ACC{self.__next_account_number:06d}"
        self.__next_account_number += 1
        return acc_num
    
    def generate_transaction_id(self):
        txn_id = f"TXN{self.__next_transaction_id:08d}"
        self.__next_transaction_id += 1
        return txn_id
    
    def add_customer(self, customer):
        self.__customers[customer.get_customer_id()] = customer
    
    def add_account(self, account):
        self.__accounts[account.get_account_number()] = account
    
    def add_transaction(self, transaction):
        self.__transactions.append(transaction)
    
    def find_customer(self, customer_id):
        return self.__customers.get(customer_id)
    
    def find_account(self, account_number):
        return self.__accounts.get(account_number)
    
    def get_all_customers(self):
        return list(self.__customers.values())
    
    def get_all_accounts(self):
        return list(self.__accounts.values())
    
    def create_account(self, customer, account_type):
        acc_num = self.generate_account_number()
        
        if account_type == "savings":
            balance = float(input("Initial balance: "))
            account = SavingsAccount(acc_num, customer, balance)
        elif account_type == "checking":
            balance = float(input("Initial balance: "))
            account = CheckingAccount(acc_num, customer, balance)
        elif account_type == "loan":
            amount = float(input("Loan amount: "))
            account = LoanAccount(acc_num, customer, amount)
        else:
            raise ValueError("Invalid type")
        
        self.add_account(account)
        customer.add_account(account)
        print(f"✓ {account_type.capitalize()} account created: {acc_num}")
        return account
    
    def save_data(self):
        try:
            data = {
                "customers": [c.to_dict() for c in self.__customers.values()],
                "accounts": [a.to_dict() for a in self.__accounts.values()],
                "next_customer_id": self.__next_customer_id,
                "next_account_number": self.__next_account_number,
                "next_transaction_id": self.__next_transaction_id
            }
            with open(self.__data_file, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"✓ Data saved")
            return True
        except Exception as e:
            print(f"✗ Save failed: {e}")
            return False
    
    def load_data(self):
        if not os.path.exists(self.__data_file):
            print("Starting fresh")
            return False
        try:
            with open(self.__data_file, 'r') as f:
                data = json.load(f)
            self.__next_customer_id = data.get("next_customer_id", 1)
            self.__next_account_number = data.get("next_account_number", 1000)
            self.__next_transaction_id = data.get("next_transaction_id", 1)
            print(f"✓ Data loaded")
            return True
        except Exception as e:
            print(f"✗ Load failed: {e}")
            return False


def main():
    bank = BankingSystem()
    bank.load_data()
    
    while True:
        print("\n" + "="*60)
        print("BANKING SYSTEM")
        print("="*60)
        print("[1] Create Customer  [2] Create Account  [3] Deposit  [4] Withdraw  [5] Transfer  [6] View Customer  [7] View Account  [8] List All  [9] Exit")
        
        try:
            choice = input("Select: ").strip()
            
            if choice == "1":
                print("\n[1] Individual  [2] Corporate")
                ctype = input("Type: ").strip()
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                address = input("Address: ")
                cust_id = bank.generate_customer_id()
                
                if ctype == "1":
                    dob = input("Date of birth (YYYY-MM-DD): ")
                    customer = IndividualCustomer(cust_id, name, email, phone, address, dob)
                else:
                    company = input("Company name: ")
                    tax_id = input("Tax ID: ")
                    customer = CorporateCustomer(cust_id, name, email, phone, address, company, tax_id)
                
                bank.add_customer(customer)
                print(f"✓ Customer created: {cust_id}")
            
            elif choice == "2":
                cust_id = input("Customer ID: ")
                customer = bank.find_customer(cust_id)
                if not customer:
                    print("✗ Customer not found")
                    continue
                
                print("[1] Savings  [2] Checking  [3] Loan")
                atype = input("Type: ").strip()
                
                if atype == "1":
                    bank.create_account(customer, "savings")
                elif atype == "2":
                    bank.create_account(customer, "checking")
                elif atype == "3":
                    bank.create_account(customer, "loan")
            
            elif choice == "3":
                acc_num = input("Account number: ")
                account = bank.find_account(acc_num)
                if not account:
                    print("✗ Account not found")
                    continue
                
                amount = float(input("Amount: "))
                txn_id = bank.generate_transaction_id()
                txn = DepositTransaction(txn_id, account, amount)
                txn.execute()
                bank.add_transaction(txn)
            
            elif choice == "4":
                acc_num = input("Account number: ")
                account = bank.find_account(acc_num)
                if not account:
                    print("✗ Account not found")
                    continue
                
                amount = float(input("Amount: "))
                txn_id = bank.generate_transaction_id()
                txn = WithdrawalTransaction(txn_id, account, amount)
                txn.execute()
                bank.add_transaction(txn)
            
            elif choice == "5":
                from_acc = input("From account: ")
                to_acc = input("To account: ")
                source = bank.find_account(from_acc)
                dest = bank.find_account(to_acc)
                
                if not source or not dest:
                    print("✗ Account(s) not found")
                    continue
                
                amount = float(input("Amount: "))
                txn_id = bank.generate_transaction_id()
                txn = TransferTransaction(txn_id, source, dest, amount)
                txn.execute()
                bank.add_transaction(txn)
            
            elif choice == "6":
                cust_id = input("Customer ID: ")
                customer = bank.find_customer(cust_id)
                if customer:
                    customer.get_info()
                else:
                    print("✗ Not found")
            
            elif choice == "7":
                acc_num = input("Account number: ")
                account = bank.find_account(acc_num)
                if account:
                    account.view_balance()
                else:
                    print("✗ Not found")
            
            elif choice == "8":
                print("\n=== All Customers ===")
                for c in bank.get_all_customers():
                    print(f"  {c}")
                print("\n=== All Accounts ===")
                for a in bank.get_all_accounts():
                    print(f"  {a}")
            
            elif choice == "9":
                bank.save_data()
                print("\nGoodbye!")
                break
            
            else:
                print("Invalid choice")
        
        except Exception as e:
            print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()