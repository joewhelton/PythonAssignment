import datetime
from config import *
from Functions.commonFunctions import write_tabbed_list


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
