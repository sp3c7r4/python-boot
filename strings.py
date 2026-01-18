# Working with Strings

course = "Python Programming"

#Length
print(len(course)) #18
# Accessing specific characters in a string
print( course[0], course[-1] ) #Pg
#Slicing strings
print ( course[0:3], course[0:] ) #pyt Python Programming
print( course[:3] ) #Pyt
print( course[:] ) #Python Programming

#Formatted Strings
first = "Spectra"
last = "Gee"
full = f"{first} {last}" # Similar to `${first} {name}` in Javascript
print(full) #Spectra Gee

#String Methods - Functions in an object
print(course.upper()) #Returns a new value in upper case
print(course.lower()) #Returns a new value in lower case

# Removing whitespaces
print(course.strip()) #Removes whitespace from beginning and start of a string
print(course.lstrip()) #Removes whitespace from left of a string
print(course.rstrip()) #Removes whitespace from right of a string

#Finding characters
print(course.find("Pro")) # Outputs 7

#Replacing characters
print(course.replace("P", "j")) #Replace all uppercase P with j

#Expressions
print("Pro" in course) #Ture i.e. Note python is case-sensitive
print("The" not in course) #True because The isn't in the course variable