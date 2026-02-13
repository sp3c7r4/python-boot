"""
Docstring for new learning.conditional-statements
"""

# if 2 > 1:
#   print("This is a True statement")

# Getting inputs from a user
# user_input = input("How much is that doggy in the window?: "); # Takes in user's input as stdin
# user_input = int(user_input); # Casts to an integer

# if (user_input < 10):
#   print("Cheap doggy")
# elif 10 <= user_input <= 20:
#   print("I'd still pay that!");
# else:
#   print("Uhhhh, Too expensive!");

# Boolean operations
"""
  or - If any condition is true, Run
  and - If all conditions are true, Run
  not - if it's false Run
"""

# Examples
x = 10;
y = 12;

if (x <= 10 and y == 12):
  print("The or check passed!")
else:
  print("The statement was False")

my_list = [1,2,3,4];
x = 10;

if x not in my_list: 
  print("'x' is not in the list, so this is True.")

# or testung 'not' with !=
# if x != my_list: --- valid
if x != 11:
  print("me")

# Checking for nothing
empty_list = [];
empty_tuple = ();
empty_dictionary = {};
empty_string = '';
nothing = None;

# if empty_list == []:
# if empty_list.__len__() == 0:
if not empty_list:
  print("This list is empty")

# if empty_tuple == ():
# if empty_tuple.__len__() == 0:
if not empty_tuple:
  print("This is an empty tuple")

# if empty_string == '':
if not empty_string:
  print("This is an empty string")

if not nothing:
  print("There's nothing")
