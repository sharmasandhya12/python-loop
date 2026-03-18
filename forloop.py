# What is a Loop?
# A loop is used to repeat a block of code multiple 
# times until a condition is met.

# Types of Loops in Python
# 1. for loop
# Used when we know how many times we want to repeat.

# Syntax:
# for variable in sequence:
#     # code

# range() function is commonly used to generate a 
# sequence of numbers.

# range comes with 3 parameters:
# 1. start (inclusive)
# 2. stop (exclusive)
# 3. step (optional, default is 1)

# range(start, stop-1, step)


# Example:
for i in range(1, 6):
    print(i)

# Key Points:
# 1. range(start, stop) generates numbers
# 2. Loop runs fixed number of times

# -----------------------------------------------------------------

# 2. while loop
# Used when we repeat until a condition becomes False

# Syntax:
# while condition:
#     # code

# Example:
i = 1
while i <= 5:
    print(i)
    i += 1

# Output:
# 1 2 3 4 5

# Key Points:
# 1. Condition is checked every time
# 2.Can run infinite loop if condition never becomes False

# ----------------------------------------------------------------------------

# Loop Control Statements

# 1. break
# Stops the loop immediately

# ex:
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Output:
# 1 2

# 2. continue
# Skips current iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# 1 2 4 5

# 3. pass
# Does nothing (placeholder)

for i in range(5):
    pass

# --------------------------------------------------------------------------

# Task 1
# Print numbers from 1 to 10 
# using a for loop.

for i in range(1, 11):
    print(i, end=' ')

# Expected Output
# 1 2 3 4 5 6 7 8 9 10

# Task 2
# Print even numbers from 1 to 20.

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, end=' ')

for i in range(2, 21, 2):
    print(i, end=' ')

# Output
# 2 4 6 8 10 12 14 16 18 20

# Task 3
# Print odd numbers from 1 to 15.

# start:1
# end:16
# step:2

for i in range(1, 16, 2):
    print(i, end=' ')

# Output
# 1 3 5 7 9 11 13 15

# Task 4
# Print each character of the string.
text = "Python"

for char in text:
    print(char)

# Output
# P
# y
# t
# h
# o
# n

# Task 5
# Print all items in the list.

data = ["Data", "Science", "AI"]

for item in data:
    print(item)

# Output
# Data
# Science
# AI

# Task 6
# Find the sum of numbers from 1 to 10.

total = 0
for i in range(1, 11):
    total += i

print(total)
# Output
# 55

# Task 7
# Print multiplication table of 5.

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# f = format string, allows embedding expressions 
# inside string literals using {}

# Output
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

# Task 8
# Count how many vowels are in a string.

text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
# Output
# Number of vowels: 3

# Task 9
# Print numbers in reverse order from 10 to 1.

for i in range(10, 0, -1):
    print(i)

# Output
# 10 9 8 7 6 5 4 3 2 1

# Task 10
# Print square of numbers from 1 to 5.

for i in range(1, 6):
    print(i ** 2)
    
# Output
# 1
# 4
# 9
# 16
# 25