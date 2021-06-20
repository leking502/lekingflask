from flask_login import UserMixin


class User(UserMixin):
    def get_id(self):
        return self.id

    def __init__(self, name, password):
        self.id = name
        self.password = password
    id = ""
    password = ""