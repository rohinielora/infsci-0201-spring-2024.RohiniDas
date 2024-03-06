class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def to_json(self):
        return json.dumps({
            "customers": [json.loads(cust.to_json()) for cust in self.customers],
            "accounts": [json.loads(acc.to_json()) for acc in self.accounts]
        })
