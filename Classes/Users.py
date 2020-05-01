from config import *


class Users:
    def __init__(self, data_file):
        self.data_file = data_file
        self.user = []
        self.logged_in_user = ""

    def load_data(self):
        connection = open(DATA_PATH + self.data_file)
        while True:
            line = connection.readline().rstrip()
            if line == "":
                break
            username = line
            line = connection.readline().rstrip()
            password = line
            self.user.append(User(username, password))

    def validate(self, username, password):
        for u in self.user:
            if u.username == username:
                if u.password == password:
                    self.logged_in_user = username;
                    return True
        return False


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
