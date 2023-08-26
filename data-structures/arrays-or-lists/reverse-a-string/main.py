def reverse_string(string):
    """Reverses the passed string."""
    if not string or type(string) is not str:
        return "Invalid Input!!!"
    else:
        # The easiest method to reverse a string is to use slice. Here, start = last character | end = first
        # character | increment = -1 return string[::-1]

        # OR

        # Using List comprehension reverse the string and store it as a List. Then append the elements of the list
        # together as a string.
        string_list = [string[char_index] for char_index in range(len(string) - 1, -1, -1)]
        return "".join(string_list)


print(reverse_string("My name is Meowya."))
