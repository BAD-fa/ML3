class Customer:
    def __init__(self, name):
        self.name = name
        self.bank_accounts: [int, BankAccount] = {}
        self.cash = 0

    def get_bank_account(self, bank_account_id):
        bank_account = self.bank_accounts.get(bank_account_id, None)
        if not bank_account:
            raise Exception("Bank account not found")

        if bank_account.customer != self:
            raise Exception("Bank account not yours")

        return bank_account

    def withdraw_request(self, bank_account_id, amount):
        bank_account = self.get_bank_account(bank_account_id)

        balance = bank_account.withdraw(amount)
        self.cash += amount

        return f"{amount} is withdrawed new balance is : {bank_account.balance}"

    def deposit_request(self, bank_account_id, amount):
        bank_account = self.get_bank_account(bank_account_id)

        bank_account.deposit(amount)
        self.cash -= amount

        return f"{amount} is deposit new balance is : {bank_account.balance}"

    def transaction(self, bank_account_id, customer, bank_account_id2, amount):
        bank_account = self.get_bank_account(bank_account_id)

        # # -------- real world ---------
        # bank_account2 = Database.get(bank_account_id2)

        # --------- our world -------------
        bank_account2 = customer.get_bank_account(bank_account_id2)

        bank_account.withdraw(amount)
        bank_account2.deposit(amount)

        return "successful"

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.branch


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

    def deposit(self, amount: int):
        self._balance += amount

    def __str__(self):
        return str(self.balance)
