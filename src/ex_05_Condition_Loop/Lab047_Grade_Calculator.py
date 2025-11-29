"""
Grade Calculator Program
# Write a Program that calculates and displays the letter grade
# for a given numerical score (Ex: A, B, C, D, or F)
# based on the following grading scale
"""
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Step 1: Logic Building
# i/p: number
# o/p: A,B,C,D and F

# Step 2: Rough logic
# User input and using if and elif and else logic to print each grade.

grade = int(input("Enter the score of the student: ").strip())

if grade <= -1 or grade > 100:
    print("Enter a valid score")
else:
    if grade <= 100 and grade >= 90:
        print("Student as scored A Grade")
    elif grade <= 89 and grade >= 80:
        print("Student as scored B Grade")
    elif grade <= 79 and grade >= 70:
        print("Student as scored C Grade")
    elif grade <= 69 and grade >= 60:
        print("Student as scored D Grade")
    else:
        print("Fail")
