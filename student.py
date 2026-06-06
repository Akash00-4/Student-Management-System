from db import conn, cursor

def add_student ():
    name = input("Enter Name : ")
    age = int(input("Enter age : "))
    course = input("Enter course : ")
    email = input("Enter email : ")

    query = """
    INSERT INTO students (name, age, course, email)
    VALUES(%s, %s, %s, %s)
    """

    values = (name, age, course, email)

    cursor.execute(query, values)
    conn.commit()
    print("Student Added Successfully..!")

def view_stu ():
    query = "SELECT * FROM students"
    cursor.execute(query)

    students = cursor.fetchall()
    print("\n---student Records---")
    for student in students:
        print(student)

def search_stu ():
    student_id = int(input("Enter student ID : "))

    query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(query,(student_id,))

    student = cursor.fetchone()

    if student:
        print(student)
    else:
        print("Student Not Found")

def update_stu ():
    student_id = int(input("Enter Student ID to Update : "))

    name = input("Enter Name : ")
    age = int(input("Enter age : "))
    course = input("Enter course : ")
    email = input("Enter email : ")

    query = """
    UPDATE students
    SET name=%s, age=%s, course=%s, email=%s
    WHERE id=%s
    """
    values = (name, age, course, email, student_id)
    cursor.execute(query,values)
    conn.commit()

    print("Student Update Successfully..!")

def delete_stu ():
    student_id = int(input("Enter Student ID to Delete : "))
    
    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query,(student_id,))

    conn.commit()
    print("Student Deleted successfully!")