def find_factorial_iterative(query_number):
    """Calculates the factorial of query_number iteratively. Returns factorial."""
    if query_number < 0:
        return "undefined"
    else:
        factorial = 1
        while query_number > 0:
            factorial *= query_number
            query_number -= 1
        return factorial


def find_factorial_recursive(query_number):
    """Calculates the factorial of query_number recursively. Returns factorial."""
    if query_number > 1:
        query_number *= find_factorial_recursive(query_number - 1)
    elif query_number == 0:
        return 1
    elif query_number < 0:
        return "undefined"
    return query_number


factorial_of = 10
print(f"The factorial of {factorial_of} using iterative function is {find_factorial_iterative(factorial_of)}.")
print(f"The factorial of {factorial_of} using recursive function is {find_factorial_recursive(factorial_of)}.")
