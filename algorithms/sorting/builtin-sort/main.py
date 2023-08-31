def sorting(before_sort):
    print(f"Before Sort: {before_sort}")
    before_sort.sort()
    print(f"After Sort: {before_sort}")


letters = ['a', 'd', 'z', 'e', 'l', 'b']
integers = [2, 64, 34, 2, 1, 7, 8]
sorting(integers)
