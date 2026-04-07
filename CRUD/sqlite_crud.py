import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Table creation

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTGER,
        grade TEXT
     )'''
)

# conn.commit()
# print("Table created successfully")

# Function to add a student
def add_student(name, age, grade): 
  cursor.execute(
     '''
       INSERT INTO students (name, age, grade)
       VALUES (?, ?, ?)
     ''',(name, age, grade)
  )
  conn.commit()
  print(f"Student added successfully.")
  add_student('Alex', 23, 'A')
  add_student('Tovino', 25, 'B')

# Function to retrieve all students



# Function to update a student's details

def update_student(student_id, new_name, new_age, new_grade):
   cursor.execute(
        '''UPDATE students
        SET name = ? , age = ? , grade = ?
        WHERE id = ?'''(new_name, new_age, new_grade, student_id)
   )
update_student(1, 'Alex Pandian', 28, 'A+')

def fetch_all_students():
   cursor.execute('SELECT * FROM students')
   rows = cursor.fetchall()
   for row in rows:
      print(row)
fetch_all_students()


# Function to delete a student by ID

def delete_student(student_id):
   cursor.execute('DELETE FROM students WHERE id = ?', (student_id))
   conn.commit()
   print(f'Student deleted successfully.')
delete_student(2)

# Close the connection
conn.close()
print("Database connection closed.")