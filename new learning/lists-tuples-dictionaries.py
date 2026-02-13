"""
Docstring for new learning.lists-tuples-dictionaries

"""

# Python lists -- way's to create a list
my_list: str = [];
my_list = list() #--Python's built in method

# Examples of lists
my_list1 = [1,2,3];
my_list2 = ["a", "b", "c"];
my_list3 = ["a", 1, "Python", 5]

my_nested_list = [my_list, my_list1];

# print(my_nested_list)


# If we're combining a list we use the .extend() method
combo_list = [];
one_list = [4,5]
# combo_list.extend(one_list);

# print(combo_list) ---> [4,5]

# Or much simpler just add the lists together
print(combo_list + one_list) #---> [4,5]

# Sorting a list
alpha_list = [3,6,5,3,1,0,9]
alpha_list.sort();


#Python Tuples --- Immutable lists
my_tuple = (1,2,3,4,5)
my_tuple[0:3] # Can be sliced aldo
another_tuple = tuple();
abc = tuple([1,2,3])

# Casting - Ability to change a given datatype to another
abc_list = list(abc)
print("Casted list: %s" % abc_list)


#Python Dictionaries - This is basically a hash table or a hash mapping. They might be referenced to as associative memories or associative arrays. They're indexed with kets which can be any immutable type string/number
# You can get a list of keys by calling the .keys() method
# To check if it has a key you'll use the in method

# Creating a dictionary
my_dict = {}
another_dict = dict()
my_other_dict = {
  "one": 1,
  "two": 2,
  "three": 3
}

#Accessing a valie in a dictionary
print(my_other_dict["one"])

#checking if a key exists in a dictionary @returns - Boolean
print("one" in my_other_dict)

#fetching all keys
print(my_other_dict.keys())