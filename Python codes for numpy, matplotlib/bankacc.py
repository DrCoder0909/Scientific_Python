from bank_account import BankAccount
import customer
customer1=customer.Customer("Helen Smith", " 76 The Warren, Blandings , Sussex",
                    "1976-02-29")

account1 =BankAccount(customer1, 21457288, 1000)
a = "helen"
print(type(a))

print(type(account1))
r=account1.customer.get_age()
print(r)
print(account1.customer)
print(account1.customer.address)
