# ==========================================
# DAY 1: PYTHON FUNDAMENTALS PRACTICE
# ==========================================

print("--- 1. Core Syntax & Operations ---")
name = "Arbal"
age = 20
gpa = 3.94
is_student = True
print(f"Student: {name}, Age: {age}, GPA: {gpa}, Enrolled: {is_student}")

# Type conversion
age_str = input("Enter your age: ") if False else "20" # Skipping input for automated run
next_age = int(age_str) + 1
print(f"Next year age: {next_age}")

# Operators
print(f"10 // 3 = {10 // 3} (Floor division)")
print(f"10 % 3 = {10 % 3} (Remainder)")
print(f"10 > 5 and 3 < 4: {10 > 5 and 3 < 4} (Logical)")


print("\n--- 2. Control Flow & Strings ---")
marks = 78
if marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Needs improvement")

# Loops
for number in range(1, 6):
    if number == 2:
        continue
    if number == 5:
        break
    print(f"Loop number: {number}")

# Strings
message = "Python to AI"
print(f"First char: {message[0]}, Last char: {message[-1]}")
print(f"Sliced: {message[0:6]}")
print(f"Cleaned: {'  akif  '.strip().title()}")


print("\n--- 3. Data Structures ---")
# Lists
skills = ["Python", "SQL"]
skills.append("AI")
print(f"List (mutable): {skills}")

# Tuples
coordinates = (10, 20)
print(f"Tuple (immutable): {coordinates}")

# Sets
unique_ids = {101, 102, 101, 103}
print(f"Set (unique): {unique_ids}")

# Dictionaries
student = {"name": "Akif", "age": 20, "gpa": 3.94}
for key, value in student.items():
    print(f"{key}: {value}")


print("\n--- 4. Functions & Mini Project ---")
# MINI PROJECT: Student Marks Analyzer (Modified as requested)
def analyze_marks(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    
    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"
        
    highest = max(marks_list)
    lowest = min(marks_list)
    
    print("Marks:", marks_list)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Result:", result)
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)

student_marks = [78, 85, 42, 67, 90]
analyze_marks(student_marks)