"""
  Developers have to make decisions all the time. How do you intend to approach this problem?
  This topic is usually called control flow in python
  In Python, you can control the flow of your program using
  + if
  + elif
  + else
"""

# Comparison Operators
## This lets you ask if something equals something else or if they're greater than or less than a value etc.

# Operator        Meaning
# >          Greater than- This is True if the left operand is greater than the right
# <          Less than- This is True if the left operand is less than the right one
# ==         Equal to- This is True only when both operands are equal
# !=         Not equal to- This is True if the operands are not equal
# >=         Greater than or equal to- This is True when the left operand is greater than or equal to the right
# <=         Less than or equal to- This is True when the left operand is less than or equal to the right

a = 2
b = 3

print(f"Is a equals to b: {a == b}")
print(f"Is a not equals to b: {a != b}")
print(f"Is a greater than b: {a > b}")
print(f"Is a less than b: {a < b}")
print(f"Is a greater than or equals to b: {a >= b}")
print(f"Is a less than or equals to b: {a <= b}")

# Creating a Simple Conditional
authenticated = True
if authenticated:
  print("Come on in. You're authenticated 😊")

# Branching conditional statements
AUTHENTICATED = False
if AUTHENTICATED:
  print("You're logged in")
else:
  print("Please login")

# Logical operators
## and- Only True if both the operands are true
## or- True if either of the operands are true
## not- True if the operand is false

# Special operators
## is- True when the operands are identical (i.e. have the same id)
## is not- True when the operands are not identical
## in- True when the value is in a collection (list, tuple, set, etc.)
## not in- True when the value is not in a collection