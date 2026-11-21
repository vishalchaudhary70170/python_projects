def demonstrate_data_structures():
    # 1. List
    departments = ["CSE", "ECE", "IT", "ME"]
    departments.append("CSE")  # List method

    # 2. Tuple
    subjects = ("Python", "Maths", "English")

    # 3. Set (stores unique values)
    unique_departments = set(departments)

    # 4. Dictionary (key-value pairs)
    student_example = {"Name": "Aarav", "Department": "CSE", "Year": 1}

    # 5. List methods: append(), sort()
    departments.sort()

    print("\\nPython data structures demonstration:")
    print("List:", departments)
    print("Tuple:", subjects)
    print("Set:", unique_departments)
    print("Dictionary:", student_example)
