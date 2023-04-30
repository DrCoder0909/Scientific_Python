from bank_account import BankAccount, SavingsAccount, CurrentAccount

my_savings = SavingsAccount("Mathew Walsh", 41522887, 5.5, 1000)
my_savings.check_balance()
my_savings.add_interest()
my_savings.check_balance()

my_current=CurrentAccount("Alison Wicks", 78300991, 20.,200.)
my_current.withdraw(220)
my_current.deposit(750)
my_current.check_balance()
my_current.withdraw(220)
