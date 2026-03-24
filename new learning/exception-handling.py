"""
 In order to make our softwares better, our application needs to keep working even when the unexpected occurs.
"""

# The most common exceptions
"""
  - Exception - The base exception that all the others are based on
  - AttributeError - Raised when an attribute reference or assignment fails
  ImportError- Raised when an import statement fails to find the module definition or when afrom … import fails to find a name that is to be imported.
  - ModuleNotFoundError- A subclass of ImportError which is raised by import when a module
could not be located
  - IndexError- Raised when a sequence subscript is out of range.
  - KeyError- Raised when a mapping (dictionary) key is not found in the set of existing keys.
  - KeyboardInterrupt- Raised when the user hits the interrupt key (normally Control-C or
Delete)
  - NameError- Raised when a local or global name is not found.
  - OSError- Raised when a function returns a system-related error.
  - RuntimeError- Raised when an error is detected that doesn’t fall in any of the other categories.
  - SyntaxError- Raised when the parser encounters a syntax error.
  - TypeError- Raised when an operation or function is applied to an object of inappropriate type.
The associated value is a string giving details about the type mismatch.
  - ValueError- Raised when a built-in operation or function receives an argument that has the
right type but an inappropriate value, and the situation is not described by a more precise
exception such as IndexError.
  - ZeroDivisionError- Raised when the second argument of a division or modulo operation is
zero.
"""

# Handling Exceptions
try: 
  # Executes
  pass;
except ImportError:
  # Executes
  pass;

# Example
# try:
#   with open("example.txt") as f:
#     for line in f:
#       print(line)
# except:
#   print("An error occured")
# Note: This is a bad practice because we don't know the exception we're catching 

try:
  with open("example.txt") as f:
    for line in f:
      print(line)
  import something
except (OSError, ImportError):
  print("Unknown error")
# except OSError:
#   print("An error occured")
# except ImportError:
#   print('Unknown import!')


# Raising Exceptions
try:
  raise Exception("Something bad happened")
except Exception as e:
  print(f"Caught an Import Error!: {e}")
# Note: When you raise an exception, you can have it print out a custom message

# Finally statement
try:
  1 / 1
except ZeroDivisionError:
  print('You can not divide by zero!')
else:
  print("Runs if try is true")
finally:
  print('Cleaning up')