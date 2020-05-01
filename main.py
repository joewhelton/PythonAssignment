from config import *
from Functions.commonFunctions import *
from Classes.Users import Users
from Classes.Modules import Modules


def main():
    users = Users("Login_data.txt")
    users.load_data()

    while not login(users):
        print("Access Denied")
    print(f"Welcome {users.logged_in_user}!")
    modules = Modules("Modules.txt")
    modules.load_data()

    main_menu(modules)
    exit()


main()
