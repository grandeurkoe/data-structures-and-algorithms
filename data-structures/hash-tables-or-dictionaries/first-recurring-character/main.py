SAMPLE = [2, 9, 0, 1, 5, 3, 6, 2]

print(f"SAMPLE: {SAMPLE}")


def first_recurring_character_using_nested_loops(sample):
    """Get first recurring character using nested loops. Return first recurring character"""
    recurring_char = None
    recurring_distance = len(sample) - 1
    while True:
        for sample_index in range(len(sample)):
            for check_index in range(sample_index + 1, len(sample)):
                if sample[sample_index] == sample[check_index]:
                    if (check_index - sample_index) < recurring_distance:
                        recurring_distance = check_index - sample_index
                        recurring_char = sample[sample_index]
        if recurring_distance == len(sample) - 1:
            if sample[0] == sample[-1]:
                return sample[0]
            else:
                return None
        elif recurring_distance < len(sample) - 1:
            return recurring_char


def first_recurring_character_using_hash(sample):
    """Get first recurring character using hash. Return first recurring character."""
    recurring_hash = {}
    for char in sample:
        if char in recurring_hash:
            return char
        else:
            recurring_hash[char] = True


recurring_char_nested = first_recurring_character_using_nested_loops(SAMPLE)
recurring_char_hash = first_recurring_character_using_hash(SAMPLE)
print(f"First recurring character using nested loops: {recurring_char_nested}")
print(f"First recurring character using hash: {recurring_char_hash}")
