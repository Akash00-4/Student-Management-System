from student import add_student, view_stu, search_stu, update_stu, delete_stu
from db import close_db 


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_stu()

    elif choice == "3":
        search_stu()

    elif choice == "4":
        update_stu()

    elif choice == "5":
        delete_stu()

    elif choice == "6":
        close_db()
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")