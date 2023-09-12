STRINGS = ['b', 'c', 'e', 'f']

# LOOKUP OPERATION
# For example, if I want to get the data element at a certain index. 
# Time complexity - O(1)
print(STRINGS[1])

# To get the index of a data element.
# Time complexity - O(n)
print(STRINGS.index('c'))

# INSERTION OPERATION
# To append data element at the end of the list.
# Time complexity - O(1)
STRINGS.append('g')

# To insert data element at a given index.
# Time complexity - O(n)
STRINGS.insert(0, 'a')

# DELETION OPERATION
# To delete data element from the end of the list.
# Time complexity - O(1)
STRINGS.pop()

# To delete data element at a given index.
# Time complexity - O(n)
del STRINGS[0]

# To delete data element if you know the data you wish to delete.
# Time complexity - O(n)
STRINGS.remove('b')

print(STRINGS)