import numpy as np
import pandas as pd
from student_operations import FILE_NAME

def run_analysis():
    # Pandas: read CSV file and create a DataFrame
    df = pd.read_csv(FILE_NAME)
    print("\\n========== DATA ANALYSIS ==========")

    # Handle missing values
    print("\\nMissing values before cleaning:")
    print(df.isnull().sum())
    for col in ["Python", "Maths", "English"]:
        df[col] = df[col].fillna(df[col].mean())

    # Create a calculated Percentage column
    subject_cols = ["Python", "Maths", "English"]
    df["Total"] = df[subject_cols].sum(axis=1)
    df["Percentage"] = df["Total"] / 3

    # Selected rows and columns
    print("\\nFirst 5 rows:")
    print(df.head())
    print("\\nSelected columns (Name and Department):")
    print(df[["Name", "Department"]].head())

    # Filtering and sorting
    print("\\nStudents scoring 80 or more in Python:")
    print(df[df["Python"] >= 80][["Name", "Python"]])
    print("\\nTop 5 students by percentage:")
    print(df.sort_values("Percentage", ascending=False)[["Name", "Percentage"]].head())

    # GroupBy operation
    print("\\nDepartment-wise average percentage:")
    print(df.groupby("Department")["Percentage"].mean())

    # Statistical analysis using Pandas
    print("\\nStatistical summary:")
    print(df[subject_cols + ["Percentage"]].describe())

    # NumPy: 1D and 2D arrays, indexing, slicing and calculations
    python_marks = np.array(df["Python"].to_numpy())       # 1D array
    marks_2d = df[subject_cols].to_numpy()                  # 2D array
    print("\\nNumPy 1D array (Python marks):", python_marks)
    print("NumPy 2D array (first 5 students):\\n", marks_2d[:5])
    print("Array indexing - first student's Python mark:", python_marks[0])
    print("Array slicing - first 5 Python marks:", python_marks[:5])
    print("Sum:", np.sum(python_marks))
    print("Mean:", np.mean(python_marks))
    print("Maximum:", np.max(python_marks))
    print("Minimum:", np.min(python_marks))
    print("Standard deviation:", np.std(python_marks))

    # Summary report
    print("\\n========== SUMMARY REPORT ==========")
    print("Total students:", len(df))
    print("Overall average percentage:", round(df["Percentage"].mean(), 2))
    topper = df.loc[df["Percentage"].idxmax()]
    print("Topper:", topper["Name"], "| Percentage:", round(topper["Percentage"], 2))
    print("Department count:\\n", df["Department"].value_counts())

    # Save processed data as another CSV file
    df.to_csv("student_analysis_report.csv", index=False)
    print("\\nAnalysis saved to student_analysis_report.csv")
