def record_attendance(module):
    choice = -1
    print(f"Module Record System(Attendance) {module.code}")
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
