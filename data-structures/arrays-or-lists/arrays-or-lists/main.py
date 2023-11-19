SAMPLE_ARRAY = ['a', 'b', 'c', 'z', 'y']

print(f"SAMPLE_ARRAY: {SAMPLE_ARRAY}")

# LOOKUP OPERATION
print("\nLOOKUP OPERATION")

# For example, if I want to get the data element at a certain index.
# Time complexity or BIG(O) - O(1)
print(f"Element at SAMPLE_ARRAY[0]: {SAMPLE_ARRAY[0]}")

# If I wish to obtain the index of a specific element in the list.
# Time complexity or BIG(O) - O(n)
print(f"Index of 'y' in SAMPLE_ARRAY: {SAMPLE_ARRAY.index('y')}")

# PUSH OPERATION
print("\nPUSH OPERATION")

# If I want to append data element at the end of the list.
# Time complexity or BIG(O) - O(1)
SAMPLE_ARRAY.append('w')
print(f"SAMPLE_ARRAY after pushing 'w': {SAMPLE_ARRAY}")

# INSERT OPERATION
print("\nINSERT OPERATION")

# If I want to insert data element at a given index.
# Time complexity or BIG(O) - O(n)
# Using the insert() function.
SAMPLE_ARRAY.insert(3, 'd')
print(f"SAMPLE_ARRAY after inserting element at index [2]: {SAMPLE_ARRAY}")


# POP OPERATION
print("\nPOP OPERATION")

# If I want to pop data element from the end of the list.
# Time complexity or BIG(O) - O(1)
SAMPLE_ARRAY.pop()
print(f"SAMPLE_ARRAY after popping 'w': {SAMPLE_ARRAY}")

# DELETE OPERATION
print("\nDELETE OPERATION")

# If I want to delete data element at a given index.
# Time complexity or BIG(O) - O(n)
# Using the pop() function.
print("Delete data element using pop() function.")
SAMPLE_ARRAY.pop(2)
print(f"SAMPLE_ARRAY after removing element at index [2]: {SAMPLE_ARRAY}")

# Using the del keyword.
print("\nDelete data element using 'del' keyword")
del SAMPLE_ARRAY[2]
print(f"SAMPLE_ARRAY after removing element at index [2]: {SAMPLE_ARRAY}")

# If I want to delete data element by value.
# Time complexity or BIG(O) - O(n)
# Using the remove() function.
print("\nDelete data element using remove() function")
SAMPLE_ARRAY.remove('y')
print(f"SAMPLE_ARRAY after removing element with value 'y': {SAMPLE_ARRAY}")
