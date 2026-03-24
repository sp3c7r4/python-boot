## How do you create a dictionary
a = dict(one=1, two=2, three=3)
b = { "one": 1, "two": 2, "three": 3 }

# You have the following dictionary. How do you change the last_name field to ‘Smith’?
test_dict1 = { "last_name": "Testing" }

test_dict1.update([("last_name", "Smith")])
print(test_dict1)

test_dict1["last_name"] = "spectre"

print(test_dict1)


my_dict = {'first_name': 'James', 'last_name': 'Doe', 'email': 'jdoe@gmail.com'}
#  Using the dictionary above, how would you remove the email field from the dictionary?
my_dict.pop("email")
print(my_dict)

# How do you get just the values from a dictionary?
print(my_dict.values())