dynamic_counter = 0
non_dynamic_counter = 0


def fibonacci_non_dynamic(n):
    global non_dynamic_counter
    non_dynamic_counter += 1
    if n < 2:
        return n

    return fibonacci_non_dynamic(n - 1) + fibonacci_non_dynamic(n - 2)


def fibonacci_dynamic(n):
    global dynamic_counter
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        dynamic_counter += 1
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci.pop()


fibonacci_of = 5
print(
    f"With Dynamic Programming: Fibonacci of {fibonacci_of} is {fibonacci_dynamic(fibonacci_of)}: {dynamic_counter} calculations")
print(
    f"Without Dynamic Programming: Fibonacci of {fibonacci_of} is {fibonacci_non_dynamic(fibonacci_of)}: {non_dynamic_counter} calculations")
