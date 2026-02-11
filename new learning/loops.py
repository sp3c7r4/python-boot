"""
Docstring for new learning.loops
"""

# We have two kind of loops 
## for loop
## While loop
# Loops are used when you want to do something many times
# You use a loop when you want to iteratte over something n number of times

# Range function --> range(n)
# range(beginningInt, endInt, step)
## Creates a list that's n in length
# print(range(5))
# print(list(range(1,20,3)))

# For loop with range 
# for i in range(5): # same as for i in [0,1,2,3,4]: \n\tprint(i)
#   print(i)

# For loop with dict
# a_dict = { "name": "spectra", "second_name": "gee" };
# for i in a_dict: # @returns - Keys
#   print(i)

# keys = a_dict.keys();
# for key in keys:
#   print(key);

# Using the modulus operator
# for number in range(10): # same as for number in range(0, 10, 2): \n\tprint(number) 
  # if number % 2 == 0:
  #   print(number)

# The while loop
# i = 0 # Intitializing our counter
# while i < 10: # So far i < 10 is True, Loop
#   print(i) # Print the value of i at that moment
#   i = i + 1 # Increase the count of i by one
  # Since there's no break statement go back to the loop

# j = 0
# Using the break keyword inside a while loop
# while j < 10:
#   print(j);
#   if j == 5: # If j is 5
#     break; # Stop the loop
#   j += 1;

# Using the continue keyword
# print("------Using the continue keyword------")
# k = 0;
# while k < 10:
#   if k == 3:
#     k += 1
#     continue
#   print(k)

#   if  k == 5:
#     break
#   k += 1;

#Using else statements inside of For Loops
my_lists = list(range(5))

for i in my_lists:
  if (i == 9):
    print ("Item found");
    i += 1;
    break;
else:
  print("Item not found");