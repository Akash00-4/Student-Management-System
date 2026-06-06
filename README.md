# student Management System
# Student Management System

A simple Student Management System project built using Python and MySQL.
This project performs basic CRUD operations on student records.

---

# Features

* Add Student
* View Students
* Search Student
* Update Student
* Delete Student

---

# Technologies Used

* Python
* MySQL

---

# Project Structure

```text
student-management-system/
│
├── main.py
├── db.py
├── student.py
├── requirements.txt
├── README.md
├── student_db.sql
└── .gitignore
```

---

# Database Table

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    email VARCHAR(100)
);
```

---

# Example Menu

```text
===== Student Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

---

# Concepts Used

* Python Functions
* MySQL Database Connectivity
* CRUD Operations
* SQL Queries
* Modular Programming

---

# Developed by
Akash Halder
