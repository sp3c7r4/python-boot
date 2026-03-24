"""
@ info - You wanna know if something is True of False
"""

# The bool function
print(f"Truthy: {bool(1)} and Falsey: {bool(0)}")

## Falseys
### bool(''), bool([]), bool({})

## Truthys
### bool(['spectra]), bool({ 1: 'one'}), bool(12)

# What about None?
## Python null's value. This is a keyword in Pythonand it's data type is None Type. None is not the same as 0, False or an empty string

print(None)
print(None == []) # False
print(None == '') # False
print(None == None) # True