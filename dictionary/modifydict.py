# Define the dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Add a new key-value pair
my_dict['occupation'] = 'Engineer'

# Print the updated dictionary
# print(my_dict)

# updating an existing value
my_dict['age']= 39
print(my_dict)

# removing key-value pair
del my_dict['city']
print(my_dict)

age = my_dict.pop("age")
print(age)
print(my_dict)

# clearing a dictionary
my_dict.clear()
print(my_dict)