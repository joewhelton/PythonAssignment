from config import *
import datetime

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
            generate_statistics_menu(modules)
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


def generate_statistics_menu(modules):
    choice = -1
    loop = True
    while loop:
        menu_heading("Module Record System(Attendance) - Choose a Module")
        for i, mod in enumerate(modules.module):
            print(f"{i + 1} - {mod.code} {mod.title}")
        print("x - Back to Main Menu")
        choice = input(">")

        if choice.lower() == "x":
            return
        try:
            module = modules.module[int(choice) - 1]
            generate_statistics(module)
        except:
            print("Invalid choice")


def generate_statistics(module):
    today = datetime.datetime.now()
    filename = f"{DATA_PATH}{module.code}{today.strftime('%Y-%m-%d')}.txt"
    number_of_students = len(module.students)
    number_of_classes = module.students[0].present + module.students[0].absent + module.students[0].excused
    total_attendance, top_attendance = 0, 0
    low_attendance, non_attendance, best_attendance = [], [], []

    for student in module.students:
        total_attendance += student.present
        if student.present < (number_of_classes * 0.7):
            low_attendance.append(student.name)
        if student.present == 0:
            non_attendance.append(student.name)
        if student.present > top_attendance:
            top_attendance = student.present

    for student in module.students:
        if student.present == top_attendance:
            best_attendance.append(student.name)

    connection = open(filename, "w+")
    connection.write(f"Module: {module.code} {module.title}\n")
    connection.write(f"Number of students: {number_of_students}\n")
    connection.write(f"Number of classes: {number_of_classes}\n")
    connection.write(f"Average attendance: {(total_attendance / number_of_students):.1f}\n")
    connection.write("Low Attender(s): under 70.0 %\n")
    write_tabbed_list(low_attendance, connection)
    connection.write("Non Attender(s):\n")
    write_tabbed_list(non_attendance, connection)
    connection.write("Best Attender(s):\n")
    connection.write(f"\tAttended{top_attendance}/{number_of_classes} days\n")
    write_tabbed_list(best_attendance, connection)

    connection.close()
    connection = open(filename)
    print(connection.read())


def write_tabbed_list(list, connection):
    if len(list) == 0 :
        connection.write("\tNONE\n")
    else:
        for x in range(len(list)):
            connection.write(f"\t{list[x]}\n")
