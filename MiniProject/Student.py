class Student:
   all_students =  []
   def __init__(self, name, roll_number, marks):
      self.marks = marks
      self.roll_number = roll_number
      self.marks = marks

   def menu():
       print("\n ============= Student Management System ================")
       print("1. Add Student")
       print("2. Update Marks")
       print("3. Show All Student")
       print("4. Exit")

       choice = input("Enter your option(1-4): ")
       if choice == '1':
           Student.add_students()
       elif choice == '2':
           Student.update_student_marks()
       elif choice == '3':
           Student.show_all_students()
       elif choice == '4':
           print("Exiting Student Management System. GoodBye!")
           break
       else:
           print("Invalid choice. Please try again.")