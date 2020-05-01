# Stuff for testing functionality as I go, not formal unit testing

from config import *
from Classes.Modules import Modules
from Classes.Users import Users
def main():
    modules = Modules("Modules.txt")
    modules.load_data()
    print(f"{modules.module[0].code} - {modules.module[0].title}")

    print(f"{modules.module[1].students[0].name}")

    modules.module[1].students[0].absent = 1
    modules.module[1].save_data()

    users = Users("Login_data.txt")
    users.load_data()
    print(f"{users.user[0].username}")

    if users.validate("Anna", "12345"):     #expect Success
        print("Success")
    else:
        print("Failure")

    if users.validate("Anna", "ewrwer"):    #expect Failure
        print("Success")
    else:
        print("Failure")

    if users.validate("wrwerr", "12345"):   #expect Failure
        print("Success")
    else:
        print("Failure")

main()