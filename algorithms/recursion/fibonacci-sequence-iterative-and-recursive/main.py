def fibonacci_iterative(index):
    # Time complexity - O(n)
    """Finds the value at the given index in the fibonacci sequence using interation. Return the value."""
    if index == 0:
        return 0
    else:
        first_root = 0
        second_root = 1
        fibonacci_sequence = f"{first_root}, {second_root}"
        for start in range(2, index + 1):
            temp = first_root
            first_root = second_root
            second_root += temp
            fibonacci_sequence += f", {second_root}"
        # print(f"Fibonacci Sequence: {fibonacci_sequence}")
        # print(f"N at index {index}: {second_root}")
        return second_root


def fibonacci_recursive(index):
    # Time complexity - O(2^n)
    """Finds the value at the given index in the fibonacci sequence using recursion. Return the value."""
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        fibonacci = fibonacci_recursive(index - 1) + fibonacci_recursive(index - 2)
        return fibonacci


fibonacci_index = 8
print(f"N at index {fibonacci_index} using fibonacci_iterative(): {fibonacci_iterative(fibonacci_index)}")
print(f"N at index {fibonacci_index} using fibonacci_recursive(): {fibonacci_recursive(fibonacci_index)}")
