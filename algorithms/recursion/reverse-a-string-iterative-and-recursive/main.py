def reverse_string_iterative(query_string):
    """Reverses a query_string iteratively. Returns the reversed_string"""
    reversed_string = ""
    # reversed_string = query_string[::-1]
    for character_index in range(len(query_string) - 1, -1, -1):
        reversed_string += query_string[character_index]
    return reversed_string


def reverse_string_recursive(query_string):
    """Reverses a query_string recursively. Returns the reversed_string"""
    if len(query_string) > 0:
        return "" + query_string[len(query_string) - 1] + reverse_string_recursive(query_string[:-1])
    return query_string


string_to_reverse = "Yoyo Mastery"
print(f"Original String: {string_to_reverse}")
print(f"Reversed String using iteration: {reverse_string_iterative(string_to_reverse)}")
print(f"Reversed String using recursion: {reverse_string_recursive(string_to_reverse)}")
