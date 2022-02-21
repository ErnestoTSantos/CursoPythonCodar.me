import hashlib


class Users:
    user_id = 1

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.user_id = Users.user_id
        Users.user_id += 1

    def hash_string(self):
        password = hashlib.sha256(self.password.encode()).hexdigest()
        sliced_password = password[:5]
        return sliced_password + '...'
