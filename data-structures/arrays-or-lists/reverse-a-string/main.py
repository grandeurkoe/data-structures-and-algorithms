STRING = "Can you reverse this string?"


# Time complexity or BIG(O) - O(length of string)
def is_input_valid(string):
    """Check if input is valid. Return True if valid else return false."""
    if type(string) is str:
        return True
    else:
        return False


def reverse_using_slice(original):
    """Reverse string using list slicing. Return reversed string."""
    if is_input_valid(original):
        if len(original) <= 1:
            return original
        else:
            reverse_string = ''.join(STRING[::-1])
            return reverse_string
    else:
        return "Invalid input."


def reverse_using_comprehension(original):
    """Reverse string using list comprehension. Return reversed string."""
    if is_input_valid(original):
        if len(original) <= 1:
            return original
        else:
            original = [original[index] for index in range(len(original) - 1, -1, -1)]
            reverse_string = ''.join(original)
            return reverse_string
    else:
        return "Invalid input."


print(f"ORIGINAL STRING: {STRING}")
print(f"REVERSED STRING USING LIST SLICING: {reverse_using_slice(STRING)}")
print(f"REVERSED STRING USING LIST COMPREHENSION: {reverse_using_comprehension(STRING)}")
