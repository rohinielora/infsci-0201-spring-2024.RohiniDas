class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def to_json(self):
        return json.dumps({
            "account_id": self.account_id,
            "balance": self.balance
        })
