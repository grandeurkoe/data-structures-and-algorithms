dynamic_counter = 0
non_dynamic_counter = 0


def fibonacci_non_dynamic(n):
    global non_dynamic_counter
    non_dynamic_counter += 1
    if n < 2:
        return n

    return fibonacci_non_dynamic(n - 1) + fibonacci_non_dynamic(n - 2)


def fibonacci_dynamic():
    fibonacci_cache = {}

    def fibonacci(n):
        global dynamic_counter
        dynamic_counter += 1
        if n in fibonacci_cache:
            return fibonacci_cache[n]
        elif n < 2:
            fibonacci_cache[n] = n
            return fibonacci_cache[n]
        else:
            fibonacci_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return fibonacci_cache[n]

    return fibonacci


fibonacci_of = 35
memoization = fibonacci_dynamic()
print(
    f"With Dynamic Programming: Fibonacci of {fibonacci_of} is {memoization(fibonacci_of)}: {dynamic_counter} calculations")
print(
    f"Without Dynamic Programming: Fibonacci of {fibonacci_of} is {fibonacci_non_dynamic(fibonacci_of)}: {non_dynamic_counter} calculations")
