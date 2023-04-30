class BankAccount:
    """ An abstract base class representing a bank account"""
    currency="$"

    def __init__(self, customer,account_number,balance=0):
        """
        Initialize the Bankaccount class with a customer, account number and
        oprning balance(deafulting to 0)
        """

        self.customer= customer
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        """Deposit amount into the bank account"""
        if amount>0:
            self.balance+=amount
        else:
            print("Invalid deposit amount:", amount)

    def withdraw(self, amount):
        """
        Withdraw amount from the bank account"""

        if amount>0:
            if amount>self.balance:
                print("Insufficient funds")
            else:
                self.balance-=amount
        else:
            print("Invalid withdrawal amount:", amount)

    def check_balance(self):
        """ Print a statement of the account balance."""
        print("The balance of account number {:d} is {:s}{:.2f}"
              .format(self.account_number,self.currency,self.balance))

class SavingsAccount(BankAccount):
    """ A class representing a savings account"""

    def __init__(self, customer, account_number, interest_rate, balance=0):
        """Initialize the savings account"""
        self.interest_rate=interest_rate
        super().__init__(customer, account_number, balance)

    def add_interest(self):
        """Add interest to the account at the rate self.interest_rate"""

        self.balance*=(1. + self.interest_rate/100)

class CurrentAccount(BankAccount):
    """ A class representing a current (checking) account."""
    def __init__(self, customer, account_number, annual_fee,
                 transaction_limit,balance=0):
        """Initialize the current account"""

        self.annual_fee= annual_fee
        self.transaction_limit=transaction_limit
        super().__init__(customer, account_number , balance)

    def withdraw(self, amount):
        """
        Withdraw amount if sufficient funds exist in the account
        and amount is less than the single transaction limit."""

        if amount<=0:
            print("Invalid withdrawal amount:", amount)
            return

        if amount>self.balance:
            print("Insufficient funds")
            return

        if amount>self.transaction_limit:
            print("{0:s}{1:.2f} exceeds the single transaction transaction_limit"
                   "of{0:s}{2:.2f}".format(self.currency, amount,self.transaction_limit))
            return

        self.balance-=amount

    def apply_annual_fee(self):
        """ deduct the annual fee from the account balance"""

        self.balance= max(0., self_balance-self.annual_fee)
