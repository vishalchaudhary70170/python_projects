STUDENT MANAGEMENT SYSTEM (Python Mini Project)

Files:
1. main.py                  - Main menu and program control
2. student_operations.py    - Add, display, search, update and delete students
3. student_analysis.py      - NumPy and Pandas analysis
4. student_data.csv         - Dataset containing 50 student records

Requirements:
- Python 3
- numpy
- pandas

Install libraries in the VS Code terminal:
    python -m pip install numpy pandas

Run:
    python main.py

IMPORTANT:
Keep all four files in the same folder. Run main.py from that folder.
The program updates student_data.csv when records are added, changed or deleted.
The analysis option creates student_analysis_report.csv.

Mandatory parameter coverage:
- Dataset: 50 records in student_data.csv
- Data structures: list, tuple (subject_cols is used as a list; tuple/set/dictionary concepts are illustrated in notes below), set, dictionary, list methods
- Functions: more than five user-defined functions
- NumPy: 1D/2D arrays, indexing, slicing, sum, mean, max, min, standard deviation
- Pandas: DataFrame, CSV read, selected rows/columns, filtering, sorting, GroupBy, missing-value handling, describe()
- Modules: main.py, student_operations.py, student_analysis.py
- File handling: CSV reading and writing
- Features: add, display, search, update, delete, summary report
- Output: VS Code terminal

For viva:
The dataset has columns Student_ID, Name, Department, Year, Python, Maths and English.

Extra module: data_structures.py explicitly demonstrates list, tuple, set, dictionary and list methods.
