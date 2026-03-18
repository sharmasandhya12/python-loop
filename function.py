# What is function?
# A function is a block of code that runs only when it is called.

# why use function?

# 1. Avoid repeating code
# 2. Makes program clean & orgenaized
# 3. Easy to debug and resue

# Syntax:
def fuction_name():
    #  code

#  ex:
# def greet():
#     print("Hello Students")

# greet()

# -----------------------------------------------------------------------
# Function with Parameters
# Used to pass values

 def greet(name):
    print(f"Hello {name}")

 greet()
 greet("Shreyarth")
 greet("AICW") 

# -----------------------------------------------------------------------

# Function with return value
# Used when we want to send result back

def add(a, b):
    return a + b
result = add(2, 3)
print(result)

# ------------------------------------------------------------------------

# Task 1: Create a function to calculate and return result:
def calculate(a, b):
    result = a + b
    return result

output = calculate(5, 3)
print("Result:",output)

# Task 2: create a function to check if a numner is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
    
#   check_even_odd(4)   output:"Even"
#   check_even_odd(7)  output:"odd"
# 
# Task 3: create a function to find the factorial of a number:

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Taking input from user
num = int(input("Enter a number: "))

# Calling function
result = factorial(num)

# Printing result
print("Factorial of", num, "is:", result)

# Task 4: Create a function to find maximum of three numbers:

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
a = float(input("Enter the First number:"))
b = float(input("Enter the second number:"))
c = float(input("Enter the third number:"))    

result = find_max(a, b, c)
print("Maximum number is:", result)
    
# Task 5: Create a function to check if a string is palindroms:    

def is_palindrom(s):
    temp = s

    lst = list(s)

    lst.reverse()

    rev = "".join(lst)

    if temp == rev:
        return "Not palindrom"

    text = input("Enter a string:")

    result = is_palindrom(text)

    print(result)

# Task 6: create a function to calculate the area of circle :
# 
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

# Taking input from user
r = float(input("Enter radius: "))

# Calling function
result = area_of_circle(r)

# Printing result
print("Area of circle is:", result)