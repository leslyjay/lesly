# GRADE CALCULATOR PROGRAM
# Write a program that takes marks as input and prints the grade based on the following criteria:
# If the marks is
#     >= 90 : then prints Grade A
#     >= 80 : then prints Grade B   
#     >= 70 : then prints Grade C
#     >= 60 : then prints Grade D
#     < 60 : then prints Grade F
# def marks_grade(marks):
#     if marks >= 90:
#         return "Grade A"
#     elif marks >= 80:
#         return "Grade B"
#     elif marks >= 70:
#         return "Grade C"
#     elif marks >= 60:
#         return "Grade D"
#     else:
#         return "Grade F"
# marks = int(input("Enter your marks: "))
# grade = marks_grade(marks)
# print(f"Hello, your grade is {grade}.")

# CREATE A SIMPLE LOGIC SYSTEM THAT ASKS FOR A USER'S USERNAME AND PASSWORD. IF THE USERNAME IS
# ADMIN AND PASSWORD IS PASSWORD1234 PRINT LOGING SUCCESSFUL ELSE INVALID USERNAME OR PASSWORD
def login_system(username,password):
    if username == "admin" and password == "password1234":
        return "Login successful."
    else:
        return "Invalid username or password."
username = input("Enter your username: ")
password = input("Enter your password: ")
login = login_system(username,password)
print(login)