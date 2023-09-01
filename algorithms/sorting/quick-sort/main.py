def quick_sort(before_sort, left, right):
    """Sorts before_sort using quick sort. Returns the sorted before_sort"""
    if len(before_sort) == 1:
        return before_sort
    elif len(before_sort) == 0:
        return []
    elif len(before_sort) == 2:
        if before_sort[left] > before_sort[right]:
            duo_swap = before_sort[left]
            before_sort[left] = before_sort[right]
            before_sort[right] = duo_swap
        return before_sort
    else:
        pivot = before_sort[right]
        greater_number = []
        greater_index = 0

        while left < right:
            if before_sort[left] > before_sort[right]:
                greater_number.append(before_sort[left])
                left += 1
            elif before_sort[left] < before_sort[right]:
                temp = before_sort[greater_index]
                before_sort[greater_index] = before_sort[left]
                before_sort[left] = temp
                greater_index += 1
                left += 1

        temp = before_sort[greater_index]
        before_sort[greater_index] = before_sort[right]
        before_sort[right] = temp

        pivot_index = before_sort.index(pivot)

        return quick_sort(before_sort[0: pivot_index], 0, pivot_index - 1) + [before_sort[pivot_index]] + quick_sort(
            before_sort[pivot_index + 1: len(before_sort)], 0, (len(before_sort) - (pivot_index + 1)) - 1)


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(f"Before Sort: {numbers}")
print(f"After Quick Sort: {quick_sort(numbers, 0, len(numbers) - 1)}")
