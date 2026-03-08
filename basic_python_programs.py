# -----------------------------------------------------------
# Q1. Write a Python program to find the remainder
# when a number is divided by z .
# -----------------------------------------------------------

a = int(input("Enter value of a: "))
z = int(input("Enter value of z: "))

c = a % z

print("Remainder is:", c)


# -----------------------------------------------------------
# Q2. Use comparison operator to find out whether a given
# variable 'a' is greater than 'b' or not.
# Take a = 34 and b = 80 (or user input)
# -----------------------------------------------------------

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("a is greater than b:", a > b)


# -----------------------------------------------------------
# Q3. Write a Python program to find the average
# of two numbers entered by the user.
# -----------------------------------------------------------

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

c = (a + b) / 2

print("Average of two numbers is:", c)


# -----------------------------------------------------------
# Q4. Write a Python program to calculate the square
# of a number entered by the user.
# -----------------------------------------------------------

a = int(input("Enter a number: "))

print("The square of the number is:", a ** 2)


# -----------------------------------------------------------
# Q5. Write a Python program to fill in a letter template
# given below with name and date.
#
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# -----------------------------------------------------------

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Tanya").replace("<|Date|>", "24 January"))


# -----------------------------------------------------------
# Q6. Write a Python program to detect double space
# in a string.
# -----------------------------------------------------------

name = "Harry is a good boy and"

print(name.find("  "))   # returns -1 if no double space


# -----------------------------------------------------------
# Q7. Write a Python program to replace double spaces
# with single space.
# -----------------------------------------------------------

name = "Harry  is  a  good  boy  and"

print(name.replace("  ", " "))
