#Task 1
a = 15
b = 4

print("Task 1:");
if a>b:
    print("a is greater than b")

#Task 2
name1 = "Alice"
name2 = "Alice"

print("Task 2:");
if name1 == name2:
    print("Both names matched")

#Task 3
num1 = 10
num2 = 20

print("Task 3:");
if num1 < num2:
    print("First number is less than second number")

#Task 4
age = 25

print("Task 4:");   
if age >= 18:
    print("You can vote")

#Task 5
marks = 85
print("Task 5:");
if marks >= 50:
    print("Pass")

#Task 6
num3 = 7
num4 = 3
print("Task 6:");
if num3 < num4:
    print("First number is less than second number")
else:
    print("First number is greater than second number")

#Task 7
c = ""
print("Task 7:");
if not c:
    print("String is empty")
else:
    print("String is not empty")

#Task 8
my_name = "Kazim"
print("Task 8:");
if my_name == "Kazim":
    print("Name is available")

#Task 9
zero = 0
print("Task 9:");
if zero:
    print("0 is Truthy")
else:
    print("0 is Falsy")

#Task 10
num_val = 42
print("Task 10:");
if num_val:
    print("Non-zero number is Truthy")
else:
    print("Non-zero number is Falsy")

#Task 11
student_marks = 85
print("Task 11:");
if student_marks >= 80:
    print("A Grade")
else:
    print("Needs Improvement")

#Task 12
correct_username = "admin"
correct_password = "password123"
entered_username = "admin"
entered_password = "password123"

print("Task 12:");
if entered_username == correct_username and entered_password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")