class Customer:
    def __init__(self, name):
        self.name = name
        self.bank_accounts: [int, BankAccount] = {}
        self.cash = 0

    def withdraw_request(self, bank_account_id, amount):
        bank_account = self.bank_accounts.get(bank_account_id, None)
        if not bank_account:
            raise Exception("Bank account not found")

        if bank_account.customer != self:
            raise Exception("Bank account not yours")

        balance = bank_account.withdraw(amount)
        self.cash += amount

        return f"{amount} is withdrawed new balance is : {balance}"

    def deposit_request(self):
        pass

    def transaction(self):
        pass


class Bank:
    bank_account_id = 1

    def __init__(self, branch):
        self.branch = branch
        self.bank_accounts = {}
        self.customers = []

    def create_bank_account(self, customer, amount: int):
        if customer in self.customers:
            new_bank_account = BankAccount(self, customer)
            new_bank_account.deposit(amount)
            self.bank_accounts[Bank.bank_account_id] = new_bank_account
            customer.bank_accounts[Bank.bank_account_id] = new_bank_account
            Bank.bank_account_id += 1
        else:
            self.register(customer)
            self.create_bank_account(customer, amount)

    def register(self, customer: Customer):
        self.customers.append(customer)


class BankAccount:
    def __init__(self, bank, customer):
        self._balance = 0
        self.bank = bank
        self.customer = customer
        self.history = []

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amonut: int):
        if amonut > self.balance:
            raise Exception("Not enough balance")

        self._balance -= amonut

        return self.balance

    def deposit(self, amount: int):
        self._balance += amount
