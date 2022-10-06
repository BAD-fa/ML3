from models import Bank, BankAccount, Customer

c1 = Customer("customer1")
c2 = Customer("customer2")
c3 = Customer("customer3")
c4 = Customer("customer4")

bank1 = Bank("branch1")
bank2 = Bank("branch2")

bank1.create_bank_account(c1, 50_000)
bank1.create_bank_account(c2, 50_000)
bank2.create_bank_account(c3, 50_000)
bank2.create_bank_account(c4, 50_000)
bank2.create_bank_account(c1, 50_000)

print(c1.bank_accounts)
print(c2.bank_accounts)
print(c3.bank_accounts)
print(c4.bank_accounts)

print("bank 1 :")
for c in bank1.customers:
    print(c)

print("bank 2 :")
for c in bank2.customers:
    print(c)

print("bank 1 :")
for k, v in bank1.bank_accounts.items():
    print(k, v)

print("bank 2 :")
for k, v in bank2.bank_accounts.items():
    print(k, v)


print(c1.withdraw_request(1, 10_000))

# c1.withdraw_request(2, 20_000)

print(c2.transaction(2, c3, 3, 20_000))
print(c2.get_bank_account(2).balance)
print(c3.get_bank_account(3).balance)
