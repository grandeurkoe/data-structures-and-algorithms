def merge(left, right):
    left_merge_right = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            left_merge_right.append(left[left_index])
            left_index += 1
        else:
            left_merge_right.append((right[right_index]))
            right_index += 1
    left_merge_right += left[left_index:len(left)] + right[right_index: len(right)]
    return left_merge_right


def merge_sort(before_sort):
    """Sorts before_sort using merge sort. Returns the sorted before_sort"""
    if len(before_sort) == 1:
        return before_sort

    center = int(len(before_sort) / 2)
    left = before_sort[0: center]
    right = before_sort[center: len(before_sort)]

    return merge(merge_sort(left), merge_sort(right))


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(f"Before Sort: {numbers}")
print(f"After Merge Sort: {merge_sort(numbers)}")
