import json

class Customer:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        return json.dumps({
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name
        })
