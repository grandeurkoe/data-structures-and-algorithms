def selection_sort(before_sort):
    """Sorts before_sort using selection sort. Returns the sorted before_sort"""
    minimum_index = 0
    for i in range(len(before_sort)):
        minimum = before_sort[i]
        for j in range(i + 1, len(before_sort)):
            if before_sort[j] < minimum:
                minimum = before_sort[j]
                minimum_index = j
        temp = before_sort[i]
        before_sort[i] = before_sort[minimum_index]
        before_sort[minimum_index] = temp
    return before_sort


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(f"Before Sort: {numbers}")
print(f"After Selection Sort: {selection_sort(numbers)}")
