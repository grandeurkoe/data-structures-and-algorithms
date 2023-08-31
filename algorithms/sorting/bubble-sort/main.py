def bubble_sort(before_sort):
    """Sorts before_sort using bubble sort. Returns the sorted before_sort"""
    for i in range(1, len(before_sort)):
        for j in range(len(before_sort) - i):
            if before_sort[j] > before_sort[j + 1]:
                temp = before_sort[j]
                before_sort[j] = before_sort[j + 1]
                before_sort[j + 1] = temp
    return before_sort


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(f"Before Sort: {numbers}")
print(f"After Bubble Sort: {bubble_sort(numbers)}")
