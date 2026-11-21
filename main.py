from student_operations import (
    display_students, add_student, search_student,
    update_student, delete_student
)
from student_analysis import run_analysis
from data_structures import demonstrate_data_structures

def main():
    while True:
        print("\\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add new student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Generate summary report and data analysis")
        print("7. Show Python data structures")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            run_analysis()
        elif choice == "7":
            demonstrate_data_structures()
        elif choice == "8":
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice. Please select 1 to 8.")

if __name__ == "__main__":
    main()
