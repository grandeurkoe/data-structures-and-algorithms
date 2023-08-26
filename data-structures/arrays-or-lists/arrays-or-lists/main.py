# In a 32-bit system, each character in STRINGS will use 4 shelves in the memory. So, 4 * 4 = 16 bytes of storage
# will be used for storing STRINGS. This is a rather simplified way of looking at things.
STRINGS = ['b', 'c', 'e', 'f', 'g']

# To add an element at the end of an array.
# Time complexity of the append() function is O(1).

# To remove the last element from an array.
# Time complexity of the pop() function for the last element is O(1).
STRINGS.pop()

# To remove a specific element from an array, we simply provide its index.
# Time complexity of the pop() function for any arbitrary value is O(n).
# STRINGS.pop(1)

# To insert an element at a given position in an array, we use the insert function.
# Time complexity of the insert() function is O(n).
# Inserts an item at the beginning of the array.
STRINGS.insert(0, 'a')

# Inserts an item at index 3 of the array.
STRINGS.insert(3, 'd')

print(STRINGS)
