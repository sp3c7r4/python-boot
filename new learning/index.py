print ("Hello python\n") #I'm a comment
# Data Types in Python

## @info - Strings

#### types of strings 
# - inline strings
# inline_string = 'This is an inline string'
# inline_string_double = "This is also an inline string"
# print(inline_string, inline_string_double)

# # - multi-line strings
# multi_line_string = '''This is a multi-line string.
# It can span multiple lines.
# Like this.'''
# print(multi_line_string)
# print ('\n')
# print ("First value of inline_string:", inline_string[0])
# print (f"Unicode string: {u'This is unicode string with \u03A9 character'}")

# # String concatenation
# string_one = "My cat\n ate "
# string_two = "my food"
# string_three = string_one + string_two

# print ('\n')
# # String methods
# # string_three.upper() # Converts a string to upper case
# # string_three.capitalize()
# # print(string_three.__len__())

# # string slicing -> it start's from initial position but doesn't include value of ending position
# my_string: str = "I like python!!"
# print(my_string[:-5])
# print(my_string[3:-2]) 

# string formatting - AKA substitution
# my_string = "I like %s" % "Python"
# print(my_string)

# var = "Python"
# newString = "I love %s" % var
# print(newString)

# newString2 = u"I love %s and \u03B9 %s" % ("Python", "Typescript")
# print(newString2)


## @info - Numbers
# my_number: int = 10 #integrer
# print(my_number)

# Note: No conversion from string to number when it's not a number string;
# print (int("10")) #This works
# print (int("Ten")) #This will raise an error

