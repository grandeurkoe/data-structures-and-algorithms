my_dict = {'a': True}
# Here we are not copying the value of my_dict to pointer_dict.  The pointer_dict simply points to my_dict.
pointer_dict = my_dict

# Making changes to the value of 'a' in my_dict also changes the value of pointer_dict['a'] because pointer_dict
# points to my_dict.
my_dict['a'] = "Changes"

print(my_dict)
print(pointer_dict)
