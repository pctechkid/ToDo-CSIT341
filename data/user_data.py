"""
Sample data.
Password -> 123456
"""
user_data = [
    {'name': 'CIT', 'email': 'cit@cit.edu', 'password': 'aA@123456', 'id': 1}
]


class UserData:
    def __init__(self):
        self.user_data = user_data
        self.payload = {}

    def validate(self, payload):
        if 'name' not in payload or not payload['name']:
            raise Exception("You should fill name")

        if 'name' not in payload or not payload['email']:
            raise Exception("You should fill email")

        if 'password' not in payload or not payload['password']:
            raise Exception("You should fill email")

    def clear(self):
        self.payload = {}

    def get(self, id=None):
        if not id:
            return self.user_data

        value = []
        for item in self.user_data:
            if item['id'] == id:
                value = item
                break

        return value

    def get_by_email(self, email=None):
        value = None

        for item in self.user_data:
            if item['email'] == email:
                value = item
                break

        return value

    def insert(self):
        self.validate(self.payload)

        length = len(self.user_data)
        self.payload['id'] = (length + 1)

        self.user_data.append(self.payload)
        data = self.payload.copy()

        self.clear()
        return data

    def update(self, id):
        self.validate(self.payload)

        for item in self.user_data:
            if item['id'] == id:
                item.update(self.payload)
                break

        self.clear()

    def delete(self, id):
        index = 0

        for idx, item in self.user_data:
            if item['id'] == id:
                index = idx
                break

        self.user_data.pop(index)
        self.clear()
