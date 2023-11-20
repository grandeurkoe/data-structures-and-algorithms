SAMPLE_DICT = {'fname': 'Vishal'}

print(f"SAMPLE_DICT: {SAMPLE_DICT}")

# LOOKUP OPERATION
print("\nLOOKUP OPERATION")

# Get the value of a dictionary entry based on key provided.
# Time complexity or BIG(O) - O(1)
print(f"Entry with key('fname'): {SAMPLE_DICT['fname']}")

# Get all keys in dictionary.
# Time complexity or BIG(O) - O(1)
# list() function changes the time complexity from O(1) to O(n).
print(f"SAMPLE_DICT keys: {list(SAMPLE_DICT.keys())}")

# Get all values in dictionary.
# Time complexity or BIG(O) - O(1)
# list() function changes the time complexity from O(1) to O(n).
print(f"SAMPLE_DICT values: {list(SAMPLE_DICT.values())}")

# INSERT OPERATION
print("\nINSERT OPERATION")

# Insert entry into a dictionary.
# Time complexity or BIG(O) - O(1)
SAMPLE_DICT['lname'] = 'Kushwaha'
print(f"SAMPLE_DICT after inserting ('lname', 'Kushwaha'): {SAMPLE_DICT}")

# DELETE OPERATION
print("\nDELETE OPERATION")

# Delete entry from a dictionary.
# Time complexity or BIG(O) - O(1)
del SAMPLE_DICT['lname']
print(f"SAMPLE_DICT after deleting ('lname', 'Kushwaha'): {SAMPLE_DICT}")

# Clear dictionary.
# Time complexity or BIG(O) - O(1)
SAMPLE_DICT.clear()
print(f"SAMPLE_DICT after clearing: {SAMPLE_DICT}")
