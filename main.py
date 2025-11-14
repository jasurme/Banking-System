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

        def add_account(self, account):
            self.accounts_list.append(account)

        def remove_account(self, account):
            if account in self.accounts_list:
                self.accounts_list.remove(account)

        def get_total_balance(self) -> float:
            return  sum(account.balance for account in self.accounts_list)



class IndividualCustomer(Customer):
    def __init__(self, customer_id: str, name: str, email: str, phone: int, address: str, accounts_list: list, date_of_birth, SSN, employment_status):
        super().__init__(customer_id, name, email, phone, address, accounts_list)
        self.date_of_birth = date_of_birth
        self.SSN = SSN
        self.employment_status = employment_status

    def credit_score_calculation(self):
        """
        Calculates a realistic credit score between 300 and 850.
        Factors used:
        - total balance (more savings → slightly higher score)
        - number of accounts
        - employment status
        """

        base_score = 600  # Neutral starting score

        total_balance = self.get_total_balance()
        num_accounts = len(self.accounts_list)

        # Weight 1: Savings & balance behavior
        if total_balance > 20000:
            base_score += 120
        elif total_balance > 10000:
            base_score += 80
        elif total_balance > 5000:
            base_score += 40
        else:
            base_score -= 20

        # Weight 2: Account maturity (more accounts = better credit mix)
        if num_accounts >= 3:
            base_score += 40
        elif num_accounts == 2:
            base_score += 20
        else:
            base_score -= 10

        # Weight 3: Employment status
        if self.employment_status.lower() == "employed":
            base_score += 50
        elif self.employment_status.lower() == "self-employed":
            base_score += 30
        else:  # unemployed
            base_score -= 40

        # Clamp score between 300 and 850
        return max(300, min(850, base_score))

    def personal_loan_eligibility(self):
        credit_score = self.credit_score_calculation()
        total_balance = self.get_total_balance()

        # Basic rules:
        if credit_score < 650:
            return False  # Too risky

        if credit_score >= 700:
            # Good score → low minimum balance requirement
            return total_balance >= 2000

        # Medium score → higher balance required
        return total_balance >= 5000


class CorporateCustomer(Customer):
    def __init__(self, customer_id: str, name: str, email: str, phone: int, address: str, accounts_list: list, company_name, tax_id, business_type, num_of_employees):
        super().__init__(customer_id, name, email, phone, address, accounts_list)
        self.company_name = company_name
        self.tax_id = tax_id
        self.business_type = business_type
        self.num_of_employees = num_of_employees

    def business_loan_eligibility(self):
        total_balance = self.get_total_balance()

        # Business stability factor
        business_stable_types = ["manufacturing", "technology", "retail"]

        stability_factor = 0
        if self.business_type.lower() in business_stable_types:
            stability_factor = 1
        else:
            stability_factor = 0.7  # higher risk sector

        # Score formula
        score = (
                        total_balance * 0.4 +
                        self.num_of_employees * 50
                ) * stability_factor

        # Threshold example: Need score ≥ 20,000
        return score >= 20000

    def bulk_transactions(self, amount, transaction_count):
        """
        Calculates total cost of bulk transactions with fees:
        - 0.5% fee for up to 50 transactions
        - 0.4% fee for 50–200 transactions
        - 0.25% fee for >200 transactions
        """

        total_amount = amount * transaction_count

        if transaction_count <= 50:
            fee_rate = 0.005
        elif transaction_count <= 200:
            fee_rate = 0.004
        else:
            fee_rate = 0.0025

        fee = total_amount * fee_rate
        return total_amount + fee


class Transaction:
    def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account):
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        self.amount = amount
        self.transaction_type = transaction_type
        self.from_account = from_account
        self.to_account = to_account
        self.executed = False


    def validate(self):
    if self.amount <= 0:
        raise ValueError("Transaction amount must be greater than zero")

    def execute(self):
        raise NotImplementedError("Execute must be implemented by subclasses")


    def reverse(self):
        raise NotImplementedError("Reverse must be implemented by subclasses")

class Deposit(Transaction):
    def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account, deposit_method):
        super().__init__(transaction_id, timestamp, amount, transaction_type, from_account, to_account)
        self.deposit_method = deposit_method

    def validate(self):
        super().validate()
        if self.to_account is None:
            raise ValueError("Deposit requires a target account")

    def execute(self):
        self.validate()
        self.to_account.deposit(self.amount)
        self.executed = True

    def reverse(self):
        if not self.executed:
            raise ValueError("Cannot reverse a transaction that was never executed")

        if self.amount > self.to_account.balance:
            raise ValueError("Cannot reverse deposit: insufficient funds in account")

        self.to_account.withdraw(self.amount)
        self.executed = False

class Withdraw(Transaction):
    def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account, withdrawal_method):
        super().__init__(transaction_id, timestamp, amount, transaction_type, from_account, to_account)
        self.deposit_method = withdrawal_method

    def validate(self):
        super().validate()
        if self.from_account is None:
            raise ValueError("Withdrawal requires a source account")

        if self.amount > self.from_account.balance:
            raise ValueError("Insufficient funds")

    def execute(self):
        self.validate()
        self.from_account.withdraw(self.amount)
        self.executed = True

    def reverse(self):
        if not self.executed:
            raise ValueError("Cannot reverse a non-executed transaction")

        self.from_account.deposit(self.amount)
        self.executed = False

class Transfer(Transaction):
    def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account, source_account, destination_account, transfer_fee):
        super().__init__(transaction_id, timestamp, amount, transaction_type, from_account, to_account)
        self.source_account = source_account
        self.destination_account = destination_account
        self.transfer_fee = transfer_fee

    class Transfer(Transaction):
        def __init__(self, transaction_id, timestamp, amount, transaction_type, from_account, to_account,
                     source_account, destination_account, transfer_fee):
            super().__init__(transaction_id, timestamp, amount, transaction_type, from_account, to_account)
            self.source_account = source_account
            self.destination_account = destination_account
            self.transfer_fee = transfer_fee

        def validate(self):
            super().validate()

            if self.source_account is None or self.destination_account is None:
                raise ValueError("Transfer requires both source and destination accounts")

            total_cost = self.amount + self.transfer_fee
            if total_cost > self.source_account.balance:
                raise ValueError("Insufficient balance including transfer fee")

        def execute(self):
            self.validate()
            total_cost = self.amount + self.transfer_fee

            # deduct from source
            self.source_account.withdraw(total_cost)

            # add to destination
            self.destination_account.deposit(self.amount)

            self.executed = True

        def reverse(self):
            if not self.executed:
                raise ValueError("Cannot reverse an unexecuted transaction")

            # remove the transferred amount from the destination account
            if self.amount > self.destination_account.balance:
                raise ValueError("Destination account lacks funds to reverse")

            self.destination_account.withdraw(self.amount)

            # restore original amount + fee to the source account
            refund = self.amount + self.transfer_fee
            self.source_account.deposit(refund)

            self.executed = False

