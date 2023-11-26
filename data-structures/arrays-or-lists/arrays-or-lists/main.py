SAMPLE = [1, 2, 4]

# LOOKUP OPERATION
print("\nLOOKUP OPERATION")

# For example, if I want to get the data element at a certain index.
print(f"By Index, SAMPLE[0]: {SAMPLE[0]}")  # -> Big O - O(1)

# If I wish to obtain the index of a specific element in the list.
print(f"By Value, SAMPLE.index(1): {SAMPLE.index(1)}")  # -> Big O - O(n)

# PUSH OPERATION
print("\nPUSH OPERATION")

# If I want to append data element at the end of the list.
SAMPLE.append(3)  # -> Big O - O(1)
print(f"Append Value(3).")

# INSERT OPERATION
print(f"\nINSERT OPERATION")

# If I want to insert data element at a given index.
SAMPLE.insert(0, 0)  # -> Big O - O(n)
print(f"Insert Value({SAMPLE[0]}) at Index[0].")

# POP OPERATION
print(f"\nPOP OPERATION")

# If I want to pop data element from the end of the list.
print(f"Pop Value({SAMPLE[-1]}).")
SAMPLE.pop()  # -> Big O - O(1)

# DELETE OPERATION
print(f"\nDELETE OPERATION")

# If I want to delete data element at a given index.
print(f"Delete Value(1) at Index[{SAMPLE[1]}] using pop() function.")
SAMPLE.pop(1)  # -> Big O - O(n)

# If I want to delete data element by value.
print(f"Delete Value(2) using remove() function.")
SAMPLE.remove(2)  # -> Big O - O(n)

print(f"Delete at Index[1] using del keyword.")
del SAMPLE[1]  # -> Big O - O(n)

print(f"\nSAMPLE = {SAMPLE}")
