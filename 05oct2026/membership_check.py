allowed_departments = ["CSE", "ECE", "IT", "EEE"]
student_department = input("Enter the student's department: ")

if student_department in allowed_departments:
    print("The department is available.")
else:
    print("The department is not available.")