def menu():
    while True:
        print("\n ========= Student Management System Via SQLLite DB ========")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            marks = input("Enter student marks: ")
            add_student(name, marks)
        elif choice == '2':
            show_students()
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            new_marks = input("Enter new marks: ")
            update_student(student_id, new_marks)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break