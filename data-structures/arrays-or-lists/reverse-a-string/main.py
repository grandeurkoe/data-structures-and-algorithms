def is_valid_input(string):
    """Check if the given string is valid input."""
    if type(string) == str:
        return type(string) == str
    else:
        return False


# Time complexity - O(length of string)
def reverse_string_using_slice(string):
    """Reverses a given string using list slicing."""
    if is_valid_input(string):
        if len(string) <= 1:
            print(string)
        else:
            reverse_string = string[::-1]
            print(reverse_string)
    else:
        print("Invalid input.")


# Time complexity - O(length of string)
def reverse_string_using_comprehension(string):
    """Reverses a given string using list comprehension."""
    if is_valid_input(string):
        if len(string) <= 1:
            print(string)
        else:
            string = list(string)
            reverse_string = [string[index] for index in range(len(string) - 1, -1, -1)]
            reverse_string = ''.join(reverse_string)
            print(reverse_string)
    else:
        print("Invalid input.")


original_string = "My name is Meowya."
reverse_string_using_slice(original_string)
reverse_string_using_comprehension(original_string)

