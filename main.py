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

        def add_account(self, account) -> bool:
            """Add an account to the customer's account list"""
            if account is None:
                print("Error: Account cannot be None")
                return False

            # Check if account already exists
            for acc in self.accounts_list:
                if acc.get_account_number() == account.get_account_number():
                    print(f"Account {account.get_account_number()} already exists")
                    return False

            self.accounts_list.append(account)
            print(f"Account {account.get_account_number()} added successfully to customer {self.name}")
            return True

        def remove_account(self, account_number: str) -> bool:
            """Remove an account from the customer's account list by account number"""
            for i, acc in enumerate(self.accounts_list):
                if acc.get_account_number() == account_number:
                    removed_account = self.accounts_list.pop(i)
                    print(f"Account {account_number} removed successfully from customer {self.name}")
                    return True

            print(f"Account {account_number} not found")
            return False

        def get_total_balance(self) -> float:
            """Calculate total balance across all customer's accounts"""
            total = 0.0
            for account in self.accounts_list:
                total += account.get_balance()
            return total

        def get_account_by_number(self, account_number: str):
            """Find and return an account by its account number"""
            for account in self.accounts_list:
                if account.get_account_number() == account_number:
                    return account
            return None

        def list_accounts(self) -> None:
            """Display all accounts belonging to this customer"""
            if not self.accounts_list:
                print(f"Customer {self.name} has no accounts")
                return

            print(f"\n=== Accounts for {self.name} (ID: {self.customer_id}) ===")
            for account in self.accounts_list:
                print(f"  - Account #: {account.get_account_number()}, "
                      f"Balance: ${account.get_balance():,.2f}")

        def __eq__(self, other) -> bool:
            """Operator overloading: Compare customers by ID"""
            if isinstance(other, Customer):
                return self.customer_id == other.customer_id
            return False

        def __str__(self) -> str:
            """String representation of customer"""
            return f"Customer(ID: {self.customer_id}, Name: {self.name}, Accounts: {len(self.accounts_list)})"



class IndividualCustomer(Customer):
    def __init__(self, customer_id: str, name: str, email: str, phone: int, address: str, accounts_list: list, date_of_birth, SSN, employment_status):
        super().__init__(customer_id, name, email, phone, address, accounts_list)
        self.date_of_birth = date_of_birth
        self.SSN = SSN
        self.employment_status = employment_status

    def credit_score_calculation(self) -> int:
        """
        Calculate credit score based on:
        - Employment status
        - Total balance across all accounts
        - Number of accounts
        - Account history (basic simulation)
        """
        base_score = 300  # Minimum credit score

        # Employment status bonus
        if self.employment_status.lower() == "employed":
            base_score += 200
        elif self.employment_status.lower() == "self-employed":
            base_score += 150
        elif self.employment_status.lower() == "unemployed":
            base_score += 50

        # Balance-based scoring
        total_balance = self.get_total_balance()
        if total_balance >= 100000:
            base_score += 200
        elif total_balance >= 50000:
            base_score += 150
        elif total_balance >= 20000:
            base_score += 100
        elif total_balance >= 5000:
            base_score += 50

        # Number of accounts (shows financial diversity)
        num_accounts = len(self.accounts_list)
        if num_accounts >= 3:
            base_score += 50
        elif num_accounts >= 2:
            base_score += 30
        elif num_accounts >= 1:
            base_score += 10

        # Cap at maximum credit score
        credit_score = min(base_score, 850)

        return credit_score

    def personal_loan_eligibility(self) -> dict:
        """
        Check if customer is eligible for a personal loan
        Returns a dictionary with eligibility status and details
        """
        credit_score = self.credit_score_calculation()
        total_balance = self.get_total_balance()

        # Eligibility criteria
        min_credit_score = 650
        min_balance = 5000
        required_employment = ["employed", "self-employed"]

        is_eligible = True
        reasons = []

        # Check credit score
        if credit_score < min_credit_score:
            is_eligible = False
            reasons.append(f"Credit score ({credit_score}) below minimum ({min_credit_score})")

        # Check employment status
        if self.employment_status.lower() not in required_employment:
            is_eligible = False
            reasons.append(f"Employment status '{self.employment_status}' does not meet requirements")

        # Check balance
        if total_balance < min_balance:
            is_eligible = False
            reasons.append(f"Total balance (${total_balance:,.2f}) below minimum (${min_balance:,.2f})")

        # Calculate maximum loan amount if eligible
        max_loan_amount = 0
        if is_eligible:
            # Loan amount based on income/balance ratio (simplified)
            max_loan_amount = total_balance * 3  # Can borrow up to 3x total balance
            if credit_score >= 750:
                max_loan_amount *= 1.5  # 50% bonus for excellent credit

        return {
            "eligible": is_eligible,
            "credit_score": credit_score,
            "reasons": reasons if not is_eligible else ["All criteria met"],
            "max_loan_amount": max_loan_amount
        }

    def __str__(self) -> str:
        """String representation of individual customer"""
        return (f"IndividualCustomer(ID: {self.customer_id}, Name: {self.name}, "
                f"Employment: {self.employment_status}, Accounts: {len(self.accounts_list)})")

class CorporateCustomer(Customer):
    def __init__(self, customer_id: str, name: str, email: str, phone: int, address: str, accounts_list: list, company_name, tax_id, business_type, num_of_employees):
        super().__init__(customer_id, name, email, phone, address, accounts_list)
        self.company_name = company_name
        self.tax_id = tax_id
        self.business_type = business_type
        self.num_of_employees = num_of_employees


def business_loan_eligibility(self) -> dict:
    """
    Check if business is eligible for a business loan
    Returns a dictionary with eligibility status and details
    """
    total_balance = self.get_total_balance()

    # Eligibility criteria
    min_balance = 50000
    min_employees = 5
    min_accounts = 1

    is_eligible = True
    reasons = []

    # Check total balance
    if total_balance < min_balance:
        is_eligible = False
        reasons.append(f"Total balance (${total_balance:,.2f}) below minimum (${min_balance:,.2f})")

    # Check number of employees
    if self.num_of_employees < min_employees:
        is_eligible = False
        reasons.append(f"Number of employees ({self.num_of_employees}) below minimum ({min_employees})")

    # Check if business has accounts
    if len(self.accounts_list) < min_accounts:
        is_eligible = False
        reasons.append("Business must have at least one active account")

    # Calculate maximum loan amount if eligible
    max_loan_amount = 0
    if is_eligible:
        # Base loan on balance and company size
        base_loan = total_balance * 5  # Can borrow up to 5x total balance

        # Adjust based on company size
        if self.num_of_employees >= 100:
            base_loan *= 2  # Large company bonus
        elif self.num_of_employees >= 50:
            base_loan *= 1.5
        elif self.num_of_employees >= 20:
            base_loan *= 1.2

        max_loan_amount = base_loan

    return {
        "eligible": is_eligible,
        "total_balance": total_balance,
        "num_employees": self.num_of_employees,
        "reasons": reasons if not is_eligible else ["All criteria met"],
        "max_loan_amount": max_loan_amount
    }


def bulk_transactions(self, transactions: List[dict]) -> dict:
    """
    Process multiple transactions at once for corporate efficiency

    Args:
        transactions: List of transaction dictionaries with format:
            {
                'type': 'deposit' | 'withdraw' | 'transfer',
                'account_number': str,
                'amount': float,
                'to_account': str (for transfers only)
            }

    Returns:
        Dictionary with summary of successful and failed transactions
    """
    successful = []
    failed = []
    total_processed = 0.0

    for i, txn in enumerate(transactions):
        try:
            txn_type = txn.get('type', '').lower()
            account_number = txn.get('account_number')
            amount = txn.get('amount', 0)

            # Find the account
            account = self.get_account_by_number(account_number)
            if not account:
                failed.append({
                    'transaction_num': i + 1,
                    'reason': f"Account {account_number} not found",
                    'transaction': txn
                })
                continue

            # Process based on transaction type
            if txn_type == 'deposit':
                account.deposit(amount)
                successful.append({
                    'transaction_num': i + 1,
                    'type': 'deposit',
                    'account': account_number,
                    'amount': amount
                })
                total_processed += amount

            elif txn_type == 'withdraw':
                if account.withdraw(amount):
                    successful.append({
                        'transaction_num': i + 1,
                        'type': 'withdraw',
                        'account': account_number,
                        'amount': amount
                    })
                    total_processed += amount
                else:
                    failed.append({
                        'transaction_num': i + 1,
                        'reason': "Insufficient funds",
                        'transaction': txn
                    })

            elif txn_type == 'transfer':
                to_account_number = txn.get('to_account')
                to_account = self.get_account_by_number(to_account_number)

                if not to_account:
                    failed.append({
                        'transaction_num': i + 1,
                        'reason': f"Destination account {to_account_number} not found",
                        'transaction': txn
                    })
                    continue

                if account.withdraw(amount):
                    to_account.deposit(amount)
                    successful.append({
                        'transaction_num': i + 1,
                        'type': 'transfer',
                        'from_account': account_number,
                        'to_account': to_account_number,
                        'amount': amount
                    })
                    total_processed += amount
                else:
                    failed.append({
                        'transaction_num': i + 1,
                        'reason': "Insufficient funds for transfer",
                        'transaction': txn
                    })
            else:
                failed.append({
                    'transaction_num': i + 1,
                    'reason': f"Unknown transaction type: {txn_type}",
                    'transaction': txn
                })

        except Exception as e:
            failed.append({
                'transaction_num': i + 1,
                'reason': f"Error: {str(e)}",
                'transaction': txn
            })

    return {
        "total_transactions": len(transactions),
        "successful": len(successful),
        "failed": len(failed),
        "total_amount_processed": total_processed,
        "successful_details": successful,
        "failed_details": failed
    }


def __str__(self) -> str:
    """String representation of corporate customer"""
    return (f"CorporateCustomer(ID: {self.customer_id}, Company: {self.company_name}, "
            f"Type: {self.business_type}, Employees: {self.num_of_employees}, "
            f"Accounts: {len(self.accounts_list)})")


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

    will write meethods

