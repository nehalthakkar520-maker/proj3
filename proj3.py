# Student Data Organizer (Beginner Friendly)

students = []

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    # 1. ADD STUDENT
    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        subjects = input("Enter Subjects (comma): ").split(",")
        subjects_set = set(subjects)   # Set use

        sid = input("Enter Student ID: ")
        dob = input("Enter DOB: ")

        unique = (sid, dob)   # Tuple use

        student = {
            "name": name,
            "age": age,
            "subjects": subjects_set,
            "unique": unique
        }

        students.append(student)
        print("✅ Student Added!")

    # 2. SHOW STUDENTS
    elif choice == "2":
        if len(students) == 0:
            print("No Data Found")
        else:
            for s in students:
                print("\nID:", s["unique"][0])
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Subjects:", ", ".join(s["subjects"]))

    # 3. DELETE STUDENT
    elif choice == "3":
        sid = input("Enter ID to delete: ")

        for i in range(len(students)):
            if students[i]["unique"][0] == sid:
                del students[i]   # del keyword
                print("🗑️ Deleted!")
                break

    # 4. EXIT
    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")