# How do you create a set? 

a = set(["a", "b"])
b = {"a", "b"}

# Using the following set, how would you check to see if it contains the string, "b"?
print("b" in a)

#  How do you add an item to a set?
a.add("c")
print(a)

# Remove the letter “c” from the following set using a set method
a.discard("c")
print(a)

# How do you find the common items between two sets?
print(a.intersection(b))