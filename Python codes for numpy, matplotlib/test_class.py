from bank_account import BankAccount, SavingsAccount, CurrentAccount
from customer import Customer

customer1 = Customer("Helen Smith", "76 The Warren , Baldings, Sussex", "1976-02-29")
account1 = BankAccount(customer1, 2157288,1000)
print(account1.customer.get_age())
print(account1.customer.address)

#using class savings account

my_savings = SavingsAccount("Mathew Walsh", 4152287, 5.5, 1000)
(my_savings.check_balance())
my_savings.add_interest()
(my_savings.check_balance())

my_current= CurrentAccount("Allison Wicks", 78300991, 20., 200.)
my_current.withdraw(220)
my_current.deposit(750)
my_current.check_balance()
my_current.withdraw(220)
