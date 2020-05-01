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
            record_attendance_menu(modules)
        elif choice == "2":
            generate_statistics(modules)
        elif choice == "3":
            return
        else:
            print("Invalid choice")


def record_attendance_menu(modules):
    choice = -1
    loop = True
    while loop:
        menu_heading("Module Record System(Attendance) - Choose a Module")
        for i, mod in enumerate(modules.module):
            print(f"{i+1} - {mod.code} {mod.title}")
        print("x - Back to Main Menu")
        choice = input(">")

        if choice.lower() == "x":
            return
        try:
            module = modules.module[int(choice)-1]
            record_attendance(module)
        except:
            print("Invalid choice")


def record_attendance(module):
    choice = -1
    menu_heading(f"Module Record System(Attendance) {module.code}")
    print(f"There are {len(module.students)} students enrolled")
    for i, student in enumerate(module.students):
        print(f"Student #{i+1}: {student.name}")
        print("1. Present")
        print("2. Absent")
        print("3. Excused")
        choice = input(">")

        if choice == "1":
            student.present += 1
        if choice == "2":
            student.absent += 1
        if choice == "3":
            student.excused += 1

    module.save_data()
    print(f"{module.code}.txt updated with latest attendance records")


def generate_statistics(modules):
    return 0
