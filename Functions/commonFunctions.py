from config import *
from Functions.attendance import record_attendance
from Functions.statistics import generate_statistics

def menu_heading(heading_text):
    print(heading_text)
    print("-" * len(heading_text))
    print("\n")


def login(users):
    username = input("Name: ")
    password = input("Password: ")
    return users.validate(username, password)


def main_menu(modules):
    choice, submenu_choice = -1, -1
    loop = True
    while loop:
        menu_heading("Module Record System - Options")
        print("1. Record Attendance")
        print("2. Generate Statistics")
        print("3. Exit")
        choice = input(">")

        if choice == "1":
            submenu_choice = submenu(modules, "Attendance")
            if submenu_choice != 0:
                record_attendance(submenu_choice)
        elif choice == "2":
            submenu_choice = submenu(modules, "Statistics")
            if submenu_choice != 0:
                generate_statistics(submenu_choice)
        elif choice == "3":
            return
        else:
            print("Invalid choice")


def submenu(modules, heading):
    choice = -1
    loop = True
    while loop:
        menu_heading(f"Module Record System({heading}) - Choose a Module")
        for i, mod in enumerate(modules.module):
            print(f"{i+1} - {mod.code} {mod.title}")
        print("x - Back to Main Menu")
        choice = input(">")

        if choice.lower() == "x":
            return 0
        try:
            module = modules.module[int(choice)-1]
            return module
        except:
            print("Invalid choice")






def write_tabbed_list(list, connection):
    if len(list) == 0 :
        connection.write("\tNONE\n")
    else:
        for x in range(len(list)):
            connection.write(f"\t{list[x]}\n")
