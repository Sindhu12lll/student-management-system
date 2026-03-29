import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=SINDHU\MSSQLSERVER01;'   # Example: DESKTOP-XXXX
    'DATABASE=student_db;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Add Student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    print("Student added!")

# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor:
        print(row)

# Update Student
def update_student():
    id = int(input("Enter ID: "))
    name = input("Enter new name: ")

    cursor.execute(
        "UPDATE students SET name=? WHERE id=?",
        (name, id)
    )
    conn.commit()
    print("Updated!")

# Delete Student
def delete_student():
    id = int(input("Enter ID: "))

    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("Deleted!")

# Menu
while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

conn.close()
