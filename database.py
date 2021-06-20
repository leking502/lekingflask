import redis
import  chardet
from userdata import User
r = redis.Redis(host="localhost", port=6379, db=0)


class UserData:
    @staticmethod
    def get_user_for_id(user_id):
        password = r.get(user_id)
        if password is None:
            return None
        return User(user_id, password.decode())

    @staticmethod
    def add_user_in_database(user_id, password):
        if not r.get(user_id) is None:
            return False
        r.set(user_id, password)
        return True
