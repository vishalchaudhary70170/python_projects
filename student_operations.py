import csv
import os

FILE_NAME = "student_data.csv"
FIELDNAMES = ["Student_ID", "Name", "Department", "Year", "Python", "Maths", "English"]

def read_students():
    """Read all student records from the CSV file."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
        return []
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def write_students(students):
    """Write the complete student list back to the CSV file."""
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)

def display_students():
    students = read_students()
    if not students:
        print("No student records found.")
        return
    print("\\n{:<6} {:<20} {:<10} {:<6} {:<8} {:<8} {:<8}".format(
        "ID", "NAME", "DEPT", "YEAR", "PYTHON", "MATHS", "ENGLISH"))
    print("-" * 75)
    for s in students:
        print("{:<6} {:<20} {:<10} {:<6} {:<8} {:<8} {:<8}".format(
            s["Student_ID"], s["Name"], s["Department"], s["Year"],
            s["Python"], s["Maths"], s["English"]))

def add_student():
    students = read_students()
    new_id = max([int(s["Student_ID"]) for s in students], default=0) + 1
    print("\\nEnter student details:")
    name = input("Name: ").strip()
    department = input("Department: ").strip().upper()
    year = input("Year (1/2/3/4): ").strip()
    try:
        marks = [int(input(subject + " marks (0-100): ")) for subject in ["Python", "Maths", "English"]]
        if not name or not department or year not in ["1", "2", "3", "4"] or any(m < 0 or m > 100 for m in marks):
            print("Invalid details. Record not added.")
            return
    except ValueError:
        print("Please enter numbers for year and marks.")
        return
    students.append({
        "Student_ID": str(new_id), "Name": name, "Department": department,
        "Year": year, "Python": str(marks[0]), "Maths": str(marks[1]),
        "English": str(marks[2])
    })
    write_students(students)
    print("Student added successfully. New Student ID:", new_id)

def search_student():
    students = read_students()
    key = input("Enter Student ID or name to search: ").strip().lower()
    found = [s for s in students if s["Student_ID"] == key or key in s["Name"].lower()]
    if found:
        for s in found:
            print(s)
    else:
        print("Student not found.")

def update_student():
    students = read_students()
    sid = input("Enter Student ID to update: ").strip()
    for s in students:
        if s["Student_ID"] == sid:
            print("Leave a field blank to keep its old value.")
            name = input(f'Name [{s["Name"]}]: ').strip()
            dept = input(f'Department [{s["Department"]}]: ').strip()
            if name: s["Name"] = name
            if dept: s["Department"] = dept.upper()
            for subject in ["Python", "Maths", "English"]:
                value = input(f'{subject} marks [{s[subject]}]: ').strip()
                if value:
                    try:
                        mark = int(value)
                        if 0 <= mark <= 100:
                            s[subject] = str(mark)
                        else:
                            print("Marks must be from 0 to 100; old value kept.")
                    except ValueError:
                        print("Invalid mark; old value kept.")
            write_students(students)
            print("Student record updated.")
            return
    print("Student ID not found.")

def delete_student():
    students = read_students()
    sid = input("Enter Student ID to delete: ").strip()
    remaining = [s for s in students if s["Student_ID"] != sid]
    if len(remaining) == len(students):
        print("Student ID not found.")
    else:
        write_students(remaining)
        print("Student record deleted.")
