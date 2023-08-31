def insertion_sort(before_sort):
    """Sorts before_sort using insertion sort. Returns the sorted before_sort"""
    for i in range(1, len(before_sort)):
        for j in range(i - 1, -1, -1):
            if before_sort[i] < before_sort[j]:
                temp = before_sort[j]
                before_sort[j] = before_sort[i]
                before_sort[i] = temp
                i -= 1
    return before_sort


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(f"Before Sort: {numbers}")
print(f"After Insertion Sort: {insertion_sort(numbers)}")
