def menu_heading(heading_text):
    print(heading_text)
    print("-" * len(heading_text))
    print("\n")


def login(users):
    username = input("Name: ")
    password = input("Password: ")
    return users.validate(username, password)


def main_menu(modules):
    choice = -1
    loop = True
    while loop:
        menu_heading("Module Record System - Options")
        print("1. Record Attendance")
        print("2. Generate Statistics")
        print("3. Exit")
        choice = input(">")

        if choice == "1":
            record_attendance(modules)
        elif choice == "2":
            generate_statistics(modules)
        elif choice == "3":
            return
        else:
            print("Invalid choice")


def record_attendance(modules):
    return 0


def generate_statistics(modules):
    return 0
