# Day 2 - Python Basics

# 1. Variables and Data Types
name = "Jashwanth"
age = 20
score = 95.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Score:", score)
print("Is Student:", is_student)

print(type(name))
print(type(age))
print(type(score))
print(type(is_student))

# 2. Operators
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

print("a > b:", a > b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a > 5 and b < 10:", a > 5 and b < 10)
print("not(a > b):", not(a > b))

# 3. if / else
marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# 4. For loop
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)

# 5. While loop
print("While loop from 1 to 5:")
count = 1
while count <= 5:
    print(count)
    count += 1

# 6. Functions
def greet():
    print("Hello, welcome to AI/ML internship")

greet()

def add(x, y):
    return x + y

print("Sum:", add(4, 6))

def check_number(x):
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-3)

# 7. Even or Odd
num = 8
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 8. Sum of two numbers
x = 10
y = 20
print("Sum =", x + y)

# 9. Factorial using loop
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)