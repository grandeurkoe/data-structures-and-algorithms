dictionary = {
    'first_name': 'Me',
}

# LOOKUP OPERATION
# To get the value of a dictionary entry based on the key provided.
# The key gets passed to the hash function which then generates a value of fixed length.
# Assigns memory location to dictionary entry based on this hash value.
# Time complexity - O(1)
print(dictionary['first_name'])

# INSERTION OPERATION
# To insert entries into a dictionary.
# Time complexity - O(1)
dictionary['last_name'] = 'Meowya'

# DELETION OPERATION
# To delete entries from dictionary.
# Time complexity - O(1)
del dictionary['last_name']

print(dictionary)
