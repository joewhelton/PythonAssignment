from config import *
from Functions.commonFunctions import *
from Classes.Users import Users
from Classes.Modules import Modules


def login(users):
    username = input("Name: ")
    password = input("Password: ")
    return users.validate(username, password)


def main():
    users = Users("Login_data.txt")
    users.load_data()

    while not login(users):
        print("Access Denied")



main()
