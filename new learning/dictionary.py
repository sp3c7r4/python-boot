## Creating a dictionary
my_dict1 = dict(one=1, two=2, three=3)
my_dict2 = { "name": "Spectra gee", "age": 21, "color": "blue" }

## Accessing dictionaries
print('one' in my_dict1)
my_dict1['one']

print('two' not in my_dict1)

## Dictionary methods
### d.get(key, default_value)  -> default value can be anything

print(my_dict1.get("four", "Not found")) #Get's a value from the dictionary with it's key
print(my_dict1.clear()) # Empty's the dictionary

# Creating a shallow copy
shallow_copy = my_dict2.copy()
print(f"Shallow copy: {shallow_copy}")

# Returning a new view of a dictionary
print(f"New dictionary view: {my_dict2.items()}\n")

# Returning a key view of the dictionary
print(f"Key's view of the dictionary: {my_dict2.keys()}\n")

# Returning a value view of the dictionary
print(f"Value's view of the dictionary: {my_dict2.values()}\n")

# Removing an item from the dictionary
print(f"Removing age from the dictionary: {my_dict2.pop("Age", "Not found")}") 
#Note --> i purposely used 'Age' instead of 'age' so if it exists it will return 21 instead of Not founc

# Pop Item, LIFO -> Stack data structure
print(f"Removing last item from dictionary: {my_dict2.popitem()}")

# Overwriting an existing key
my_dict2.update([("age", 24)])
print(f"Overwrite key: {my_dict2}")

