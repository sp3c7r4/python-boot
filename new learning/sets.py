"""
  A set is a data type as an unordered collection of distinct hashable objects
  + Usable for
    - Membership testing
    - Removing duplicates from sequencing and computing mathematical operations like intersection, union, difference and symmetric difference
Note: No element position is recorded for sets or order of insertion
## We have two types of sets in python
  + Set --> This is mutable which means it can be changed
  + Frozen set --> This is immutable and hashable
"""

# Creating a set
a: set = { "a", "b", "c", "d" }
print(f"My set: {a}")

my_list = [1,2,3,4]
b = set(my_list)
print(f"My mutated list -> set: {b}")

# Accessing set memebers
print(f"a exists in set a: {"a" in a}")

# for item in a:
#   print(item)

# Adding items to a set
a.add("e")
print(f"Added e to set a: {a}")
a.update(["f", "g", "h"])
print(f"Updated set a with new values: {a}")

# Removing items from a set
a.remove("h")
print(f"h has been removed from set a: {a}")

a.discard("h") #Since h doesn't exist it will not throw up an error
print(f"No error thrown removing h: {a}")

## Note: the difference between .remove & .discard is thar remove throws and error and discard doesn't

a.pop() # Removes and return the last item
## Note: if your set is empty and try to remove an item you get an error

# Clearing or deleting a set
# .clear()
# del my_set --> completely removes the set

# set operations

## union(): combines two sets and returns new set
print(a.union(b))
## intersection(): Returns a new set with the elements that are common btw the two sets
print(a.intersection(b))
## difference(): Returns a new set with elements that are not in the other set
print(a.difference(b))
